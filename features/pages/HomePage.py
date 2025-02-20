from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.SearchPage import SearchPage

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_option_xpath="//span[text()='My Account']"
    select_login_option_link_text="Login"
    search_box_field_name="search"
    search_button_xpath="//div[@id='search']//button"

    def click_on_my_account_option(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("select_login_option_link_text", self.select_login_option_link_text)
        return LoginPage(self.driver)

    def verify_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)





        