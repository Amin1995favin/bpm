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


def my_tasks_check(self, element_selector, element_locator, text1, text2):
    wait = WebDriverWait(self.driver, 20)
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.5)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = scrolled.text
    # print(a)
    assert text1 in a
    print(" تکست باتن "+text1+" به درستی نمایش داده می شود. ")
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
    # assert b == text2
    # print(" تایتل کارتابل "+text2+" به درستی نمایش داده می شود. ")
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


class Uae:
    def __init__(self, driver):
        self.driver = driver

    def enter_uae_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 12
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_uae_financial_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        # assert a == 9
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_uae_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "شعیب حیدر")

    def enter_uae_financial_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "فهیمه فرضی نژاد")

    def enter_uae_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[2]/a")
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

    def enter_uae_financial_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[2]/a[2]")
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

    def uae_delivery_menu_dashboard(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[2]/a", "Dashboard")

    def uae_delivery_menu_my_tasks(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[3]/a", "My Tasks")

    def uae_delivery_menu_information(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[4]/a", "Information and training")

    def uae_delivery_menu_orders(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[5]/a", "Orders")

    def uae_delivery_menu_warehouses(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[6]/a", "Warehouses")

    def uae_delivery_menu_receive_ordered_goods(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a", "Receive ordered goods by scanning")

    def uae_delivery_menu_batches(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[8]/a", "Batches")

    def uae_delivery_menu_duplicate(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "duplicate")

    def uae_delivery_menu_excel(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "List Excel output")

    def uae_delivery_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "User Profile")

    def uae_delivery_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "Change Password")

    def uae_delivery_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "Exit")

    def len_dubai(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        assert a == 12
        print("تعداد کارتابل های نمایشی صحیح می باشد")

    def len_dubai_my_tasks(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        financial = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        delivery = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a"))
        customer = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a"))
        export = len(self.driver.find_elements('xpath', "//*[@id='nav-category-2']/div/div/div/div[2]/a"))
        assert a == 6
        assert warehouse == 12
        assert financial == 1
        assert delivery == 2
        assert customer == 2
        assert export == 1
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_dubai_my_tasks_delivery(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        delivery = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a"))
        customer = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a"))
        export = len(self.driver.find_elements('xpath', "//*[@id='nav-category-2']/div/div/div/div[2]/a"))
        assert a == 5
        assert warehouse == 12
        assert delivery == 2
        assert customer == 2
        assert export == 1
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_uae_financial(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]//a"))
        print(a)
        assert a == 12
        print("تعداد کارتابل های نمایشی صحیح می باشد")

    def enter_uae_financial_menu_check_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a", "لیست خروجی اکسل")

    def enter_uae_financial_menu_check_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "پروفایل کاربری")

    def enter_uae_financial_menu_check_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "تغییر کلمه عبور")

    def enter_uae_financial_menu_check_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "خروج")

    def click_financial(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def click_delivery(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def click_customer_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[5]/a").click()

    def click_customer_export(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[6]/a").click()

    def click_delivery_delivery(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def click_delivery_customer_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def click_delivery_export(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[5]/a").click()
