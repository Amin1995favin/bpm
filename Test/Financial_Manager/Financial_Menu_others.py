from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Financial_Manager.Menu import Financial_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Financial_Manager_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_financial_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_financial)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        print("############################################")

    ################### financial_check_my_tasks ###################

    def test02_financial_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        financial = Financial_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        # financial.len_financial_manager_my_task()
        financial.click_customer_manager()
        financial.check_china_transaction()
        my_tasks.my_tasks_check_table(5, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)'])
        financial.sales_claims()
        my_tasks.my_tasks_check_table(7, ['ردیف', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])
        financial.click_warehouses()
        financial.auto_billed_order()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
