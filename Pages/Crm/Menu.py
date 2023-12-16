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


class Crm_My_Tasks:
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
            assert spa in c
        print("مقدار روی کارتابل" + " به درستی نمایش داده می شود. ")
        # assert b == text2
        assert b == a
        print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود.  وبرابر با تکست باتن است. ")

    def enter_crm_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 36
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_crm_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "مهناز عنقایی")

    def enter_crm_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        # assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[2]")
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

    def crm_dashboard(self):
        menu_check(self, 'xpath', admin_dashboard, "پیشخوان")

    def crm_my_task(self):
        menu_check(self, 'xpath', admin_my_task, "کارتابل من")

    def crm_inbox(self):
        menu_check(self, 'xpath', admin_inbox, "پیام های من")

    def crm_train(self):
        menu_check(self, 'xpath', admin_train, "اطلاع رسانی و آموزش")

    def crm_report(self):
        menu_check(self, 'xpath', admin_report, "گزارش های مدیریتی")

    def crm_orders(self):
        menu_check(self, 'xpath', admin_orders, "سفارش ها")

    def crm_shipping_cost(self):
        menu_check(self, 'xpath', admin_warehouses, "محاسبه نرخ حمل")

    def crm_exchangerates(self):
        menu_check(self, 'xpath', admin_fast_bill_scan, "نرخ های ارز")

    def crm_excel_export_files(self):
        menu_check(self, 'xpath', admin_accept_order_op_by_scan, "لیست خروجی اکسل")

    def crm_check_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "پروفایل کاربری")

    def crm_check_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "تغییر کلمه عبور")

    def crm_check_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "خروج")

    def len_crm(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-9']/div/div/div/div[2]/a"))
        print(a)
        assert a == 2
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")








