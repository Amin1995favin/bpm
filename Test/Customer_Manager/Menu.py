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


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_customer_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

    ################### customer_manager_check_menu ###################

    # def test02_customer_manager_check_menu(self):
    #     menu = Menu(driver=self.driver)
    #     menu.enter_customer_manager_menu_check_tag()
    #     menu.enter_customer_manager_menu_check_tag_dashboard()
    #     menu.enter_customer_manager_menu_check_name()
    #     menu.enter_customer_manager_menu_check_search()
    #     menu.enter_customer_manager_menu_check_dashboard()
    #     menu.enter_customer_manager_menu_check_my_tasks()
    #     menu.enter_customer_manager_menu_check_inbox()
    #     menu.enter_customer_manager_menu_check_information_and_training()
    #     menu.enter_customer_manager_menu_check_management_reports()
    #     menu.enter_customer_manager_menu_check_orders()
    #     menu.enter_customer_manager_menu_shipping_rate()
    #     menu.enter_customer_manager_menu_check_exchange_rates()
    #     menu.enter_customer_manager_menu_check_payment()
    #     menu.enter_customer_manager_menu_check_investigate_theron()
    #     menu.enter_customer_manager_menu_check_talk_to_customers()
    #     menu.enter_customer_manager_menu_check_list_excel_output()
    #     menu.enter_customer_manager_menu_check_user_profile()
    #     menu.enter_customer_manager_menu_check_change_password()
    #     menu.enter_customer_manager_menu_check_exit()
    #     print("تمام موارد منوی مدیر مشتری به درستی نمایش داده شد.")
    #     print("_________________________________________________________")

    ################### customer_manager_check_my_tasks ###################

    def test03_customer_manager_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        # tasks_list.review_and_correct_order()
        # tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
        #                                     'وزن سفارش (KG)', 'خدمات موردنیاز'])
        # tasks_list.need_to_issue_shipping_queries()
        # tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
        #                                      'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل',
        #                                      'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        # tasks_list.send_invoice_to_customer()
        # tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره پیش فاکتور', 'عنوان', 'قیمت اعلامی', 'نرخ تبدیل به ریال', 'ضریب مالیات', 'قیمت نهایی', 'کاربر ثبت کننده', 'زمان ثبت'])
        # tasks_list.conformation_by_customer()
        # tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'پیش فاکتور به نام فرد', 'پیش فاکتور به نام شرکت'])
        # tasks_list.auto_need_pick_up_order()
        # tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'نوع حمل'])
        # tasks_list.the_need_for_the_final_shipping_inquiry()
        # tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        # tasks_list.fixing_discharge_clearance_defect()
        # tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        # tasks_list.auto_need_shipping()
        # tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
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
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'ارزش کل', 'توضیحات',
                                             'نوع پیش فاکتور خرید'])
        tasks_list.flight_delay_notification()
        tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شماره ترک فرعی', 'مبدا', 'مقصد',
                                             'وزن سفارش (KG)', 'اطلاع رسانی به مشتری', 'خروج از کارتابل'])
        tasks_list.information_shipping_orders_by_partner_company()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شهر ارسال کننده',
                                             'شهر دریافت کننده', 'نام شرکت', 'شماره پیگیری شرکت حمل کننده', 'خروج از کارتابل'])
        tasks_list.pending_to_specify_the_sender()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)'])
        tasks_list.complete_order_information()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مبلغ', 'توضیحات'])
        tasks_list.notify_customer_completion_destination_order()
        tasks_list.my_tasks_check_table(15, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شخص ارسال کننده', 'شرکت ارسال کننده', 'تلفن تماس شخص فرستنده',
                                         'تاریخ و زمان آمادگی فرستنده جهت پیک آپ',
                                         'توضیحات تاریخ و زمان آمادگی فرستنده', 'شماره ترک سفارش در شرکت حمل کننده',
                                         'نام شرکت حمل کننده', 'فایل پیوست', 'لیبل 1', 'لیبل 2', 'خروج از کارتابل'])
        tasks_list.auto_chat_by_customer()
        tasks_list.my_tasks_check_table(10,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده',
                                         'تعداد سفارشات',
                                         'کارکرد مالی'])
        tasks_list.notify_order_pickup()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دفعات بارگیری سفارش'])
        tasks_list.settlement_problem()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایراد تسویه', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        tasks_list.review_buy_requests()
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها', 'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        tasks_list.notify_of_buy()
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها', 'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        tasks_list.sales_claims()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])
        tasks_list.check_china_transaction()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)'])
        tasks_list.solve_defection_transport_invoice()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        tasks_list.complete_user_info_to_register_in_arian()
        tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'کدملی', 'موبایل1', 'موبایل2', 'تلفن ثابت 1', 'وضعیت', 'توضیحات عدم تایید'])
        tasks_list.assign_money_to_invoices()
        sleep(1)
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'عنوان', 'قیمت اعلامی', 'پرداخت شده (در واحد)'])
        tasks_list.auto_expert_customer_recovery()
        tasks_list.my_tasks_check_table(12,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'عملیات', 'نام و نام خانوادگی', 'دوره تجدید سفارش',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات',
                                         'کارکرد مالی'])
        tasks_list.auto_pick_status_wrong_number()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شخص ارسال کننده', 'خدمات موردنیاز', 'وزن سفارش (KG)'])
        tasks_list.enter_clearance_information()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'مقصد', 'توضیحات علت برگشت', 'تاییدیه اصلاح اطلاعات'])
        tasks_list.awaiting_settlement()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز'])
        tasks_list.auto_orders_transport_batches()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])


    ################### customer_manager_check_menu_order ###################

    def test04_customer_manager_check_menu_order(self):
        dashboard = Dashboard(driver=self.driver)
        menu = Menu(driver=self.driver)
        dashboard.enter_customer_manager_click_dashboard()
        dashboard.enter_customer_manager_dashboard_click_track_orders()
        sleep(1)
        menu.enter_customer_manager_orders_check_create_order()
        menu.enter_customer_manager_orders_list_all_orders()
        menu.enter_customer_manager_orders_draft()
        menu.enter_customer_manager_orders_pre_order()
        menu.enter_customer_manager_orders_pending_approval()
        menu.enter_customer_manager_orders_canceled()
        menu.enter_customer_manager_orders_suspended()
        menu.enter_customer_manager_orders_doing_open()
        menu.enter_customer_manager_orders_picked_up()
        menu.enter_customer_manager_orders_delivered()
        # menu.enter_customer_manager_orders_delivered_settled()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
