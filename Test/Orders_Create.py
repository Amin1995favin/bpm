from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
import unittest
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل شد")

###Orders_Create

    def test02_orders_create_no_data(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_create()
        orders_create.enter_orders_create_chooseservices()
        print("وارد کردن صاحب سفارش الزامی می باشد.")

    def test03_orders_create_no_user_id_owner(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print(" امکان ثبت سفارش بدون صاحب سفارش وجود ندارد.")

    def test04_orders_create_no_service(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_name_select()
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_chooseservices()
        print(" لازم است حداقل یکی از سرویس ها را انتخاب نمایید.")

    def test05_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز می باشد.")

###orders_create_products

    def test06_orders_create_check_data(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_data()

    def test07_orders_create_check_data_sender(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_data_sender()

    def test08_orders_create_check_data_receiver(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_data_receiver()

    def test09_orders_create_check_data_factor(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_data_factor()

    def test10_orders_create_check_city(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_information_approve()
        print(" برای ادامه و ثبت سفارش لازم است شهر ارسال کننده را انتخاب نمایید")
        orders_create.enter_orders_create_information_receiver_city()
        orders_create.enter_orders_create_information_receiver_city_name("Tehran")
        sleep(1)
        orders_create.enter_orders_create_information_receiver_city_option()
        orders_create.enter_orders_create_information_approve()
        print(" برای ادامه و ثبت سفارش لازم است شهر دریافت کننده را انتخاب نمایید")

    def test11_orders_create_check_city(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()









    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
