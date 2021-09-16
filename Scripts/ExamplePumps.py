"""ExamplePumps - Contains some generic pumps"""

from DHLLDV.PumpObj import Pump
from DHLLDV.DHLLDV_Utils import interpDict

Ladder_Pump = Pump(name="0.864x0.864x1.880m Pump at 225 RPM",
                         design_speed=3.75,
                         design_impeller=1.88,
                         suction_dia=0.864,
                         disch_dia=0.864,
                         design_QH_curve=interpDict({0.3567568: 34.522178,
                                                        0.7135136: 33.866193,
                                                        1.0702704: 33.428535,
                                                        1.4270272: 33.085783,
                                                        1.7837840: 32.743065,
                                                        2.1405408: 32.329986,
                                                        2.4972976: 31.799882,
                                                        2.8540544: 31.129858,
                                                        3.0324328: 30.741542,
                                                        3.2108112: 30.319924,
                                                        3.5675680: 29.390430,
                                                        3.9243248: 28.377845,
                                                        4.2810816: 27.329607,
                                                        4.6378384: 26.299124,
                                                        4.9945952: 25.341972,
                                                        5.3513520: 24.514100,
                                                        }),
                         design_QP_curve=interpDict({0.356757: 270.270082,
                                                        0.713514: 405.162632,
                                                        1.070270: 527.361832,
                                                        1.427027: 646.087460,
                                                        1.783784: 763.474573,
                                                        2.140541: 879.495459,
                                                        2.497298: 993.638414,
                                                        2.854054: 1105.845987,
                                                        3.032433: 1161.488082,
                                                        3.210811: 1217.135708,
                                                        3.567568: 1329.976262,
                                                        3.924325: 1448.427566,
                                                        4.281082: 1578.046817,
                                                        4.637838: 1725.537065,
                                                        4.994595: 1898.039569,
                                                        5.351352: 2101.868428,
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
                         design_QH_curve=interpDict({0.3567568: 86.667547,
                                                        0.7135136: 85.835199,
                                                        1.0702704: 85.181045,
                                                        1.4270272: 84.580755,
                                                        1.7837840: 83.935478,
                                                        2.1405408: 83.170464,
                                                        2.4972976: 82.234854,
                                                        2.8540544: 81.101573,
                                                        3.0324328: 80.458690,
                                                        3.2108112: 79.766608,
                                                        3.5675680: 78.247307,
                                                        3.9243248: 76.579653,
                                                        4.2810816: 74.814796,
                                                        4.6378384: 73.015297,
                                                        4.9945952: 71.251676,
                                                        5.3513520: 69.599804,
                                                        }),
                         design_QP_curve=interpDict({0.356757: 925.566665,
                                                        0.713514: 1344.069400,
                                                        1.070270: 1701.188943,
                                                        1.427027: 2028.399098,
                                                        1.783784: 2335.371660,
                                                        2.140541: 2624.967982,
                                                        2.497298: 2897.581746,
                                                        2.854054: 3153.054763,
                                                        3.032433: 3274.430070,
                                                        3.210811: 3391.720606,
                                                        3.567568: 3614.993973,
                                                        3.924325: 3825.648000,
                                                        4.281082: 4027.852656,
                                                        4.637838: 4227.036044,
                                                        4.994595: 4429.630959,
                                                        5.351352: 4642.766776,
                                                        }),
                         avail_power=4239.3,
                         limited="torque",
                         )
Main_Pump.slurry.fluid = 'fresh'
Main_Pump.slurry.rhom = Main_Pump.slurry.rhol