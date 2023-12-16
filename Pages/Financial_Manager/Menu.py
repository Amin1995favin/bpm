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
    sleep(0.7)
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.7)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = self.driver.find_element(element_selector, element_locator+"/small").text
    print(a)
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


class Financial_My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def enter_financial_menu_check_tag(self):
        a = len(self.driver.find_elements('xpath', "/html/body/div[1]/aside/section/ul/li/a"))
        assert a == 18
        print("تعداد منو به درستی نمایش داده شد.")
        print("__________")

    def enter_financial_manager_menu_check_name(self):
        menu_check(self, 'xpath', customer_manager_menu_name, "زهرا عمرانی")

    def enter_financial_manager_menu_check_tag_dashboard(self):
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

    def enter_financial_batches(self):
        menu_check(self, 'xpath', financial_batches, "بسته ها")

    def enter_financial_persons(self):
        # menu_check(self, 'xpath', financial_persons, "اشخاص")
        menu_check(self, 'xpath', financial_persons, "مشتریان")

    def enter_financial_companies(self):
        menu_check(self, 'xpath', financial_companies, "شرکت ها")

    def enter_financial_manager_shipping_rate(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[10]/a", "محاسبه نرخ حمل")

    def enter_financial_manager_check_exchange_rates(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[11]/a", "نرخ های ارز")

    def enter_financial_last_payments(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[12]/a", "پرداخت")

    def enter_financial_china_expenses(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[13]/a", "هزینه های چین")

    def enter_financial_china_expenses2(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[14]/a", "حساب ماهانه چین")

    def enter_financial_crypto_gateway_recovery(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[15]/a", "بررسی تراکنش شبکه‌ ترون")

    def enter_financial_manager_check_list_excel_output(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[16]/a", "لیست خروجی اکسل")

    def enter_financial_manager_check_user_profile(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[18]/a", "پروفایل کاربری")

    def enter_financial_manager_check_change_password(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[19]/a", "تغییر کلمه عبور")

    def enter_financial_manager_check_exit(self):
        menu_check(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[20]/a", "خروج")

    def len_financial_manager(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div[1]/div/div/div[2]/a"))
        print(a)
        assert a == 19
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def len_financial(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div[1]/div/div/div[2]/a"))
        assert a == 1
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def auto_new_payment(self):
        my_tasks_check(self, 'xpath', financial_auto_new_payment)

    def auto_custom_bill_orders(self):
        my_tasks_check(self, 'xpath', financial_auto_custom_bill_orders)

    def factors_price_unit_change_after_insert_arian(self):
        my_tasks_check(self, 'xpath', financial_factors_price_unit_change_after_insert_arian)

    def auto_new_online_payment(self):
        my_tasks_check(self, 'xpath', financial_auto_new_online_payment)

    def update_integrated_user_in_arian(self):
        my_tasks_check(self, 'xpath', financial_update_integrated_user_in_arian)

    def cancelled_orders_with_paid_invoice(self):
        my_tasks_check(self, 'xpath', financial_cancelled_orders_with_paid_invoice)

    def submit_in_financial_system_official(self):
        my_tasks_check(self, 'xpath', financial_submit_in_financial_system_official)

    def after_payment_changed(self):
        my_tasks_check(self, 'xpath', financial_after_payment_changed)

    def changes_in_invoices(self):
        my_tasks_check(self, 'xpath', financial_changes_in_invoices)

    def arian_register_cryp_to_payments(self):
        my_tasks_check(self, 'xpath', financial_arian_register_cryp_to_payments)

    def order_owner_migration_to_arian(self):
        my_tasks_check(self, 'xpath', financial_order_owner_migration_to_arian)

    def my_tasks_need_official_invoice(self):
        my_tasks_check(self, 'xpath', financial_my_tasks_need_official_invoice)

    def submit_in_financial_system(self):
        my_tasks_check(self, 'xpath', financial_submit_in_financial_system)

    def factors_chang_after_insert_arian(self):
        my_tasks_check(self, 'xpath', financial_factors_chang_after_insert_arian)

    def china_transaction_log(self):
        my_tasks_check(self, 'xpath', financial_china_transaction_log)

    def settled_no_payment(self):
        my_tasks_check(self, 'xpath', financial_settled_no_payment)

    def check_commission_payment_request(self):
        my_tasks_check(self, 'xpath', financial_check_commission_payment_request)

    def arian_register_foreign_payments(self):
        my_tasks_check(self, 'xpath', financial_arian_register_foreign_payments)

    def auto_wallet_refund(self):
        my_tasks_check(self, 'xpath', financial_auto_wallet_refund)

    def new_of_invoice_after_print_delivery(self):
        my_tasks_check(self, 'xpath', financial_new_of_invoice_after_print_delivery)

    def click_customer_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def check_china_transaction(self):
        my_tasks_check(self, 'xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a[1]")

    def sales_claims(self):
        my_tasks_check(self, 'xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a[2]")

    def click_warehouses(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def auto_billed_order(self):
        my_tasks_check(self, 'xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a")

    def len_financial_manager_my_task(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        clearance = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        financial = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        sale = len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div/div/div/div[2]/a"))
        assert a == 4
        assert clearance == 1
        assert financial == 18
        assert sale == 2
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")









