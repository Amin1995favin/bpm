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
        report.enter_admin_report_select_the_report08()
        report.enter_admin_report_filter()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report08_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report09()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report09_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report09_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report_select_the_report09_status_check()
        report.enter_admin_report_select_the_report05_detail()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report10()
        report.enter_admin_report_select_the_report10_check_table()
        # report.enter_admin_report()
        # report.enter_admin_report_select_the_report11()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_select_the_report11_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report12()
        report.enter_admin_report_select_the_report12_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report13()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report13_check_table()
        report.enter_admin_report_select_the_report13_show_name()
        report.enter_admin_report_select_the_report13_show_name()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report14()
        report.enter_admin_report_select_the_report14_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report15()
        report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report15_check_table()
        report.enter_admin_report_select_the_report15_agency_id()
        report.enter_admin_report_select_the_report15_origin_filter()
        report.enter_admin_report_select_the_report15_destination_filter()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report16()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report16_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report17()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report17_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report18()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report18_check_table()
        # report.enter_admin_report()
        # report.enter_admin_report_select_the_report19()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        # report.enter_admin_report_select_the_report19_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report20()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report20_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report20_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report_select_the_report20_status_check()
        report.enter_admin_report_select_the_report20_destination_filter()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report21()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report21_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report22()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report22_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report22_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        # report.enter_admin_report_select_the_report22_delivery_person_check()
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
