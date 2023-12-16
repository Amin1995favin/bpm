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


class Test_Isfahan_Menu3(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_export ###################

    def test01_export(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_isfahan)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################### export_check_my_tasks ###################

    def test02_export_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.check_china_transaction_isfahan()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)'])
        tasks_list.assign_money_to_invoices_isfahan()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'عنوان', 'قیمت اعلامی', 'پرداخت شده (در واحد)'])
        tasks_list.auto_pick_status_wrong_number_isfahan()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شخص ارسال کننده', 'خدمات موردنیاز', 'وزن سفارش (KG)'])
        tasks_list.auto_new_online_payment_experts_isfahan()
        tasks_list.my_tasks_check_table(12, ['ردیف', 'عملیات', 'لیست', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'سفارش',
                                             'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده',
                                             'مدیر مشتری'])

        tasks_list.auto_chat_by_customer()
        tasks_list.my_tasks_check_table(10,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده',
                                         'تعداد سفارشات',
                                         'کارکرد مالی'])
        tasks_list.request_costumer_manager_isfahan()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', '', 'سفارش', 'جزئیات', 'وزن سفارش (KG)', 'شهر مبدا', 'کالاهای ریپک', 'تایید درخواست ریپک'])
        tasks_list.notify_order_pickup_isfahan()
        sleep(1)
        tasks_list.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دفعات بارگیری سفارش'])
        tasks_list.sales_claims_isfahan()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
