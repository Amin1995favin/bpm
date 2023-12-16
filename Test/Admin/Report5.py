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
        report.enter_admin_report_select_the_report58()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report58_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report59()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report59_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report60()
        report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report60_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report61()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report61_check_table()
        report.enter_admin_report_arian_management_report5_created_by_check()
        report.enter_admin_report_select_the_report61_document_type_check()
        report.enter_admin_report_select_the_report61_inquery_type_check()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report62()
        report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report62_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report63()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report63_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report64()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report64_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report65()
        report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report65_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report66()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report66_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report67()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report67_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report68()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report68_check_table()
        a = report.enter_admin_report_select_the_report68_batch()
        report.enter_admin_report_reports_search_tn(a)
        report.enter_admin_report_select_the_report02_tn_assert_search()
        report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report_select_the_report68_filter_check()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report69()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report69_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report70()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report70_check_table()
        report.enter_admin_report()
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
        report.enter_admin_report()
        report.enter_admin_report_select_the_report72()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report72_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report73()
        # report.enter_admin_report_filter()
        # report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report73_check_table()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report74()
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report74_check_table()
        d = report.enter_admin_report_select_the_report34_tn()
        report.enter_admin_report_reports_search_tn(d)
        report.enter_admin_report_select_the_report05_tn_assert_search()
        report.enter_admin_report()
        report.enter_admin_report_select_the_report75()
        sleep(1)
        report.enter_admin_report_filter()
        report.enter_admin_report_check_excel()
        report.enter_admin_report_select_the_report75_check_table()
        e = report.enter_admin_report_select_the_report75_tn()
        # report.enter_admin_report_reports_search_tn(e)
        # report.enter_admin_report_select_the_report20_tn_assert_search()
        # report.enter_admin_report_reports_search_tn("")
        report.enter_admin_report_select_the_report09_status_check()
        report.enter_admin_report_select_the_report75_filter()

        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
