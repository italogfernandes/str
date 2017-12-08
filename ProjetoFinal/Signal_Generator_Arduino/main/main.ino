/* UNIVERSIDADE FEDERAL DE UBERLANDIA
   Biomedical Engineering
   Autors: Ítalo G S Fernandes
   contact: italogsfernandes@gmail.com
   URLs: https://github.com/italogfernandes/SEB
  Este codigo faz parte da disciplina de sistemas em tempo real
  para engenhara biomedica e visa emular um gerador de sinais
  utilizando o Arduino Due
  Tal sinal tambem sera enviado para a interface Serial
  podendo ser visualizado pelo serial plotter.
  Podem ser utilizados:
    SIN_WAVE,
    SQUARE_WAVE,
    TRIANGLE_WAVE,
    RAMP_WAVE,
    CONST_WAVE,
    ECG_WAVE,
    EMG_WAVE,
    ADC_WAVE
*/
#include<DueTimer.h>

#define PINOADC A0
#define UART_BAUDRATE 115200

//Freq aquire  = 1K
const double emg_wave[2200] = {
  -0.061748, -0.04892, -0.034584, -0.038985, -0.037979, -0.031063, -0.037979, -0.048669, -0.021882, -0.050807, -0.063886, -0.066275, -0.067659, -0.051561, -0.071809, -0.044896,
  -0.057346, -0.052064, -0.047914, -0.057598, -0.056215, -0.064389, -0.049172, -0.035967, -0.050933, -0.049675, -0.093817, -0.065018, -0.083253, -0.097589, -0.089541, -0.092559,
  -0.072186, -0.069419, -0.077594, -0.058352, -0.064515, -0.025906, -0.023769, -0.043136, -0.025781, -0.02402, -0.05961, -0.056969, -0.045902, -0.044142, -0.044016, -0.060616,
  -0.053574, -0.075707, -0.046531, -0.061245, -0.065269, -0.050304, -0.041626, -0.032823, -0.040495, -0.059862, -0.078474, -0.056843, -0.069419, -0.034081, -0.042129, -0.061496,
  -0.081744, -0.045399, -0.035716, -0.052819, -0.054328, -0.050304, -0.035464, -0.028673, -0.037225, -0.033326, -0.050807, -0.060742, -0.055334, -0.046028, -0.056843, -0.05131,
  -0.074701, -0.083379, -0.11406, -0.12589, -0.073569, -0.08275, -0.08778, -0.059233, -0.049298, -0.014965, -0.0054077, -0.056089, -0.025529, -0.057346, -0.06791, -0.083253,
  -0.069797, -0.056592, -0.067156, -0.099727, -0.083379, -0.068287, -0.067407, -0.055837, -0.047286, -0.044393, -0.029805, -0.041626, -0.051687, -0.052945, -0.045776, -0.03647,
  -0.038231, -0.05546, -0.060616, -0.06703, -0.057095, -0.032949, -0.026661, 0.0025152, -0.011696, -0.003647, -0.064012, -0.077719, -0.080109, -0.095577, -0.10752, -0.087906,
  -0.075078, -0.064892, -0.05219, -0.066527, -0.073569, -0.050052, -0.018612, -0.025403, -0.040872, -0.047663, -0.058478, -0.038482, -0.070048, -0.081492, -0.061371, -0.0703,
  -0.070928, -0.057598, -0.043387, -0.019367, -0.058855, -0.050681, -0.043387, -0.025026, -0.026158, -0.023643, -0.054831, -0.050681, -0.047914, -0.060993, -0.079983, -0.057346,
  -0.068665, -0.085265, -0.099476, -0.090044, -0.069294, -0.068665, -0.055837, -0.037728, -0.033075, -0.030811, -0.041249, -0.04716, -0.051561, -0.046154, -0.086774, -0.070803,
  -0.074324, -0.07118, -0.053071, -0.025655, -0.012199, -0.078474, -0.081115, -0.057724, -0.085894, -0.060993, -0.073318, -0.061622, -0.06703, -0.048795, -0.046154, -0.065521,
  -0.070174, -0.054077, -0.084259, -0.06288, -0.061496, -0.066653, -0.037854, -0.022008, -0.05634, -0.080989, -0.079983, -0.058855, -0.047914, -0.070803, -0.053196, -0.073821,
  -0.06703, -0.045022, -0.038482, -0.033578, -0.02817, -0.034081, -0.03471, -0.062251, -0.04062, -0.0054077, -0.012827, -0.04892, -0.069545, -0.081995, -0.076588, -0.076965,
  -0.07948, -0.093942, -0.061622, -0.072941, -0.046028, -0.031817, -0.061371, -0.055711, -0.052064, -0.022762, -0.037351, -0.035087, -0.021631, -0.017481, -0.037225, -0.048166,
  -0.057346, -0.074701, -0.07948, -0.0869, -0.078474, -0.085139, -0.07206, -0.089792, -0.08778, -0.044267, -0.076713, -0.011318, -0.053825, -0.023894, -0.046908, -0.061874,
  -0.034961, -0.049046, -0.055586, -0.080235, -0.05546, -0.081115, -0.067156, -0.065647, -0.058227, -0.080235, -0.068665, -0.072438, -0.060239, -0.049424, -0.037728, -0.03471,
  -0.021756, -0.0249, -0.057975, -0.090044, -0.093188, -0.077468, -0.064263, -0.072186, -0.058227, -0.081115, -0.04804, -0.045902, -0.040872, -0.040117, -0.035338, -0.035841,
  -0.028547, -0.0050304, -0.037225, -0.073066, -0.1069, -0.07445, -0.048543, -0.039237, -0.021253, -0.01157, -0.037351, -0.063257, -0.08451, -0.086523, -0.059862, -0.038482,
  -0.047034, -0.034332, -0.054328, -0.047286, -0.057221, -0.075582, -0.070928, -0.096458, -0.095452, -0.065521, -0.07533, -0.045022, -0.064012, -0.049298, -0.038985, -0.034081,
  -0.041249, -0.027919, -0.019241, -0.034961, -0.051813, -0.065521, -0.081492, -0.080109, -0.078222, -0.065269, -0.065395, -0.072941, -0.072941, -0.081241, -0.040746, -0.03559,
  -0.035967, -0.041249, -0.029931, -0.037979, -0.037225, -0.057346, -0.067659, -0.038734, -0.028296, -0.062754, -0.069419, -0.093942, -0.068287, -0.089289, -0.055837, -0.048292,
  -0.011444, -0.00012576, -0.024397, -0.044645, -0.11255, -0.11042, -0.093439, -0.03886, -0.02314, -0.074198, -0.078474, -0.06879, -0.082498, -0.064389, -0.065395, -0.052693,
  -0.080989, -0.053699, -0.065018, -0.01245, 0.016852, 0.011318, -0.047034, -0.06791, -0.094194, -0.090421, -0.078222, -0.073066, -0.072312, -0.061748, -0.01987, -0.035338,
  -0.01987, -0.050178, -0.031063, -0.022008, -0.040369, -0.039363, -0.061874, -0.062628, -0.089541, -0.10098, -0.10048, -0.073695, -0.078977, -0.05634, -0.05961, -0.060993,
  -0.042507, -0.052568, -0.027164, -0.035716, -0.035213, -0.034835, -0.054454, -0.049801, -0.063509, -0.062377, -0.068539, -0.066778, -0.066275, -0.065772, -0.060239, -0.060868,
  -0.039866, -0.03471, -0.036345, -0.041375, -0.082247, -0.03886, -0.047537, -0.02905, -0.067407, -0.063509, -0.058227, -0.045022, -0.017984, -0.073821, -0.11733, -0.10815,
  -0.09017, -0.08451, -0.078097, -0.058352, -0.062125, -0.027164, -0.036345, -0.034207, -0.063131, -0.069922, -0.073444, -0.054202, -0.05873, -0.057095, -0.06703, -0.065647,
  -0.04892, -0.02641, -0.037854, -0.058855, -0.043261, -0.062125, -0.045776, -0.031943, -0.043639, -0.058478, -0.072689, -0.061748, -0.075959, -0.045399, -0.052568, -0.030811,
  -0.00025152, -0.046657, -0.084133, -0.099476, -0.099476, -0.072815, -0.074575, -0.057975, -0.051687, -0.031943, -0.053574, -0.059987, -0.066024, -0.06615, -0.076839, -0.068287,
  -0.053951, -0.051184, -0.037476, -0.023391, -0.013959, -0.049298, -0.046154, -0.041375, -0.030937, -0.0093062, -0.0030182, -0.048795, -0.13846, -0.15997, -0.16047, -0.10564,
  -0.06615, -0.054328, -0.063634, -0.040998, -0.012073, -0.013079, -0.013708, -0.035464, -0.040746, -0.02314, -0.054202, -0.075582, -0.078222, -0.05634, -0.067784, -0.066904,
  -0.066778, -0.059359, -0.04301, -0.039992, -0.056718, -0.029176, -0.048166, -0.010815, -0.038608, -0.040243, -0.061622, -0.083127, -0.084762, -0.10375, -0.093565, -0.085517,
  -0.10501, -0.093314, -0.10463, -0.080738, -0.075959, -0.05961, -0.058101, -0.046405, -0.066653, -0.032697, -0.025655, -0.026661, -0.010815, -0.044645, -0.036973, -0.048795,
  -0.049801, -0.050807, -0.041249, -0.021128, -0.027919, -0.051561, -0.057221, -0.07948, -0.071306, -0.0703, -0.050304, -0.049801, -0.062377, -0.053196, -0.03471, -0.052819,
  -0.063131, -0.050304, -0.05458, -0.073066, -0.084133, -0.040998, -0.066778, -0.056215, -0.089038, -0.073947, -0.085139, -0.089541, -0.075959, -0.056466, -0.05219, -0.07206,
  -0.047789, -0.021128, 0.0017606, -0.046908, -0.068162, -0.071557, -0.058101, -0.048292, -0.059987, -0.018864, -0.056466, -0.049549, -0.020373, -0.051436, -0.056592, -0.076839,
  -0.087529, -0.053196, -0.076965, -0.062503, -0.06464, -0.070425, -0.041123, -0.056969, -0.032697, -0.036848, -0.033326, -0.046908, -0.015971, -0.021379, -0.066653, -0.07621,
  -0.081869, -0.082373, -0.10086, -0.084007, -0.056843, -0.080863, -0.084133, -0.076839, -0.053322, -0.04477, -0.046783, -0.075456, -0.075707, -0.070803, -0.056843, -0.058855,
  -0.048669, -0.055586, -0.052819, -0.055837, -0.058352, -0.045273, -0.054454, -0.058855, -0.044016, -0.034584, -0.01899, -0.014085, 0.0075456, 0.058855, 0.040746, 0.040998,
  -0.02402, -0.11344, -0.22687, -0.19732, -0.1704, -0.12023, -0.10325, -0.064515, -0.016726, -0.0044016, -0.0042758, -0.02729, -0.026913, -0.032194, -0.042632, -0.011696,
  -0.026535, -0.049424, -0.04628, -0.078725, -0.085642, -0.064263, -0.080989, -0.10275, -0.089541, -0.07206, -0.057472, -0.083127, -0.061119, -0.050052, -0.05219, -0.049927,
  -0.050681, -0.071809, -0.066653, -0.068162, -0.066778, -0.070677, -0.060113, -0.068916, -0.043136, -0.043261, -0.05219, -0.046531, -0.035967, -0.028799, -0.022511, -0.027541,
  -0.041752, -0.061999, -0.068287, -0.060993, -0.093565, -0.074953, -0.079732, -0.071431, -0.045776, -0.052819, -0.044016, -0.053196, -0.048292, -0.053951, -0.073695, -0.07118,
  -0.066527, -0.055208, -0.072941, -0.082247, -0.084636, -0.0703, -0.078474, -0.06376, -0.039866, -0.053574, -0.05219, -0.019744, 0.033075, 0.041752, -0.025403, -0.065647,
  -0.13305, -0.11532, -0.12387, -0.11117, -0.089289, -0.051687, -0.034207, -0.03559, -0.032823, -0.0022637, -0.0091804, -0.025026, -0.060113, -0.086145, -0.087277, -0.066024,
  -0.069168, -0.08778, -0.05131, -0.066275, -0.040243, -0.03144, -0.027919, -0.066778, -0.072563, -0.077971, -0.067533, -0.039489, -0.032949, -0.081492, -0.059233, -0.072815,
  -0.064012, -0.021631, 0.0015091, -0.05131, -0.09608, -0.073066, -0.037099, -0.025529, -0.0030182, -0.047286, -0.10187, -0.11947, -0.099979, -0.094823, -0.10212, -0.089038,
  -0.057095, -0.02075, 0.0051561, 0.027919, 0.045022, -0.0049046, -0.058478, -0.076965, -0.049927, -0.13381, -0.19002, -0.18285, -0.16864, -0.14311, -0.13205, -0.074198,
  -0.057724, 0.0052819, 0.014965, 0.017355, 0.029302, 0.020247, 0.0083001, -0.047411, -0.020499, -0.035841, -0.027416, -0.033955, -0.063131, -0.07445, -0.041501, -0.015091,
  -0.01987, 0.0065395, -0.010564, -0.019744, -0.07118, -0.084007, -0.087151, -0.084762, -0.098721, -0.12262, -0.07206, -0.10337, -0.07118, -0.089164, -0.086397, -0.12161,
  -0.12299, -0.12802, -0.069922, -0.014714, 0.011193, 0.04628, 0.00050304, -0.05458, -0.083756, -0.077719, -0.074072, -0.045902, -0.012073, 0.06288, 0.076588, -0.003144,
  -0.10124, -0.1484, -0.17367, -0.15217, -0.11645, -0.13192, -0.1035, -0.065018, -0.06791, -0.073318, -0.077594, -0.062125, -0.07948, -0.072941, -0.063257, 0.0088032,
  -0.015217, -0.017606, 0.026787, 0.019241, 0.018109, -0.012953, -0.019115, -0.027164, -0.052819, -0.085642, -0.053574, -0.058352, -0.06288, -0.040998, -0.059107, -0.085894,
  -0.11482, -0.11067, -0.057975, 0.020122, 0.018612, -0.05458, -0.12878, -0.17028, -0.13205, -0.088661, -0.11243, -0.061119, -0.039237, -0.030811, -0.097338, -0.1289,
  -0.079983, -0.022762, -0.011821, -0.0096835, -0.042507, -0.012199, 0.024272, 0.024397, -0.0040243, -0.033201, 0.088661, 0.062377, 0.0023894, -0.10954, -0.17694, -0.18952,
  -0.14953, -0.12513, -0.1069, -0.061119, -0.074198, -0.032194, -0.036973, -0.04804, -0.022008, 0.034081, -0.033829, -0.078725, -0.085265, -0.024272, 0.055711, 0.09935,
  -0.0033955, -0.14399, -0.2148, -0.1982, -0.19996, -0.186, -0.16839, -0.099602, -0.088157, -0.032446, -0.023014, 0.010438, 0.014337, 0.036345, 0.025906, 0.029679,
  -0.02314, 0.012827, 0.098721, 0.099099, 0.053951, -0.07445, -0.21618, -0.32647, -0.27856, -0.15632, -0.12035, -0.1206, -0.073318, -0.040998, 0.015217, 0.025781,
  0.059987, 0.11947, 0.11847, 0.0023894, -0.028673, -0.027667, -0.10929, -0.15167, -0.15959, -0.067659, -0.038357, -0.088661, -0.12551, -0.13934, -0.096709, 0.021128,
  0.051058, -0.06879, -0.11972, -0.04804, -0.063509, -0.097338, -0.099853, -0.094445, -0.066401, -0.04892, -0.03056, -0.097841, -0.10388, -0.076462, -0.042255, 0.037099,
  0.17556, 0.25768, 0.10174, -0.12501, -0.33741, -0.39765, -0.28912, -0.19354, -0.1196, -0.10664, -0.099476, -0.035087, 0.003647, 0.073318, 0.042004, 0.029428,
  0.03647, 0.036093, 0.052693, 0.14953, 0.19203, 0.43714, 0.23404, -0.15594, -0.43639, -0.51838, -0.44569, -0.11507, -0.050681, -0.11494, -0.2241, -0.22712,
  -0.058352, -0.026661, -0.0030182, 0.0044016, 0.19945, 0.21744, 0.15783, 0.024146, -0.15242, -0.33515, -0.39375, -0.35389, -0.22423, -0.1284, -0.061119, 0.0057849,
  0.11507, 0.15468, 0.12425, 0.075582, 0.052064, 0.062628, 0.013834, 0.0028925, 0.035464, -0.077971, 0.00075456, 0.1323, 0.062125, -0.0025152, -0.43161, -0.69168,
  -0.58654, -0.29843, -0.082121, 0.20235, 0.20134, 0.092559, 0.0013834, -0.051813, -0.056592, -0.043513, -0.022762, -0.043136, -0.052819, 0.011067, 0.037476, 0.033326,
  0.0020122, -0.027793, 0.0057849, -0.026661, -0.021756, -0.019115, -0.0023894, 0.20122, 0.35175, 0.10614, -0.17481, -0.18474, -0.2607, -0.28522, -0.43374, -0.51662,
  -0.42268, -0.25215, -0.12199, -0.062125, -0.092811, -0.12375, -0.17493, -0.18625, -0.069419, -0.045022, 0.025655, 0.090798, 0.15795, 0.17845, 0.2646, 0.20197,
  0.032572, -0.055083, -0.015594, 0.049801, 0.072438, 0.059359, 0.027164, 0.088535, 0.21819, 0.04477, -0.19317, -0.3608, -0.43978, -0.41853, -0.35301, -0.14638,
  0.010564, 0.010312, -0.028799, -0.10677, -0.037225, 0.061119, -0.051687, -0.19166, -0.22385, -0.20612, -0.098847, 0.081744, 0.17833, 0.065395, -0.044393, -0.06288,
  0.12752, 0.29013, 0.18524, -0.12714, -0.37816, -0.35376, -0.19203, -0.081241, -0.094068, -0.12387, -0.056843, 0.046405, 0.01157, -0.01245, -0.017103, -0.02075,
  0.014714, 0.0055334, 0.13708, 0.079103, -0.15141, -0.34056, -0.32798, -0.20738, -0.11293, -0.00088032, 0.10614, 0.11004, 0.21656, 0.25454, 0.043764, -0.16286,
  -0.26762, -0.32899, -0.23643, -0.18675, -0.18977, -0.092559, -0.040243, 0.0013834, 0.03559, 0.024146, 0.10727, 0.059107, -0.04892, -0.088032, 0.023517, 0.28057,
  0.14877, -0.28887, -0.44544, -0.32547, -0.15079, -0.11494, -0.088283, -0.054957, 0.071557, 0.062628, 0.021379, -0.028422, -0.047034, 0.039237, 0.13406, 0.051058,
  -0.073192, -0.16864, -0.16022, -0.1235, -0.15443, -0.09935, -0.032069, -0.07533, -0.036848, 0.096332, 0.20449, -0.015846, -0.37803, -0.3808, -0.25793, -0.065521,
  -0.052819, 0.037476, 0.013959, 0.036973, 0.037225, 0.019996, -0.045399, -0.045399, 0.064263, -0.010312, -0.11997, -0.15745, -0.16751, -0.10576, 0.011696, 0.12236,
  0.18109, 0.36634, 0.25969, 0.10438, -0.36181, -0.59736, -0.34634, -0.10639, 0.28698, -0.15053, -0.58365, -0.62402, -0.40998, -0.24322, -0.055586, 0.04301,
  0.12412, 0.1196, 0.072941, 0.057598, 0.072186, 0.07621, 0.093062, 0.057724, 0.028799, 0.039992, 0.048417, 0.031943, 0.038482, 0.0081744, -0.03647, -0.026158,
  -0.043136, -0.050933, -0.059107, -0.044896, -0.049675, -0.048543, -0.065898, -0.097841, -0.068413, -0.054454, 0.029176, -0.12953, -0.36546, -0.46179, -0.35779, -0.12551,
  -0.068916, -0.029554, -0.019493, 0.087906, 0.052568, -0.021631, -0.031188, -0.023391, 0.0059107, 0.072186, 0.20008, 0.13922, 0.013205, -0.12035, -0.2446, -0.13205,
  -0.04628, -0.16261, -0.25542, -0.23115, -0.13444, 0.013079, 0.21429, 0.25642, 0.32911, 0.17443, -0.11117, -0.23504, -0.24498, -0.25139, 0.24963, 0.15305,
  0.096583, -0.25253, -0.78172, -0.96533, -0.78738, -0.44242, -0.051436, 0.18763, 0.39048, 0.29528, 0.061748, -0.019618, 0.052693, 0.097589, 0.22762, 0.56378,
  0.42419, 0.077971, 0.0075456, -0.012827, -0.10602, -0.3515, -0.22788, -0.28082, -0.14425, 0.15682, 0.021002, -0.23177, -0.24334, -0.21832, -0.14915, -0.17594,
  -0.2778, -0.2646, -0.17204, -0.039111, 0.10966, 0.41299, 0.76663, 0.23253, -0.33477, -0.43727, -0.38923, -0.26636, -0.14249, -0.07948, 0.013834, 0.29465,
  0.097086, 0.0013834, -0.012199, 0.19216, 0.19203, 0.061622, -0.20423, -0.37325, -0.23542, -0.37351, -0.31201, -0.21643, -0.1323, -0.075959, -0.082498, 0.038357,
  0.03232, 0.16173, 0.12827, 0.013456, -0.073318, -0.12299, -0.18864, -0.16198, -0.1909, -0.21719, -0.16852, -0.053071, 0.32924, 0.20914, -0.11054, -0.24058,
  -0.17455, -0.073695, -0.0056592, 0.027667, 0.077216, 0.08275, 0.079229, 0.11268, 0.12073, 0.10388, 0.062628, -0.043513, -0.1528, -0.16575, -0.16512, -0.18625,
  -0.20449, -0.11042, -0.013834, -0.10463, -0.14651, -0.17883, -0.16902, -0.031314, -0.088535, 0.14563, 0.092308, -0.099853, -0.42859, -0.52467, -0.435, -0.20738,
  -0.091427, 0.035716, 0.25315, 0.59849, 0.7074, 0.20499, -0.29918, -0.48606, -0.39275, -0.1567, -0.0011318, 0.099476, 0.040243, 0.051184, -0.13481, -0.018612,
  -0.091427, -0.11847, -0.13846, -0.063886, 0.053071, 0.045525, 0.0040243, -0.15003, -0.11268, -0.09105, -0.080612, -0.11306, -0.11582, -0.08036, 0.028547, -0.036722,
  -0.043513, 0.30333, 0.37476, 0.67256, 0.22612, -0.088032, -0.67017, -0.83592, -0.65496, -0.54793, -0.496, -0.27516, -0.21694, -0.050681, 0.0037728, 0.10614,
  0.17745, 0.16449, 0.22612, 0.42331, 0.43777, 0.18977, -0.1079, -0.22737, -0.17631, -0.16122, -0.12287, -0.055208, -0.019241, 0.13444, 0.18814, -0.0091804,
  -0.092056, -0.11117, -0.14576, -0.16751, -0.16776, -0.13293, -0.067784, -0.0056592, 0.0021379, -0.043261, -0.045148, -0.037476, -0.026032, -0.047034, -0.1489, -0.18185,
  -0.1406, -0.10174, -0.061748, -0.087026, -0.03647, 0.033452, 0.087403, -0.059484, -0.09193, -0.21153, -0.21895, -0.21492, -0.17694, -0.055334, -0.058101, -0.06376,
  -0.1235, -0.15733, -0.065521, -0.015846, 0.11909, 0.15582, 0.074701, 0.016349, -0.066904, -0.073947, -0.037979, -0.058227, -0.030182, -0.018235, 0.0020122, 0.065018,
  0.0869, -0.003647, -0.030434, -0.018864, -0.056969, -0.11142, -0.13708, -0.12903, -0.12903, -0.12475, -0.11884, -0.070551, -0.072689, -0.0869, -0.095074, -0.098218,
  -0.073192, -0.097338, -0.084007, -0.087654, -0.07118, -0.06879, -0.042381, -0.033955, -0.048292, -0.039992, -0.033075, -0.0085517, 0.01157, -0.031817, -0.04716, -0.049046,
  -0.052442, -0.039237, -0.077342, -0.093439, -0.078474, -0.081492, -0.071306, -0.056718, -0.053322, -0.03974, -0.034961, -0.03471, -0.023769, -0.061622, -0.050933, -0.018361,
  -0.023643, -0.060868, -0.08778, -0.094068, -0.103, -0.091679, -0.10061, -0.086648, -0.070425, -0.076839, -0.065521, -0.036093, -0.037854, -0.030434, -0.050807, -0.052819,
  -0.047914, -0.029302, -0.03056, -0.053825, -0.069419, -0.061245, -0.059987, -0.062125, -0.043764, -0.064389, -0.050178, -0.065898, -0.057724, -0.049172, -0.041752, -0.041752,
  -0.031566, -0.048669, -0.044267, -0.045022, -0.049298, -0.049927, -0.070928, -0.050052, -0.045148, -0.047411, -0.052442, -0.047537, -0.042129, -0.039111, -0.032069, -0.064515,
  -0.091301, -0.060616, -0.078348, -0.069168, -0.072815, -0.061874, -0.096835, -0.097589, -0.079229, -0.072438, -0.084888, -0.077091, -0.055586, -0.050304, -0.065898, -0.040369,
  -0.029805, -0.03144, -0.03471, -0.044896, -0.038734, -0.055963, -0.058352, -0.058227, -0.05873, -0.053322, -0.07118, -0.028547, -0.011947, -0.038608, -0.054328, -0.045651,
  -0.050555, -0.077971, -0.08451, -0.096709, -0.07948, -0.083127, -0.079983, -0.076085, -0.08036, -0.064892, -0.062125, -0.089667, -0.065395, -0.081115, -0.055586, -0.052442,
  -0.057221, -0.054202, -0.055334, -0.043764, -0.034584, -0.033075, -0.039237, -0.021505, -0.040495, -0.074198, -0.085768, -0.078725, -0.067407, -0.052819, -0.041501, -0.036093,
  -0.04301, -0.03974, -0.042381, -0.036345, -0.027667, -0.029176, -0.040872, -0.04804, -0.058855, -0.061496, -0.073569, -0.068916, -0.0869, -0.052945, -0.060365, -0.04716,
  -0.064389, -0.052819, -0.081115, -0.052945, -0.062125, -0.049046, -0.04628, -0.049675, -0.060868, -0.053196, -0.085139, -0.074701, -0.052316, -0.036219, -0.053196, -0.065521,
  -0.058101, -0.051184, -0.045399, -0.07206, -0.064012, -0.051184, -0.046028, -0.054705, -0.071431, -0.073947, -0.082876, -0.060868, -0.0869, -0.080486, -0.080612, -0.095577,
  -0.049675, -0.042632, -0.042129, -0.0249, -0.024523, -0.025655, -0.019493, -0.02729, -0.034207, -0.038357, -0.035464, -0.042632, -0.04716, -0.065898, -0.072312, -0.0703,
  -0.062251, -0.059862, -0.067533, -0.054202, -0.060113, -0.050304, -0.00088032, -0.0017606, -0.0096835, -0.08602, -0.12714, -0.14903, -0.14148, -0.13242, -0.099853, -0.075456,
  -0.051561, -0.062628, -0.033578, -0.040243, -0.036722, -0.03144, -0.031188, -0.0075456, -0.01069, -0.0027667, -0.030308, -0.047411, -0.06791, -0.044519, -0.059987, -0.047537,
  -0.056718, -0.072186, -0.070677, -0.069294, -0.048292, -0.043764, -0.033829, -0.022008, -0.03974, -0.037602, -0.066778, -0.084007, -0.087151, -0.1001, -0.11344, -0.069671,
  -0.083882, -0.085013, -0.09608, -0.079354, -0.094823, -0.051561, -0.042255, -0.051687, -0.067533, -0.070174, -0.068036, -0.082876, -0.060616, -0.058227, -0.061496, -0.045902,
  -0.040495, -0.049801, -0.046531, -0.034961, -0.027793, -0.022511, -0.028422, -0.035464, -0.030308, -0.032069, -0.049172, -0.068665, -0.047537, -0.060365, -0.062377, -0.06879,
  -0.03886, -0.028799, 0.0095577, -0.0249, -0.063006, -0.10614, -0.087026, -0.1069, -0.10086, -0.1123, -0.075204, -0.075833, -0.079103, -0.061245, -0.066401, -0.066904,
  -0.076588, -0.055586, -0.060239, -0.032446, -0.032194, -0.044142, -0.022888, -0.022008, -0.024146, -0.0041501, -0.012953, -0.030182, -0.028673, -0.047286, -0.054705, -0.070928,
  -0.066653, -0.071054, -0.08778, -0.07948, -0.08602, -0.080486, -0.079354, -0.056843, -0.072941, -0.031188, -0.039363, -0.042255, -0.039237, -0.070048, -0.086648, -0.080738,
  -0.072815, -0.064389, -0.086271, -0.046028, -0.06049, -0.040746, -0.049801, -0.061874, -0.043387, -0.040243, -0.028296, -0.020122, -0.028296, -0.027416, -0.05961, -0.077971,
  -0.077594, -0.070048, -0.073947, -0.067533, -0.063634, -0.087151, -0.072689, -0.064263, -0.054957, -0.023643, -0.061748, -0.051939, -0.046405, -0.040117, -0.030308, -0.038985,
  -0.072941, -0.073695, -0.069671, -0.061496, -0.076965, -0.056592, -0.057724, -0.038231, -0.054705, -0.03647, -0.056718, -0.038608, -0.032446, -0.037728, -0.028422, -0.062377,
  -0.079103, -0.083882, -0.093942, -0.10312, -0.081492, -0.065018, -0.029302, -0.040746, -0.039363, -0.059862, -0.030937, -0.057849, -0.05219, -0.048292, -0.075204, -0.065521,
  -0.087026, -0.084385, -0.061119, -0.067156, -0.072312, -0.066904, -0.062251, -0.078977, -0.083504, -0.057472, -0.052568, -0.046783, -0.02905, -0.034458, -0.029931, -0.009935,
  -0.033201, -0.045651, -0.058478, -0.060239, -0.061999, -0.070551, -0.043639, -0.063886, -0.045148, -0.038357, -0.037854, -0.037728, -0.04716, -0.04892, -0.036219, -0.05043,
  -0.048543, -0.06703, -0.061874, -0.064263, -0.071054, -0.068287, -0.05961, -0.048669, -0.070048, -0.06376, -0.066527, -0.058101, -0.064389, -0.070928, -0.054957, -0.053699,
  -0.062125, -0.069545, -0.077216, -0.079983, -0.066778, -0.064137, -0.068287, -0.068413, -0.04628, -0.041249, -0.050933, -0.059736, -0.040243, -0.060993, -0.056969, -0.047286,
  -0.047914, -0.038608, -0.04389, -0.050178, -0.058352, -0.057346, -0.061119, -0.064892, -0.054831, -0.053699, -0.037099, -0.014085, -0.029805, -0.035213, -0.061748, -0.038608,
  -0.04389, -0.042758, -0.027416, -0.040243, -0.061748, -0.074198, -0.10048, -0.10991, -0.097086, -0.10023, -0.082121, -0.085517, -0.085517, -0.050555, -0.059862, -0.030057,
  -0.039614, -0.017606, -0.017606, -0.0016349, -0.015217, -0.071306, -0.09432, -0.10589, -0.11017, -0.086397, -0.089289, -0.087151, -0.056969, -0.043639, -0.023517, -0.0166,
  0.003144, -0.038734, -0.033704, -0.023014, -0.069042, -0.065395, -0.077845, -0.073444, -0.072815, -0.049298, -0.056466, -0.050304, -0.053825, -0.029302, -0.057598, -0.058227,
  -0.069294, -0.033578, -0.044016, -0.029679, -0.030685, -0.052316, -0.065143, -0.077719, -0.06464, -0.084888, -0.066778, -0.058604, -0.021505, -0.033452, -0.048543, -0.078725,
  -0.086271, -0.068162, -0.069168, -0.065898, -0.073947, -0.062377, -0.05634, -0.060239, -0.072815, -0.052064, -0.058352, -0.063131, -0.059987, -0.074827, -0.04628, -0.057221,
  -0.024775, -0.038985, -0.029176, -0.084888, -0.061119, -0.061748, -0.019367, -0.064766, -0.067659, -0.078977, -0.091553, -0.072815, -0.059736, -0.076462, -0.082121, -0.064766,
  -0.052693, -0.033578, -0.042758, -0.02905, -0.038482, -0.046657, -0.042758, -0.056592, -0.076462, -0.076713, -0.041752, -0.062125, -0.052568, -0.070048, -0.041752, -0.059107,
  -0.050681, -0.061119, -0.046783, -0.030685, -0.042381, -0.026787, -0.030811, -0.063131, -0.070174, -0.082247, -0.066401, -0.076588, -0.081492, -0.06879, -0.06791, -0.084007,
  -0.063006, -0.047789, -0.036219, -0.035716, -0.057472, -0.046154, -0.044142, -0.035967, -0.037099, -0.073192, -0.10514, -0.10249, -0.088283, -0.064263, -0.050933, -0.056969,
  -0.041752, -0.03647, -0.04301, -0.047034, -0.050052, -0.082624, -0.044267, -0.053699, -0.021002, -0.039363, -0.062125, -0.059359, -0.049298, -0.049046, -0.036722, -0.032069,
  -0.058352, -0.04628, -0.029302, -0.054202, -0.081241, -0.076336, -0.065521, -0.052945, -0.063634, -0.076588, -0.081618, -0.062377, -0.061999, -0.077216, -0.078474, -0.068665,
  -0.020876, -0.0089289, -0.015846, -0.054328, -0.086648, -0.11281, -0.11356, -0.09608
};

const double ecg_wave[500] = {
  0, 0.00027337, 0.00054675, 0.00082012, 0.0010935, 0.0013669, 0.0016402, 0.0019136, 0.002187, 0.0024604, 0.0027337, 0.0030071, 0.0032805, 0.0035539, 0.0038272, 0.0041006,
  0.004374, 0.0046473, 0.0049207, 0.0051941, 0.0054675, 0.0057408, 0.0060142, 0.0062876, 0.006561, 0.0068343, 0.0071077, 0.0073811, 0.0076545, 0.0079278, 0.0082012, 0.0084746,
  0.017655, 0.026836, 0.036017, 0.045198, 0.054379, 0.063559, 0.07274, 0.081921, 0.091102, 0.10028, 0.10946, 0.11864, 0.12782, 0.13701, 0.14619, 0.15537,
  0.16455, 0.17373, 0.18291, 0.19209, 0.20127, 0.21045, 0.21963, 0.22881, 0.23799, 0.24718, 0.25636, 0.26554, 0.27472, 0.2839, 0.29308, 0.30226,
  0.31144, 0.32062, 0.3298, 0.33898, 0.3298, 0.32062, 0.31144, 0.30226, 0.29308, 0.2839, 0.27472, 0.26554, 0.25636, 0.24718, 0.23799, 0.22881,
  0.21963, 0.21045, 0.20127, 0.19209, 0.18291, 0.17373, 0.16455, 0.15537, 0.14619, 0.13701, 0.12782, 0.11864, 0.10946, 0.10028, 0.091102, 0.081921,
  0.07274, 0.063559, 0.054379, 0.045198, 0.036017, 0.026836, 0.017655, 0.0084746, 0.0082903, 0.0081061, 0.0079219, 0.0077377, 0.0075534, 0.0073692, 0.007185, 0.0070007,
  0.0068165, 0.0066323, 0.006448, 0.0062638, 0.0060796, 0.0058954, 0.0057111, 0.0055269, 0.0053427, 0.0051584, 0.0049742, 0.00479, 0.0046057, 0.0044215, 0.0042373, 0.0040531,
  0.0038688, 0.0036846, 0.0035004, 0.0033161, 0.0031319, 0.0029477, 0.0027634, 0.0025792, 0.002395, 0.0022108, 0.0020265, 0.0018423, 0.0016581, 0.0014738, 0.0012896, 0.0011054,
  0.00092115, 0.00073692, 0.00055269, 0.00036846, 0.00018423, 0, -0.026194, -0.052388, -0.078582, -0.10478, -0.13097, -0.15716, -0.18336, -0.20955, -0.23575, -0.26194,
  -0.28814, -0.23661, -0.18508, -0.13356, -0.082034, -0.030508, 0.021017, 0.072542, 0.12407, 0.17559, 0.22712, 0.27864, 0.33017, 0.38169, 0.43322, 0.48475,
  0.53627, 0.5878, 0.63932, 0.69085, 0.74237, 0.7939, 0.84542, 0.89695, 0.94847, 1, 0.92644, 0.85288, 0.77932, 0.70576, 0.6322, 0.55864,
  0.48508, 0.41153, 0.33797, 0.26441, 0.19085, 0.11729, 0.043729, -0.029831, -0.10339, -0.17695, -0.25051, -0.32407, -0.39763, -0.47119, -0.54475, -0.61831,
  -0.69186, -0.76542, -0.83898, -0.76907, -0.69915, -0.62924, -0.55932, -0.48941, -0.41949, -0.34958, -0.27966, -0.20975, -0.13983, -0.069915, 0, 0.00018625,
  0.00037251, 0.00055876, 0.00074502, 0.00093127, 0.0011175, 0.0013038, 0.00149, 0.0016763, 0.0018625, 0.0020488, 0.0022351, 0.0024213, 0.0026076, 0.0027938, 0.0029801, 0.0031663,
  0.0033526, 0.0035388, 0.0037251, 0.0039113, 0.0040976, 0.0042839, 0.0044701, 0.0046564, 0.0048426, 0.0050289, 0.0052151, 0.0054014, 0.0055876, 0.0057739, 0.0059601, 0.0061464,
  0.0063327, 0.0065189, 0.0067052, 0.0068914, 0.0070777, 0.0072639, 0.0074502, 0.0076364, 0.0078227, 0.0080089, 0.0081952, 0.0083814, 0.0085677, 0.008754, 0.0089402, 0.0091265,
  0.0093127, 0.009499, 0.0096852, 0.0098715, 0.010058, 0.010244, 0.01043, 0.010617, 0.010803, 0.010989, 0.011175, 0.011362, 0.011548, 0.011734, 0.01192, 0.012107,
  0.012293, 0.012479, 0.012665, 0.012852, 0.013038, 0.013224, 0.01341, 0.013597, 0.013783, 0.013969, 0.014155, 0.014342, 0.014528, 0.014714, 0.0149, 0.015087,
  0.015273, 0.015459, 0.015645, 0.015832, 0.016018, 0.016204, 0.01639, 0.016577, 0.016763, 0.016949, 0.021422, 0.025895, 0.030367, 0.03484, 0.039313, 0.043785,
  0.048258, 0.052731, 0.057203, 0.061676, 0.066149, 0.070621, 0.075094, 0.079567, 0.08404, 0.088512, 0.092985, 0.097458, 0.10193, 0.1064, 0.11088, 0.11535,
  0.11982, 0.12429, 0.12877, 0.13324, 0.13771, 0.14218, 0.14666, 0.15113, 0.1556, 0.16008, 0.16455, 0.16902, 0.17349, 0.17797, 0.17349, 0.16902,
  0.16455, 0.16008, 0.1556, 0.15113, 0.14666, 0.14218, 0.13771, 0.13324, 0.12877, 0.12429, 0.11982, 0.11535, 0.11088, 0.1064, 0.10193, 0.097458,
  0.092985, 0.088512, 0.08404, 0.079567, 0.075094, 0.070621, 0.066149, 0.061676, 0.057203, 0.052731, 0.048258, 0.043785, 0.039313, 0.03484, 0.030367, 0.025895,
  0.021422, 0.016949, 0.016142, 0.015335, 0.014528, 0.013721, 0.012914, 0.012107, 0.011299, 0.010492, 0.0096852, 0.0088781, 0.008071, 0.0072639, 0.0064568, 0.0056497,
  0.0048426, 0.0040355, 0.0032284, 0.0024213, 0.0016142, 0.0008071, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0
};

const double sin_wave[500] = {
  0, 0.012591, 0.02518, 0.037766, 0.050345, 0.062916, 0.075477, 0.088027, 0.10056, 0.11308, 0.12558, 0.13806,
  0.15052, 0.16296, 0.17537, 0.18775, 0.2001, 0.21243, 0.22471, 0.23696, 0.24918, 0.26135, 0.27348, 0.28557, 0.29762, 0.30962, 0.32156, 0.33346,
  0.3453, 0.35709, 0.36883, 0.3805, 0.39212, 0.40367, 0.41515, 0.42658, 0.43793, 0.44922, 0.46043, 0.47157, 0.48264, 0.49363, 0.50454, 0.51537,
  0.52612, 0.53678, 0.54736, 0.55786, 0.56826, 0.57858, 0.5888, 0.59893, 0.60897, 0.61891, 0.62875, 0.63849, 0.64813, 0.65767, 0.6671, 0.67643,
  0.68565, 0.69476, 0.70376, 0.71265, 0.72143, 0.73009, 0.73863, 0.74706, 0.75537, 0.76357, 0.77164, 0.77958, 0.78741, 0.79511, 0.80268, 0.81013,
  0.81744, 0.82463, 0.83169, 0.83861, 0.84541, 0.85206, 0.85859, 0.86497, 0.87122, 0.87734, 0.88331, 0.88914, 0.89483, 0.90038, 0.90579, 0.91105,
  0.91617, 0.92115, 0.92597, 0.93065, 0.93519, 0.93957, 0.94381, 0.9479, 0.95183, 0.95562, 0.95925, 0.96273, 0.96606, 0.96924, 0.97226, 0.97513,
  0.97784, 0.9804, 0.9828, 0.98505, 0.98714, 0.98908, 0.99085, 0.99247, 0.99394, 0.99524, 0.99639, 0.99738, 0.99821, 0.99889, 0.9994, 0.99976,
  0.99996, 1, 0.99988, 0.9996, 0.99916, 0.99857, 0.99782, 0.9969, 0.99584, 0.99461, 0.99322, 0.99168, 0.98998, 0.98813, 0.98611, 0.98395,
  0.98162, 0.97914, 0.9765, 0.97371, 0.97077, 0.96767, 0.96442, 0.96101, 0.95745, 0.95374, 0.94988, 0.94587, 0.94171, 0.9374, 0.93294, 0.92833,
  0.92358, 0.91868, 0.91363, 0.90844, 0.9031, 0.89763, 0.892, 0.88624, 0.88034, 0.8743, 0.86812, 0.8618, 0.85534, 0.84875, 0.84203, 0.83517,
  0.82818, 0.82105, 0.8138, 0.80642, 0.79891, 0.79127, 0.78351, 0.77562, 0.76762, 0.75949, 0.75123, 0.74286, 0.73438, 0.72577, 0.71705, 0.70822,
  0.69927, 0.69022, 0.68105, 0.67178, 0.6624, 0.65291, 0.64332, 0.63363, 0.62384, 0.61395, 0.60396, 0.59388, 0.5837, 0.57343, 0.56307, 0.55262,
  0.54208, 0.53146, 0.52075, 0.50996, 0.49909, 0.48814, 0.47711, 0.46601, 0.45483, 0.44358, 0.43226, 0.42087, 0.40942, 0.3979, 0.38632, 0.37467,
  0.36297, 0.35121, 0.33939, 0.32752, 0.3156, 0.30362, 0.2916, 0.27954, 0.26742, 0.25527, 0.24308, 0.23084, 0.21857, 0.20627, 0.19393, 0.18156,
  0.16917, 0.15675, 0.1443, 0.13183, 0.11933, 0.10682, 0.094296, 0.081754, 0.069198, 0.056632, 0.044056, 0.031474, 0.018886, 0.0062957, -0.0062957, -0.018886,
  -0.031474, -0.044056, -0.056632, -0.069198, -0.081754, -0.094296, -0.10682, -0.11933, -0.13183, -0.1443, -0.15675, -0.16917, -0.18156, -0.19393, -0.20627, -0.21857,
  -0.23084, -0.24308, -0.25527, -0.26742, -0.27954, -0.2916, -0.30362, -0.3156, -0.32752, -0.33939, -0.35121, -0.36297, -0.37467, -0.38632, -0.3979, -0.40942,
  -0.42087, -0.43226, -0.44358, -0.45483, -0.46601, -0.47711, -0.48814, -0.49909, -0.50996, -0.52075, -0.53146, -0.54208, -0.55262, -0.56307, -0.57343, -0.5837,
  -0.59388, -0.60396, -0.61395, -0.62384, -0.63363, -0.64332, -0.65291, -0.6624, -0.67178, -0.68105, -0.69022, -0.69927, -0.70822, -0.71705, -0.72577, -0.73438,
  -0.74286, -0.75123, -0.75949, -0.76762, -0.77562, -0.78351, -0.79127, -0.79891, -0.80642, -0.8138, -0.82105, -0.82818, -0.83517, -0.84203, -0.84875, -0.85534,
  -0.8618, -0.86812, -0.8743, -0.88034, -0.88624, -0.892, -0.89763, -0.9031, -0.90844, -0.91363, -0.91868, -0.92358, -0.92833, -0.93294, -0.9374, -0.94171,
  -0.94587, -0.94988, -0.95374, -0.95745, -0.96101, -0.96442, -0.96767, -0.97077, -0.97371, -0.9765, -0.97914, -0.98162, -0.98395, -0.98611, -0.98813, -0.98998,
  -0.99168, -0.99322, -0.99461, -0.99584, -0.9969, -0.99782, -0.99857, -0.99916, -0.9996, -0.99988, -1, -0.99996, -0.99976, -0.9994, -0.99889, -0.99821,
  -0.99738, -0.99639, -0.99524, -0.99394, -0.99247, -0.99085, -0.98908, -0.98714, -0.98505, -0.9828, -0.9804, -0.97784, -0.97513, -0.97226, -0.96924, -0.96606,
  -0.96273, -0.95925, -0.95562, -0.95183, -0.9479, -0.94381, -0.93957, -0.93519, -0.93065, -0.92597, -0.92115, -0.91617, -0.91105, -0.90579, -0.90038, -0.89483,
  -0.88914, -0.88331, -0.87734, -0.87122, -0.86497, -0.85859, -0.85206, -0.84541, -0.83861, -0.83169, -0.82463, -0.81744, -0.81013, -0.80268, -0.79511, -0.78741,
  -0.77958, -0.77164, -0.76357, -0.75537, -0.74706, -0.73863, -0.73009, -0.72143, -0.71265, -0.70376, -0.69476, -0.68565, -0.67643, -0.6671, -0.65767, -0.64813,
  -0.63849, -0.62875, -0.61891, -0.60897, -0.59893, -0.5888, -0.57858, -0.56826, -0.55786, -0.54736, -0.53678, -0.52612, -0.51537, -0.50454, -0.49363, -0.48264,
  -0.47157, -0.46043, -0.44922, -0.43793, -0.42658, -0.41515, -0.40367, -0.39212, -0.3805, -0.36883, -0.35709, -0.3453, -0.33346, -0.32156, -0.30962, -0.29762,
  -0.28557, -0.27348, -0.26135, -0.24918, -0.23696, -0.22471, -0.21243, -0.2001, -0.18775, -0.17537, -0.16296, -0.15052, -0.13806, -0.12558, -0.11308, -0.10056,
  -0.088027, -0.075477, -0.062916, -0.050345, -0.037766, -0.02518, -0.012591, -2.4493e-16
};

//Obs: A forma de onda quadrada, triangular e rampa sera gerada em tempo de execução

//Tipos de ondas possiveis de se selecionar
typedef enum {
  SIN_WAVE,
  SQUARE_WAVE,
  TRIANGLE_WAVE,
  RAMP_WAVE,
  CONST_WAVE,
  ECG_WAVE,
  EMG_WAVE,
  ADC_WAVE
} waveforms_t;

/////////////////////////////////////////////////
// Implementacao de um timer atraves do micros //
/////////////////////////////////////////////////
class Timer_t {
  private:
    unsigned long _actual_time;
    unsigned long _waited_time;
    bool _running;
    uint32_t _interval;

  public:
    bool elapsed;

    Timer_t(uint32_t interval = 1000) {
      _interval = interval;
      elapsed = false;
      _actual_time = micros();
      _waited_time = _actual_time + interval;
    }

    void setInterval(uint32_t interval) {
      _interval = interval;
    }

    uint32_t getInterval() {
      return _interval;
    }

    void start() {
      _running = true;
      _actual_time = millis();
      _waited_time = _actual_time + _interval;
    }

    void stop() {
      _running = false;
    }

    void wait_next() {
      elapsed = false;
    }

    void update() {
      _actual_time = micros();
      if (_running) {
        if (_actual_time >= _waited_time) {
          _waited_time = _actual_time + _interval;
          elapsed = true;
        }
      }
    }

};

/////////////////////////////////////////
//Classe para gerar as formas de onda //
////////////////////////////////////////

class SignalGenerator {
  private:
    Timer_t _sampling_control;
    waveforms_t _waveform; //Acessible by getter and setter
    uint16_t _actual_index;
    uint8_t _pin_out;
    uint8_t _resolution_bits;
    uint16_t _max_value_resolution;
    double _actual_value;
    double _offset;
    double _amplitude;

    double get_next() {
      switch (_waveform) {
        case SIN_WAVE:
          _actual_value = sin_wave[_actual_index*5];
          break;
        case SQUARE_WAVE:
          _actual_index > 250 ? _actual_value = -1 : _actual_value = 1;
          break;
        case TRIANGLE_WAVE:
          _actual_value = (double) _actual_index / 250.0;
          if (_actual_value > 1) {
            _actual_value = 2 - _actual_value;
          }
          break;
        case RAMP_WAVE:
          _actual_value = (double) _actual_index / 500.0;
          break;
        case CONST_WAVE:
          _actual_value = 1;
          break;
        case ECG_WAVE:
          _actual_value = ecg_wave[_actual_index];
          break;
        case EMG_WAVE:
          _actual_value = emg_wave[_actual_index]; //Work around
          break;
        case ADC_WAVE:
          _actual_value = (double) analogRead(PINOADC) / 1024.0;
          break;
      }
      _actual_value = _actual_value * _amplitude + _offset;
      ++_actual_index %= 100; //Incremento circular
      return _actual_value;
    }

    void begin() {
      //pinMode(_pin_out, OUTPUT);
      //analogWriteResolution(12);
    }

  public:
    SignalGenerator (uint8_t pin_out = DAC0, uint8_t resolution_bits = 12) {
      _pin_out = pin_out;

      _resolution_bits = resolution_bits;
      _max_value_resolution = pow(2, 12) - 1;
      begin();
      _waveform = SIN_WAVE;
      _actual_index = 0;

      _sampling_control.setInterval(1000);
      _offset = 0;
      _amplitude = 100;
    }

    void start() {
      _sampling_control.start();
    }

    void stop() {
      _sampling_control.stop();
    }

    void generate_value() {
      get_next();
      //analogWrite(DAC0,(uint16_t) _actual_value);
      //analogWrite(DAC1,(uint16_t) _actual_value);
      //Serial.println(String((uint16_t) _actual_value));
      Serial.write('j');
      Serial.write((uint8_t) ((uint16_t) _actual_value >> 8));
      Serial.write((uint8_t) ((uint16_t) _actual_value));
      //Serial.write('\n');
    
    }

    void update() {
      _sampling_control.update();
      if (_sampling_control.elapsed) {
        generate_value();
        _sampling_control.wait_next();
      }
    }

    ////////////////////////
    //Getters and Setters //
    ////////////////////////
    void setAquireInterval(uint32_t interval) {
      _sampling_control.setInterval(interval);
    }

    uint32_t getAquireInterval() {
      return _sampling_control.getInterval();
    }

    void setFreq(double frequency) {
      // 500 ticks /s = 1 Hz
      // 500Hz = 1Hz
      // 5000Hz = 10Hz
      // 5000Hz = 0.2ms
      frequency = frequency * 500;
      setAquireInterval((uint32_t) (1000000 / frequency));
    }

    double getFreq() {
      //500 ticks /s = 1 Hz
      return (double) 500 * 1000000 / (double) getAquireInterval();
    }

    waveforms_t getWaveform() {
      return _waveform;
    }

    void setWaveform(waveforms_t waveform) {
      _waveform = waveform;
    }

    void setAmplitude(double amplitude) {
      _amplitude = amplitude;
    }

    void setOffset(double offset) {
      _offset = offset;
    }
};

//////////////////////
//Variaveis globais //
//////////////////////
const int chaves[] = {2, 3, 4, 5, 6, 7};
SignalGenerator my_generator; //lazy thing, work around...
bool status_led = false;
char serialOp;

void timerDataAcq();

//////////////////
//Main Function //
//////////////////
void setup() {
  //analogWriteResolution(12);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(UART_BAUDRATE);
  Serial.println("Signal Generator Started!");
  my_generator.setOffset(512);
  my_generator.setAmplitude(512);
  my_generator.setWaveform(SIN_WAVE);
  //  my_generator.setFreq(1); //1Hz
  //  my_generator.start();
  delay(100);
  Timer3.attachInterrupt(timerDataAcq).setFrequency(1000).start();//100Hz
}
void loop() {
  if (Serial.available()) {
    switch (Serial.read()) {
      case 's':
        Timer3.attachInterrupt(timerDataAcq).setFrequency(1000).start();//100Hz
        break;
      case 'p':
        Timer3.stop();
        break;
      default:
        //TODO: Imaginar outros comandos
        break;
    }
  }
}

void timerDataAcq() {
  //Serial.println(4);
  my_generator.generate_value();
}