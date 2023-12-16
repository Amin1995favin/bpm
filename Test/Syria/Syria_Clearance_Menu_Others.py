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


# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Syria_Clearance_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_syria_clearance ###################

    def test01_syria_clearance(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(syria_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت اکانت ترخیص سوریه شد. ")
        print("############################################")

    ################### syria_clearance_check_my_tasks_others ###################

    def test02_syria_clearance_check_my_tasks_others(self):
        tasks_list = Tasks_list(driver=self.driver)
        syria = Syria(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        syria.len_syria_my_task_clearance()
        syria.clearance_click_clearance()
        admin.my_tasks_check("//*[@id='nav-category-1']/div/div/div/div[2]/a[1]")
        syria.my_tasks_check_table(12, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'کود الاستعلام عن التخلیص', 'مدینة المنشأ', 'مدینة الوجهة', 'الطلب', 'طلب جدید', 'الوزن الفعلی الکلی (کغ)', 'القیمة الکلیة', 'واحدة القیمة'])
        admin.my_tasks_check("//*[@id='nav-category-1']/div/div/div/div[2]/a[2]")
        syria.my_tasks_check_table(14, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'طلب جدید', 'مدینة المنشأ', 'طلبات إعادة حزم', 'الوزن الفعلی الکلی (کغ)', 'القیمة الکلیة', 'واحدة القیمة', 'الوصف', 'نوع فاتورة التخلیص', 'سعر التصفیة الأساسی بالریال'])
        syria.clearance_click_warehouse()
        admin.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a")
        syria.my_tasks_check_table(6, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'تأکید الطلب'])
        syria.clearance_click_delivery()
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a")
        syria.my_tasks_check_table(11, ['رقم', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'نوع التخلیص', 'الدفعة: رقم الدفعة', 'ملفات الطلب', 'هماهنگی های انجام شده', 'توصیل', 'موزع', 'معرف السیارة', 'کیفیة توصیل البضائع'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
