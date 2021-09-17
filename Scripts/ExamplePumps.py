"""ExamplePumps - Contains some generic pumps"""

from DHLLDV.PumpObj import Pump
from DHLLDV.DHLLDV_Utils import interpDict

Ladder_Pump = Pump(name="0.864x0.864x1.880m Pump at 225 RPM",
                         design_speed=3.75,
                         design_impeller=1.88,
                         suction_dia=0.864,
                         disch_dia=0.864,
                         design_QH_curve=interpDict({0.0000000: 34.161388,
                                                    0.3567568: 33.838151,
                                                    0.7135136: 33.621503,
                                                    1.0702704: 33.430302,
                                                    1.4270272: 33.199471,
                                                    1.7837840: 32.879414,
                                                    2.1405408: 32.436629,
                                                    2.4972976: 31.854328,
                                                    2.8540544: 31.132250,
                                                    3.2108112: 30.285232,
                                                    3.5675680: 29.340576,
                                                    3.9243248: 28.334589,
                                                    4.2810816: 27.308934,
                                                    4.6378384: 26.307421,
                                                    4.9945952: 25.373782,
                                                    5.3513520: 24.550769,
                                                    5.7081088: 23.880782,
                                                    6.0648656: 23.408195,
                                                    }),
                         design_QP_curve=interpDict({0.000000: 149.140000,
                                                    0.356757: 261.693568,
                                                    0.713514: 400.786895,
                                                    1.070270: 527.401079,
                                                    1.427027: 649.033464,
                                                    1.783784: 767.446418,
                                                    2.140541: 882.893409,
                                                    2.497298: 995.493173,
                                                    2.854054: 1105.931264,
                                                    3.210811: 1215.870450,
                                                    3.567568: 1328.165127,
                                                    3.924325: 1446.916945,
                                                    4.281082: 1577.388546,
                                                    4.637838: 1725.757340,
                                                    4.994595: 1898.625852,
                                                    5.351352: 2102.123994,
                                                    5.708109: 2340.407922,
                                                    6.064866: 2613.520140,
                                                    }),
                         avail_power=1491.4,
                         limited="power",
                         )
Ladder_Pump.slurry.fluid = 'fresh'
Ladder_Pump.slurry.rhom = Ladder_Pump.slurry.rhol

Main_Pump = Pump(name="0.864x0.864x2.134m Pump at 315 RPM",
                         design_speed=5.25,
                         design_impeller=2.134,
                         suction_dia=0.864,
                         disch_dia=0.864,
                         design_QH_curve=interpDict({0.0000000: 86.747272,
                                                    0.3567568: 86.141862,
                                                    0.7135136: 85.656934,
                                                    1.0702704: 85.195754,
                                                    1.4270272: 84.679434,
                                                    1.7837840: 84.046416,
                                                    2.1405408: 83.252655,
                                                    2.4972976: 82.271843,
                                                    2.8540544: 81.095235,
                                                    3.2108112: 79.730788,
                                                    3.5675680: 78.201548,
                                                    3.9243248: 76.543376,
                                                    4.2810816: 74.802270,
                                                    4.6378384: 73.031608,
                                                    4.9945952: 71.289679,
                                                    5.3513520: 69.637824,
                                                     5.7081088: 68.139467,
                                                     6.0648656: 66.860267,
                                                     }),
                         design_QP_curve=interpDict({0.000000: 596.560000,
                                                    0.356757: 916.044826,
                                                    0.713514: 1339.569252,
                                                    1.070270: 1701.644829,
                                                    1.427027: 2031.949718,
                                                    1.783784: 2339.857059,
                                                    2.140541: 2628.620537,
                                                    2.497298: 2899.359089,
                                                    2.854054: 3152.729751,
                                                    3.210811: 3389.781303,
                                                    3.567568: 3612.402860,
                                                    3.924325: 3823.517334,
                                                    4.281082: 4027.095378,
                                                    4.637838: 4228.043905,
                                                    4.994595: 4432.014834,
                                                    5.351352: 4645.172441,
                                                     5.708109: 4873.950361,
                                                     6.064866: 5124.826258,
                                                     }),
                         avail_power=4239.3,
                         limited="torque",
                         )
Main_Pump.slurry.fluid = 'fresh'
Main_Pump.slurry.rhom = Main_Pump.slurry.rhol