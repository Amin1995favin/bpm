
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


class Check_Wallet:
    def __init__(self, driver):
        self.driver = driver

    def enter_check_wallet_click_order5(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5)

    def enter_check_wallet_click_order5_check_iranian_rial(self):
        scrolled = self.driver.find_element('xpath', check_wallet_click_order5_check_iranian_rial)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        el1 = "return  $('#main-content-wrapper > section.content > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(9) > div.small-box.bg-olive > div.inner > h4 > span').html().replace(/,/g , '')"
        el2 = self.driver.execute_script(el1)
        if el2 =="0.00":
            el2 = 0
            print(el2)
            return el2
        else:
            el2 = int(el2)
            print(el2)
            return el2

    def enter_check_wallet_click_order5_check_euro(self):
        scrolled = self.driver.find_element('xpath', check_wallet_click_order5_check_euro)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        el1 = "return $('#main-content-wrapper > section.content > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(4) > div.small-box.bg-olive > div.inner > h4 > span').html().replace(/,/g , '')"
        el2 = self.driver.execute_script(el1)
        if el2 =="0.00":
            el2 = 0
            print(el2)
            return el2
        else:
            # el2 = int(el2)
            print(el2)
            return el2

    def enter_check_wallet_click_order5_charge(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge)

    def enter_check_wallet_click_order5_charge_amount(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', check_wallet_click_order5_charge_amount, text)

    def enter_check_wallet_click_order5_charge_unit(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_unit)

    def enter_check_wallet_click_order5_charge_unit_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_unit_option)

    def enter_check_wallet_click_order5_charge_unit_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_unit_option2)

    def enter_check_wallet_click_order5_charge_account(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_account)

    def enter_check_wallet_click_order5_charge_account_option1(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_account_option1)

    def enter_check_wallet_click_order5_charge_account_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_account_option2)

    def enter_check_wallet_click_order5_charge_payment_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_payment_type)

    def enter_check_wallet_click_order5_charge_payment_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_payment_type_option)

    def enter_check_wallet_click_order5_charge_description(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', check_wallet_click_order5_charge_description, text)

    def enter_check_wallet_click_order5_charge_time(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', check_wallet_click_order5_charge_time, text)

    def enter_check_wallet_click_order5_charge_payer_account(self, text):
        scrolled = self.driver.find_element('xpath', check_wallet_click_order5_charge_payer_account)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', check_wallet_click_order5_charge_payer_account, text)

    def enter_check_wallet_click_order5_charge_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_wallet_click_order5_charge_btn)










