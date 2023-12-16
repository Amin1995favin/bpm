from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Uae.Menu import Uae
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Uae_Menu_Delivery_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_admin ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(uae_delivery)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل دلیوری شعبه امارات شد. ")
        print("############################################")

    ################### admin_dubai_check_my_tasks_others ###################

    def test03_admin_dubai_check_my_tasks_others(self):
        my_tasks = My_Tasks(driver=self.driver)
        uae = Uae(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        uae.len_dubai_my_tasks_delivery()
        uae.click_delivery_delivery()
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Batch :batchno', 'هماهنگی های انجام شده', 'delivery', 'distributor', 'Car ID', 'How to deliver goods'])
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', 'the operation', 'Task entry time to this card', 'Order', 'Order batches', 'هماهنگی های انجام شده', 'Type of clearance', 'Order files', 'The reason for returning from ready to deliver to the customer'])
        uae.click_delivery_customer_manager()
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order weight (KG)', 'sender', 'receiver', 'starting city', 'Postal code', 'Address'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'sender', 'receiver', "The date and time of the sender's readiness for pick-up", 'Description of the date and time of the transmitter readiness'])
        uae.click_delivery_export()
        admin.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Total value', 'Description', 'Purchase invoice type'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
