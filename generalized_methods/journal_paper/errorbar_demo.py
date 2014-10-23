#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pdb
# example data
'''
gammas = [0.001,0.005, 0.01,0.05,0.1,0.5,1,5,10,50,100,150,200,300,400,500,1000]

x = np.arange(17)

ymat = np.load('gamma_variation_sensitivity.npy')
ymat = ymat.reshape((15,17))
ymean  = ymat.mean(axis=0)

yerr_upper = ymat.max(axis=0) - ymean
yerr_lower = ymean - ymat.min(axis=0)

# example variable error bar values


# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, ymean, yerr=[yerr_lower, yerr_upper],fmt='o')

plt.axis([0,17,0,100])
plt.xticks(np.arange(17),gammas)

plt.xlabel('gamma values')
plt.ylabel('Average dice measure')
plt.show()
#plt.savefig(fname = 'gamma_variation.eps', dpi=120)
# Now switch to a more OO interface to exercise more features.
'''
'''
#________________________________________________________________________________________________________________________________

ymat = np.load('c_variation_sensitivity.npy')
Cs = [1,5,10,25,50,75,100,150,200,250,300,400,500,750,1000,1250,1500]
ymat = ymat.reshape((15,17))
ymean  = ymat.mean(axis=0)
x = np.arange(17)
yerr_upper = ymat.max(axis=0) - ymean
yerr_lower = ymean - ymat.min(axis=0)

# example variable error bar values


# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, ymean, yerr=[yerr_lower, yerr_upper],fmt='o')

plt.axis([0,17,0,100])
plt.xticks(np.arange(17),Cs)

plt.xlabel('C values')
plt.ylabel('Average dice measure')
plt.show()
#plt.savefig(fname = 'C_variation.eps', dpi=120)
'''
#------------------------------------------------------------------------------------------------------------------------------------
'''
Factors = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,50])
mask = [0,7,12,17,22,23,24,25,26,27]
x = np.arange(len(Factors))

ymat = np.array([66.3082867,67.2302335,69.0286384,67.9647716,67.826511,66.6569785,67.9769242,64.641953,67.115671,71.1176489,63.66821,68.1869923,49.631507,35.3377218,65.902889,69.9684624,69.2884507,67.428882,50.7771383,47.5822636,49.5339692,67.1360602,47.3107025,45.7211063,50.6177652,40.2189135,48.213649,47.6256827,77.5962828,78.3798159,77.653164,76.8018755,77.6166628,77.7040143,76.8789181,76.9822891,76.281492,78.4217981,78.1233291,77.7036313,76.6579247,77.0508166,75.0406509,76.7205628,75.154843,78.1978599,75.7355322,79.127672,76.2264925,77.2554869,72.9440426,72.4021024,76.938539,74.9502348,76.2377115,78.2735656,70.3082279,66.615634,70.6590427,67.9426893,66.9907355,65.3702092,64.3942987,63.1107797,73.204839,72.6936391,60.2448906,69.9217453,72.1050382,65.8164812,66.964272,64.5912673,66.0825306,58.6325629,66.5043774,64.8262058,64.8211247,63.6051023,67.9956301,66.0808035,55.0693859,61.4945148,66.4798963,68.3230027,76.2832908,75.7251498,74.753151,54.6667794,76.6837057,74.9660265,68.1140826,75.4714654,72.7047556,76.2490864,33.7983031,77.1977692,69.9905391,67.5704347,33.5827103,73.2458711,75.6274371,18.6510075,58.7927189,76.3968129,52.2935069,66.0592043,58.3565374,77.2882162,49.2822627,59.7722181,31.6356292,74.4828813,49.6127019,44.3718146,61.0275823,52.1120263,51.6305415,47.5180978,51.7384999,37.0527218,54.4869466,28.3593989,37.0649599,42.2482922,36.4569041,56.3542891,36.2855517,54.0733034,42.5479401,43.0008155,47.599849,55.0844637,42.5658389,53.0702588,21.2969211,50.317561,50.9225245,27.6760744,27.2260197,50.03786,62.5308659,62.7339932,65.8783202,59.1214273,60.4734516,59.4228967,54.8129001,63.4894852,49.9211832,61.223264,65.0185133,47.6026752,41.5803136,58.8114008,45.8631964,34.2433725,68.0152799,35.0803382,49.4597443,55.7062751,18.9002934,40.5830564,43.7644221,24.4602475,46.0275766,65.5856152,39.6979356,34.7031047,77.816917,78.4031158,76.7092936,77.5127312,79.3224531,76.1368663,75.9034961,72.122051,77.3663953,73.1202462,74.4397853,73.1928392,71.7245031,76.2845758,70.0991315,73.800045,72.5560467,73.4151198,72.9637064,66.5924192,74.0388918,73.0588267,73.8767593,71.4054754,68.3423258,72.1426408,67.3927141,64.7220776,80.1884351,80.3687029,79.3153366,80.4281812,80.1709555,80.6149763,79.4149562,79.9458606,79.7543992,79.7189252,78.4510304,78.2384909,79.5299062,80.2504539,75.9446769,78.4639381,80.4703757,78.5862071,79.0479507,76.9307369,75.983809,81.4028609,78.8539988,70.4710968,79.0976413,79.0091941,77.6827598,79.525173,78.7850759,78.3285214,77.2280844,77.2146799,70.425883,77.9468235,72.0646232,73.1177085,78.9594316,73.3087341,70.1173185,75.8279428,74.7910793,76.9424241,77.5594625,74.5888118,70.2857305,76.7974892,76.4402948,75.0501865,71.1633893,72.0893189,77.4704826,67.6521931,72.9748458,72.3627869,74.2887425,68.0761293,67.1927649,66.6706187,69.301429,66.2575998,67.1845464,67.5823456,66.383472,65.0844509,65.8095312,61.7976706,67.1798486,66.8001399,66.2805581,60.6541308,63.619699,61.0915161,65.8249593,62.2507371,65.3370195,65.9506818,62.151743,60.3863239,61.9775354,59.7288085,64.1411603,64.871017,59.5044376,61.2512465,63.8577186,65.2369039,65.0079005,64.7164926,63.4282308,63.7248674,60.6226586,63.3241952,60.2179949,58.5549679,64.1343831,61.9702052,59.9559034,59.4419691,56.3918021,61.134527,56.5157286,62.3219383,59.3046588,59.888862,59.3643429,62.1903236,61.9037174,60.6802357,57.7351261,57.2015461,58.9543387,48.2214194,74.3367428,75.0373254,75.0591057,75.8015575,74.83692,76.9640368,74.6608012,72.5467787,75.2116991,69.8014193,74.1445943,73.3808986,70.280424,68.0347016,68.6713271,68.8712881,69.1109252,72.8385887,76.6232824,64.6522868,65.9904523,67.3159356,75.7664336,74.9893215,72.2661479,70.161251,74.0336854,64.8850024,67.8620721,63.1804205,60.5651934,63.7273403,60.8080466,60.8027918,61.1927626,59.2896006,54.5690125,56.8551822,60.6099602,52.7895263,53.1560831,58.033764,60.5755331,56.7926597,59.8968525,53.9177903,59.2920161,63.2256607,52.5314089,50.5040906,67.8002015,57.7720876,74.9677079,53.4330363,54.1723282,53.7989584,66.5005599,68.2620293,64.2754856,64.3855235,64.8436301,65.7092219,63.7409836,66.8361522,62.7724064,58.6173797,59.5298234,58.2495432,58.8841034,60.2954952,57.8574126,59.8798595,56.9167524,59.1448485,69.5202184,57.1876203,58.2478345,58.9315787,66.3617661,58.1094931,55.4127446,58.6012751,54.9535403,58.0356783,69.6956654,67.7195614,70.4636127,70.6814256,67.8051306,68.5281757,72.0480422,71.4720669,67.2416215,66.0262525,67.9690222,67.9218263,73.3056148,70.4505703,65.4232837,60.2764416,52.2476538,61.5065976,41.2758382,69.9232411,59.0715333,64.8146454,50.4454336,63.263017,38.8758038,38.8995968,38.5467873,43.5883665])
#np.save('gamma_variation_time_sensitivity.npy',ymat)

#pdb.set_trace()
ymat = ymat.reshape((15,len(Factors)))
ymat = ymat[:,mask]
ymean  = ymat.mean(axis=0)

yerr_upper = ymat.max(axis=0) - ymean
yerr_lower = ymean - ymat.min(axis=0)



# example variable error bar values

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
#plt.errorbar(x, ymean, yerr=[yerr_lower, yerr_upper],fmt='s', mfc='black', ms=5, ecolor='black')
# marker='s'  use this argument to connect the markers to gether while mfc produces scatter plot of errorbars. 
# mfc is used to determince the color of marker
# ecolor is used for the color of the error bars
for i in range(15):
 plt.plot(ymat[i,:])

plt.axis([0,10,0,100])
ind = Factors[mask]
plt.xticks(np.arange(len(ind)),ind)

plt.xlabel('gamma values')
plt.ylabel('Average time measure in sec')
plt.show()
'''
#----------------------------------------------------------------------------------------------------------------------
'''
nb_brains = 9
Factors = np.array([2000,1500,1000,900,800,700,600,500,400,300,200,100,75,50,40,30,20,10])
#mask = [0,7,12,17,22,23,24,25,26,27]
x = np.arange(len(Factors))

ymat = np.array([75.2073341,73.5969717,75.18602,74.7298824,75.448804,73.6727766,74.0572256,73.4065197,74.9657255,73.7050515,73.0971584,69.8820684,70.2403196,67.3491376,67.221241,61.0910062,51.4327805,35.5246777,68.3324266,67.6852491,67.5137827,67.5723542,67.6461761,67.1060806,65.8472213,66.5858867,66.7573093,66.6506358,65.0219309,63.9803506,62.2993705,60.6076312,60.8862695,60.9945429,60.7536978,55.6192681,63.9740155,65.99126,64.9168904,65.7802831,63.9273308,66.2633817,63.6446017,65.9686789,63.4419976,61.3250037,61.1822916,58.4139206,59.05415,54.8899622,52.2098818,45.944977,48.5805828,33.6363676,77.9671615,78.6575728,77.9010274,77.6779826,78.0736491,77.2635776,77.7649515,77.1419902,76.5475827,75.9682276,73.9121423,71.618821,71.1618932,62.4275415,52.1893778,56.5061421,44.4945783,35.4643288,64.2911147,65.1708585,64.5325941,63.9011199,65.0046089,63.2823119,63.0240999,62.7615436,64.603457,64.1703347,62.2007673,60.2958552,60.1543912,60.1586277,58.2621184,55.3844708,52.1731468,38.5665865,69.4307354,68.6466979,68.063611,69.4402431,68.9338485,69.5587093,68.4634795,68.7789823,68.7548598,69.2916046,68.3763673,58.4176724,54.1190623,43.4177108,43.997544,42.6843324,34.4834943,26.6690431,70.9312425,74.1017386,72.0857879,74.4716989,74.3927373,73.3746777,72.2213042,69.125353,70.1769198,69.6944839,65.1728701,62.3787154,50.2211865,40.0668097,49.6135323,52.2611759,40.9851327,41.7195717,78.5251255,77.7323684,76.9388045,78.6829856,78.4926163,77.8963738,77.971625,77.7538155,75.7826673,73.4825917,74.1259107,71.61701,72.2376662,69.3755735,69.6881081,70.5202755,65.1430776,48.6338214,77.7376321,77.9024559,77.2041487,77.1552504,76.6323,76.4201784,76.3018067,75.9280894,76.5084729,76.032734,75.4031474,75.8505392,75.5606195,73.2050107,71.697365,66.5056044,59.3499832,48.1255926])
#np.save('gamma_variation_time_sensitivity.npy',ymat)

#pdb.set_trace()
ymat = ymat.reshape((nb_brains,len(Factors)))
#ymat = ymat[:,mask]
ymean  = ymat.mean(axis=0)

yerr_upper = ymat.max(axis=0) - ymean
yerr_lower = ymean - ymat.min(axis=0)



# example variable error bar values

# First illustrate basic pyplot interface, using defaults where possible.
#plt.errorbar(x, ymean, yerr=[yerr_lower, yerr_upper],fmt='s', mfc='black', ms=5, ecolor='black')
# marker='s'  use this argument to connect the markers to gether while mfc produces scatter plot of errorbars. 
# mfc is used to determince the color of marker
# ecolor is used for the color of the error bars

#--------------
#plt.figure()
#for i in range(nb_brains):
# plt.plot(ymat[i,:])
#-----------------

plt.figure()
plt.errorbar(Factors, ymean, yerr=[yerr_lower, yerr_upper],fmt='o') 

plt.axis([0,10,0,100])
#ind = Factors[mask]
#plt.xticks(np.arange(len(ind)),ind)
#ind = Factors[mask]
#plt.xticks(np.arange(len(Factors)),Factors)

plt.xlabel('gamma values')
plt.ylabel('Average time measure in sec')
plt.show()
'''