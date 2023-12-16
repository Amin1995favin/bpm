from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
from Pages.Syria.Menu import Syria
import unittest
from Pages.Warehouses.Menu import Warehouses_My_Tasks

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Syria_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_syria ###################

    def test01_syria(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_syria)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت شعبه سوریه شد. ")
        print("############################################")

    ################### syria_check_menu ###################

    def test02_syria_check_menu(self):
        menu = Menu(driver=self.driver)
        warehouses = Warehouses_My_Tasks(driver=self.driver)
        syria = Syria(driver=self.driver)
        syria.enter_syria_menu_check_tag()
        syria.enter_syria_menu_check_name()
        syria.enter_syria_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        syria.syria_menu_dashboard()
        syria.syria_menu_my_tasks()
        syria.syria_menu_inbox()
        syria.syria_menu_train()
        syria.syria_menu_orders()
        syria.syria_menu_warehouses()
        syria.syria_menu_accept_order_op_by_scan()
        syria.syria_menu_batches()
        syria.syria_menu_crypto_gateway_recovery()
        syria.syria_menu_list_excel_output()
        syria.syria_menu_user_profile()
        syria.syria_menu_change_password()
        syria.syria_menu_exit()
        print("تمام موارد منوی اکانت مدیر شعبه سوریه به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### syria_check_my_tasks ###################

    def test03_syria_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        syria = Syria(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        syria.len_syria()
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[1]")
        syria.my_tasks_check_table(10, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'طلب جدید', 'خدمات مطلوبة', 'الوزن الإجمالی المستحق للدفع (کغ)', 'القیمة الکلیة', 'واحدة القیمة'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[2]")
        syria.my_tasks_check_table(6, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'تأکید الطلب'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
