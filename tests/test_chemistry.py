import unittest
import sys
sys.path.insert(0, '..')

from brliant_calc import chemistry


class TestChemistryOperations(unittest.TestCase):

    def test_dilution(self):
        self.assertAlmostEqual(chemistry.dilution(6, 0.5, 1.5), 2.0)
        self.assertAlmostEqual(chemistry.dilution(1, 1, 2), 0.5)
        self.assertAlmostEqual(chemistry.dilution("6", "0.5", "1.5"), 2.0)
        self.assertEqual(chemistry.dilution(1, 1, 0), "Error: Final concentration (c2) cannot be zero.")

    def test_molality(self):
        self.assertAlmostEqual(chemistry.molality(2, 0.5), 4.0)
        self.assertAlmostEqual(chemistry.molality("2", "0.5"), 4.0)
        self.assertEqual(chemistry.molality(2, 0), "Error: Solvent mass cannot be zero.")

    def test_mole_fraction(self):
        self.assertAlmostEqual(chemistry.mole_fraction(2, 3), 0.4)
        self.assertAlmostEqual(chemistry.mole_fraction("2", "3"), 0.4)
        self.assertEqual(chemistry.mole_fraction(0, 0), "Error: Total moles cannot be zero.")

    def test_limiting_reagent(self):
        result = chemistry.limiting_reagent(10, 2, 6, 1)
        self.assertIn("Reagent 1", result)
        self.assertIn("Limiting", result)
        result2 = chemistry.limiting_reagent(4, 1, 3, 2)
        self.assertIn("Reagent 2", result2)
        self.assertEqual(chemistry.limiting_reagent(4, 1), "Error: Provide amount/coefficient pairs for at least two reagents.")
        self.assertEqual(chemistry.limiting_reagent(4, 1, 3), "Error: Provide amount/coefficient pairs for at least two reagents.")
        self.assertIn("Error", chemistry.limiting_reagent(4, 1, 3, 0))

    def test_percent_yield(self):
        self.assertAlmostEqual(chemistry.percent_yield(8, 10), 80.0)
        self.assertAlmostEqual(chemistry.percent_yield("8", "10"), 80.0)
        self.assertEqual(chemistry.percent_yield(8, 0), "Error: Theoretical yield cannot be zero.")

    def test_boiling_point_elevation(self):
        self.assertAlmostEqual(chemistry.boiling_point_elevation(0.5, 0.512), 0.256)
        self.assertAlmostEqual(chemistry.boiling_point_elevation(0.5, 0.512, 2), 0.512)
        self.assertAlmostEqual(chemistry.boiling_point_elevation("0.5", "0.512"), 0.256)

    def test_freezing_point_depression(self):
        self.assertAlmostEqual(chemistry.freezing_point_depression(0.5, 1.86), 0.93)
        self.assertAlmostEqual(chemistry.freezing_point_depression(0.5, 1.86, 3), 2.79)

    def test_osmotic_pressure(self):
        self.assertAlmostEqual(chemistry.osmotic_pressure(0.1, 298), 0.1 * 0.0821 * 298)
        self.assertAlmostEqual(chemistry.osmotic_pressure("0.1", "298"), 0.1 * 0.0821 * 298)

    def test_henderson_hasselbalch(self):
        self.assertAlmostEqual(chemistry.henderson_hasselbalch(4.76, 10), 4.76 + 1.0)
        self.assertAlmostEqual(chemistry.henderson_hasselbalch("4.76", "10"), 5.76)
        self.assertEqual(chemistry.henderson_hasselbalch(4.76, 0), "Error: Ratio must be positive.")

    def test_half_life(self):
        self.assertAlmostEqual(chemistry.half_life(0.1), 6.931471805599453, places=5)
        self.assertAlmostEqual(chemistry.half_life("0.1"), 6.931471805599453, places=5)
        self.assertEqual(chemistry.half_life(0), "Error: Decay constant must be positive.")

    def test_radioactive_decay(self):
        self.assertAlmostEqual(chemistry.radioactive_decay(100, 0.1, 5), 100 * 2.718281828 ** (-0.5), places=5)
        self.assertAlmostEqual(chemistry.radioactive_decay("100", "0.1", "5"), 100 * 2.718281828 ** (-0.5), places=5)

    def test_density(self):
        self.assertAlmostEqual(chemistry.density(50, 25), 2.0)
        self.assertAlmostEqual(chemistry.density("50", "25"), 2.0)
        self.assertEqual(chemistry.density(50, 0), "Error: Volume cannot be zero.")

    def test_ppm_to_concentration(self):
        self.assertAlmostEqual(chemistry.ppm_to_concentration(100, 58.44), 100 / (58.44 * 1000), places=6)
        self.assertAlmostEqual(chemistry.ppm_to_concentration("100", "58.44"), 100 / (58.44 * 1000), places=6)
        self.assertEqual(chemistry.ppm_to_concentration(100, 0), "Error: Molar mass cannot be zero.")

    def test_molarity_to_ppm(self):
        self.assertAlmostEqual(chemistry.molarity_to_ppm(0.1, 58.44), 5844.0)
        self.assertAlmostEqual(chemistry.molarity_to_ppm("0.1", "58.44"), 5844.0)

    def test_invalid_number_raises(self):
        with self.assertRaises(ValueError):
            chemistry.dilution("abc", 1, 2)


if __name__ == '__main__':
    unittest.main()
