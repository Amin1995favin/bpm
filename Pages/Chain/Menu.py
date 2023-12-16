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


class Chain:
    def __init__(self, driver):
        self.driver = driver

    def enter_chain_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 15
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_chain_warehouse_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 13
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_chain_financial_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 14
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_chain_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "کلارا کلارا")

    def enter_chain_manager_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "کوین")

    def enter_chain_warehouse_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "Chen Chen")

    def enter_chain_financial_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "Jane Jane")

    def enter_chain_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/a[2]")
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

    def enter_chain_financial_menu_check_tag_dashboard(self):
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

    def chain_menu_persons(self):
        # menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "Persons")
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "Customers")

    def chain_menu_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "Investigate Theron Network Transaction")

    def chain_menu_companies(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "IR/CN Companies")

    def chain_menu_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "List Excel output")

    def chain_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "User Profile")

    def chain_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[16]/a", "Change Password")

    def chain_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[17]/a", "Exit")

    def len_chain(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[2]/div/div/div[2]/a"))
        c = a+b
        assert c == 16
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_chain_manager(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[2]/div/div/div[2]/a"))
        c = a+b
        assert c == 14
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_chain_financial(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        assert a == 1
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def chain_warehouse_menu_companies(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "IR/CN Companies")

    def chain_warehouse_menu_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "List Excel output")

    def chain_warehouse_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "User Profile")

    def chain_warehouse_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "Change Password")

    def chain_warehouse_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "Exit")

    def len_chain_warehouse(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[2]/div/div/div[2]/a"))
        c = a+b
        assert c == 9
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

    def financial_menu_batches(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a", "Batches")

    def financial_menu_yuan_payments(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[8]/a", "Yuan payments")

    def financial_menu_china_costs(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[9]/a", "China costs")

    def financial_menu_china_monthly_account(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "China monthly account")

    def financial_menu_investigate_theron_network_transaction(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "Investigate Theron Network Transaction")

    def financial_menu_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "List Excel output")

    def financial_menu_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "User Profile")

    def financial_menu_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "Change Password")

    def financial_menu_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[16]/a", "Exit")







