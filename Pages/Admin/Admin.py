import re
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.75)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.75)
    element.send_keys(text)
    sleep(0.5)


class Admin:
    def __init__(self, driver):
        self.driver = driver

    def enter_admin_my_task(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_my_task)

    def enter_admin_my_task_customer_manager_tab(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_my_task_customer_manager_tab)

    def enter_admin_my_task_customer_manager_tab_auto_need_pick_up_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_my_task_customer_manager_tab_auto_need_pick_up_order)

    def enter_admin_my_task_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_my_task_update)

    def enter_admin_my_task_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_my_task_search, text)

    def enter_admin_my_task_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_my_task_search_btn)

    def enter_admin_my_task_tn(self):
        sleep(1)
        a = self.driver.find_element('xpath', admin_my_task_customer_manager_tab_auto_need_pick_up_order_tn).text
        print(a)
        b = re.sub("\D", "", a)
        print(b)
        return b

    def enter_admin_batches(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_batches)

    def enter_admin_batches_shopping_list(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_batches_shopping_list)

    def enter_admin_batches_shopping_list_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_batches_shopping_list_search, text)

    def enter_admin_batches_shopping_list_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_batches_shopping_list_search_btn)

    def enter_admin_batches_shopping_list_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr[1]/td[2]/a")

    def enter_admin_batches_shopping_list_batch_op1(self):
        a = self.driver.find_element('xpath', admin_batches_shopping_list_batch_op1).text
        print(a)
        return a
