#python标准库中的unittest提供了测试工具
#单元测试：核实函数的某个方面没有问题
#测试用例：一组单元测试，一起核实函数在各个情形下的行为均符合要求
#全覆盖性测试：包含一整套单元测试

import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','jolpin')
        self.assertEqual(formatted_name,'Janis Jolpin')

unittest.main()

#首先，导入了模块unittest和要测试的函数
#创建了一个名为NamesTestCase的类，用于包含一系列针对get_formatted_name()的测试
#这个类必须继承unittest.Testcase
#这里NamesTestCase只包含一个方法，用于测试get_formatted_name()的一个方面
#测试方法名称必须以test开头
#在运行该程序时，所有test_打头的方法都将自动运行,而不用编写调用它们的代码
#在test_first_last_name中，我们调用了要测试的函数，并存储了要测试的返回值
#接下来，我们使用了unittest类中的一个功能：一个断言方法：用来核实得到的结果是否与期望值一致
#self.assertEqual(formatted_name,'Janis Jolpin')的意思是，
#比较formatted_name与'Janis Jolpin'的值
#unittest.main()让python运行这个测试