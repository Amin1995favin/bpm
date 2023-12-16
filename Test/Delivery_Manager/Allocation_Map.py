from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.Warehouses.Warehouses import Warehouses
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest
import random

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

w = ""


def random_phone_num2():
    first = str(random.randint(0, 99)).zfill(2)
    w = '{}'.format(first)
    return w


def random_phone_num3():
    second = str(random.randint(1, 888)).zfill(3)
    w = '{}'.format(second)
    return w


def random_letter():
    alphabet = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع',
                'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
    w = random.choice(alphabet)
    return w


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### login_delivery_manager ###################

    def test01_login_delivery_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        print("############################################")

    ################### delivery_manager_allocation_map ###################

    def test02_delivery_manager_allocation_map(self):
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery.enter_delivery_manager_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak()
        delivery.enter_delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map()
        delivery.enter_deliver_cars_area_allocation_map()
        delivery.enter_delivery_manager_allocation_map()
        delivery.enter_deliver_cars_area_allocation_map_submit()
        delivery.enter_deliver_cars_area_allocation_map_popup_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("موقعیت به درستی اختصاص داده شد.")
        delivery.enter_delivery_manager_allocation_map_zoom_out()
        delivery.enter_deliver_cars_area_allocation_map_delete_location()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("موقعیت به درستی حذف شد.")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
