from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Uae.Menu import Uae
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Uae_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_admin ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_uae)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شعبه امارات شد. ")
        print("############################################")

    ################### dubai_check_menu ###################

    def test02_dubai_check_menu(self):
        menu = Menu(driver=self.driver)
        menu.enter_dubai_menu_check_tag()
        menu.enter_dubai_menu_check_tag_dashboard()
        menu.enter_account_dubai_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        menu.enter_customer_manager_menu_check_dashboard()
        menu.enter_customer_manager_menu_check_my_tasks()
        menu.enter_customer_manager_menu_check_inbox()
        menu.enter_customer_manager_menu_check_information_and_training()
        menu.enter_dubai_menu_check_orders()
        menu.enter_dubai_menu_check_warehouses()
        menu.enter_dubai_menu_check_accept_order_op_by_scan()
        menu.enter_dubai_menu_check_batches()
        menu.enter_dubai_menu_check_persons()
        menu.enter_dubai_menu_check_delivery_info_search()
        menu.enter_dubai_menu_check_crypto_gateway_recovery()
        menu.enter_dubai_menu_check_list_excel_output()
        menu.enter_dubai_menu_check_user_profile()
        menu.enter_dubai_menu_check_change_password()
        menu.enter_dubai_menu_check_exit()
        print("تمام موارد منوی مدیر مشتری به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### admin_dubai_check_my_tasks ###################

    def test03_admin_dubai_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        uae = Uae(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        uae.len_dubai()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص ارسال کننده', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'تاییدیه دریافت سفارش'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)', 'پیگیری کننده'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'بارگیری کالا', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[10]")
        sleep(1)
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
