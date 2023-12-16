from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Warehouses_Iran.Report import Report
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### login_warehouse_iran_manager ###################

    def test01_login_warehouse_iran_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر انبار دار ایران شد")
        print("############################################")

################### warehouse_iran_manager_report_check ###################

    def test02_manager_report_check(self):
        report = Report(driver=self.driver)
        report.enter_report()
        report.enter_report_manager_check()
        report.enter_len_report_manager_check()
        print("############################################")

################### warehouse_iran_manager_report_arian_management_reports ###################

    def test03_manager_report_arian_management_reports(self):
        report = Report(driver=self.driver)
        report.enter_report()
        report.enter_admin_report_select_the_report149()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report149_check_table()
        report.enter_report()
        report.enter_admin_report_select_the_report146()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report146_check_table()
        report.enter_report()
        report.enter_admin_report_select_the_report22()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report22_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report22_tn_assert_search()
        report.enter_report()
        report.enter_admin_report_select_the_report111()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report111_check_table()
        report.enter_admin_report_select_the_report111_created_by_check()
        report.enter_report()
        report.enter_admin_report_select_the_report71()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report71_check_table()
        b = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(b)
        report.enter_admin_report_select_the_report02_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        c = report.enter_admin_report_select_the_report71_batch()
        report.enter_admin_report_select_the_report71_search_batch(c)
        report.enter_admin_report_select_the_report05_tn_assert_search()
        report.enter_report()
        report.enter_admin_report_select_the_report07()
        # report.enter_admin_report_filter()
        report.enter_admin_report_select_the_report07_car()
        report.enter_admin_report_select_the_report07_check_map()
        report.enter_report()
        report.enter_admin_report_select_the_report76()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report76_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report22_tn_assert_search()
        report.enter_report()
        report.enter_admin_report_select_the_report55()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report55_check_table()
        report.enter_report()
        report.enter_admin_report_select_the_report115()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report115_check_table()
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
