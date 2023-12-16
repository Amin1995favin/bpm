from Locators import *
from time import sleep


def customer_manager_menu_check(self, element_selector, element_locator, text):
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.5)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = scrolled.text
    # print(a)
    assert text in a
    print(" تکست "+text+" به درستی نمایش داده می شود. ")
    print("__________")


class Menu:
    def __init__(self, driver):
        self.driver = driver

    ################### customer_manager_check_menu ###################

    def enter_customer_manager_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 16
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_dubai_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 15
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_yazd_manager_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 17
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_account_isfahan_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        assert a == 14
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_account_yazd_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        # assert a == 13
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def len_account_isfahan(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[2]/div/div/div[2]/a"))
        print(a+b)
        assert a+b == 30
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_account_yazd(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[1]/div/div/div[2]/a"))
        print(a)
        assert a == 25
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def enter_customer_manager_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[1]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[2]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a")
        assert self.driver.find_element('xpath', "/html/body/div[1]/header/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[3]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[5]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[6]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/img")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/span")
        print("بخش های مختلف داشبورد به درستی نمایش داده شد.")
        print("لوگو به درستی نمایش داده شد.")
        print("بخش های مختلف navbar به درستی نمایش داده شد.")
        print("_______________________________________________")

    def enter_dubai_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a")
        assert self.driver.find_element('xpath', "/html/body/div[1]/header/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[3]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[5]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[6]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/img")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/span")
        print("بخش های مختلف داشبورد به درستی نمایش داده شد.")
        print("لوگو به درستی نمایش داده شد.")
        print("بخش های مختلف navbar به درستی نمایش داده شد.")
        print("_______________________________________________")

    def enter_customer_manager_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "زهرا پیروز Zahra Pirooz")

    def enter_account_isfahan_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "علی جلالیان")

    def enter_account_isfahan_manager_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "شیرین امیر")

    def enter_account_dubai_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "محمد جواد رضایی")

    def enter_account_yazd_manager_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "فاطمه فهیمی")

    def enter_account_yazd_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "محمد پور میرزایی")

    def enter_account_alborz_menu_check_name(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_name, "سید علیرضا حسینی")

    def enter_customer_manager_menu_check_search(self):
        assert self.driver.find_element('xpath', customer_manager_menu_search)
        print("جستجو", "به درستی مشاهده شد.")

    def enter_customer_manager_menu_check_dashboard(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_dashboard, "پیشخوان")

    def enter_customer_manager_menu_check_my_tasks(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_my_tasks, "کارتابل من")

    def enter_customer_manager_menu_check_inbox(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_inbox, "پیام های من")

    def enter_customer_manager_menu_check_information_and_training(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_information_and_training, "اطلاع رسانی و آموزش")

    def enter_customer_manager_menu_check_management_reports(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_management_reports, "گزارش های مدیریتی")

    def enter_dubai_menu_check_orders(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_management_reports, "سفارش ها")

    def enter_customer_manager_menu_check_orders(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_orders, "سفارش ها")

    def enter_dubai_menu_check_warehouses(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_orders, "انبار ها")

    def enter_customer_manager_menu_check_persons(self):
        # customer_manager_menu_check(self, 'xpath', customer_manager_menu_persons, "اشخاص")
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_persons, "مشتریان")

    def enter_customer_manager_menu_shipping_rate(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_shipping_rate, "محاسبه نرخ حمل")

    def enter_customer_manager_menu_check_exchange_rates(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_exchange_rates, "نرخ های ارز")

    def enter_customer_manager_menu_check_payment(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_payment, "پرداخت")

    def enter_customer_manager_menu_check_investigate_theron(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_investigate_theron, "بررسی تراکنش شبکه‌ ترون")

    def enter_account_isfahan_menu_check_investigate_theron(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_payment, "بررسی تراکنش شبکه‌ ترون")

    def enter_customer_manager_menu_check_talk_to_customers(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_talk_to_customers, "گفتگو با مشتری ها")

    def enter_customer_manager_menu_check_list_excel_output(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_list_excel_output, "لیست خروجی اکسل")

    def enter_customer_manager_menu_check_phone_marketer_calls(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_list_excel_output, "تماس های بازاریاب تلفنی")

    def enter_account_isfahan_menu_check_list_excel_output(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_investigate_theron, "لیست خروجی اکسل")

    def enter_customer_manager_menu_check_user_profile(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_user_profile, "پروفایل کاربری")

    def enter_customer_manager_menu_check_change_password(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_change_password, "تغییر کلمه عبور")

    def enter_customer_manager_menu_check_exit(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_exit, "خروج")

    def enter_account_isfahan_menu_check_user_profile(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "پروفایل کاربری")

    def enter_account_isfahan_menu_check_change_password(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "تغییر کلمه عبور")

    def enter_account_isfahan_menu_check_exit(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[16]/a", "خروج")

    def enter_account_yazd_menu_check_list_excel_output(self):
        customer_manager_menu_check(self, 'xpath', customer_manager_menu_payment, "لیست خروجی اکسل")

    def enter_account_yazd_menu_check_user_profile(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "پروفایل کاربری")

    def enter_account_yazd_menu_check_change_password(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "تغییر کلمه عبور")

    def enter_account_yazd_menu_check_exit(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "خروج")

    def enter_yazd_manager_menu_check_list_excel_output(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "لیست خروجی اکسل")

    def enter_yazd_manager_menu_check_user_profile(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[17]/a", "پروفایل کاربری")

    def enter_yazd_manager_menu_check_change_password(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[18]/a", "تغییر کلمه عبور")

    def enter_yazd_manager_menu_check_exit(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[19]/a", "خروج")

    def enter_dubai_menu_check_accept_order_op_by_scan(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[8]/a", "دریافت کالا های سفارش با اسکن")

    def enter_dubai_menu_check_batches(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "بسته ها")

    def enter_dubai_menu_check_persons(self):
        # customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "اشخاص")
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "مشتریان")

    def enter_dubai_menu_check_delivery_info_search(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "جستجوی سفارش آماده تحویل")

    def enter_dubai_menu_check_crypto_gateway_recovery(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "بررسی تراکنش شبکه‌ ترون")

    def enter_dubai_menu_check_list_excel_output(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "لیست خروجی اکسل")

    def enter_dubai_menu_check_user_profile(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "پروفایل کاربری")

    def enter_dubai_menu_check_change_password(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[16]/a", "تغییر کلمه عبور")

    def enter_dubai_menu_check_exit(self):
        customer_manager_menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[17]/a", "خروج")

    ################### customer_manager_check_menu_order ###################

    def enter_customer_manager_orders_check_create_order(self):
        assert "ایجاد سفارش" or "Create Order" in (self.driver.find_element('xpath', customer_manager_orders_create_order).text)
        print("ایجاد سفارش", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_list_all_orders(self):
        assert "فهرست همه سفارش ها" or "List all orders" in (self.driver.find_element('xpath', customer_manager_orders_list_all_orders).text)
        print("فهرست همه سفارش ها", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_draft(self):
        assert "پیش نویس" or "Draft" in (self.driver.find_element('xpath', customer_manager_orders_draft).text)
        print("پیش نویس", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_pre_order(self):
        assert "در انتظار تایید" or "Pending approval" in (self.driver.find_element('xpath', customer_manager_orders_pre_order).text)
        print("در انتظار تایید", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_pending_approval(self):
        assert "لغو شده" or "Canceled" in (self.driver.find_element('xpath', customer_manager_orders_pending_approval).text)
        print("لغو شده", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_canceled(self):
        assert "تعلیق شده" or "suspended" in (self.driver.find_element('xpath', customer_manager_orders_canceled).text)
        print("تعلیق شده", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_suspended(self):
        assert "در حال انجام" or "Doing/Open" in (self.driver.find_element('xpath', customer_manager_orders_suspended).text)
        print("در حال انجام", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_doing_open(self):
        assert "بارگیری شده" or "Pickedup" in (self.driver.find_element('xpath', customer_manager_orders_doing_open).text)
        print("بارگیری شده", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_picked_up(self):
        assert "تحویل شده / تسویه نشده" or "Delivered" in (self.driver.find_element('xpath', customer_manager_orders_picked_up).text)
        print("تحویل شده / تسویه نشده", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_delivered(self):
        assert "تحویل شده / تسویه شده" or "Delivered / Settled" in (self.driver.find_element('xpath', customer_manager_orders_delivered).text)
        print("تحویل شده / تسویه شده", "به درستی مشاهده شد.")

    def enter_customer_manager_orders_delivered_settled(self):
        assert "تحویل شده / تسویه شده" or "" in (self.driver.find_element('xpath', customer_manager_orders_delivered_settled).text)
        print("تحویل شده / تسویه شده", "به درستی مشاهده شد.")





