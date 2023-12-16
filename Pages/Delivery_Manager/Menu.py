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


class Delivery_My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def enter_delivery_manager_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "مهدی خالقی")

    def enter_delivery_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "طاهر غنی ابادی")

    def enter_delivery_manager_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/a[1]/div")
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

    def enter_delivery_menu_check_tag_dashboard(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[2]/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a/div/div")
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

    def enter_delivery_manager_accept_order_op_by_scan(self):
        menu_check(self, 'xpath', delivery_manager_accept_order_op_by_scan, "دریافت کالا های سفارش با اسکن")

    def enter_delivery_manager_batches(self):
        menu_check(self, 'xpath', delivery_manager_batches, "بسته ها")

    def enter_delivery_manager_receive_confirm_box(self):
        menu_check(self, 'xpath', delivery_manager_receive_confirm_box, "چاپ مجدد برچسب کالا + چاپ")

    def enter_delivery_manager_delivery_info(self):
        menu_check(self, 'xpath', delivery_manager_delivery_info, "جستجوی سفارش آماده تحویل")

    def enter_delivery_manager_shipping_rate(self):
        menu_check(self, 'xpath', delivery_manager_shipping_rate, "محاسبه نرخ حمل")

    def enter_delivery_manager_check_exchange_rates(self):
        menu_check(self, 'xpath', delivery_manager_exchange_rates, "نرخ های ارز")

    def enter_delivery_manager_check_list_excel_output(self):
        menu_check(self, 'xpath', delivery_manager_list_excel_output, "لیست خروجی اکسل")

    def enter_delivery_manager_check_user_profile(self):
        menu_check(self, 'xpath', delivery_manager_user_profile, "پروفایل کاربری")

    def enter_delivery_manager_check_change_password(self):
        menu_check(self, 'xpath', delivery_manager_change_password, "تغییر کلمه عبور")

    def enter_delivery_manager_check_exit(self):
        menu_check(self, 'xpath', delivery_manager_exit, "خروج")

    def len_delivery_manager(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a"))
        assert a == 4
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def ready_to_deliver_to_customer(self):
        my_tasks_check(self, delivery_manager_ready_to_deliver_to_customer)

    def select_a_driver_for_delivery(self):
        my_tasks_check(self, delivery_manager_select_a_driver_for_delivery)

    def delivery_warehouse_inventory(self):
        my_tasks_check(self, delivery_manager_delivery_warehouse_inventory)

    def enter_delivery_menu_check_inbox(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[4]/a", "پیام های من")

    def enter_delivery_menu_check_information_and_training(self):
        menu_check(self, 'xpath', delivery_menu_information_and_training, "اطلاع رسانی و آموزش")

    def enter_delivery_menu_check_management_reports(self):
        menu_check(self, 'xpath', delivery_menu_management_reports, "گزارش های مدیریتی")

    def enter_delivery_menu_check_orders(self):
        menu_check(self, 'xpath', delivery_menu_orders, "سفارش ها")

    def enter_delivery_menu_search_orders(self):
        menu_check(self, 'xpath', delivery_menu_search_orders, "جستجوی سفارش آماده تحویل")

    def enter_delivery_shipping_rate(self):
        menu_check(self, 'xpath', delivery_shipping_rate, "محاسبه نرخ حمل")

    def enter_delivery_check_exchange_rates(self):
        menu_check(self, 'xpath', delivery_exchange_rates, "نرخ های ارز")

    def enter_delivery_check_list_excel_output(self):
        menu_check(self, 'xpath', delivery_list_excel_output, "لیست خروجی اکسل")

    def enter_delivery_check_user_profile(self):
        menu_check(self, 'xpath', delivery_user_profile, "پروفایل کاربری")

    def enter_delivery_check_change_password(self):
        menu_check(self, 'xpath', delivery_change_password, "تغییر کلمه عبور")

    def enter_delivery_check_exit(self):
        menu_check(self, 'xpath', delivery_exit, "خروج")

    def len_delivery(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a"))
        assert a == 1
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def enter_delivery_my_tasks_warehouse(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def enter_delivery_my_tasks_customer_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def enter_delivery_my_tasks_customer_manager1(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[2]/a").click()

    def receive_customer_payment_from_delivery(self):
        my_tasks_check(self, "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a[4]")

    def print_clearance_documents(self):
        my_tasks_check(self, "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a[3]")

    def receive_customer_payment_from_delivery1(self):
        my_tasks_check(self, "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a[1]")

    def print_clearance_documents1(self):
        my_tasks_check(self, "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a[2]")

    def op_delivery_call(self):
        my_tasks_check(self, "//*[@id='nav-category-4']/div/div/div/div[2]/a")
