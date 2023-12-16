from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Warehouses.Menu import Warehouses_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Warehouses_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_warehouses_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(warehouse_id2)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر انبار چین شد. ")
        print("############################################")

    ################### warehouses_manager_check_menu ###################

    def test02_warehouses_manager_check_menu(self):
        warehouses = Warehouses_My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        warehouses.enter_warehouses_menu_check_tag()
        warehouses.enter_warehouses_menu_check_tag_dashboard()
        warehouses.enter_warehouses_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        warehouses.warehouses_menu_dashboard()
        warehouses.warehouses_menu_my_tasks()
        warehouses.warehouses_menu_inbox()
        warehouses.warehouses_menu_information_and_training()
        warehouses.warehouses_menu_orders()
        warehouses.warehouses_menu_warehouses()
        warehouses.warehouses_menu_receive_ordered_goods_by_scanning()
        warehouses.warehouses_menu_batches()
        warehouses.warehouses_menu_persons()
        warehouses.warehouses_menu_crypto_gateway_recovery()
        warehouses.warehouses_menu_companies()
        warehouses.warehouses_menu_list_excel_output()
        warehouses.warehouses_menu_user_profile()
        warehouses.warehouses_menu_change_password()
        warehouses.warehouses_menu_exit()
        print("تمام موارد منوی warehouses_china به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### warehouses_check_my_tasks ###################

    def test03_warehouses_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        warehouses = Warehouses_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        warehouses.len_warehouses()
        warehouses.orders_are_waiting_to_be_batched()
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order product', 'Required services', 'Total chargeable weight (kg)', 'Total value', 'Unit of value'])
        warehouses.order_with_tax_returns()
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order weight (KG)', 'Type of clearance', 'Destination', 'Order batches', 'Exit the card'])
        warehouses.print_warehouse_documents()
        my_tasks.my_tasks_check_table(12, ['No.', 'the operation', 'Track number', 'Task entry time to this card', 'Customer manager', 'Number of goods', 'track value (USD)', 'PL', 'PI', 'Batch number', 'Print', 'Exit the card'])
        warehouses.sending_to_warehouse()
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order weight (KG)'])
        warehouses.loading()
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'status', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        warehouses.repack_request_origin_warehouse()
        my_tasks.my_tasks_check_table(10, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'the details', 'Order weight (KG)', 'starting city', 'Repack goods', ' '])
        warehouses.request_references()
        my_tasks.my_tasks_check_table(9, ['No.', 'the operation', 'Cost registration and final approval', 'Task entry time to this card', 'Order', 'Order goods', 'Order weight (KG)', 'Sub-crack numbers', 'Returning fee payer'])
        warehouses.notification_of_change_of_route_to_the_source_warehouse()
        my_tasks.my_tasks_check_table(11, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Order', 'Order weight (KG)', 'Sender (person)', 'Receiver (person)', 'Order type', 'The location has changed', 'Exit the card'])
        warehouses.loaded()
        my_tasks.my_tasks_check_table(8, ['No.', 'Order', 'Task entry time to this card', 'Cargo pickup', 'Sender (company)', 'Internal transport information', 'Order goods', 'Order weight (KG)'])
        warehouses.click_customer_manager()
        warehouses.request_buy_car_table()
        my_tasks.my_tasks_check_table(11, ['No.', 'the operation', ' ', 'Task entry time to this card', 'Approvals Buy requests', 'Order', 'Origin', 'Destination', 'Service', 'Purchase request information', 'the operation'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
