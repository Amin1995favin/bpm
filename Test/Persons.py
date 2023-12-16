from selenium import webdriver
from Locators import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Manager.Manager import Manager
from Pages.MongoDB.Mongo import Mongodb
from Pages.Persons import Persons
import unittest
import random

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

w = ""


def random_phone_num_generator():
    first = str(random.randint(0, 9)).zfill(1)
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    w = '{}{}{}{}'.format(9891, first, second, last)
    return w


def random_phone_chin_num_generator():
    first = str(random.randint(0, 9)).zfill(1)
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    w = '{}{}{}{}'.format(86172, first, second, last)
    return w


def national_code_generator():
    number_list = []
    _sum = 0
    out = ""
    for i in reversed(range(2, 11)):
        _j = random.randint(0, 9)
        number_list.append(str(_j))
        _sum += _j * i
    _m = _sum % 11
    if _m < 2:
        number_list.append(str(_m))
    elif _m >= 2:
        number_list.append(str(11 - _m))
    return out.join(number_list)


class Test_Persons(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

################### Login_customer_manager ###################

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")

###persons_create_check_data

    def test02_persons_create_check_data(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        persons = Persons(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_create()
        persons.enter_click_create_order_create_person()
        persons.enter_create_order_create_person_check_form()
        persons.enter_create_order_create_person_check_selection()
        print("تعداد فیلد های فرم صحیح می باشد و چک شد که همان فیلد های مورد نیاز موجود باشد.")
        print("############################################")
        persons.enter_create_order_create_person_submit()
        print("دیتایی وارد نشده است.")
        print("############################################")

###persons_create_check_check_data

    def test03_persons_create_check_data(self):
        persons = Persons(driver=self.driver)
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_create_order_create_person_submit()
        print("اطلاعات کاربر کامل وارد نشده است.")
        print("############################################")

###persons_create_check_check_data_name_en

    def test04_persons_create_check_data_name_en(self):
        persons = Persons(driver=self.driver)
        mobile = random_phone_num_generator()
        persons.enter_create_order_create_person_phon1(mobile)
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("کاربر")
        persons.enter_persons_create_firstname_en("کاربر")
        persons.enter_persons_create_lastname_en("کاربر")
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_create_order_create_person_submit()
        print("اطلاعات کاربر صحیح نیست. نام انگلیسی صحیح وارد شود.")
        print("############################################")

####persons_create_check_data_name

    def test05_persons_create_check_data_name(self):
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        code_melli = national_code_generator()
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("user")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli(code_melli)
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_create_order_create_person_submit()
        print("فیلد های تکراری؛ نام و نام خانوادگی به درستی وارد نشده اند.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("############################################")

###persons_create_check_data_address

    def test06_persons_create_check_data_address(self):
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        scrolled = self.driver.find_element('xpath', persons_create_address)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        persons.enter_persons_create_address(
            "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد،")
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        sleep(1)
        persons.enter_create_order_create_person_submit()
        print(" مقدار وارد شده برای آدرس باید بین 0 و 255 کاراکتر باشد!")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print("############################################")

##persons_create_check_data_phone

    def test07_persons_create_check_data_phone(self):
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        scrolled = self.driver.find_element('xpath', create_order_create_person_phon1)
        scrolled.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1(000000000000)
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_create_order_create_person_submit()
        print(" شماره موبایل معتبر نیست؛ همه کارکتر ها 0 می باشد.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print("############################################")
        scrolled.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1("09379161533")
        persons.enter_create_order_create_person_submit()
        print(" شماره موبایل معتبر نیست.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print("############################################")
        scrolled.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1("98937916153")
        persons.enter_create_order_create_person_submit()
        print(" شماره موبایل معتبر نیست؛ کارکتر کمتر.")
        print("############################################")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        scrolled.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1("9893791615333")
        sleep(1)
        persons.enter_create_order_create_person_submit()
        print(" شماره موبایل معتبر نیست؛ کارکتر بیشتر.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print("############################################")

####persons_create_check_data_code_melli

    def test08_persons_create_check_data_code_melli(self):
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        mobile = random_phone_num_generator()
        scrolled1 = self.driver.find_element('xpath', create_order_create_person_phon1)
        scrolled1.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1(mobile)
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli("0000000000")
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_create_order_create_person_submit()
        print("کد ملی تکراری میباشد.")
        print("############################################")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        scrolled = self.driver.find_element('xpath', persons_create_code_melli)
        scrolled.location_once_scrolled_into_view
        persons.enter_persons_create_code_melli("123456789")
        persons.enter_create_order_create_person_submit()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print(" کد ملی وارد شده معتبر نمی باشد، کاراکتر کمتر از ده رقم.")
        print("############################################")
        scrolled.location_once_scrolled_into_view
        persons.enter_persons_create_code_melli("12345678900")
        persons.enter_create_order_create_person_submit()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print(" کد ملی وارد شده معتبر نمی باشد، کاراکتر بیشتر از ده رقم.")
        print("############################################")

    ################### Orderorders_create_and_person_creates_Create ###################

    def test09_orders_create_and_person_create(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        persons = Persons(driver=self.driver)
        # code_melli = national_code_generator()
        mobile = random_phone_num_generator()
        # sleep(1)
        # orders_create.enter_click_orders()
        # orders_create.enter_click_orders_create()
        # persons.enter_click_create_order_create_person()
        scrolled1 = self.driver.find_element('xpath', create_order_create_person_phon1)
        scrolled1.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1(mobile)
        persons.enter_assert_create_order_create_person_representation()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli("")
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_create_order_create_person_language()
        persons.enter_create_order_create_person_language_option()
        persons.enter_persons_create_phone_number2("989129999999")
        persons.enter_persons_create_phone1("0212345678")
        persons.enter_persons_create_phone2("0212345678")
        persons.enter_persons_create_company_phone("0212345678")
        persons.enter_persons_create_company_name("favin")
        persons.enter_persons_create_postalcode("1234567890")
        persons.enter_persons_create_address("tehran")
        persons.enter_persons_create_description("این یک کاربر تست می باشد.")
        sleep(2)
        persons.enter_create_order_create_person_submit()
        print("کاربر با موفقیت ایجاد شد.")
        sleep(1)
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")
        print("############################################")
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve()
        orders_create.enter_product_final_order_confirmation()
        print("############################################")

################## Login_manager ###################

    def test10_login_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شد")
        print("############################################")

################### check_add_person ###################

    def test11_check_add_person(self):
        manager = Manager(driver=self.driver)
        persons = Persons(driver=self.driver)
        manager.enter_click_manager_my_task()
        manager.enter_manager_my_task_all()
        sleep(2)
        manager.enter_manager_my_task_set_customer_manager()
        manager.enter_manager_my_task_update()
        manager.enter_manager_my_task_search("کاربر تست")
        manager.enter_manager_my_task_search_btn()
        manager.enter_manager_my_task_set_customer_manager_click()
        manager.enter_manager_my_task_set_customer_manager_state()
        manager.enter_manager_my_task_set_customer_manager_state_name("تهران")
        sleep(1)
        manager.enter_manager_my_task_set_customer_manager_state_option()
        sleep(1)
        manager.enter_manager_my_task_set_customer_manager_city()
        manager.enter_manager_my_task_set_customer_manager_city_name("تهران")
        sleep(1)
        manager.enter_manager_my_task_set_customer_manager_city_option()
        manager.enter_manager_my_task_set_customer_manager_select()
        manager.enter_manager_my_task_set_customer_manager_name("زهرا پیروز")
        sleep(1)
        manager.enter_manager_my_task_set_customer_manager_option()
        manager.enter_manager_my_task_set_customer_manager_btn()
        sleep(5)
        manager.enter_manager_my_task_set_customer_manager_click_person()
        all_handle1 = self.driver.window_handles
        self.driver.switch_to.window(all_handle1[1])
        sleep(1)
        persons.enter_persons_create_check_name()
        persons.enter_persons_create_check_expert_user()
        persons.enter_persons_create_check_phone_number()
        persons.enter_persons_create_check_connected_user()
        persons.enter_persons_create_check_inventory()
        persons.enter_persons_create_check_records()
        print("############################################")

################## Login_customer_manager_add_person_china ###################

    def test12_Login_customer_manager_add_person_china(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        persons = Persons(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_create()
        persons.enter_click_create_order_create_person()
        mobile = random_phone_chin_num_generator()
        # scrolled1 = self.driver.find_element('xpath', create_order_create_person_phon1)
        # scrolled1.location_once_scrolled_into_view
        persons.enter_create_order_create_person_phon1(mobile)
        persons.enter_assert_create_order_create_person_representation()
        persons.enter_persons_create_firstname("کاربر چینی")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli("")
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_create_order_create_person_language()
        persons.enter_create_order_create_person_language_option()
        persons.enter_persons_create_phone_number2("989129999999")
        persons.enter_persons_create_phone1("0212345678")
        persons.enter_persons_create_phone2("0212345678")
        persons.enter_persons_create_company_phone("0212345678")
        persons.enter_persons_create_company_name("favin")
        persons.enter_persons_create_postalcode("1234567890")
        persons.enter_persons_create_address("tehran")
        persons.enter_persons_create_description("این یک کاربر تست با شماره چینی می باشد.")
        persons.enter_create_order_create_person_submit()
        a = self.driver.find_element('xpath', orders_create_name_select_option_text).text
        print(a)
        assert 'کاربر چینی تست' in a
        print("کاربر با موفقیت ایجاد شد.")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Persons , 'Persons')
