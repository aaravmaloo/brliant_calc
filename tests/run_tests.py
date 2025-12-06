import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_basic_ops import TestBasicOperations
from tests.test_advanced_ops import TestAdvancedOperations
from tests.test_matrix_ops import TestMatrixOperations
from tests.test_complex_ops import TestComplexOperations
from tests.test_vector_ops import TestVectorOperations
from tests.test_plotting import TestPlotting
from tests.test_precision_ops import TestPrecisionOperations
from tests.test_security import TestSecurityFeatures
from tests.test_convolution import TestConvolution

def run_all_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestBasicOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestAdvancedOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestMatrixOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestComplexOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestVectorOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestPlotting))
    suite.addTests(loader.loadTestsFromTestCase(TestPrecisionOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestSecurityFeatures))
    suite.addTests(loader.loadTestsFromTestCase(TestConvolution))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
