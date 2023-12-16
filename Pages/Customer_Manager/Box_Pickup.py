
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


class Box_Pickup:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_cargo_pickup(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_cargo_pickup)

    def enter_box_pickup_check_order(self):
        assert self.driver.find_element('xpath', box_pickup_order)
        print("تاییدیه بارگیری کالا", " به درستی مشاهده شد")

    def enter_box_pickup_check_order_check(self):
        assert len(self.driver.find_elements('xpath', "//span[@class='select2-selection select2-selection--single']")) == 3
        assert len(self.driver.find_elements('xpath', "//select")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]//button")) == 5
        print("تعداد و بخش های مختلف تاییدیه فاکتور صحیح می باشد.")

    def enter_box_pickup_check_internal_carriage(self):
        assert self.driver.find_element('xpath', box_pickup_internal_carriage)
        print("آیا بازگشت مالیاتی دارد؟", " به درستی مشاهده شد")

    def enter_box_pickup_sender_information(self):
        assert self.driver.find_element('xpath', box_pickup_sender_information)
        print("اطلاعات فرستنده", " به درستی مشاهده شد")

    def enter_box_pickup_sender_person(self):
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_sender_person)

    def enter_box_pickup_sender_person_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', box_pickup_sender_person_name, text)

    def enter_box_pickup_sender_person_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_sender_person_option)

    def enter_box_pickup_sender_company(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_sender_company)

    def enter_box_pickup_sender_company_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', box_pickup_sender_company_name, text)

    def enter_box_pickup_sender_company_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_sender_company_option)

    def enter_box_pickup_sender_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_sender_submit)

    def enter_box_pickup_send_the_pickup_command(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_send_the_pickup_command)

    def enter_box_pickup_send_the_pickup_command_error(self):
        sleep(2)
        assert self.driver.find_element('xpath', box_pickup_send_the_pickup_command_error)
        print(" لطفا اطلاعات ارسال کننده را تکمیل کنید.")

    def enter_box_pickup_cancel_the_download_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_pickup_cancel_the_download_order)
