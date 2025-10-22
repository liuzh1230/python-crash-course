import unittest
from survey import AnonymousSurvey

class TestAnonymousSyrvey(unittest.TestCase):

    def setUp(self):
        """创建一个调查对象和一组答案"""
        question="What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)   #以self为前缀名存储以便于在整个类中使用
        self.responses=['English','Spanish','Mandarin']
    #unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，
    #并在每个测试中使用它们
    #python将先运行setUp()，再运行以test_打头的方法

    #测试编写的类时，可在setUp()中创建一系列实例并设置它们的属性，再在测试方法中使用
    #相比于在每个测试方法中创建实例，这更加方便简单

    def test_store_single_resopnse(self):
        self.my_survey.store_resopnse(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_responses(self):
        for response in self.responses:
            self.my_survey.store_resopnse(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()