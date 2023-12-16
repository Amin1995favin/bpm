from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Locators import *

from Pages.Customer_Manager.Dashboard import Dashboard
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Isfahan_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_account_isfahan ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_isfahan)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شعبه اصفهان شد")

    ################### account_isfahan_check_my_tasks ###################

    def test02_account_isfahan_check_my_tasks_others(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.len_customer_manager_my_task()
        tasks_list.enter_customer_manager_my_tasks_clearance()
        tasks_list.need_clearance_inquiry()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        sleep(.2)
        tasks_list.cleared_orders()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        tasks_list.need_final_clearance()
        tasks_list.my_tasks_check_table(12, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'شهر مبدا', 'درخواست های ریپک', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        tasks_list.need_final_clearance_urgency_in_auto_billed_order_isfahan()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ', 'تاریخ تحویل'])
        tasks_list.auto_billed_order_isfahan()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])
        tasks_list.enter_customer_manager_my_tasks_warehouse()
        tasks_list.auto_pickup_status_sending_to_the_warehouse()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص ارسال کننده', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        tasks_list.auto_need_to_batch()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        # tasks_list.print_clearance_documents()
        # tasks_list.my_tasks_check_table(5, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'فایل های قبضی', 'آماده تحویل به مشتری'])
        tasks_list.enter_customer_manager_my_tasks_financial()
        tasks_list.auto_new_payment()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        tasks_list.op_need_print_official_invoice()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        tasks_list.auto_wallet_refund()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        tasks_list.enter_customer_manager_my_tasks_delivery()
        tasks_list.op_ready_to_deliver()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        tasks_list.determine_driver()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        tasks_list.enter_customer_manager_my_tasks_manager()
        tasks_list.arrived_op_in_batch_conflict_isfahan2()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد مشخصه', 'موقعیت', 'ترک فرعی', 'جمع وزن جرمی(kg)', 'ارزش', 'توضیحات'])
        tasks_list.deliver_not_cleared_request_isfahan()
        # tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ترخیص', 'خدمات موردنیاز', 'مقصد سفارش', 'توضیحات درخواست', 'کالاهای سفارش'])
        tasks_list.auto_wallet_refund_check_admin_isfahan()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        tasks_list.auto_new_discount_isfahan()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'نوع تخفیف', 'سفارش', 'مبلغ درخواستی', 'واحد', 'علت تخفیف', 'توضیحات', 'کاربر ثبت کننده', 'مدیر مشتری'])
        tasks_list.check_discount_per_kilo_isfahan()
        tasks_list.my_tasks_check_table(4, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'اطلاعات سفارش', 'واحد و نرخ هر کیلو'])
        tasks_list.transport_is_accumulative_isfahan()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
