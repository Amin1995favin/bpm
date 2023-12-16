from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Report import Report
from Pages.Login import LoginPage
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

################### admin_report_check ###################

    def test02_admin_report_check(self):
        report = Report(driver=self.driver)
        report.enter_admin_report()
        report.enter_admin_report_check()
        report.enter_admin_reports_check()
        print("############################################")

################### admin_report_arian_management_reports ###################

    def test03_admin_report_arian_management_reports(self):
        report = Report(driver=self.driver)
        report.enter_admin_report_arian_management_report1()
        report.enter_admin_report_arian_management_report1_document_type()
        report.enter_admin_report_arian_management_report1_created_by_check()
        report.enter_admin_report_arian_management_report1_check_table()
        report.enter_admin_report_filter()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report2()
        report.enter_admin_report_filter()
        report.enter_admin_report_arian_management_report2_check_table()
        a = report.enter_admin_report_arian_management_report2_batch()
        report.enter_admin_report_reports_search(a)
        report.enter_admin_report_arian_management_report2_check_batch(a)
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report3()
        # report.enter_admin_report_filter()
        report.enter_admin_report_arian_management_report3_check_table()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report4()
        report.enter_admin_report_filter()
        report.enter_admin_report_arian_management_report4_check_table()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report5()
        report.enter_admin_report_filter()
        report.enter_admin_report_arian_management_report5_check_table()
        report.enter_admin_report_arian_management_report5_created_by_check()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report6()
        report.enter_admin_report_arian_management_report6_check_table()
        # report.enter_admin_report_filter()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report7()
        report.enter_admin_report_arian_management_report7_check_table()
        # report.enter_admin_report_filter()
        report.enter_admin_report()
        report.enter_admin_report_arian_management_report8()
        report.enter_admin_report_arian_management_report8_check_table()
        # report.enter_admin_report_filter()
        report.enter_admin_report()

    ################### admin_report_select_the_reports ###################

    def test04_admin_report_select_the_reports(self):
        report = Report(driver=self.driver)
        report.enter_admin_report_select_the_report01()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report01_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report02()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report02_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_select_the_report02_status_check()
        report.enter_admin_report_select_the_report02_marketer_check()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report02_tn_assert_search()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report03()
        # report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report03_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report04()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report04_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report05()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report05_check_table()
        a = report.enter_admin_report_select_the_report02_tn()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report05_tn_assert_search()
        report.enter_admin_report_select_the_report05_detail()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report06()
        report.enter_admin_report_filter()
        # report.enter_admin_report_select_the_report06_check_table()
        # report.enter_admin_report()
        # report.enter_admin_report_select_the_report07()
        # # report.enter_admin_report_filter()
        # report.enter_admin_report_select_the_report07_car()
        # report.enter_admin_report_select_the_report07_check_map()
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
