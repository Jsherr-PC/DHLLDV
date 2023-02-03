"""ExamplePumps - Contains some generic pumps"""

from DHLLDV.PumpObj import Pump
from DHLLDV.SlurryObj import Slurry
from DHLLDV.DHLLDV_Utils import interpDict

base_slurry = Slurry(fluid='salt')
Ladder_Pump = Pump(name="0.864x0.864x1.880m Pump at 225 RPM",
                   design_speed=3.75,
                   design_impeller=1.88,
                   suction_dia=0.864,
                   disch_dia=0.864,
                   design_QH_curve=interpDict({0.0000000: 34.161388,
                                               0.3567568: 34.109928,
                                               0.7135136: 33.968864,
                                               1.0702704: 33.727283,
                                               1.4270272: 33.378805,
                                               1.7837840: 32.921761,
                                               2.1405408: 32.359135,
                                               2.4972976: 31.698232,
                                               2.8540544: 30.950121,
                                               3.2108112: 30.128877,
                                               3.5675680: 29.250727,
                                               3.9243248: 28.333156,
                                               4.2810816: 27.394067,
                                               4.6378384: 26.451062,
                                               4.9945952: 25.520877,
                                               5.3513520: 24.619007,
                                               5.7081088: 23.759512,
                                               6.4216224: 22.216815,
                                               }),
                   design_QP_curve=interpDict({0.000000: 149.140000,
                                               0.356757: 265.086004,
                                               0.713514: 407.005162,
                                               1.070270: 534.014231,
                                               1.427027: 653.694156,
                                               1.783784: 768.682260,
                                               2.140541: 880.423455,
                                               2.497298: 990.182072,
                                               2.854054: 1099.454369,
                                               3.210811: 1210.185521,
                                               3.567568: 1324.910404,
                                               3.924325: 1446.866948,
                                               4.281082: 1580.106542,
                                               4.637838: 1729.610908,
                                               4.994595: 1901.405500,
                                               5.351352: 2102.626065,
                                               5.708109: 2341.436276,
                                               6.421622: 2966.399621,
                                               }),
                   avail_power=1491.4,
                   limited="torque",
                   slurry=base_slurry,
                   )

Main_Pump = Pump(name="0.864x0.864x2.134m Pump at 315 RPM",
                 design_speed=5.25,
                 design_impeller=2.134,
                 suction_dia=0.864,
                 disch_dia=0.864,
                 design_QH_curve=interpDict({0.0000000: 86.747272,
                                             0.3567568: 86.450473,
                                             0.7135136: 86.051460,
                                             1.0702704: 85.533415,
                                             1.4270272: 84.883885,
                                             1.7837840: 84.094935,
                                             2.1405408: 83.163187,
                                             2.4972976: 82.089738,
                                             2.8540544: 80.879942,
                                             3.2108112: 79.543051,
                                             3.5675680: 78.091749,
                                             3.9243248: 76.541591,
                                             4.2810816: 74.910387,
                                             4.6378384: 73.217564,
                                             4.9945952: 71.483541,
                                             5.3513520: 69.729161,
                                             5.7081088: 67.975189,
                                             6.4216224: 64.548811,
                                             }),
                 design_QP_curve=interpDict({0.000000: 596.560000,
                                             0.356757: 921.629130,
                                             0.713514: 1349.538023,
                                             1.070270: 1712.125463,
                                             1.427027: 2039.315319,
                                             1.783784: 2341.820028,
                                             2.140541: 2624.644708,
                                             2.497298: 2890.613974,
                                             2.854054: 3141.699072,
                                             3.210811: 3379.626591,
                                             3.567568: 3606.189582,
                                             3.924325: 3823.412498,
                                             4.281082: 4033.634912,
                                             4.637838: 4239.546513,
                                             4.994595: 4444.191894,
                                             5.351352: 4650.956491,
                                             5.708109: 4863.540484,
                                             6.421622: 5322.321057,
                                             }),
                 avail_power=4239.3,
                 limited="torque",
                 slurry=base_slurry,
                 )

Ladder_Pump600 = Pump(name="0.600x0.600x1.118m Pump at 300 RPM",
                      design_speed=5.0,
                      design_impeller=1.1176,
                      suction_dia=0.6,
                      disch_dia=0.6,
                      design_QH_curve=interpDict({0.0000000: 21.430053,
                                                  0.1722065: 21.412179,
                                                  0.3444130: 21.327235,
                                                  0.5166194: 21.167398,
                                                  0.6888259: 20.928420,
                                                  0.8610324: 20.609779,
                                                  1.0332389: 20.214599,
                                                  1.2054454: 19.749335,
                                                  1.3776519: 19.223251,
                                                  1.5498583: 18.647749,
                                                  1.7220648: 18.035622,
                                                  1.8942713: 17.400307,
                                                  2.0664778: 16.755212,
                                                  2.2386843: 16.113174,
                                                  2.4108907: 15.486061,
                                                  2.5830972: 14.884552,
                                                  2.7553037: 14.318070,
                                                  3.0997167: 13.322144,
                                                  }),
                      design_QP_curve=interpDict({0.000000: 149.140000,
                                                  0.172206: 65.269284,
                                                  0.344413: 105.039933,
                                                  0.516619: 143.171017,
                                                  0.688826: 181.500777,
                                                  0.861032: 220.878834,
                                                  1.033239: 262.061262,
                                                  1.205445: 306.003106,
                                                  1.377652: 354.040500,
                                                  1.549858: 408.062625,
                                                  1.722065: 470.709112,
                                                  1.894271: 545.599628,
                                                  2.066478: 637.545159,
                                                  2.238684: 752.527526,
                                                  2.410891: 896.806727,
                                                  2.583097: 1073.607690,
                                                  2.755304: 1274.810680,
                                                  3.099717: 1589.740236,
                                                  }),
                      avail_power=550,
                      limited="torque",
                      )

Main_Pump500 = Pump(name="0.600x0.500x1.422m Pump at 450 RPM",
                    design_speed=7.50,
                    design_impeller=1.4224,
                    suction_dia=0.6,
                    disch_dia=0.5,
                    design_QH_curve=interpDict({0.0000000: 78.627157,
                                                0.1195878: 78.377502,
                                                0.2391757: 78.020587,
                                                0.3587635: 77.539928,
                                                0.4783513: 76.923729,
                                                0.5979392: 76.165052,
                                                0.7175270: 75.261842,
                                                0.8371148: 74.216805,
                                                0.9567027: 73.037111,
                                                1.0762905: 71.733957,
                                                1.1958783: 70.321994,
                                                1.3154662: 68.818664,
                                                1.4350540: 67.243488,
                                                1.5546418: 65.617353,
                                                1.6742297: 63.961839,
                                                1.7938175: 62.298616,
                                                1.9134054: 60.648952,
                                                2.1525810: 57.471239,
                                                }),
                    design_QP_curve=interpDict({0.000000: 596.560000,
                                                0.119588: 312.828525,
                                                0.239176: 452.214571,
                                                0.358764: 568.416766,
                                                0.478351: 671.536543,
                                                0.597939: 765.176468,
                                                0.717527: 851.008969,
                                                0.837115: 929.976294,
                                                0.956703: 1002.741242,
                                                1.076291: 1069.890871,
                                                1.195878: 1132.036558,
                                                1.315466: 1189.862444,
                                                1.435054: 1244.145028,
                                                1.554642: 1295.755647,
                                                1.674230: 1345.652771,
                                                1.793818: 1394.868582,
                                                1.913405: 1444.492652,
                                                2.152581: 1549.504172,
                                                }),
                    avail_power=1800,
                    limited="torque",
                    )
