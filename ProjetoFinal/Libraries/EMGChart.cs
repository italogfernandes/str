﻿using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;


namespace DetectorContracao
{
    public class EMGChart : ChartHandler
    {
        public Series Envoltoriaseries;
        public double[] envoltoria_values;

        public Series LimiarSeries;
        public double limiar {
            get { return limiar_values[0];  }
            set {
                for (int i = 0; i < qnt_pontos; i++)
                {
                    limiar_values[i] = value;
                };
            }
        }
        public double[] limiar_values;
        public CircularBuffer<double> EnvoltoriaBuffer;

        public Series DetectionSeries;
        //Some testes:
        double[] detection_values;
        double[] x_contraction;
        double time_start_contract;
        double time_end_contract;


        public EMGChart(ref Chart _chart, int _qnt_points = 20,
            double facq = 1000)
        {
            Envoltoriaseries = new Series();
            LimiarSeries = new Series();
            DetectionSeries = new Series();

            this.freq_aquire = facq;
            this.chart = _chart;
            this.chartArea = new ChartArea();
            this.titleChart = new Title();
            this.series = new Series();

            SetQntPoints(_qnt_points);

            ConfigureChart();

            this.PlotterUpdater = new Timer();
            this.PlotterUpdater.Interval = 30;
            this.PlotterUpdater.Tick += this.PlotterUpdater_Tick;
        }

        public override void SetQntPoints(int qnt = 15)
        {
            qnt_pontos = qnt;

            envoltoria_values = new double[qnt_pontos];
            EnvoltoriaBuffer = new CircularBuffer<double>(qnt_pontos);
           
            y_values = new double[qnt_pontos];
            x_values = new double[qnt_pontos];
            limiar_values = new double[qnt_pontos];
            //detection_values = new double[qnt_pontos];

            PlotterBuffer = new CircularBuffer<double>(qnt_pontos);
            for (int i = 0; i < qnt_pontos; i++)
            {
                x_values[i] = i * (1 / freq_aquire);
                limiar_values[i] = limiar;
                //detection_values[i] = -2.5;
            }
        }

        public override void ConfigureSeries(
            string xtitle = "Tempo (s)", string ytitle = "Tensão (V)")
        {
            series.ChartType = SeriesChartType.FastLine; //tipo de gráfico do path
            series.Color = Color.Blue;
            series.ChartArea = chartArea.Name; //vincular a serie path à chartArea
            chart.Series.Add(series); //vincular a serie path ao chart       
            chartArea.AxisX.Title = xtitle;
            chartArea.AxisY.Title = ytitle;

            Envoltoriaseries.ChartType = SeriesChartType.FastLine;
            Envoltoriaseries.Color = Color.Green;
            Envoltoriaseries.ChartArea = this.chartArea.Name; //vincular a serie path à chartArea
            this.chart.Series.Add(Envoltoriaseries); //vincular a serie path ao chart    

            LimiarSeries.ChartType = SeriesChartType.FastLine;
            LimiarSeries.Color = Color.Orange;
            LimiarSeries.ChartArea = this.chartArea.Name; //vincular a serie path à chartArea
            this.chart.Series.Add(LimiarSeries); //vincular a serie path ao chart  

            DetectionSeries.ChartType = SeriesChartType.Area;
            DetectionSeries.Color = Color.FromArgb(50, Color.Cyan);//Cor Transparente
            DetectionSeries.ChartArea = this.chartArea.Name; //vincular a serie path à chartArea
            this.chart.Series.Add(DetectionSeries); //vincular a serie path ao chart  
        }

        public void AddEnvoloriaToBuffer(double Y)
        {
            if (!EnvoltoriaBuffer.SecureEnqueue(Y))
            {
                //MessageBox.Show("Buffer de Plottagem Cheio");
                EnvoltoriaBuffer.SecureDequeue();
                EnvoltoriaBuffer.SecureEnqueue(Y);
            }
        }

        public override void UpdateXYChartPoints()
        {
            #region EMG
            int points_to_add = PlotterBuffer.Count;

            if (points_to_add > 0) //Se existem pontos a sem adicionados no chart
            {
                //Desloca os Pontos atuais para a esquerda
                for (int i = 0; i < (qnt_pontos - points_to_add); i++)
                {
                    y_values[i] = y_values[i + points_to_add];
                    x_values[i] = x_values[i + points_to_add];
                }

                //Adiciona os novos pontos no novo espaço a direita
                for (int i = (qnt_pontos - points_to_add); i < qnt_pontos; i++)
                {
                    y_values[i] = PlotterBuffer.SecureDequeue();
                    x_values[i] = x_values[i - 1] + (1 / freq_aquire);
                }

                //Joga todo o conjunto de pontos no chart
                series.Points.DataBindXY(x_values, y_values);

                chartArea.AxisX.Minimum = Convert.ToDouble(Math.Floor(
                    x_values[0] * (1000.0 / PlotterUpdater.Interval))
                    / (1000.0 / PlotterUpdater.Interval));
                chartArea.AxisX.Maximum = Convert.ToDouble(Math.Ceiling(
                    x_values[qnt_pontos - 1] * (1000.0 / PlotterUpdater.Interval))
                    / (1000.0 / PlotterUpdater.Interval));
                chartArea.AxisY.Minimum = -2.5 ;
                chartArea.AxisY.Maximum = 2.5;
            }
            #endregion

            #region Envoltoria, Limiar e Contracao
            points_to_add = EnvoltoriaBuffer.Count;

            if (points_to_add > 0) //Se existem pontos a sem adicionados no chart
            {
                //Desloca os Pontos atuais para a esquerda
                for (int i = 0; i < (qnt_pontos - points_to_add); i++)
                {
                    envoltoria_values[i] = envoltoria_values[i + points_to_add];
                }

                //Adiciona os novos pontos no novo espaço a direita
                for (int i = (qnt_pontos - points_to_add); i < qnt_pontos; i++)
                {
                    envoltoria_values[i] = EnvoltoriaBuffer.SecureDequeue();
                }

                //Joga todo o conjunto de pontos no chart
                Envoltoriaseries.Points.DataBindXY(this.x_values,envoltoria_values);
                LimiarSeries.Points.DataBindXY(this.x_values, limiar_values);
                x_contraction = new double[1000];
                detection_values = new double[x_contraction.Length];
                for (int j = 0; j < x_contraction.Length; j++)
                {
                    detection_values[j] = 2.5;
                }
                DetectionSeries.Points.
                            DataBindXY(x_contraction, detection_values);

                double time_inicio = x_values[0];
                double time_end = x_values[0];
                for (int i = 1; i < qnt_pontos; i++)
                {
                    //Subida
                    if (envoltoria_values[i] > limiar & envoltoria_values[i - 1] < limiar)
                    {
                        time_inicio = x_values[i];
                    }
                    //Descida
                    if (envoltoria_values[i] < limiar & envoltoria_values[i - 1] > limiar)
                    {
                        time_end = x_values[i];
                        x_contraction = new double[
                            Convert.ToInt32(
                                Math.Ceiling((time_end - time_inicio) * 1000)
                            )];
                        detection_values = new double[x_contraction.Length];
                        for (int j = 0; j < x_contraction.Length; j++)
                        {
                            x_contraction[j] = time_inicio + j * 0.001;
                            detection_values[j] = 2.5;
                        }
                        DetectionSeries.Points.
                            DataBindXY(x_contraction, detection_values);
                    }
                }
            }
            #endregion
        }

    }
}