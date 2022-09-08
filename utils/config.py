# -*- codeing = utf-8 -*-
# @Time : 8/22/2022 12:06 AM
# @Author : Shao
# @File : config.py
# @Software : PyCharm

INDEX = [
    161, 162, 165, 170, 173, 181, 190, 191, 196, 197, 198, 205, 210, 211, 214, 225, 233, 234, 600, 601,
    606, 607, 608, 609, 615, 616, 627, 634, 649, 658, 663, 665, 681, 689, 695, 698, 706, 712, 721, 725,
    747, 758, 777, 778, 779, 801, 820, 823, 831, 858, 867, 868, 875, 884, 897, 900, 902, 908, 918, 926,
    927, 969, 998, 999, 1010, 1011, 1013, 1014, 1015, 1046, 1051, 1052, 1056, 1057, 1062, 1066, 1077, 1078,
    1080, 1081, 1087, 1102, 1108, 1109, 1123, 1129, 1132, 1153, 1154, 1155, 1167, 1175, 1178, 1185, 1186,
    1191, 1193, 1202, 1203, 1207, 1227, 1234, 1240, 1261, 1271, 1276, 1283, 1285, 1295, 1319, 1328, 1337,
    1344, 1352, 1355, 1363, 1380, 1386, 1387, 1388, 1417, 1418, 1438, 1444, 1450, 1459, 1462, 1470, 1474,
    1482, 1484, 1485, 1491, 1504, 1523, 1538, 1559, 1571, 1577, 1581, 1588, 1592, 1613, 1616, 1620, 1633,
    1679, 1681, 1682, 1702, 1706, 1710, 1716, 1753, 1761, 1767, 1775, 1803, 1812, 1820, 1822, 1829, 1844,
    1872, 1884, 1890, 1895, 1898, 1900, 1901, 1921, 1922, 1923, 1930, 1948, 1959, 1962, 1965, 1967, 1973,
    1985, 1996, 2003, 2009, 2014, 2015, 2018, 2019, 2020, 2021, 2025, 2026, 2027, 2028, 2029, 2031, 2035,
    2045, 2046, 2069, 2070, 2098, 2124, 2135, 2157, 2159, 2193, 2200, 2228, 2242, 2255, 2256, 2266, 2304,
    2309, 2315, 2327, 2330, 2333, 2334, 2335, 2364, 2378, 2384, 2386, 2387, 2390, 2400, 2458, 2464, 2470,
    2474, 2477, 2481, 2488, 2494, 2515, 2520, 2525, 2535, 2537, 2539, 2542, 2544, 2565, 2566, 2569, 2583,
    2584, 2593, 2612, 2615, 2645, 2657, 2666, 2677, 2678, 2680, 2681, 2696, 2700, 2711, 2718, 2733, 2746,
    2767, 2770, 2771, 2780, 2786, 2803, 2831, 2844, 2848, 2876, 2917, 2926, 2929, 2930, 2935, 2936, 2937,
    2938, 2942, 2970, 2972, 2976, 2980, 2981, 2982, 2997, 3000, 3005, 3009, 3014, 3026, 3030, 3041, 3044,
    3045, 3046, 3068, 3074, 3076, 3085, 3091, 3102, 3135, 3143, 3155, 3156, 3198, 3220, 3224, 3234, 3238,
    3267, 3298, 3300, 3322, 3326, 3332, 3336, 3337, 3338, 3368, 3372, 3374, 3382, 3386, 3403, 3416, 3436,
    3440, 3448, 3450, 3475, 3508, 3520, 3521, 3525, 3529, 3534, 3540, 3541, 3554, 3561, 3569, 3584, 3589,
    3607, 3643, 3651, 3668, 3670, 3675, 3690, 3709, 3722, 3754, 3756, 3770, 3772, 3779, 3788, 3855, 3860,
    3978, 4200, 4337, 4341, 4345, 4353, 4361, 4393, 4396, 4399, 4400, 4430, 4444, 4488, 4494, 4519, 4520,
    4521, 4524, 4527, 4546, 4573, 4626, 4671, 4675, 4736, 4747, 4750, 4758, 4760, 4762, 4788, 4799, 4803,
    4804, 4834, 4844, 4863, 4881, 4883, 4885, 4886, 4895, 4906, 4907, 4931, 4938, 4944, 4950, 4955, 4972,
    4973, 4974, 4987, 5000, 5005, 5006, 5007, 5008, 5018, 5022, 5027, 5050, 5065, 5069, 5081, 5094, 5095,
    5114, 5115, 5131, 5133, 5139, 5143, 5173, 5185, 5189, 5192, 5202, 5218, 5219, 5247, 5267, 5269, 5289,
    5313, 5345, 5375, 5409, 5450, 5485]

DATASET_INDEX = [1, 2, 3, 4, 5, 6, 7, 8, 20, 55, 67, 86, 100, 101, 107, 137, 140, 141, 145, 150, 152, 155, 158, 160,
                 161, 162, 165, 170, 173, 181, 190, 191, 196, 197, 198, 205, 210, 211, 214, 225, 233, 234, 600, 601,
                 606, 607, 608, 609, 615, 616, 627, 634, 649, 658, 663, 665, 681, 689, 695, 698, 706, 712, 721, 725,
                 747, 758, 777, 778, 779, 801, 820, 823, 831, 858, 867, 868, 875, 884, 897, 900, 902, 908, 918, 926,
                 927, 969, 998, 999, 1010, 1011, 1013, 1014, 1015, 1046, 1051, 1052, 1056, 1057, 1062, 1066, 1077, 1078,
                 1080, 1081, 1087, 1102, 1108, 1109, 1123, 1129, 1132, 1153, 1154, 1155, 1167, 1175, 1178, 1185, 1186,
                 1191, 1193, 1202, 1203, 1207, 1227, 1234, 1240, 1261, 1271, 1276, 1283, 1285, 1295, 1319, 1328, 1337,
                 1344, 1352, 1355, 1363, 1380, 1386, 1387, 1388, 1417, 1418, 1438, 1444, 1450, 1459, 1462, 1470, 1474,
                 1482, 1484, 1485, 1491, 1504, 1523, 1538, 1559, 1571, 1577, 1581, 1588, 1592, 1613, 1616, 1620, 1633,
                 1679, 1681, 1682, 1702, 1706, 1710, 1716, 1753, 1761, 1767, 1775, 1803, 1812, 1820, 1822, 1829, 1844,
                 1872, 1884, 1890, 1895, 1898, 1900, 1901, 1921, 1922, 1923, 1930, 1948, 1959, 1962, 1965, 1967, 1973,
                 1985, 1996, 2003, 2009, 2014, 2015, 2018, 2019, 2020, 2021, 2025, 2026, 2027, 2028, 2029, 2031, 2035,
                 2045, 2046, 2069, 2070, 2098, 2124, 2135, 2157, 2159, 2193, 2200, 2228, 2242, 2255, 2256, 2266, 2304,
                 2309, 2315, 2327, 2330, 2333, 2334, 2335, 2364, 2378, 2384, 2386, 2387, 2390, 2400, 2458, 2464, 2470,
                 2474, 2477, 2481, 2488, 2494, 2515, 2520, 2525, 2535, 2537, 2539, 2542, 2544, 2565, 2566, 2569, 2583,
                 2584, 2593, 2612, 2615, 2645, 2657, 2666, 2677, 2678, 2680, 2681, 2696, 2700, 2711, 2718, 2733, 2746,
                 2767, 2770, 2771, 2780, 2786, 2803, 2831, 2844, 2848, 2876, 2917, 2926, 2929, 2930, 2935, 2936, 2937,
                 2938, 2942, 2970, 2972, 2976, 2980, 2981, 2982, 2997, 3000, 3005, 3009, 3014, 3026, 3030, 3041, 3044,
                 3045, 3046, 3068, 3074, 3076, 3085, 3091, 3102, 3135, 3143, 3155, 3156, 3198, 3220, 3224, 3234, 3238,
                 3267, 3298, 3300, 3322, 3326, 3332, 3336, 3337, 3338, 3368, 3372, 3374, 3382, 3386, 3403, 3416, 3436,
                 3440, 3448, 3450, 3475, 3508, 3520, 3521, 3525, 3529, 3534, 3540, 3541, 3554, 3561, 3569, 3584, 3589,
                 3607, 3643, 3651, 3668, 3670, 3675, 3690, 3709, 3722, 3754, 3756, 3770, 3772, 3779, 3788, 3855, 3860,
                 3978, 4200, 4337, 4341, 4345, 4353, 4361, 4393, 4396, 4399, 4400, 4430, 4444, 4488, 4494, 4519, 4520,
                 4521, 4524, 4527, 4546, 4573, 4626, 4671, 4675, 4736, 4747, 4750, 4758, 4760, 4762, 4788, 4799, 4803,
                 4804, 4834, 4844, 4863, 4881, 4883, 4885, 4886, 4895, 4906, 4907, 4931, 4938, 4944, 4950, 4955, 4972,
                 4973, 4974, 4987, 5000, 5005, 5006, 5007, 5008, 5018, 5022, 5027, 5050, 5065, 5069, 5081, 5094, 5095,
                 5114, 5115, 5131, 5133, 5139, 5143, 5173, 5185, 5189, 5192, 5202, 5218, 5219, 5247, 5267, 5269, 5289,
                 5313, 5345, 5375, 5409, 5450, 5485, 5489, 5496, 5501, 5505, 5507, 5516, 5521, 5528, 5553, 5559, 5560]
