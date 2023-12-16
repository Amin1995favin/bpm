from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
from Pages.Syria.Menu import Syria
import unittest
from Pages.Warehouses.Menu import Warehouses_My_Tasks

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Syria_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_syria ###################

    def test01_syria(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_syria)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت شعبه سوریه شد. ")
        print("############################################")

    ################### syria_check_my_tasks_others ###################

    def test02_syria_check_my_tasks_others(self):
        tasks_list = Tasks_list(driver=self.driver)
        syria = Syria(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        syria.len_syria_my_task()
        syria.click_financial()
        admin.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[1]")
        syria.my_tasks_check_table(11, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الشروط', 'المبلغ', 'محدد مسبقًا للفوترة', 'الحساب', 'الوصف', 'المنشئ', 'مدیر العملاء'])
        admin.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[2]")
        syria.my_tasks_check_table(9, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'المستخدم', 'المبلغ', 'الوحدة', 'الوصف', 'وقت التغییر'])
        admin.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[3]")
        syria.my_tasks_check_table(8, ['رقم', 'العملیة', 'الطلب', 'وقت دخول المهمة لهذه البطاقة', 'الفاتورة', 'المدفوع (باعملات)', 'تسجیل المستخدم', 'الموافقة المالیة'])
        syria.click_delivery()
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a")
        syria.my_tasks_check_table(13, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'نوع التخلیص', 'الدفعة: رقم الدفعة', 'ملفات الطلب', 'هماهنگی های انجام شده', 'توصیل', 'موزع', 'معرف السیارة', 'کیفیة توصیل البضائع'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
