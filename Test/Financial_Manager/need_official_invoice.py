from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

from Locators import *

from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Financial_Manager.financial_manager import Financial_Manager
from Pages.Login import LoginPage
import unittest


driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### login_Financial_Manager ###################

    def test38_login_financial_manager(self):
        # a = self.driver.find_element('xpath', customer_manager_date_filter).text
        # print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        financial = Financial_Manager(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        financial.enter_financial_my_tasks()

################### my_tasks_need_official_invoice ###################

    def test39_my_tasks_need_official_invoice(self):
        self.driver.implicitly_wait(5)
        financial = Financial_Manager(driver=self.driver)
        financial.enter_financial_my_tasks_need_official_invoice()
        financial.enter_financial_update_my_tasks()
        financial.enter_financial_search("")
        financial.enter_financial_search_btn()
        financial.enter_financial_my_tasks_click_need_official_invoice()
        sleep(.1)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
