from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### Login_clearance ###################

    def test01_login_clearance(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")

################### clearance_my_tasks_final_clearance #########################

    def test02_my_tasks_final_clearance(self):
        my_tasks = My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        my_tasks.enter_clearance_my_tasks_need_final_clearance()
        print("وارد قسمت نیاز به استعلام ترخیص نهایی شد.")
        my_tasks.enter_clearance_my_tasks_update()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_search("")
        my_tasks.enter_clearance_my_tasks_search_btn()
        my_tasks.enter_clearance_my_tasks_final_clearance()
        my_tasks.enter_clearance_my_tasks_final_clearance_text_issue()
        scrolled = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_loaded_goods)
        scrolled.location_once_scrolled_into_view
        my_tasks.enter_clearance_my_tasks_final_clearance_loaded_goods()
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        sleep(.1)
        # my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval_error()
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value_of_goods()
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value("2000")
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value_send()
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        my_tasks.enter_clearance_my_tasks_final_clearance_checkbox_order()


        my_tasks.enter_clearance_my_tasks_final_clearance_category()
        sleep(.2)
        my_tasks.enter_clearance_my_tasks_final_clearance_category_option()
        my_tasks.enter_clearance_my_tasks_final_clearance_category_send()
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        sleep(1)



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
