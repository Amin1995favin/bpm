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


class Test_Chain_Menu1(unittest.TestCase):
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

    ################### chain_check_menu ###################

    def test02_chain_check_menu(self):
        menu = Menu(driver=self.driver)
        warehouses = Warehouses_My_Tasks(driver=self.driver)
        chain = Chain(driver=self.driver)
        chain.enter_chain_menu_check_tag()
        chain.enter_chain_menu_check_name()
        chain.enter_chain_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        warehouses.warehouses_menu_dashboard()
        warehouses.warehouses_menu_my_tasks()
        warehouses.warehouses_menu_inbox()
        warehouses.warehouses_menu_information_and_training()
        warehouses.warehouses_menu_orders()
        warehouses.warehouses_menu_warehouses()
        warehouses.warehouses_menu_receive_ordered_goods_by_scanning()
        warehouses.warehouses_menu_batches()
        chain.chain_menu_persons()
        chain.chain_menu_crypto_gateway_recovery()
        chain.chain_menu_companies()
        chain.chain_menu_list_excel_output()
        chain.chain_menu_user_profile()
        chain.chain_menu_change_password()
        chain.chain_menu_exit()
        print("تمام موارد منوی اکانت مدیر چین به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### chain_check_my_tasks ###################

    def test03_chain_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        chain = Chain(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        chain.len_chain()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")
        chain.my_tasks_check_table(8, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Sender (company)', 'Order goods', 'Packaging description', 'Order weight (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")
        chain.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Required services', 'Total chargeable weight (kg)', 'Total value', 'Unit of value'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")
        chain.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order weight (KG)', 'Type of clearance', 'Destination', 'Order batches', 'Exit the card'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[4]")
        chain.my_tasks_check_table(12, ['No.', 'the operation', 'Track number', 'Task entry time to this card', 'Customer manager', 'Number of goods', 'track value (USD)', 'PL', 'PI', 'Batch number', 'Print', 'Exit the card'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[5]")
        chain.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order weight (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
