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


class Test_Yazd_Manager_Menu2(unittest.TestCase):
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
        tasks_list.op_delivery_call()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مشخصات وزن (KG)', 'نوع ترخیص', 'خدمات موردنیاز', 'بروزرسانی', 'مقصد سفارش'])
        tasks_list.check_payment_by_expert()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        tasks_list.request_costumer_manager()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', '', 'سفارش', 'جزئیات', 'وزن سفارش (KG)', 'شهر مبدا', 'کالاهای ریپک', 'تایید درخواست ریپک'])
        tasks_list.auto_new_online_payment_experts()
        tasks_list.my_tasks_check_table(12, ['ردیف', 'عملیات', 'لیست', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'سفارش',
                                             'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده',
                                             'مدیر مشتری'])
        tasks_list.auto_defect_buy_information()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور خرید'])
        tasks_list.flight_delay_notification()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شماره ترک فرعی', 'مبدا', 'مقصد',
                                             'وزن سفارش (KG)', 'اطلاع رسانی به مشتری', 'خروج از کارتابل'])
        tasks_list.information_shipping_orders_by_partner_company()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شهر ارسال کننده',
                                             'شهر دریافت کننده', 'نام شرکت', 'شماره پیگیری شرکت حمل کننده', 'خروج از کارتابل'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
