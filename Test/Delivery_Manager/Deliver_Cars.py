from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.MongoDB.Mongo import Mongodb
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


class Test_Deliver_Cars(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []


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

    ################### check_deliver_cars ###################

    def test02_check_deliver_cars(self):
        delivery = Delivery(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        delivery.enter_delivery_manager_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak()
        delivery.enter_delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map()
        delivery.enter_deliver_cars_area_allocation_map()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/deliveryzones/edit/1000000027")
        print(" بخش نقشه اختصاص محدوده به درستی نمایش داده می شود.")
        self.driver.back()
        delivery.enter_deliver_cars_create_car()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/cars/delivercars/1000000027")
        print(" بخش ایجاد خودرو به درستی نمایش داده می شود.")
        self.driver.refresh()
        # delivery.enter_deliver_cars_sync()
        # warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/cars/delivercars/1000000027")
        # print(" بخش همگام سازی به درستی نمایش داده می شود.")
        self.driver.refresh()
        delivery.enter_deliver_cars_check_table()
        print("############################################")

    ################### deliver_cars_create_car ###################

    def test03_deliver_cars_create_car(self):
        delivery = Delivery(driver=self.driver)
        delivery.enter_deliver_cars_create_car()
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        num2 = random_phone_num2()
        num2b = random_phone_num2()
        num3 = random_phone_num3()
        char1 = random_letter()
        print("وارد قسمت ایجاد خودرو شد. ")
        delivery.enter_deliver_cars_create_car_name("نام ماشین")
        delivery.enter_deliver_cars_create_car_number_plates1(num2)
        delivery.enter_deliver_cars_create_car_number_plates2(num3)
        delivery.enter_deliver_cars_create_car_number_plates3(char1)
        delivery.enter_deliver_cars_create_car_number_plates4(num2b)
        delivery.enter_deliver_cars_create_car_satisfaction_coefficient("1")
        delivery.enter_deliver_cars_create_car_send()
        sleep(2)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        self.driver.refresh()
        a = num2 + "ایران" + num3 + char1 + num2b
        print(a)
        b = self.driver.find_element('xpath', deliver_cars_number_plates1).text
        print(b)
        assert a == b
        print("پلاک به درستی اضافه و نمایش داده می شود.")
        print("############################################")

    ################### deliver_cars_selection_delivery ###################

    def test04_deliver_cars_selection_delivery(self):
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery.enter_deliver_cars_selection_delivery_click()
        delivery.enter_deliver_cars_selection_delivery_user_id_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("تحویل دهنده انتخاب شد.")
        delivery.enter_deliver_cars_selection_delivery_click()
        user_id = delivery.enter_deliver_cars_selection_delivery_user_id()
        delivery.enter_deliver_cars_selection_delivery_user_id_delete()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("تحویل دهنده نمی تواند تکراری انتخاب شود و حذف شد.")
        delivery.enter_deliver_cars_selection_delivery_click()
        delivery.enter_deliver_cars_selection_delivery_user_id_select(user_id)
        delivery.enter_deliver_cars_selection_delivery_user_id_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        delivery.enter_deliver_cars_selection_delivery_click()
        user_id1 = delivery.enter_deliver_cars_selection_delivery_user_id()
        assert user_id == user_id1
        print("تحویل دهنده قبلی به درستی انتخاب شده است.")
        delivery.enter_deliver_cars_selection_delivery_user_id_delete()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("############################################")

    ################### deliver_cars_selection_distributor ###################

    def test05_deliver_cars_selection_distributor(self):
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery.enter_deliver_cars_selection_distributor_click()
        delivery.enter_deliver_cars_selection_distributor_user_id_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("موزع انتخاب شد.")
        delivery.enter_deliver_cars_selection_distributor_click()
        user_id = delivery.enter_deliver_cars_selection_delivery_user_id2()
        delivery.enter_deliver_cars_selection_distributor_user_id_delete()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("موزع نمی تواند تکراری انتخاب شود و حذف شد.")
        delivery.enter_deliver_cars_selection_distributor_click()
        delivery.enter_deliver_cars_selection_distributor_user_id_select(user_id)
        delivery.enter_deliver_cars_selection_distributor_user_id_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        delivery.enter_deliver_cars_selection_distributor_click()
        user_id1 = delivery.enter_deliver_cars_selection_delivery_user_id2()
        assert user_id == user_id1
        print("موزع قبلی به درستی انتخاب شده است.")
        delivery.enter_deliver_cars_selection_distributor_user_id_delete()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("############################################")

    ################### check_deliver_cars_the_operation_history ###################

    def test06_check_deliver_cars_the_operation_history(self):
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery.enter_deliver_cars_the_operation_edit_name()
        delivery.enter_deliver_cars_the_operation_edit_name_new("نام ماشین جدید")
        delivery.enter_deliver_cars_the_operation_edit_name_new_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        delivery.enter_deliver_cars_the_operation_disabled()
        delivery.enter_deliver_cars_the_operation_history()
        delivery.enter_check_deliver_cars_the_operation_history_time()
        self.driver.refresh()
        sleep(1)
        delivery.enter_deliver_cars_the_operation_disabled()
        delivery.enter_deliver_cars_the_operation_history()
        delivery.enter_check_deliver_cars_the_operation_history_time2()
        self.driver.refresh()
        print("############################################")

    ################### delivery_manager_allocation_map ###################

    def test07_delivery_manager_allocation_map(self):
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        # delivery.enter_delivery_manager_warehouse()
        # delivery.enter_delivery_manager_warehouse_kahrizak()
        # delivery.enter_delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map()
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


Mongodb.run_tests_and_insert_into_mongodb(Test_Deliver_Cars , 'Deliver_Cars')
