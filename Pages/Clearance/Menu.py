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


def clearance_my_tasks_check(self, element_selector, element_locator, text1, text2):
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
    assert b == text1
    print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود. و برابر با تکست روی باتن است. ")


def clearance_menu_check(self, element_selector, element_locator, text):
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.5)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = scrolled.text
    # print(a)
    assert text in a
    print(" تکست "+text+" به درستی نمایش داده می شود. ")
    print("__________")


class My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def enter_clearance_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        assert a == 17
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_delivery_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        assert a == 12
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_delivery_menu_check_tag2(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        print(a)
        assert a == 13
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_clearance_menu_check_name(self):
        clearance_menu_check(self, 'xpath', customer_manager_menu_name, "عرفان ایپکلو")

    def enter_clearance_menu_check_tag_dashboard(self):
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

    def enter_clearance_warehouses(self):
        clearance_menu_check(self, 'xpath', clearance_warehouses, "انبار ها")

    def enter_clearance_warehouses_fast_bill_scan(self):
        clearance_menu_check(self, 'xpath', clearance_warehouses_fast_bill_scan, "ثبت فوری قبض کالا")

    def enter_clearance_warehouses_accept_order_op_by_scan(self):
        clearance_menu_check(self, 'xpath', clearance_warehouses_accept_order_op_by_scan, "دریافت کالا های سفارش با اسکن")

    def enter_clearance_batches(self):
        clearance_menu_check(self, 'xpath', clearance_batches, "بسته ها")

    def enter_clearance_menu_shipping_rate(self):
        clearance_menu_check(self, 'xpath', clearance_menu_shipping_rate, "محاسبه نرخ حمل")

    def enter_clearance_menu_check_exchange_rates(self):
        clearance_menu_check(self, 'xpath', clearance_menu_exchange_rates, "نرخ های ارز")

    def enter_clearance_menu_check_list_excel_output(self):
        clearance_menu_check(self, 'xpath', clearance_menu_list_excel_output, "لیست خروجی اکسل")

    def enter_clearance_menu_settings(self):
        clearance_menu_check(self, 'xpath', clearance_menu_settings, "تنظیمات")

    def enter_clearance_menu_check_user_profile(self):
        clearance_menu_check(self, 'xpath', clearance_menu_user_profile, "پروفایل کاربری")

    def enter_clearance_menu_check_change_password(self):
        clearance_menu_check(self, 'xpath', clearance_menu_change_password, "تغییر کلمه عبور")

    def enter_clearance_menu_check_exit(self):
        clearance_menu_check(self, 'xpath', clearance_menu_exit, "خروج")

    def enter_clearance_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks)

    def len_clearance(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div[1]/div/div/div[2]/a"))
        print(a)
        assert a == 13
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_clearance_my_task(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        clearance = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        financial = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        delivery = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a"))
        customer = len(self.driver.find_elements('xpath', "//*[@id='nav-category-5']/div/div/div/div[2]/a"))
        assert a == 3
        assert clearance == 0
        assert warehouse == 0
        assert financial == 0
        assert delivery == 4
        assert customer == 0
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def need_clearance_inquiry(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_need_clearance_inquiry, "منتظر صدور پیش فاکتور ترخیص هوایی", "منتظر صدور پیش فاکتور ترخیص هوایی")

    def cleared_orders(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_cleared_orders, "سفارشات دارای کد ترخیص کار", "سفارشات دارای کد ترخیص کار")

    def need_final_clearance(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_need_final_clearance, "نیاز به استعلام ترخیص نهایی", "نیاز به استعلام ترخیص نهایی")

    def auto_other_clearance(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_auto_other_clearance, "ترخیص واردات صادرات غیر از چین", "ترخیص واردات صادرات غیر از چین")

    def clearance_update(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_clearance_update, "آپدیت ترخیص", "آپدیت ترخیص")

    def batch_files_in_formation(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_batch_files_in_formation, "ورود اطلاعات بچ", "ورود اطلاعات بچ")

    def notification_closure_batch(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_notification_closure_batch, "اطلاع از بسته شدن بچ", "اطلاع از بسته شدن بچ")

    def auto_billed_order(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_auto_billed_order, "سفارشات قبض شده", "سفارشات قبض شده")

    def pickup_by_customs(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_pickup_by_customs, "در انتظار بارگیری توسط گمرک", "در انتظار بارگیری توسط گمرک")

    def new_auto_billed_order(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_new_auto_billed_order, "ثبت هزینه ی بارهای قبضی", "ثبت هزینه ی بارهای قبضی")

    def auto_need_clearance_invoice_sea(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_auto_need_clearance_invoice_sea, "منتظر صدور پیش فاکتور ترخیص دریایی", "منتظر صدور پیش فاکتور ترخیص دریایی")

    def auto_need_clearance_invoice_sea_finaly(self):
        clearance_my_tasks_check(self, 'xpath', clearance_my_tasks_auto_need_clearance_invoice_sea_finaly, "نیاز به استعلام ترخیص دریایی نهایی", "نیاز به استعلام ترخیص دریایی نهایی")

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
