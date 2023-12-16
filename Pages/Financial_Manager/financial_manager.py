
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
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

class Financial_Manager:
    def __init__(self, driver):
        self.driver = driver

################### my_tasks_need_official_invoice ###################

    def enter_financial_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks)
        # self.driver.find_element('xpath', financial_my_tasks).click()

    def enter_financial_my_tasks_need_official_invoice(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_need_official_invoice)
        # self.driver.find_element('xpath', financial_my_tasks_need_official_invoice).click()

    def enter_financial_update_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_update_my_tasks)
        # self.driver.find_element('xpath', financial_update_my_tasks).click()

    def enter_financial_search(self, text):
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', financial_search, text)
        # self.driver.find_element('xpath', financial_search).send_keys(number)

    def enter_financial_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_search_btn)
        # self.driver.find_element('xpath', financial_search_btn).click()

    def enter_financial_my_tasks_click_need_official_invoice(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_click_need_official_invoice)
        # self.driver.find_element('xpath', financial_my_tasks_click_need_official_invoice).click()

    def enter_financial_my_tasks_need_official_invoice_click_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_need_official_invoice_click_order)
        # self.driver.find_element('xpath', financial_my_tasks_need_official_invoice_click_order).click()

    def enter_financial_my_tasks_need_official_invoice_transfer_arian(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_need_official_invoice_transfer_arian)
        # self.driver.find_element('xpath', financial_my_tasks_need_official_invoice_transfer_arian).click()

################### financial_my_tasks_check_new_payment ###################

    def enter_financial_my_tasks_check_new_payment(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment)

    def enter_financial_my_tasks_check_new_payment_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_click)

    def enter_financial_my_tasks_check_new_payment_approvals(self):
        sleep(1)
        scrolled = self.driver.find_element('xpath', financial_my_tasks_check_new_payment_approvals)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_approvals)

    def enter_financial_my_tasks_check_new_payment_not_approvals(self):
        scrolled = self.driver.find_element('xpath', financial_my_tasks_check_new_payment_not_approvals)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_not_approvals)

    def enter_financial_my_tasks_check_new_payment_approvals2(self):
        sleep(1)
        scrolled = self.driver.find_element('xpath', financial_my_tasks_check_new_payment_approvals2)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_approvals2)

    def enter_financial_my_tasks_check_new_payment_description(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', financial_my_tasks_check_new_payment_description, text)

    def enter_financial_my_tasks_check_new_payment_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_btn)

    def enter_financial_my_tasks_check_new_payment_cancellation_reason(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_cancellation_reason)

    def enter_financial_my_tasks_check_new_payment_cancellation_reason_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', financial_my_tasks_check_new_payment_cancellation_reason_option)




