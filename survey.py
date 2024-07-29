class AnonymousSurvey:
    """Зібрати анонімні відповіді на питання."""

    def __init__(self, question):
        """Зберегти питання та підготуватися для зберігання відповіді."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Показати питання."""
        print(self.question)

    def store_response(self, new_response):
        """Зберегти одну відповідь на питання."""
        self.responses.append(new_response)

    def show_result(self):
        """Показати всі надані відповіді."""
        print("Suevey results:")
        for response in self.responses:
            print(f" - {response}")