import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_gmail(self):
        stu_1 = Student('Jayden', 'Kristo')
        stu_2 = Student('Emiley', 'Watson')

        self.assertEqual(stu_1.gmail, 'Jayden.Kristo@gmail.com')
        self.assertEqual(stu_2.gmail, 'Emiley.Watson@gmail.com')

        


    def test_name(self):
        stu_1 = Student('Kelvin', 'Kristo')
        stu_2 = Student('Emiley', 'Watson')

        self.assertEqual(stu_1.name, 'Kelvin Kristo')
        self.assertEqual(stu_2.name, 'Emiley Watson')   

        stu_2.first = 'Bloom'

        self.assertEqual(stu_2.name, 'Bloom Watson')     



if __name__ =='__main___':
    unittest.main()
