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


class Test_Syria_Clearance_Menu(unittest.TestCase):
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

    ################### syria_clearance_check_menu ###################

    def test02_syria_clearance_check_menu(self):
        menu = Menu(driver=self.driver)
        syria = Syria(driver=self.driver)
        syria.enter_syria_menu_check_tag()
        syria.enter_syria_clearance_menu_check_name()
        syria.enter_syria_clearance_menu_check_tag_dashboard()
        menu.enter_customer_manager_menu_check_search()
        syria.syria_menu_dashboard()
        syria.syria_menu_my_tasks()
        syria.syria_menu_inbox()
        syria.syria_menu_train()
        syria.syria_menu_orders()
        syria.syria_clearance_menu_batches()
        syria.syria_clearance_menu_persons()
        syria.syria_clearance_menu_crypto_gateway_recovery()
        syria.syria_clearance_menu_list_excel_output()
        syria.syria_clearance_menu_settings()
        syria.syria_menu_user_profile()
        syria.syria_menu_change_password()
        syria.syria_menu_exit()
        print("تمام موارد منوی اکانت ترخیص سوریه به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### syria_clearance_check_my_tasks ###################

    def test03_syria_clearance_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        syria = Syria(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        syria.len_syria_clearance()
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[1]")
        syria.my_tasks_check_table(7, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'وزن الطلب (کغ)', 'خدمات مطلوبة'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[2]")
        syria.my_tasks_check_table(13, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'رقم الفاتورة', 'العنوان', 'السعر المعلن', 'سعر التحویل إلى الریال الإیرانی', 'معدل الضریبة', 'السعر النهائی (ریال)', 'تسجیل المستخدم', 'وقت التسجیل'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[3]")
        syria.my_tasks_check_table(8, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'طلب جدید', 'فاتورة لشخص', 'فاتورة لشرکة'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[4]")
        syria.my_tasks_check_table(8, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'طلب جدید', 'وزن الطلب (کغ)', 'نوع الشحنة'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[5]")
        syria.my_tasks_check_table(9, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'خدمات مطلوبة', 'الوزن الإجمالی المستحق للدفع (کغ)', 'القیمة الکلیة', 'واحدة القیمة'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[6]")
        syria.my_tasks_check_table(10, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'مواصفات الوزن (کغ)', 'نوع التخلیص', 'خدمات مطلوبة', 'وقت التحدیث', 'الوجهة الطلب'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[7]")
        syria.my_tasks_check_table(11, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الشروط', 'المبلغ', 'محدد مسبقًا للفوترة', 'الحساب', 'الوصف', 'المنشئ', 'مدیر العملاء'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[8]")
        syria.my_tasks_check_table(8, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'المرسل (شخص)', 'خدمات مطلوبة', 'وزن الطلب (کغ)'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[9]")
        # syria.my_tasks_check_table(6, ['رقم', 'العملیة', ' ', 'وقت دخول المهمة لهذه البطاقة', 'الطلب', 'معدل تکرار طلب التنزیل'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
