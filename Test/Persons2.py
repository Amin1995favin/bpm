from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from Locators import click_persons, persons_create_submit_btn, persons_create_check, persons_create_phone_number, \
    persons_create_check_code_melli, persons_create_check_phone, click_persons_financial, orders_create_name_select, \
    orders_create_name_select_option, orders_create_name_select_option_text
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Orders_Create2 import Orders_Create
from Pages.Persons import Persons
import unittest
import random

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

w=""

def random_phone_num_generator():
    first = str(random.randint(0, 9)).zfill(1)
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    w = '{}{}{}{}'.format(9891,first, second, last)
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


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### Login #########################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل شد")

###persons_create_check_data

    def test02_persons_create_check_data(self):
        persons = Persons(driver=self.driver)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print("دیتایی وارد نشده است.")

###persons_create_check_check_data

    def test03_persons_create_check_data(self):
        persons = Persons(driver=self.driver)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print("اطلاعات کاربر کامل وارد نشده است.")

###persons_create_check_check_data_name_en

    def test04_persons_create_check_data_name_en(self):
        persons = Persons(driver=self.driver)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("کاربر")
        persons.enter_persons_create_lastname_en("کاربر")
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_phone_number(random_phone_num_generator())
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print("اطلاعات کاربر صحیح نیست. نام انگلیسی صحیح وارد شود.")

####persons_create_check_data_name

    def test05_persons_create_check_data_name(self):
        persons = Persons(driver=self.driver)
        sleep(1)
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("user")
        persons.enter_persons_create_lastname("user")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("user")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli(national_code_generator())
        persons.enter_persons_create_phone_number(random_phone_num_generator())
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print("فیلد های تکراری؛ نام و نام خانوادگی به درستی وارد نشده اند.")

###persons_create_check_data_address

    def test06_persons_create_check_data_address(self):
        persons = Persons(driver=self.driver)
        findel = FindElement(driver=self.driver)
        sleep(1)
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_phone_number(random_phone_num_generator())
        persons.enter_persons_create_address(
            "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد،")
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" مقدار وارد شده برای آدرس باید بین 0 و 255 کاراکتر باشد!")

##persons_create_check_data_phone

    def test07_persons_create_check_data_phone(self):
        persons = Persons(driver=self.driver)
        # action = ActionChains(driver=self.driver)
        sleep(1)
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_phone_number(000000000000)
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" شماره موبایل معتبر نیست؛ همه کارکتر ها 0 می باشد.")
        # el= self.driver.find_element('xpath', persons_create_phone_number )
        # el.clear()
        persons.enter_persons_create_phone_number("09379161533")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" شماره موبایل معتبر نیست.")
        persons.enter_persons_create_phone_number("98937916153")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" شماره موبایل معتبر نیست؛ کارکتر کمتر.")
        persons.enter_persons_create_phone_number("9893791615333")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" شماره موبایل معتبر نیست؛ کارکتر بیشتر.")

####persons_create_check_data_code_melli

    def test08_persons_create_check_data_code_melli(self):
        persons = Persons(driver=self.driver)
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        persons.enter_persons_create_code_melli("0000000000")
        persons.enter_persons_create_phone_number(random_phone_num_generator())
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print("کد ملی تکراری میباشد.")
        persons.enter_persons_create_code_melli("123456789")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" کد ملی وارد شده معتبر نمی باشد، کاراکتر کمتر از ده رقم.")
        persons.enter_persons_create_code_melli("12345678900")
        persons.enter_persons_create_submit_btn()
        persons.enter_assert_persons_create_check()
        print(" کد ملی وارد شده معتبر نمی باشد، کاراکتر بیشتر از ده رقم.")

###persons_create_check_non_iranian_data_correct

    def test09_persons_create_check_data_non_iranian_correct(self):
        persons = Persons(driver=self.driver)
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option2()
        mobile = random_phone_num_generator()
        # return mobile
        persons.enter_persons_create_non_iranian_create_code_melli("code_melli1234567")
        persons.enter_persons_create_phone_number(mobile)
        persons.enter_persons_create_phone_number2("989129999999")
        persons.enter_persons_create_phone1("0212345678")
        persons.enter_persons_create_phone2("0212345678")
        persons.enter_persons_create_internal_number("0212345678")
        persons.enter_persons_create_company_phone("0212345678")
        persons.enter_persons_create_company_name("favin")
        persons.enter_persons_create_postalcode("1234567890")
        persons.enter_persons_create_address("tehran")
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_description("این یک کاربر اتباع تستی می باشد.")
        persons.enter_persons_create_submit_btn()
        print("کاربر با موفقیت ایجاد شد.")

###persons_create_check_data_correct

    def test10_persons_create_check_data_correct(self):
        persons = Persons(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        sleep(1)
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        code_melli= national_code_generator()
        mobile= random_phone_num_generator()
        persons.enter_persons_create_code_melli(code_melli)
        persons.enter_persons_create_phone_number(mobile)
        persons.enter_persons_create_phone_number2("989129999999")
        persons.enter_persons_create_phone1("0212345678")
        persons.enter_persons_create_phone2("0212345678")
        persons.enter_persons_create_internal_number("0212345678")
        persons.enter_persons_create_company_phone("0212345678")
        persons.enter_persons_create_company_name("favin")
        persons.enter_persons_create_postalcode("1234567890")
        persons.enter_persons_create_address("tehran")
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_description("این یک کاربر تست می باشد.")
        persons.enter_persons_create_submit_btn()
        print("کاربر با موفقیت ایجاد شد.")
###persons_create_check
        persons.enter_persons_create_check_name()
        persons.enter_persons_create_check_expert_user()
        persons.enter_persons_create_check_marketer()
        persons.enter_persons_create_check_agency()
        persons.enter_persons_create_check_phone_number()
        a = self.driver.find_element('xpath', persons_create_check_code_melli).text
        assert a == code_melli
        print("کدملی بصورت:", a, "و صحیح می باشد.")
        b = self.driver.find_element('xpath', persons_create_check_phone).text
        assert b == mobile
        print("تلفن بصورت:", b, "و صحیح می باشد.")
        persons.enter_persons_create_check_arian()
        persons.enter_persons_create_check_connected_user()
        persons.enter_persons_create_check_enable_disable()
        # sleep(1)
        persons.enter_persons_create_connected_user()
        # sleep(1)
        persons.enter_psp_search_select()
        persons.enter_psp_search_select_name(mobile)
        persons.enter_psp_search_select_option()
        sleep(1)
        # persons.enter_psp_search_show_financial()
        persons.enter_persons_create_check_user_btn()
        persons.enter_persons_create_check_enable()
        persons.enter_persons_create_check_inventory()
        persons.enter_persons_create_check_records()
        # orders_create.enter_click_new_orders_create()
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_create()
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select, 'class', 'selection')
        orders_create.enter_orders_create_name_select_text(mobile)
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select_option,
                                                   'class', 'select2-results__option select2-results__option--highlighted')
        # el= self.driver.find_element('xpath', orders_create_name_select_option_text)
        # assert 'کاربر تست ' in el.get_attribute('data-original-title')
        # print("نمایندگی بصورت:", a, "و صحیح می باشد.")
        orders_create.enter_orders_create_name_select_option_text()

###persons_create_check_data

    def test11_persons_create_check_data(self):
        persons = Persons(driver=self.driver)
        scrolled1 = self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_check_form()
        # sleep(1)
        persons.enter_persons_create_check_selection()
        print("تعداد فیلد های فرم صحیح می باشد و چک شد که همان فیلد های مورد نیاز موجود باشد.")

###persons_create_check_data_correct

    def test12_persons_create_check_data_correct(self):
        persons = Persons(driver=self.driver)
        sleep(1)
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_gender()
        persons.enter_persons_create_gender_option()
        persons.enter_persons_create_email("user@gmail.com")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        code_melli= national_code_generator()
        mobile= random_phone_num_generator()
        persons.enter_persons_create_code_melli(code_melli)
        persons.enter_persons_create_phone_number(mobile)
        persons.enter_persons_create_phone_number2("989129999999")
        persons.enter_persons_create_phone1("0212345678")
        persons.enter_persons_create_phone2("0212345678")
        persons.enter_persons_create_internal_number("0212345678")
        persons.enter_persons_create_company_phone("0212345678")
        persons.enter_persons_create_company_name("favin")
        persons.enter_persons_create_postalcode("1234567890")
        persons.enter_persons_create_address("tehran")
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_description("این یک کاربر تست می باشد.")
        persons.enter_persons_create_submit_btn()
        print("کاربر با موفقیت ایجاد شد.")
###check_phone
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        code_melli2= national_code_generator()
        persons.enter_persons_create_code_melli(code_melli2)
        persons.enter_persons_create_phone_number(mobile)
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_submit_btn()
        print("شماره موبایل تکراری می باشد.")
###check_code_melli
        scrolled1= self.driver.find_element('xpath', click_persons)
        scrolled1.location_once_scrolled_into_view
        persons.enter_click_persons()
        persons.enter_click_persons_create()
        persons.enter_persons_create_firstname("کاربر")
        persons.enter_persons_create_lastname("تست")
        persons.enter_persons_create_firstname_en("user")
        persons.enter_persons_create_lastname_en("test")
        persons.enter_persons_create_non_iranian_nationals()
        persons.enter_persons_create_non_iranian_nationals_option()
        mobile2= random_phone_num_generator()
        persons.enter_persons_create_code_melli(code_melli)
        persons.enter_persons_create_phone_number(mobile2)
        persons.enter_persons_create_agency()
        sleep(1)
        persons.enter_persons_create_agency_option()
        persons.enter_persons_create_expert_user()
        sleep(1)
        persons.enter_persons_create_expert_user_option()
        persons.enter_persons_create_how_find_us()
        persons.enter_persons_create_how_find_us_option()
        persons.enter_persons_create_marketer()
        persons.enter_persons_create_marketer_option()
        persons.enter_persons_create_submit_btn()
        print("کد ملی تکراری می باشد.")

###persons_create_check_data_correct_financial

    def test13_persons_create_check_data_correct_financial(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        persons = Persons(driver=self.driver)
        login.enter_login_username("9125135808")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مالی  شد")
        persons.enter_click_persons_financial()
        persons.enter_click_persons_create()
        persons.enter_financial_persons_create_check_form()
        persons.enter_financial_persons_create_check_selection()
        print("تعداد فیلد های فرم صحیح می باشد و چک شد که همان فیلد های مورد نیاز موجود باشد.")



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
