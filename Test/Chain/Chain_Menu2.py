from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Export.Menu import Export_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
from Pages.Chain.Menu import Chain
import unittest

from Pages.Warehouses.Menu import Warehouses_My_Tasks

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_Chain_Menu2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_chain ###################

    def test01_chain(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_chain)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت چین شد. ")
        print("############################################")

    ################### chain_check_my_tasks ###################

    def test02_chain_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        chain = Chain(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[6]")
        chain.my_tasks_check_table(10, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[7]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'the details', 'Order weight (KG)', 'starting city', 'Repack goods'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[8]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Cost registration and final approval', 'Task entry time to this card', 'Order', 'Order goods', 'Order weight (KG)', 'Sub-crack numbers', 'Returning fee payer'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[9]")
        chain.my_tasks_check_table(11, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order weight (KG)', 'Sender (person)', 'Receiver (person)', 'Order type', 'The location has changed', 'Exit the card'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[10]")
        chain.my_tasks_check_table(11, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Packaging description', 'Order weight (KG)', 'Tracker'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[11]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[12]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Cargo pickup', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[13]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[14]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[15]")
        chain.my_tasks_check_table(13, ['No.', 'the operation', 'Track number', 'Task entry time to this card', 'Customer manager', 'Number of goods', 'track value (USD)', 'PL', 'PI', 'Batch number', 'Print', 'Exit the card', 'Edit'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[2]/div/div/div[2]/a[1]")
        chain.my_tasks_check_table(8, ['No.', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'Internal transport information', 'Order goods', 'Order weight (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
