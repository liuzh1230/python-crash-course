import unittest
from survey import AnonymousSurvey

class TestAnonymousSyrvey(unittest.TestCase):

    def test_store_single_resopnse(self):
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_resopnse('English')
        self.assertIn('English',my_survey.responses)
    
    def test_store_responses(self):
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        responses=['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_resopnse(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

unittest.main()