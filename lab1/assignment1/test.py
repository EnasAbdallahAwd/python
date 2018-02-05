from vowels import charvowels
from charlocat import charLocat
from cal import calcarea
from multabil import MultiplicationTable
from mairo import task_mairo
from dictionary import task_dictionary
import unittest


class TestAssignmentOne(unittest.TestCase):

    def vowelsChar(self):
        self.assertEqual(charvowels('mobile'), 'mbl')
        self.assertEqual(charvowels('MOBILE'), 'MBL')
        self.assertEqual(charvowels('MobIlE'), 'Mbl')


    def test_charLocat(self):
        self.assertEqual(charLocat('This is javaScript','i'), [2,5,15])

    def test_calcarea(self):
        self.assertEqual(calcarea("r",10,10),50 )
        self.assertEqual(calcarea("t",10,20), 200)
        self.assertEqual(calcarea("s",10), 100)
        self.assertEqual(calcarea("c",10), 314)

    def test_MultiplicationTable(self):
        self.assertEqual(MultiplicationTable(3), [[1],[2,4],[3,6,9]])

    #def test_Mairo(self):
        #elf.assertEqual(task_mairo(3),"""

        #*
        #**
        #***

        #")


    def test_dictionary(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(task_dictionary(l1), d1)



if __name__ == '__main__':
    unittest.main()
