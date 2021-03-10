'''
Created on Apr 190 2019

@author: rcriii
'''
import unittest

from DHLLDV import DHLLDV_constants
from DHLLDV import DHLLDV_framework

class Test(unittest.TestCase):
    def setUp(self):
        Dp = 0.762  # Pipe diameter
        d = 1 / 1000.
        epsilon = DHLLDV_constants.steel_roughness
        nu = DHLLDV_constants.water_viscosity[20]
        rhos = 2.65
        rhol = DHLLDV_constants.water_density[20]
        Rsd = (rhos - rhol) / rhol
        Cv = 0.175
        rhom = Cv * (rhos - rhol) + rhol
        GSD = {0.11: 0.075 / 1000, 0.5: d, 0.85: d * 2.72}

        self.Erhg_obj = DHLLDV_framework.Cvs_Erhg_graded(GSD, 5.0, Dp, epsilon, nu, rhol, rhos, Cv,
                                                         get_dict=True)

    def test_dlim_500(self):
        """Test the dlim for 500mm pipe"""
        dlim = DHLLDV_framework.pseudo_dlim(0.50,
                                            DHLLDV_constants.water_viscosity[20],
                                            DHLLDV_constants.water_density[20],
                                            2.65)
        self.assertAlmostEqual(9.4907896, dlim * 10**5)


    def test_dlim_762(self):
        """Test the dlim for 762mm pipe"""
        dlim = DHLLDV_framework.pseudo_dlim(0.762,
                                            DHLLDV_constants.water_viscosity[20],
                                            DHLLDV_constants.water_density[20],
                                            2.65)
        self.assertAlmostEqual(1.0769557, dlim * 10 ** 4)

    def test_Erhg_graded_X(self):
        self.assertAlmostEqual(self.Erhg_obj['X'], 0.16447698)

    def test_Erhg_graded_fracs(self):
        fs = [1.00000000, 0.91644770, 0.83289540, 0.74934309, 0.66579079,
              0.58223849, 0.49868619, 0.41513388, 0.33158158, 0.24802928,
              0.16447698]
        fs.reverse()
        for i, f in enumerate(fs):
            self.assertAlmostEqual(self.Erhg_obj['fracs'][i], f)


    def test_Erhg_graded_ds(self):
        ds = [4.1545841, 3.2746792, 2.5811304, 2.0344693, 1.6035863,
              1.2639606, 0.9913120, 0.5691244, 0.3267413, 0.1875862,
              0.1076956]
        ds.reverse()
        for i, d in enumerate(ds):
            self.assertAlmostEqual(self.Erhg_obj['ds'][i]*1000, d)




