from Locators import *
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.7)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.5)
    element.send_keys(text)
    sleep(0.5)


class Manager:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_manager_my_task(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task)

    def enter_manager_my_task_all(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_all)

    def enter_manager_my_task_set_customer_manager(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager)

    def enter_manager_my_task_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_update)

    def enter_manager_my_task_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', manager_my_task_search, text)

    def enter_manager_my_task_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_search_btn)

    def enter_manager_my_task_set_customer_manager_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_click)

    def enter_manager_my_task_set_customer_manager_state(self):
        scrolled = self.driver.find_element('xpath', manager_my_task_set_customer_manager_state)
        sleep(.3)
        scrolled.location_once_scrolled_into_view
        sleep(.3)
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_state)

    def enter_manager_my_task_set_customer_manager_state_name(self, text):
        sleep(1)
        # self.driver.find_element('xpath', manager_my_task_set_customer_manager_state_name).send_keys(text)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', manager_my_task_set_customer_manager_state_name, text)

    def enter_manager_my_task_set_customer_manager_state_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_state_option)

    def enter_manager_my_task_set_customer_manager_city(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_city)

    def enter_manager_my_task_set_customer_manager_city_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', manager_my_task_set_customer_manager_city_name, text)

    def enter_manager_my_task_set_customer_manager_city_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_city_option)

    def enter_manager_my_task_set_customer_manager_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_select)

    def enter_manager_my_task_set_customer_manager_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', manager_my_task_set_customer_manager_name, text)

    def enter_manager_my_task_set_customer_manager_option(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_option)

    def enter_manager_my_task_set_customer_manager_btn(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_btn)

    def enter_manager_my_task_set_customer_manager_click_person(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_set_customer_manager_click_person)

################### manager_my_task_determine_the_owner_of_the_order ###################

    def enter_manager_my_task_determine_the_owner_of_the_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_determine_the_owner_of_the_order)

    def enter_manager_my_task_determine_the_owner_of_the_order_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_determine_the_owner_of_the_order_click)

    def enter_manager_my_task_determine_the_owner_of_the_order_edite(self):
        wait_until_element_has_an_attribute(self, 'xpath', manager_my_task_determine_the_owner_of_the_order_edite)










