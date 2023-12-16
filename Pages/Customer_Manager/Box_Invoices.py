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


class Box_Invoices:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_box_invoices(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_invoices)

    def enter_box_invoices_check_invoice_list(self):
        assert self.driver.find_element('xpath', box_invoices_check_invoice_list)
        print("پیش فاکتور ها ", " به درستی مشاهده شد")

    def enter_box_invoices_check_approvals_final_settlement_order(self):
        assert self.driver.find_element('xpath', box_invoices_check_approvals_final_settlement_order)
        print("تاییدیه تسویه نهایی سفارش", " به درستی مشاهده شد")

    def enter_box_invoices_check_approvals_financial_for_international_transportation(self):
        assert self.driver.find_element('xpath',
                                        box_invoices_check_approvals_financial_for_international_transportation)
        print("تاییدیه برای حمل بین الملل", " به درستی مشاهده شد")

    def enter_box_invoices_check_pick_up_order(self):
        assert self.driver.find_element('xpath', box_invoices_check_pick_up_order)
        print("تاییدیه بارگیری کالا توسط گمرک", " به درستی مشاهده شد")

    def enter_box_invoices_check_change_pro_invoice_owner(self):
        assert self.driver.find_element('xpath', box_invoices_check_change_pro_invoice_owner)
        print("تغییر صاحب پیش فاکتور", " به درستی مشاهده شد")

    def enter_box_invoices_check_send_aggregate_link(self):
        assert self.driver.find_element('xpath', box_invoices_send_aggregate_link)
        print("ارسال لینک تجمیعی", " به درستی مشاهده شد")

    def enter_box_invoices_check_filter_clearance(self):
        assert self.driver.find_element('xpath', box_invoices_filter_clearance)
        print("ترخیص ", " به درستی مشاهده شد")

    def enter_box_invoices_check_filter_other_services(self):
        assert self.driver.find_element('xpath', box_invoices_filter_other_services)
        print("سایر خدمات ", " به درستی مشاهده شد")

    def enter_box_invoices_check_filter_shipping_cost(self):
        assert self.driver.find_element('xpath', box_invoices_filter_shipping_cost)
        print("حمل ", " به درستی مشاهده شد")

    def enter_box_invoices_click_filter_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_invoices_filter_clearance)

    def enter_box_invoices_click_filter_other_services(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_invoices_filter_other_services)

    def enter_box_invoices_click_filter_shipping_cost(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_invoices_filter_shipping_cost)

    def enter_box_invoices_not_sent_to_the_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_invoices_not_sent_to_the_customer)

    def enter_box_invoices_no_customer_approval(self):
        wait_until_element_has_an_attribute(self, 'xpath', box_invoices_no_customer_approval)

    def enter_box_invoices_click_send_to_whatsapp(self):
        assert self.driver.find_element('xpath', box_invoices_send_to_whatsapp)
        print("ارسال به واتس اپ ", " به درستی مشاهده شد")



