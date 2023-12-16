from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
from Pages.Turk.Menu import Turk
import unittest


# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Turk_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_turk ###################

    def test01_turk(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_turk)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت شعبه ترکیه شد. ")
        print("############################################")

    ################### turk_check_menu ###################

    def test02_turk_check_menu(self):
        menu = Menu(driver=self.driver)
        turk = Turk(driver=self.driver)
        turk.enter_turk_menu_check_tag()
        turk.enter_turk_menu_check_name()
        turk.enter_turk_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        turk.turk_menu_dashboard()
        turk.turk_menu_my_tasks()
        turk.turk_menu_inbox()
        turk.turk_menu_train()
        turk.turk_menu_warehouses()
        turk.turk_menu_accept_order_op_by_scan()
        turk.turk_menu_batches()
        turk.turk_menu_persons()
        turk.turk_menu_crypto_gateway_recovery()
        turk.turk_menu_list_excel_output()
        turk.turk_menu_user_profile()
        turk.turk_menu_change_password()
        turk.turk_menu_exit()
        print("تمام موارد منوی اکانت مدیر شعبه ترکیه به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### turk_check_my_tasks ###################

    def test03_turk_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        turk = Turk(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        turk.len_turk()
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[1]")
        turk.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[2]")
        turk.my_tasks_check_table(11, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)', 'پیگیری کننده'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[3]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[4]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'بارگیری کالا', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[5]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[6]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[7]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[8]")
        turk.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='nav-category-3']/div[1]/div/div/div[2]/a[9]")
        turk.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
