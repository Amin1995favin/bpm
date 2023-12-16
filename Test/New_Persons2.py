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


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### Login_customer_manager ###################

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        mobile = random_phone_chin_num_generator()
        login.enter_login_username(mobile)
        login.enter_login_btn_submit_next()
        login.enter_login_btn_submit_next_captcha()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        persons.enter_new_person_check_form()
        print("تعداد فیلد های فرم صحیح می باشد و چک شد که همان فیلد های مورد نیاز موجود باشد.")
        print("############################################")
        persons.enter_new_person_btn()
        print("دیتایی وارد نشده است.")
        print("############################################")
        persons.enter_new_person_first_name("کاربر")
        persons.enter_new_person_last_name("تست")
        persons.enter_new_person_first_name_en("user")
        persons.enter_new_person_btn()
        print("اطلاعات کاربر کامل وارد نشده است.")
        print("############################################")
        persons.enter_new_person_first_name_en("کاربر")
        persons.enter_new_person_last_name_en("کاربر")
        persons.enter_new_person_gender()
        persons.enter_new_person_gender_option()
        persons.enter_new_person_email("user@gmail.com")
        persons.enter_new_person_btn()
        print("اطلاعات کاربر صحیح نیست. نام انگلیسی صحیح وارد شود.")
        print("############################################")
        persons.enter_new_person_last_name("کاربر")
        persons.enter_new_person_first_name_en("user")
        persons.enter_new_person_last_name_en("test")
        persons.enter_new_person_how_find_us()
        persons.enter_new_person_how_find_us_option()
        persons.enter_new_person_btn()
        print("فیلد های تکراری؛ نام و نام خانوادگی به درستی وارد نشده اند.")
        print("############################################")
        persons.enter_new_person_last_name("تست")
        persons.enter_new_person_address(
            "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد،")
        persons.enter_new_person_btn()
        print(" مقدار وارد شده برای آدرس باید بین 0 و 255 کاراکتر باشد!")
        print("############################################")
        persons.enter_new_person_gender2()
        persons.enter_new_person_gender2_option()
        persons.enter_new_person_language()
        persons.enter_new_person_language_option()
        persons.enter_new_person_mobile2("989129999999")
        persons.enter_new_person_phone1("0212345678")
        persons.enter_new_person_phone2("0212345678")
        persons.enter_new_person_postalcode("1234567890")
        persons.enter_new_person_address("tehran")
        persons.enter_new_person_btn()
        print("کاربر با موفقیت ایجاد شد.")
        print("############################################")
        persons.enter_new_person_profile_edit()
        persons.enter_new_person_new_password("A123456789a")
        persons.enter_new_person_new_password_repeat("A123456789a")
        persons.enter_new_person_btn()
        print("پسورد جدید ثبت شد.")
        print("############################################")
        self.driver.get(base_url)
        login.enter_login_username(mobile)
        login.enter_login_btn_submit_next()
        login.enter_login_username_with_password("A123456789a")
        login.enter_login_username_with_password_click()
        print("با موفقیت با پسورد جدید وارد شد.")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
