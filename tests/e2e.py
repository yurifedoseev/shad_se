import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class End2EndTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_shad_search(self):
        self.driver.get('https://yandex.ru')
        elem = self.driver.find_element_by_id('text')
        assert elem

        elem.send_keys('ШАД')
        form = self.driver.find_element_by_class_name('suggest2-form__node')
        form.submit()
        WebDriverWait(self.driver, 10).until(EC.title_contains('ШАД'))

        serp_list = self.driver.find_element_by_class_name('serp-list')
        li = serp_list.find_element_by_xpath('//li[@data-cid=0]')
        assert li.text.startswith('1Школа анализа данныхyandexdataschool.ru')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
