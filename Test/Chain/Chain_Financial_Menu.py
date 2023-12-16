from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
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


class Test_Chain_Financial_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_chain_financial ###################

    def test01_chain_financial(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(chain_financial)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت مالی چین شد. ")
        print("############################################")

    ################### chain_financial_check_menu ###################

    def test02_chain_financial_check_menu(self):
        menu = Menu(driver=self.driver)
        warehouses = Warehouses_My_Tasks(driver=self.driver)
        chain = Chain(driver=self.driver)
        chain.enter_chain_financial_menu_check_tag()
        chain.enter_chain_financial_menu_check_name()
        chain.enter_chain_financial_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        warehouses.warehouses_menu_dashboard()
        warehouses.warehouses_menu_my_tasks()
        warehouses.warehouses_menu_inbox()
        warehouses.warehouses_menu_information_and_training()
        warehouses.warehouses_menu_orders()
        chain.financial_menu_batches()
        chain.financial_menu_yuan_payments()
        chain.financial_menu_china_costs()
        chain.financial_menu_china_monthly_account()
        chain.financial_menu_investigate_theron_network_transaction()
        chain.financial_menu_list_excel_output()
        chain.financial_menu_user_profile()
        chain.financial_menu_change_password()
        chain.financial_menu_exit()
        print("تمام موارد منوی اکانت مدیر چین به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### chain_financial_check_my_tasks ###################

    def test03_chain_financial_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        chain = Chain(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        chain.len_chain_financial()
        admin.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a")
        chain.my_tasks_check_table(7, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Condition', 'Amount', 'Pre-assigned to factors'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
