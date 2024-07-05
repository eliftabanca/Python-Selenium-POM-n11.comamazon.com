import unittest
import pytest
from selenium import webdriver
from constants.globalConstants import *
from pages.PageBase import PageBase
from pages.categories import *
import softest
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class CategoryBrowsingTest(softest.TestCase, unittest.TestCase):

    def test_category_electronic(self):
        object_categories = CategoryProductListing(self.driver)
        object_categories.click_category()
        self.soft_assert(self.assertEqual, object_categories.category_assert() , CATEGORY_TEXT, "The text is not matching")
        self.assert_all()

    def test_subcategory_computer(self):
        object_categories = CategoryProductListing(self.driver)
        object_categories.hover_category()
        object_categories.click_subcategory()
        self.soft_assert(self.assertEqual, object_categories.assert_subcategory() , SUBCATEGORY_COMPUTER_TEXT, "The text is not matching")
        self.assert_all()

    def test_display_products_by_selected_filter(self):
        object_categories = CategoryProductListing(self.driver)
        object_categories.click_search_bar()
        object_categories.click_search_button()
        self.soft_assert(self.assertEqual, object_categories.assert_filter() , FILTER_TEXT, "The text is not matching")
        self.assert_all()

    def test_display_product_details_by_brand(self):
        object_categories = CategoryProductListing(self.driver)
        object_categories.hover_category()
        object_categories.click_subcategory()
        object_categories.product_details_by_brand()
        self.soft_assert(self.assertEqual, object_categories.assert_brand_name() , BRAND_TEXT, "The text is not matching")
        self.assert_all()

    def test_display_product_details_by_price(self):
        object_categories = CategoryProductListing(self.driver)
        object_categories.hover_category()
        object_categories.click_subcategory()
        






    



