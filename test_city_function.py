import unittest
from city_function import get_city_function

class CitiesTestCase(unittest.TestCase):
    """Тести для 'get_city_function'"""

    def test_formatted_city_country(self):
        formatted_city = get_city_function('kyiv', 'ukraine')
        self.assertEqual(formatted_city, 'Kyiv, Ukraine.')

    def test_formatted_city_country_population(self):
        formatted_city = get_city_function('kyiv', 'ukraine', '31000000')
        self.assertEqual(formatted_city, 'Kyiv, Ukraine - population 31,000,000')

if __name__ == '__main__':
    unittest.main()
