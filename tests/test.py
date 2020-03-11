import unittest

class TestProbleem(unittest.TestCase):

    def test_probemie(self):
        h=1
        self.assertEqual(h,1)

if __name__ == '__main__':
    ############# Add these lines #############
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    ###########################################
    unittest.main()