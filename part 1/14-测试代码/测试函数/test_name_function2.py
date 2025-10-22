#下面我们为这个类再添加一个方法以进行更全面的测试

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','jolpin')
        self.assertEqual(formatted_name,'Janis Jolpin')

    def test_first_middle_last_name(self):
        formatted_name=get_formatted_name('wolfgang',
        'mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()