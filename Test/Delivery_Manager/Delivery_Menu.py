from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Locators import *

from Pages.Delivery_Manager.Menu import Delivery_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Customer_Manager.Menu import Menu
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Delivery_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_delivery_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_delivery)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        print("############################################")

    ################### delivery_manager_check_menu ###################

    def test02_delivery_manager_check_menu(self):
        delivery = Delivery_My_Tasks(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        my_tasks.enter_delivery_menu_check_tag2()
        delivery.enter_delivery_menu_check_tag_dashboard()
        delivery.enter_delivery_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        menu.enter_customer_manager_menu_check_dashboard()
        menu.enter_customer_manager_menu_check_my_tasks()
        delivery.enter_delivery_menu_check_inbox()
        delivery.enter_delivery_menu_check_information_and_training()
        delivery.enter_delivery_menu_check_management_reports()
        delivery.enter_delivery_menu_check_orders()
        delivery.enter_delivery_menu_search_orders()
        delivery.enter_delivery_shipping_rate()
        delivery.enter_delivery_check_exchange_rates()
        delivery.enter_delivery_check_list_excel_output()
        delivery.enter_delivery_check_user_profile()
        delivery.enter_delivery_check_change_password()
        delivery.enter_delivery_check_exit()
        print("تمام موارد منوی delivery_manager به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### clearance_check_my_tasks ###################

    def test03_clearance_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        delivery = Delivery_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        delivery.len_delivery()
        delivery.ready_to_deliver_to_customer()
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
