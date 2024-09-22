import unittest
from life_expectancy.regions import Region


class TestRegion(unittest.TestCase):
    def test_region_enum(self):
        # Test that all enum members are correctly defined
        self.assertTrue(hasattr(Region, 'PT'))
        self.assertEqual(Region.PT.value, 'PT')

    def test_countries_method(self):
        # Test the countries method to ensure it excludes non-country regions
        countries = Region.countries()
        non_countries = {
            'DE_TOT', 'EA18', 'EA19', 'EEA30_2007', 'EEA31',
            'EFTA', 'EU27_2007', 'EU27_2020', 'EU28'
        }
        country_values = [country.value for country in countries]
        for non_country in non_countries:
            self.assertNotIn(non_country, country_values)
        # Ensure that actual countries are included
        self.assertIn('PT', country_values)
        self.assertIn('FR', country_values)


if __name__ == '__main__':
    unittest.main()