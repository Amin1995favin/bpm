from persiantools import jdatetime
from unidecode import unidecode
from Locators import *
from datetime import datetime
from persiantools.jdatetime import JalaliDate


class Orders:
    def __init__(self, driver):
        self.driver = driver

    ################### click_orders ###################

    def enter_click_orders(self):
        self.driver.find_element('xpath', click_orders).click()

    ################### check_orders_datetime ###################

    def enter_check_orders_end_date(self):
        a = self.driver.find_element('xpath', orders_end_date)
        b = a.get_attribute('value')
        b = unidecode(b)
        # now = datetime.now()
        # c = print(now.strftime("%Y/%m/%d"))
        c = JalaliDate.today().strftime("%Y/%m/%d")
        # c = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        print(b)
        print(c)
        assert c == b

        print("نام", "به درستی مشاهده شد.")

    ################### check_orders_table ###################

    def enter_orders_check_table_row(self):
        assert self.driver.find_element('xpath', orders_check_table_row)
        print("ردیف", "به درستی مشاهده شد.")

    def enter_orders_check_table_order(self):
        assert self.driver.find_element('xpath', orders_check_table_order)
        print("سفارش", "به درستی مشاهده شد.")

    def enter_orders_check_table_receiver(self):
        assert self.driver.find_element('xpath', orders_check_table_receiver)
        print("دریافت کننده", "به درستی مشاهده شد.")

    def enter_orders_check_table_sender(self):
        assert self.driver.find_element('xpath', orders_check_table_sender)
        print("ارسال کننده", "به درستی مشاهده شد.")

    def enter_orders_check_table_order_weight(self):
        assert self.driver.find_element('xpath', orders_check_table_order_weight)
        print("وزن سفارش (KG)", "به درستی مشاهده شد.")

    def enter_orders_check_table_order_product(self):
        assert self.driver.find_element('xpath', orders_check_table_order_product)
        print("کالای سفارش", "به درستی مشاهده شد.")

    def enter_orders_check_table_required_services(self):
        assert self.driver.find_element('xpath', orders_check_table_required_services)
        print("خدمات موردنیاز", "به درستی مشاهده شد.")

    def enter_orders_check_table_creator(self):
        assert self.driver.find_element('xpath', orders_check_table_creator)
        print("ایجادکننده", "به درستی مشاهده شد.")

    def enter_orders_check_table_th(self):
        el1 = len(self.driver.find_elements('xpath', orders_check_table_th))
        assert el1 == 8
        print("تعداد ستون ها بررسی و بصورت درست می باشند.")

    def enter_orders_check_table_customer_manager(self):
        a = self.driver.find_elements('xpath', orders_check_table_customer_manager)
        a = len(a)
        assert a == 30
        print("در تمام نتایج مدیر مشتری زهرا پیروز می باشد.")

    ################### check_orders_search_id ###################

    def enter_orders_check_id(self):
        a = self.driver.find_element('xpath', orders_check_id).text
        a = a.replace("-", "")
        return a

    def enter_orders_check_search(self, number):
        self.driver.find_element('xpath', orders_check_search).send_keys(number)

    def enter_orders_check_search_btn(self):
        self.driver.find_element('xpath', orders_check_search_btn).click()

    def enter_orders_check_table_search(self):
        a = self.driver.find_elements('xpath', orders_check_table_customer_manager)
        a = len(a)
        assert a == 1
        print("نتایج سرچ به درستی نمایش داده می شود.")

    def enter_orders_id_click(self):
        self.driver.find_element('xpath', orders_check_id).click()

    def enter_orders_id_customer_manager(self):
        a = self.driver.find_element('xpath', orders_id_customer_manager).text
        assert 'مدیر مشتری : زهرا پیروز / Zahra Pirooz' in a

