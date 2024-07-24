import unittest
from formatted_name import get_formatted_name

"""Модульні тести та тестові ситуації"""

class NamesTestCase(unittest.TestCase):
    """Тести для 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Чи працює ф-ція з іменами на кшталт 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

    def test_first_last_name_with_different_cases(self):
        """Перевірка форматування імені та прізвища з різними регістрами"""
        formatted_name = get_formatted_name('jOHn', 'DOE')
        self.assertEqual(formatted_name, 'John Doe')

    def test_first_last_name_with_spaces(self):
        """Перевірка форматування імені та прізвища з пробілами"""
        formatted_name = get_formatted_name('   john   ', '   doe   ')
        self.assertEqual(formatted_name, 'John Doe')


if __name__ == '__main__':
    unittest.main()


