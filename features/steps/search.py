from behave import *
from features.pages.HomePage import HomePage

@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    assert context.home_page.verify_home_page_title("Your Store")

@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("HP")

@when(u'I click on search button')
def step_impl(context):
    context.search_page=context.home_page.click_on_search_button()

@then(u'Valid product should get displayed in search field')
def step_impl(context):
    assert context.search_page.display_status_of_product()

@when(u'I enter invalid product into the search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("Honda")

@then(u'Proper message should be displayed in search result')
def step_impl(context):
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.")

@when(u'I dont enter into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
