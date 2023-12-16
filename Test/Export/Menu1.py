from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Export.Menu import Export_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Export_Menu1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_export ###################

    def test01_export(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_export)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################### export_check_menu ###################

    def test02_export_check_menu(self):
        export = Export_My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        export.enter_export_menu_check_tag()
        export.enter_export_menu_check_tag_dashboard()
        export.enter_export_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        export.export_dashboard()
        export.export_my_task()
        export.export_inbox()
        export.export_train()
        export.export_report()
        export.export_orders()
        export.enter_financial_warehouses()
        export.enter_export_accept_order_op_by_scan()
        export.enter_export_batches()
        export.enter_export_persons()
        export.enter_export_shipping_rate()
        export.enter_export_check_exchange_rates()
        export.enter_export_last_payments()
        export.enter_export_china_expenses2()
        export.enter_export_chat()
        export.enter_export_check_list_excel_output()
        export.enter_export_check_user_profile()
        export.enter_export_check_change_password()
        export.enter_export_manager_check_exit()
        print("تمام موارد منوی delivery_manager به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### export_check_my_tasks ###################

    def test03_export_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        export = Export_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        export.len_export()
        tasks_list.review_and_correct_order()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'وزن سفارش (KG)', 'خدمات موردنیاز'])
        tasks_list.need_to_issue_shipping_queries()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                             'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل',
                                             'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.send_invoice_to_customer()
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره پیش فاکتور', 'عنوان', 'قیمت اعلامی', 'نرخ تبدیل به ریال', 'ضریب مالیات', 'قیمت نهایی', 'کاربر ثبت کننده', 'زمان ثبت'])
        tasks_list.conformation_by_customer()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'پیش فاکتور به نام فرد', 'پیش فاکتور به نام شرکت'])
        tasks_list.auto_need_pick_up_order()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'نوع حمل'])
        tasks_list.the_need_for_the_final_shipping_inquiry()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.fixing_discharge_clearance_defect()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', 'رفع نقص فاکتور ترخیص', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
