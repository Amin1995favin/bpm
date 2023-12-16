from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Locators import *
from Pages.Crm.Menu import Crm_My_Tasks
from Pages.Delivery_Manager.Menu import Delivery_My_Tasks
from Pages.Warehouses.Menu import Warehouses_My_Tasks
from Pages.Admin.Menu import Admin_My_Tasks
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


class Test_Crm_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_crm ###################

    def test01_crm(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_crm)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################### crm_check_menu ###################

    def test02_crm_check_menu(self):
        delivery = Delivery_My_Tasks(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        crm = Crm_My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        my_tasks.enter_delivery_menu_check_tag()
        crm.enter_crm_menu_check_tag_dashboard()
        crm.enter_crm_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        crm.crm_dashboard()
        crm.crm_my_task()
        crm.crm_inbox()
        crm.crm_train()
        crm.crm_report()
        crm.crm_orders()
        crm.crm_shipping_cost()
        crm.crm_exchangerates()
        crm.crm_excel_export_files()
        crm.crm_check_user_profile()
        crm.crm_check_change_password()
        crm.crm_check_exit()
        print("تمام موارد منوی delivery_manager به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### crm_check_my_tasks ###################

    def test03_crm_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        crm = Crm_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        crm.len_crm()
        admin.my_tasks_check("//*[@id='nav-category-9']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'علت لغو', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        admin.my_tasks_check("//*[@id='nav-category-9']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'آخرین تماس', 'صاحب سفارش', 'سفارش های کاربر', 'عملیات'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
