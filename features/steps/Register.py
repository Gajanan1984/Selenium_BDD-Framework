from selenium import webdriver
from behave import *

@given(u'I navigate to Register page')
def step_impl(context):
    print('1')


@when(u'I enter details into mandatory fields')
def step_impl(context):
    print('1')


@when(u'I click on Continue button')
def step_impl(context):
    print('1')


@then(u'Account should get created')
def step_impl(context):
    print('1')


@when(u'I enter details into all fields')
def step_impl(context):
    print('1')


@when(u'I enter details into all fields except email field')
def step_impl(context):
    print('1')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print('1')


@when(u'I dont enter anything into fields')
def step_impl(context):
    print('1')

