from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Financial_Manager.Menu import Financial_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Financial_Manager_Menu1(unittest.TestCase):
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

    ################### financial_manager_check_menu ###################

    def test02_financial_manager_check_menu(self):
        financial = Financial_My_Tasks(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        financial.enter_financial_menu_check_tag()
        financial.enter_financial_manager_menu_check_tag_dashboard()
        financial.enter_financial_manager_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        menu.enter_customer_manager_menu_check_dashboard()
        menu.enter_customer_manager_menu_check_my_tasks()
        menu.enter_customer_manager_menu_check_inbox()
        menu.enter_customer_manager_menu_check_information_and_training()
        menu.enter_customer_manager_menu_check_management_reports()
        menu.enter_customer_manager_menu_check_orders()
        financial.enter_financial_batches()
        financial.enter_financial_persons()
        # financial.enter_financial_companies()
        financial.enter_financial_manager_shipping_rate()
        financial.enter_financial_manager_check_exchange_rates()
        financial.enter_financial_manager_check_list_excel_output()
        financial.enter_financial_manager_check_user_profile()
        financial.enter_financial_manager_check_change_password()
        financial.enter_financial_manager_check_exit()
        print("تمام موارد منوی financial_manager به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### clearance_check_my_tasks ###################

    def test03_clearance_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        financial = Financial_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        financial.len_financial_manager()
        # financial.auto_new_payment()
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        financial.auto_custom_bill_orders()
        my_tasks.my_tasks_check_table(21, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'کالای سفارش', 'شماره ترک', 'ویرایش شده', 'ترخیص توسط', 'هزینه های غیر رسمی (ریال)', 'هزینه حقوق و عوارض گمرکی (ریال)', 'هزینه صورتحساب انبار (ریال)', 'هزینه نمونه برداری آزمایشگاه (ریال)', 'هزینه تعیین ماهیت آزمایشگاه (ریال)', 'هزینه نمونه برداری انبارهای عمومی (ریال)', 'سایر هزینه ها (ریال)', 'جمع هزینه ها (ریال)', 'زمان ایجاد هزینه صدور قبض', 'شماره بچ', 'صاحب پیش فاکتور'])
        # financial.factors_price_unit_change_after_insert_arian()
        # my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایجادکننده', 'زمان ایجاد', 'واحد عرض قبلی', 'نرخ واحد عرض جدید', 'نوع پیش فاکتور', 'شناسه آرین پیش فاکتور قبلی', 'تاییدیه اطلاع'])
        financial.auto_new_online_payment()
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'وضعیت', 'مبلغ', 'سفارش', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        financial.update_integrated_user_in_arian()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'کاربر حذف شونده', 'کاربر نهایی', 'زمان ایجاد', 'ایجادکننده', 'عملیات'])
        # financial.cancelled_orders_with_paid_invoice()
        # my_tasks.my_tasks_check_table(8, ['ردیف', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        financial.submit_in_financial_system_official()
        sleep(1)
        # my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز', 'مبلغ پیش فاکتور', 'تاریخ ایجاد سفارش'])
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'خدمات موردنیاز', 'مبلغ پیش فاکتور', 'تاریخ ایجاد سفارش'])
        financial.after_payment_changed()
        my_tasks.my_tasks_check_table(5, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'سفارش'])
        financial.changes_in_invoices()
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'اطلاعات پیش فاکتور',  'تاریخچه تغییرات', 'بررسی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
