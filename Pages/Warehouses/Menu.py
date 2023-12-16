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
    sleep(0.8)
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


class Warehouses_My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def enter_warehouses_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 15
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_warehouses_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "joemin joemin joemin joemin")

    def enter_warehouses_menu_check_tag_dashboard(self):
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

    def warehouses_menu_dashboard(self):
        menu_check(self, 'xpath', warehouses_menu_dashboard, "Dashboard")

    def warehouses_menu_my_tasks(self):
        menu_check(self, 'xpath', warehouses_menu_my_tasks, "My Tasks")

    def warehouses_menu_inbox(self):
        menu_check(self, 'xpath', warehouses_menu_inbox, "Inbox")

    def warehouses_menu_information_and_training(self):
        menu_check(self, 'xpath', warehouses_menu_information_and_training, "Information and training")

    def warehouses_menu_orders(self):
        menu_check(self, 'xpath', warehouses_menu_orders, "Orders")

    def warehouses_menu_warehouses(self):
        menu_check(self, 'xpath', warehouses_menu_warehouses, "Warehouses")

    def warehouses_menu_receive_ordered_goods_by_scanning(self):
        menu_check(self, 'xpath', warehouses_menu_receive_ordered_goods_by_scanning, "Receive ordered goods by scanning")

    def warehouses_menu_batches(self):
        menu_check(self, 'xpath', warehouses_menu_batches, "Batches")

    def warehouses_menu_persons(self):
        # menu_check(self, 'xpath', warehouses_menu_persons, "Persons")
        menu_check(self, 'xpath', warehouses_menu_persons, "Customers")

    def warehouses_menu_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', warehouses_menu_crypto_gateway_recovery, "Investigate Theron Network Transaction")

    def warehouses_menu_companies(self):
        menu_check(self, 'xpath', warehouses_menu_companies, "IR/CN Companies")

    def warehouses_menu_list_excel_output(self):
        menu_check(self, 'xpath', warehouses_menu_list_excel_output, "List Excel output")

    def warehouses_menu_user_profile(self):
        menu_check(self, 'xpath', warehouses_menu_user_profile, "User Profile")

    def warehouses_menu_change_password(self):
        menu_check(self, 'xpath', warehouses_menu_change_password, "Change Password")

    def warehouses_menu_exit(self):
        menu_check(self, 'xpath', warehouses_menu_exit, "Exit")

    def len_warehouses(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a"))
        b = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div[2]/div/div/div[2]/a"))
        c = a+b
        assert c == 14
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def orders_are_waiting_to_be_batched(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_orders_are_waiting_to_be_batched)

    def order_with_tax_returns(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_order_with_tax_returns)

    def sending_to_warehouse(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_sending_to_warehouse)

    def loading(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_loading)

    def repack_request_origin_warehouse(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_repack_request_origin_warehouse)

    def print_warehouse_documents(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_print_warehouse_documents)

    def request_references(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_request_references)

    def notification_of_change_of_route_to_the_source_warehouse(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_notification_of_change_of_route_to_the_source_warehouse)

    def loaded(self):
        my_tasks_check(self, 'xpath', warehouses_my_tasks_loaded1)

    def click_customer_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def request_buy_car_table(self):
        my_tasks_check(self, 'xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a")

    def chain_click_orders(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_orders)

    def enter_click_orders_check_len(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[1]/div/a"))
        assert a == 9
        print("تعداد نوبار درست است. ")
        assert len(self.driver.find_elements('xpath', "//input")) == 3
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//button[@class='btn btn-success btn-sm btn-block mt-2']")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[2]/div/div/div/div/div[2]/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[2]/div/div/div/div/div[2]/span")) == 1
        print("تعداد باتن ها و input ها درست است. ")
        print("..................................................")






