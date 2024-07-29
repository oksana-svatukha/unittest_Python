import  unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тести для класу AnonymousSurvey"""

    def setUp(self):
        """Створи опитування та набір відповідей
         для всіх тестувальних методів."""

        question = "Which foreign country did you visit first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["Turkey","Egypt","Tanzania"]

    def test_store_single_responce(self):
        """Перевірити, чи одиночна відповідь зберігається правильно."""

        """question = "Which foreign country did you visit first?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("Turkey")
        self.assertIn('Turkey', my_survey.responses)"""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):

        """Перевірити чи три індивідуальні
        відповіді зберігаються правильно."""

        """question = "Which foreign country did you visit first?"
        my_survey = AnonymousSurvey(question)
        responses = ["Turkey","Egypt","Tanzania"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()