from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Uae.Menu import Uae
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Uae_Delivery(unittest.TestCase):
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

    ################### dubai_check_menu ###################

    def test02_dubai_check_menu(self):
        menu = Menu(driver=self.driver)
        uae = Uae(driver=self.driver)
        uae.enter_uae_menu_check_tag()
        uae.enter_uae_menu_check_tag_dashboard()
        uae.enter_uae_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        uae.uae_delivery_menu_dashboard()
        uae.uae_delivery_menu_my_tasks()
        uae.uae_delivery_menu_information()
        uae.uae_delivery_menu_orders()
        uae.uae_delivery_menu_warehouses()
        uae.uae_delivery_menu_receive_ordered_goods()
        uae.uae_delivery_menu_batches()
        uae.uae_delivery_menu_duplicate()
        uae.uae_delivery_menu_excel()
        uae.uae_delivery_menu_user_profile()
        uae.uae_delivery_menu_change_password()
        uae.uae_delivery_menu_exit()
        print("تمام موارد منوی دلیوری امارات به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### admin_dubai_check_my_tasks ###################

    def test03_admin_dubai_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        uae = Uae(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        uae.len_dubai()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(8, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'Order goods', 'Packaging description', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Sender (person)', 'Type of shipping', 'Total volumetric weight (kg)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Required services', 'Total chargeable weight (kg)', 'Total value', 'Unit of value'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(6, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order confirmation'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(11, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Packaging description', 'Order weight (KG)', 'Tracker'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Cargo pickup', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(8, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
