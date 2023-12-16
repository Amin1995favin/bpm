from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Admin.Admin import Admin
from Pages.Admin.Report import Report
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest

from Pages.Warehouses.Warehouses import Warehouses

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

################### login_admin ###################

    def test01_login_admin(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_admin02)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل ادمین شد")
        print("############################################")

################### admin_report_select_the_reports ###################

    def test02_admin_report_select_the_reports(self):
        report = Report(driver=self.driver)
        report.enter_admin_report()
        report.enter_admin_report_select_the_report23()
        # report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report23_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report24()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report24_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report25()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        # report.enter_admin_report_select_the_report25_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report26()
        # report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report26_check_table()
        report.enter_admin_report_reports_search_tn("علی فلاح")
        report.enter_admin_report_select_the_report26_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report_select_the_report26_customer_manager_check()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report27()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report27_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        # report.enter_admin_report_select_the_report26_tn_assert_search()
        # report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report()
        report.enter_admin_report_select_the_report28()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report28_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report29()
        report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report29_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report30()
        # report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report30_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_select_the_report30_search(a)
        # report.enter_admin_report_select_the_report26_tn_assert_search()



        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
