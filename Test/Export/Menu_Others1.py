from selenium import webdriver
from time import sleep
from Locators import *
from Pages.Customer_Manager.Tasks_List import Tasks_list

from Pages.Export.Menu import Export_My_Tasks
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Export_Menu_Others1(unittest.TestCase):
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

    ################### export_check_my_tasks ###################

    def test02_export_check_my_tasks_others(self):
        tasks_list = Export_My_Tasks(driver=self.driver)
        tasks = Tasks_list(driver=self.driver)
        tasks.enter_customer_manager_my_tasks()
        tasks_list.len_export_my_task()
        tasks_list.enter_export_my_tasks_clearance()
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[1]/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[1]/div/div/div[2]/a[2]")
        tasks_list.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[1]/div/div/div[2]/a[3]")
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'سفارش', 'کالای سفارش',  'زمان ایجاد', 'نوع حمل', 'وزن سفارش (KG)', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع پیش فاکتور حمل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[2]/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        # tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[2]/div/div/div[2]/a[2]")
        # tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[2]/div/div/div[2]/a[3]")
        tasks_list.my_tasks_check_table(12, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'شهر مبدا', 'درخواست های ریپک', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[2]/div/div/div[2]/a[4]")
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ', 'تاریخ تحویل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-1']/div[2]/div/div/div[2]/a[5]")
        tasks_list.my_tasks_check_table(9, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])
        tasks_list.enter_export_my_tasks_export()
        tasks_list.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a[2]")
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a[3]")
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a[4]")
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        tasks_list.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a[5]")
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور خرید'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
