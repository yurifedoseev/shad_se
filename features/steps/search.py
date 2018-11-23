from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('yandex main page')
def step_impl(context):
    context.driver = webdriver.Safari()
    context.driver.get('https://yandex.ru')


@when('we search "{text}"')
def step_impl(context, text):
    elem = context.driver.find_element_by_id('text')
    assert elem
    elem.send_keys(text)
    form = context.driver.find_element_by_class_name('suggest2-form__node')
    form.submit()
    WebDriverWait(context.driver, 10).until(EC.title_contains('ШАД'))


@then('first result is "{url}"')
def step_impl(context, url):
    serp_list = context.driver.find_element_by_class_name('serp-list')
    li = serp_list.find_element_by_xpath('//li[@data-cid=0]')
    assert url in li.text
    context.driver.close()
