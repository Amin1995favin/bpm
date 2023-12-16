from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *

from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Isfahan_Manager_Menu1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_customer_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(isfahan_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری اصفهان شد")

    ################### customer_manager_check_menu ###################

    def test02_customer_manager_check_menu(self):
        menu = Menu(driver=self.driver)
        menu.enter_customer_manager_menu_check_tag()
        menu.enter_customer_manager_menu_check_tag_dashboard()
        menu.enter_account_isfahan_manager_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        menu.enter_customer_manager_menu_check_dashboard()
        menu.enter_customer_manager_menu_check_my_tasks()
        menu.enter_customer_manager_menu_check_inbox()
        menu.enter_customer_manager_menu_check_information_and_training()
        menu.enter_customer_manager_menu_check_management_reports()
        menu.enter_customer_manager_menu_check_orders()
        menu.enter_customer_manager_menu_shipping_rate()
        menu.enter_customer_manager_menu_check_exchange_rates()
        menu.enter_customer_manager_menu_check_payment()
        menu.enter_customer_manager_menu_check_investigate_theron()
        menu.enter_customer_manager_menu_check_talk_to_customers()
        menu.enter_customer_manager_menu_check_list_excel_output()
        menu.enter_customer_manager_menu_check_user_profile()
        menu.enter_customer_manager_menu_check_change_password()
        menu.enter_customer_manager_menu_check_exit()
        print("تمام موارد منوی مدیر مشتری به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### customer_manager_check_my_tasks ###################

    def test03_customer_manager_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.len_customer_manager()
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
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        tasks_list.auto_need_shipping()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
