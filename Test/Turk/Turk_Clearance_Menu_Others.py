from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
from Pages.Turk.Menu import Turk
import unittest


# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Turk_Clearance_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_turk_clearance ###################

    def test01_turk_clearance(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(turk_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت ترخیص ترکیه شد. ")
        print("############################################")

    ################### turk_clearance_check_my_tasks ###################

    def test02_turk_clearance_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        turk = Turk(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        turk.len_turk_clearance_my_task()
        turk.clearance_click_warehouse()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")
        turk.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Required services', 'Total chargeable weight (kg)', 'Total value', 'Unit of value'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")
        turk.my_tasks_check_table(11, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Packaging description', 'Order weight (KG)', 'Tracker'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[4]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Cargo pickup', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[5]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[6]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[7]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[8]")
        turk.my_tasks_check_table(10, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[9]")
        turk.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
