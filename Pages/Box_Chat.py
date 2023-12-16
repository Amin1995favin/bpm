from Locators import *
from time import sleep


class Box_Chat:
    def __init__(self, driver):
        self.driver = driver

###click_box_chat

    def enter_click_box_chat(self):
        self.driver.find_element('xpath', click_box_chat).click()

    def enter_box_chat_check_form(self):
        assert self.driver.find_element('xpath', box_chat_check_form)
        print("فرم مذاکرات به درستی نمایش داده شد.")

###create_box_chat

    def enter_box_chat_contact(self, name):
        self.driver.find_element('xpath', box_chat_contact).send_keys(name)

    def enter_box_chat_contact_option(self):
        self.driver.find_element('xpath', box_chat_contact_option).click()

    def enter_box_chat_check(self):
        assert len(self.driver.find_elements('xpath', "//input")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 5

    def enter_box_chat_text(self, text):
        self.driver.find_element('xpath', box_chat_text).send_keys(text)

    def enter_box_chat_submit(self):
        self.driver.find_element('xpath', box_chat_submit).click()
        print("مذاکره به درستی ایجاد شد.")

    def enter_box_chat_check_text(self):
        sleep(2)
        a = self.driver.find_element('xpath', box_chat_check_text).text
        assert a == "سلام"

    def enter_box_chat_check_customer_manager(self):
        a = self.driver.find_element('xpath', box_chat_check_customer_manager).text
        assert a == "زهرا پیروز Zahra Pirooz"

    def enter_box_chat_check_contact(self):
        a = self.driver.find_element('xpath', box_chat_check_contact).text
        assert a == "ملیکا کابلی Melika Kaboli"

    def enter_box_chat_check_contact_location(self):
        a = self.driver.find_element('xpath', box_chat_check_contact_location).text
        assert a == "General Manager"

    def enter_box_chat_check_edite(self):
        assert self.driver.find_element('xpath', box_chat_check_edite)












