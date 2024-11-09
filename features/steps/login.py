from datetime import datetime, time
from behave import *
from selenium.webdriver.common.by import By
import time

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    context.home_page.click_on_my_account_option()
    context.login_page=context.home_page.select_login_option()

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("gajanan.9002@gmail.com")
    context.login_page.enter_password("Qazwsx@4466")

@when(u'I click on ok button')
def step_impl(context):
    context.account_page=context.login_page.click_on_login_button()

@then(u'I should succussfully loged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()

@when(u'I enter invalid email address and valid password')
def step_impl(context):
    time_stamp=datetime.now().strftime("%y_%m_%d_%H_%M_%S")
    invalid_email="gajanan" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("Qazwsx@4466")

@then(u'I should get proper warning message')
def step_impl(context):
    assert context.login_page.verify_warning_message_is_displayed("Warning: No match for E-Mail Address and/or Password.")

@when(u'I enter valid email address and invaid password')
def step_impl(context):
    context.login_page.enter_email_address("gajanan.9002@gmail.com")
    context.login_page.enter_password("Qazwsx@446")

@when(u'I enter invalid email address and password')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "gajanan" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("Qazwsx@446")

@when(u'I dont enter anything into search fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

