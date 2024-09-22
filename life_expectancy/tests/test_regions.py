"""Tests for the Region enum class."""

import unittest
from life_expectancy.regions import Region, NON_COUNTRIES


class TestRegion(unittest.TestCase):
    """Test cases for the Region enum"""

    def test_region_enum(self):
        """Test that the Region enum members are correctly defined"""
        self.assertTrue(hasattr(Region, "PT"))
        self.assertEqual(Region.PT.value, "PT")

    def test_countries_method(self):
        """Test that the countries method returns the correct list of countries"""
        countries = Region.countries()
        country_values = [country.value for country in countries]
        for non_country in NON_COUNTRIES:
            self.assertNotIn(non_country, country_values)
        self.assertIn("PT", country_values)
        self.assertIn("FR", country_values)
