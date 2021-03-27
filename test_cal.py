import unittest
import cal


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(10, 2), 12)
        self.assertEqual(cal.add(10, 0), 10)
        self.assertEqual(cal.add(-1, -2), -3)
        self.assertEqual(cal.add(10, -10), 0)



    def test_subtract(self):
        self.assertEqual(cal.subtract(10, 2), 8)
        self.assertEqual(cal.subtract(11, 2), 9)
        self.assertEqual(cal.subtract(-1, 2), -3)
        self.assertEqual(cal.subtract(10, -10), 20)


    def test_multiply(self):
        self.assertEqual(cal.multiply(10, 2), 20)
        self.assertEqual(cal.multiply(10, -2), -20)
        self.assertEqual(cal.multiply(1, 2), 2)
        self.assertEqual(cal.multiply(0, 2), 0)

    def test_divide(self):
        self.assertEqual(cal.divide(10, 2), 5)        
        self.assertEqual(cal.divide(-1, -1), 1)  
        self.assertEqual(cal.divide(0, 2), 0)  
        self.assertEqual(cal.divide(10, -5), -2)  
        self.assertEqual(cal.divide(5, 2), 2.5)   

# context manager 
        with self.assertRaises(ValueError):
            cal.divide(10, 0)      







if __name__ =='__main___':
    unittest.main()


