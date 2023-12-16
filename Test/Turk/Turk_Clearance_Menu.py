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


class Test_Turk_Clearance_Menu(unittest.TestCase):
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

    ################### turk_clearance_check_menu ###################

    def test02_turk_clearance_check_menu(self):
        menu = Menu(driver=self.driver)
        turk = Turk(driver=self.driver)
        turk.enter_turk_menu_check_tag()
        turk.enter_turk_clearance_menu_check_name()
        turk.enter_turk_clearance_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        turk.turk_clearance_menu_dashboard()
        turk.turk_clearance_menu_my_tasks()
        turk.turk_clearance_menu_inbox()
        turk.turk_clearance_menu_train()
        turk.turk_clearance_menu_warehouses()
        turk.turk_clearance_menu_accept_order_op_by_scan()
        turk.turk_clearance_menu_batches()
        turk.turk_clearance_menu_persons()
        turk.turk_clearance_menu_crypto_gateway_recovery()
        turk.turk_clearance_menu_list_excel_output()
        turk.turk_clearance_menu_user_profile()
        turk.turk_clearance_menu_change_password()
        turk.turk_clearance_menu_exit()
        print("تمام موارد منوی اکانت ترخیص ترکیه به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### turk_clearance_check_my_tasks ###################

    def test03_turk_clearance_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        turk = Turk(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        turk.len_turk_clearance()
        admin.my_tasks_check("//*[@id='nav-category-1']/div/div/div/div[2]/a[1]")
        turk.my_tasks_check_table(12, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Clearance Inquiry Code', 'starting city', 'Destination city', 'Order', 'Order product', 'Total actual weight (kg)', 'Total value', 'Unit of value'])
        admin.my_tasks_check("//*[@id='nav-category-1']/div/div/div/div[2]/a[2]")
        turk.my_tasks_check_table(14, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'starting city', 'Repack requests', 'Total actual weight (kg)', 'Total value', 'Unit of value', 'Description', 'Clearance invoice type', 'Base clearance price in Rial'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
