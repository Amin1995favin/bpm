from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders import Orders
import unittest

driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login_customer_manager

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9020981024")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

###check_orders

    def test02_check_orders(self):
        orders = Orders(driver=self.driver)
        orders.enter_click_orders()
        orders.enter_check_orders_end_date()
        orders.enter_orders_check_table_row()
        orders.enter_orders_check_table_order()
        orders.enter_orders_check_table_receiver()
        orders.enter_orders_check_table_sender()
        orders.enter_orders_check_table_order_weight()
        orders.enter_orders_check_table_order_product()
        orders.enter_orders_check_table_required_services()
        orders.enter_orders_check_table_creator()
        orders.enter_orders_check_table_th()
        orders.enter_orders_check_table_customer_manager()

###check_orders_search_id

    def test03_check_orders_search_id(self):
        orders = Orders(driver=self.driver)
        a = orders.enter_orders_check_id()
        orders.enter_orders_check_search(a)
        orders.enter_orders_check_search_btn()
        orders.enter_orders_check_table_search()

###check_orders_id_customer_manager

    def test04_check_orders_id_customer_manager(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_id_click()
        orders.enter_orders_id_customer_manager()



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
