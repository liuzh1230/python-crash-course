class AnonymousSurvey():
    """收集匿名调查问卷"""
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question=question
        self.responses=[]
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_resopnse(self,new_resopnse):
        """存储单份调查问卷"""
        self.responses.append(new_resopnse)
    
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print("- "+response)

#假设我们此时想进行改进：
#让每个用户可输入多个答案
#编写一个方法，只输入不同的答案并输出每个答案的次数
#再编写一个类，管理非匿名调查
#要确认在改进开发的过程中没有出错，可以编写针对这个类的测试