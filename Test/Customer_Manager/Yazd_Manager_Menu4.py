from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Yazd_Manager_Menu4(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_customer_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(yazd_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری اصفهان شد")

    ################### customer_manager_check_my_tasks ###################

    def test02_customer_manager_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.check_china_transaction()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'کالای سفارش', 'وزن سفارش (KG)'])
        tasks_list.solve_defection_transport_invoice()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                             'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص',
                                             'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        tasks_list.complete_user_info_to_register_in_arian()
        tasks_list.my_tasks_check_table(11,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی',
                                         'کدملی', 'موبایل1', 'موبایل2', 'تلفن ثابت 1', 'وضعیت', 'توضیحات عدم تایید'])
        tasks_list.assign_money_to_invoices()
        sleep(1)
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'عنوان',
                                            'قیمت اعلامی', 'پرداخت شده (در واحد)'])
        tasks_list.auto_expert_customer_recovery()
        tasks_list.my_tasks_check_table(12,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'عملیات',
                                         'نام و نام خانوادگی', 'دوره تجدید سفارش',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات',
                                         'کارکرد مالی'])
        tasks_list.auto_pick_status_wrong_number()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'شخص ارسال کننده', 'خدمات موردنیاز', 'وزن سفارش (KG)'])
        tasks_list.enter_clearance_information()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'وزن سفارش (KG)', 'مقصد', 'توضیحات علت برگشت', 'تاییدیه اصلاح اطلاعات'])
        tasks_list.awaiting_settlement()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بروزرسانی',
                                            'وزن سفارش (KG)', 'خدمات موردنیاز'])
        tasks_list.auto_orders_transport_batches()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش',
                                            'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
