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


# def my_tasks_check(self, element_selector, element_locator, text1, text2):
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


class Turk:
    def __init__(self, driver):
        self.driver = driver

    def enter_turk_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 13
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_turk_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "محسن حسین زاده")

    def enter_turk_clearance_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "Alaattin Barut")

    def enter_turk_menu_check_tag_dashboard(self):
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

    def enter_turk_clearance_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
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

    def turk_menu_dashboard(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[2]/a", "پیشخوان")

    def turk_menu_my_tasks(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[3]/a", "کارتابل من")

    def turk_menu_inbox(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[4]/a", "پیام های من")

    def turk_menu_train(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[5]/a", "اطلاع رسانی و آموزش")

    def turk_menu_warehouses(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[6]/a", "انبار ها")

    def turk_menu_accept_order_op_by_scan(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a", "دریافت کالا های سفارش با اسکن")

    def turk_menu_batches(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[8]/a", "بسته ها")

    def turk_menu_persons(self):
        # menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "اشخاص")
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "مشتریان")

    def turk_menu_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "بررسی تراکنش شبکه‌ ترون")

    def turk_menu_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "لیست خروجی اکسل")

    def turk_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "پروفایل کاربری")

    def turk_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "تغییر کلمه عبور")

    def turk_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "خروج")

    def len_turk(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a"))
        assert a == 9
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_turk_clearance(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        assert a == 2
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_turk_clearance_my_task(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        clearance = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        assert a == 3
        assert warehouse == 9
        assert clearance == 2
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

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

    def turk_clearance_menu_dashboard(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[2]/a", "Dashboard")

    def turk_clearance_menu_my_tasks(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[3]/a", "My Tasks")

    def turk_clearance_menu_inbox(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[4]/a", "Inbox")

    def turk_clearance_menu_train(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[5]/a", "Information and training")

    def turk_clearance_menu_warehouses(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[6]/a", "Warehouses")

    def turk_clearance_menu_accept_order_op_by_scan(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a", "Receive ordered goods by scanning")

    def turk_clearance_menu_batches(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[8]/a", "Batches")

    def turk_clearance_menu_persons(self):
        # menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "Persons")
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "Customers")

    def turk_clearance_menu_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "Investigate Theron Network Transaction")

    def turk_clearance_menu_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "List Excel output")

    def turk_clearance_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "User Profile")

    def turk_clearance_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "Change Password")

    def turk_clearance_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "Exit")

    def clearance_click_warehouse(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()



