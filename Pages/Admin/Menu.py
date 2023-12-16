from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from colorama import Fore


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.5)
    element.send_keys(text)
    sleep(0.5)


def my_tasks_check(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.7)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = self.driver.find_element(element_selector, element_locator+"/small").text
    # print(a)
    # assert text1 in a
    print(" تکست باتن "+a+" به درستی نمایش داده می شود. ")
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.75)
    element.click()
    sleep(0.5)
    wait.until(EC.element_to_be_clickable(('xpath', clearance_my_tasks_update))).click()
    sleep(0.5)
    b = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div[1]/h4").text
    spa = self.driver.find_element(element_selector, element_locator+"/span[1]").text
    spa = int(spa)
    # if spa > 0:
    #     sleep(.5)
    #     c = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
    #     spa = str(spa)
    #     assert spa in c
    # print("مقدار روی کارتابل"+" به درستی نمایش داده می شود. ")
    # # assert b == text2
    # assert b == a
    # print(" تایتل کارتابل "+b+" به درستی نمایش داده می شود.  وبرابر با تکست باتن است. ")
    if spa > 0:
        sleep(.5)
        c = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        spa = str(spa)
        if spa in c:
            print("تعداد نمایش داده شده روی باتن صحیح می باشد")
        else:
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(
                Fore.RED + " خطا!!!!!تعداد نمایش داده شده روی باتن و جدول کارتابل ==> " + "***" + b + "***" + " صحیح نمی باشد ")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
        # assert spa in c
    # print("مقدار روی کارتابل" + " به درستی نمایش داده می شود. ")
    # assert b == text2
    assert b == a
    print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود. و برابر با تکست روی باتن است. ")


def menu_check(self, element_selector, element_locator, text):
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.5)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = scrolled.text
    # print(a)
    assert text in a
    print(" تکست "+text+" به درستی نمایش داده می شود. ")
    print("__________")


class Admin_My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def my_tasks_check(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', element_locator)
        sleep(0.7)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        a = self.driver.find_element('xpath', element_locator + "/small").text
        # print(a)
        # assert text1 in a
        print(" تکست باتن " + a + " به درستی نمایش داده می شود. ")
        element = wait.until(EC.element_to_be_clickable(('xpath', element_locator)))
        sleep(0.75)
        element.click()
        sleep(0.5)
        wait.until(EC.element_to_be_clickable(('xpath', clearance_my_tasks_update))).click()
        sleep(0.5)
        b = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div[1]/h4").text
        spa = self.driver.find_element('xpath', element_locator + "/span[1]").text
        spa = int(spa)
        if spa > 0:
            sleep(.5)
            c = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
            spa = str(spa)
            if spa in c:
                print("تعداد نمایش داده شده روی باتن صحیح می باشد")
            else:
                print(Fore.RED + "##############################")
                print(Fore.RED + "##############################")
                print(Fore.RED +"##############################")
                print(Fore.RED +" خطا!!!!!تعداد نمایش داده شده روی باتن و جدول کارتابل ==> " + "***" + b + "***" + " صحیح نمی باشد ")
                print(Fore.RED +"##############################")
                print(Fore.RED +"##############################")
                print(Fore.RED +"##############################")
            # assert spa in c
        # print("مقدار روی کارتابل" + " به درستی نمایش داده می شود. ")
        # assert b == text2
        assert b == a
        print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود. و برابر با تکست روی باتن است. ")

    def enter_admin_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        # assert a == 34
        # assert a == 36
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_admin_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "کوثر امیرخانی")

    def enter_admin_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[1]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[2]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[3]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a")
        assert self.driver.find_element('xpath', "/html/body/div[1]/header/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[3]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[5]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[6]/a")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[10]/a/img")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[10]/a/span")
        print("بخش های مختلف داشبورد به درستی نمایش داده شد.")
        print("لوگو به درستی نمایش داده شد.")
        print("بخش های مختلف navbar به درستی نمایش داده شد.")
        print("_______________________________________________")

    def admin_dashboard(self):
        menu_check(self, 'xpath', admin_dashboard, "پیشخوان")

    def admin_my_task(self):
        menu_check(self, 'xpath', admin_my_task, "کارتابل من")

    def admin_inbox(self):
        menu_check(self, 'xpath', admin_inbox, "پیام های من")

    def admin_train(self):
        menu_check(self, 'xpath', admin_train, "اطلاع رسانی و آموزش")

    def admin_report(self):
        menu_check(self, 'xpath', admin_report, "گزارش های مدیریتی")

    def admin_orders(self):
        menu_check(self, 'xpath', admin_orders, "سفارش ها")

    def admin_warehouses(self):
        menu_check(self, 'xpath', admin_warehouses, "انبار ها")

    def admin_fast_bill_scan(self):
        menu_check(self, 'xpath', admin_fast_bill_scan, "ثبت فوری قبض کالا")

    def admin_accept_order_op_by_scan(self):
        menu_check(self, 'xpath', admin_accept_order_op_by_scan, "دریافت کالا های سفارش با اسکن")

    def admin_batches(self):
        menu_check(self, 'xpath', admin_batches, "بسته ها")

    def admin_persons(self):
        # menu_check(self, 'xpath', admin_persons, "اشخاص")
        menu_check(self, 'xpath', admin_persons, "مشتریان")

    def admin_companies(self):
        menu_check(self, 'xpath', admin_companies, "شرکت ها")

    def admin_new_relabel(self):
        menu_check(self, 'xpath', admin_new_relabel, "چاپ مجدد برچسب کالا + چاپ")

    def admin_delivery_info_search(self):
        menu_check(self, 'xpath', admin_delivery_info_search, "جستجوی سفارش آماده تحویل")

    def admin_shipping_cost(self):
        menu_check(self, 'xpath', admin_shipping_cost, "محاسبه نرخ حمل")

    def admin_exchangerates(self):
        menu_check(self, 'xpath', admin_exchangerates, "نرخ های ارز")

    def admin_exchange_rate_profits(self):
        menu_check(self, 'xpath', admin_exchange_rate_profits, "پنل کارمزد صرافی")

    def admin_last_payments(self):
        menu_check(self, 'xpath', admin_last_payments, "پرداخت")

    def admin_last_yuan_payment(self):
        menu_check(self, 'xpath', admin_last_yuan_payment, "پرداخت های یوانی")

    def admin_china_expenses(self):
        menu_check(self, 'xpath', admin_china_expenses, "هزینه های چین")

    def admin_china_expenses_costs(self):
        menu_check(self, 'xpath', admin_china_expenses_costs, "حساب ماهانه چین")

    def admin_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', admin_crypto_gateway_recovery, "بررسی تراکنش شبکه‌ ترون")

    def admin_expert_chat(self):
        menu_check(self, 'xpath', admin_expert_chat, "گفتگو با مشتری ها")

    def admin_phone_marketer_calls(self):
        menu_check(self, 'xpath', admin_phone_marketer_calls, "تماس های بازاریاب تلفنی")

    def admin_iran_china_offices(self):
        menu_check(self, 'xpath', admin_iran_china_offices, "لیست شرکت های ایران و چین")

    def admin_customer_messages(self):
        menu_check(self, 'xpath', admin_customer_messages, "پیغام های مشتریان")

    def admin_festivals(self):
        menu_check(self, 'xpath', admin_festivals, "جشنواره ها")

    def admin_excel_export_files(self):
        menu_check(self, 'xpath', admin_excel_export_files, "لیست خروجی اکسل")

    def admin_path_menu(self):
        menu_check(self, 'xpath', admin_path_menu, "مسیرها")

    def admin_pkgs(self):
        menu_check(self, 'xpath', admin_pkgs, "بسته های نرم افزاری اندروید")

    def admin_task(self):
        menu_check(self, 'xpath', admin_task, "کارتابل من (قدیم)")

    def admin_settings(self):
        menu_check(self, 'xpath', admin_settings, "تنظیمات")

    def admin_customer_expert_messages(self):
        menu_check(self, 'xpath', admin_customer_expert_messages, "پیغام های مدیر مشتریان")

    def admin_profile(self):
        menu_check(self, 'xpath', admin_profile, "پروفایل کاربری")

    def admin_change_pass(self):
        menu_check(self, 'xpath', admin_change_pass, "تغییر کلمه عبور")

    def admin_exit(self):
        menu_check(self, 'xpath', admin_exit, "خروج")

    def len_admin(self):
        a1 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a"))
        a2 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a"))
        a3 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a"))
        a4 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-5']/div[2]/div/div/div[2]/a"))
        a5 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a"))
        a6 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a"))
        a7 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a"))
        a8 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a"))
        a9 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a"))
        a10 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-7']/div[2]/div/div/div[2]/a"))
        a11 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-8']/div[1]/div/div/div[2]/a"))
        a12 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-8']/div[2]/div/div/div[2]/a"))
        a13 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-11']/div[1]/div/div/div[2]/a"))
        a14 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-2']/div[1]/div/div/div[2]/a"))
        a15 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-2']/div[2]/div/div/div[2]/a"))
        a16 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-6']/div[1]/div/div/div[2]/a"))
        a17 = len(self.driver.find_elements('xpath', "//*[@id='task-collapse-6']/div[2]/div/div/div[2]/a"))
        b = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17
        print(b)
        # assert b == 206
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")








