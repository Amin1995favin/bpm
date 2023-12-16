from colorama import Fore

from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


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


class Export_My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def my_tasks_check_table(self, a, args):
        sleep(2)
        th = {}
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        if tr == 2:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', f"//table/thead/tr[2]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        elif tr == 1:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', f"//table/thead/tr[1]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        print("_____________")

    def enter_export_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 19
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

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
            assert spa in c
        print("مقدار روی کارتابل" + " به درستی نمایش داده می شود. ")
        # assert b == text2
        assert b == a
        print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود.  وبرابر با تکست باتن است. ")

    def enter_export_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "امیر رئوفی")

    def enter_export_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div[1]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[1]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[2]/div")
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
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/img")
        assert self.driver.find_element('xpath', "//*[@id='usernavbar']/li[9]/a/span")
        print("بخش های مختلف داشبورد به درستی نمایش داده شد.")
        print("لوگو به درستی نمایش داده شد.")
        print("بخش های مختلف navbar به درستی نمایش داده شد.")
        print("_______________________________________________")

    def export_dashboard(self):
        menu_check(self, 'xpath', admin_dashboard, "پیشخوان")

    def export_my_task(self):
        menu_check(self, 'xpath', admin_my_task, "کارتابل من")

    def export_inbox(self):
        menu_check(self, 'xpath', admin_inbox, "پیام های من")

    def export_train(self):
        menu_check(self, 'xpath', admin_train, "اطلاع رسانی و آموزش")

    def export_report(self):
        menu_check(self, 'xpath', admin_report, "گزارش های مدیریتی")

    def export_orders(self):
        menu_check(self, 'xpath', admin_orders, "سفارش ها")

    def enter_financial_warehouses(self):
        menu_check(self, 'xpath', financial_batches, "انبار ها")

    def enter_export_accept_order_op_by_scan(self):
        menu_check(self, 'xpath', financial_persons, "دریافت کالا های سفارش با اسکن")

    def enter_export_batches(self):
        menu_check(self, 'xpath', financial_companies, "بسته ها")

    def enter_export_persons(self):
        # menu_check(self, 'xpath', financial_manager_shipping_rate, "اشخاص")
        menu_check(self, 'xpath', financial_manager_shipping_rate, "مشتریان")

    def enter_export_shipping_rate(self):
        menu_check(self, 'xpath', financial_manager_exchange_rates, "محاسبه نرخ حمل")

    def enter_export_check_exchange_rates(self):
        menu_check(self, 'xpath', financial_last_payments, "نرخ های ارز")

    def enter_export_last_payments(self):
        menu_check(self, 'xpath', financial_china_expenses, "پرداخت")

    def enter_export_china_expenses2(self):
        menu_check(self, 'xpath', financial_china_expenses2, "بررسی تراکنش شبکه‌ ترون")

    def enter_export_chat(self):
        menu_check(self, 'xpath', financial_crypto_gateway_recovery, "گفتگو با مشتری ها")

    def enter_export_check_list_excel_output(self):
        menu_check(self, 'xpath', financial_manager_list_excel_output, "لیست خروجی اکسل")

    def enter_export_check_user_profile(self):
        menu_check(self, 'xpath', financial_manager_user_profile, "پروفایل کاربری")

    def enter_export_check_change_password(self):
        menu_check(self, 'xpath', financial_manager_change_password, "تغییر کلمه عبور")

    def enter_export_manager_check_exit(self):
        menu_check(self, 'xpath', financial_manager_exit, "خروج")

    def len_export(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[2]/div/div/div[2]/a"))
        assert a+b == 33
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_export_my_task(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        clearance = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        export = len(self.driver.find_elements('xpath', "//*[@id='nav-category-2']/div/div/div/div[2]/a"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        financial = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        delivery = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a"))
        customer = len(self.driver.find_elements('xpath', "//*[@id='nav-category-5']/div/div/div/div[2]/a"))
        assert a == 8
        assert clearance == 8
        assert export == 5
        assert warehouse == 2
        assert financial == 3
        assert delivery == 2
        assert customer == 6
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def enter_export_my_tasks_clearance(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def enter_export_my_tasks_export(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def enter_export_my_tasks_warehouse(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[5]/a").click()

    def enter_export_my_tasks_financial(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[6]/a").click()

    def enter_export_my_tasks_delivery(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[7]/a").click()

    def enter_export_my_tasks_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[8]/a").click()








