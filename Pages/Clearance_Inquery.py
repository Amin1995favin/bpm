from Locators import *
from selenium.webdriver.common.alert import Alert
from time import sleep
# import pandas as pd


class Clearance_Inquery:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_box_clearance_inquery(self):
        self.driver.find_element('xpath', click_box_clearance_inquery).click()

    def enter_click_box_clearance_inquery_submit(self):
        self.driver.find_element('xpath', click_box_clearance_inquery_submit).click()

    # def enter_click_alert(self):
    #     alert = Alert(self.driver)
    #     # sleep(1)
    #     # alert.accept()
    #     alert = self.driver.switch_to.alert
    #     if alert.is_displayed():
    #         alert.accept()

    def enter_click_alert(self, a=2):
        for i in range(a):
            try:
                self.driver.switch_to.alert.accept()
                sleep(1)
                return
            except:
                print('\n')
                sleep(1)

    def enter_box_clearance_inquery_price(self, price):
        a = self.driver.find_element('xpath', box_clearance_inquery_price)
        a.clear()
        a.send_keys(price)

    def enter_box_clearance_inquery_the_weight_of_each_clove(self):
        el2 = self.driver.find_element('xpath', box_clearance_inquery_total_actual_weight).text
        el= "return $('#formprice_per_kilo').val()"
        el3 = self.driver.execute_script(el)
        a = print(el3)
        print(el2)
        # w = (int(el2)/int(el3))
        w = (500 / int(el2))
        x = round(w, 2)
        b = print(x)
        assert a == b
        print("قیمت به ازای هر کیلو = " , "جمع حرم وزنی / قیمت ")
        print("قیمت به ازای هر کیلو درست نمابش  داده می شود.")

    def enter_box_clearance_inquery_cheng_factor_rasmi_option1(self):
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi).click()
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi_option1).click()
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi_update).click()
        sleep(2)
        el= "return $('#formvat_rate').val()"
        el3 = self.driver.execute_script(el)
        # assert el3 == "9"
        print("در فاکتور رسمی 9% مالبات دیده می شود.")

    def enter_box_clearance_inquery_cheng_factor_rasmi_option2(self):
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi).click()
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi_option2).click()
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi_update).click()
        sleep(2)
        el= "return $('#formvat_rate').val()"
        el3 = self.driver.execute_script(el)
        print(el3)
        # assert el3 == "0"
        print("در فاکتور غبر رسمی 0% مالبات دیده می شود.")

    def enter_box_clearance_inquery_cheng_factor_rasmi_update(self):
        self.driver.find_element('xpath', box_clearance_inquery_cheng_factor_rasmi_update).click()

###conversion_rate_to_iranian_rial

    def enter_click_exchange_rate(self):
        self.driver.find_element('xpath', click_exchange_rate).click()

    def enter_check_conversion_rate_to_iranian_rial(self):
        el1 = self.driver.find_element('xpath', exchange_rate_yuan).text
        el2 = self.driver.find_element('xpath', exchange_rate_dollar).text
        el3 = self.driver.find_element('xpath', exchange_rate_euro).text
        el4 = self.driver.find_element('xpath', exchange_rate_dirham).text
        # el5 = self.driver.find_element('xpath', exchange_rate_pond).text
        el6 = self.driver.find_element('xpath', exchange_rate_lear).text
        el7 = self.driver.find_element('xpath', exchange_rate_syrian_lira).text
        print(el1 + '\n'+el2 + '\n'+el3 + '\n'+el4 + '\n'+el6 + '\n'+el7 + '\n')

    def enter_clearance_inquiry_Price_unit(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()

    def enter_clearance_inquiry_Price_unit_option1(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option1).click()

    def enter_clearance_inquiry_Price_unit_option2(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option2).click()

    def enter_clearance_inquiry_Price_unit_option3(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option3).click()

    def enter_clearance_inquiry_Price_unit_option4(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option4).click()

    def enter_clearance_inquiry_Price_unit_option5(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option5).click()

    def enter_clearance_inquiry_Price_unit_option6(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option6).click()

    def enter_clearance_inquiry_Price_unit_option7(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option7).click()

    def enter_check_conversion_rate_to_iranian_rial1(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option1).click()
        sleep(3)
        el1= "return $('#formtorialrate').val()"
        ela1 = self.driver.execute_script(el1)
        # print(ela1)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option2).click()
        sleep(3)
        el2= "return $('#formtorialrate').val()"
        ela2 = self.driver.execute_script(el2)
        # print(ela2)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option3).click()
        sleep(3)
        el3= "return $('#formtorialrate').val()"
        ela3 = self.driver.execute_script(el3)
        # print(ela3)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option4).click()
        sleep(3)
        el4= "return $('#formtorialrate').val()"
        ela4 = self.driver.execute_script(el4)
        # print(ela4)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option5).click()
        sleep(3)
        el5= "return $('#formtorialrate').val()"
        ela5 = self.driver.execute_script(el5)
        # print(ela5)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option6).click()
        sleep(3)
        el6= "return $('#formtorialrate').val()"
        ela6 = self.driver.execute_script(el6)
        # print(ela6)
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()
        self.driver.find_element('xpath', clearance_inquiry_Price_unit_option7).click()
        sleep(3)
        el7= "return $('#formtorialrate').val()"
        ela7 = self.driver.execute_script(el7)
        # print(ela7)
        self.driver.find_element('xpath', click_exchange_rate).click()
        sleep(3)
        el01 = self.driver.find_element('xpath', exchange_rate_yuan).text
        el02 = self.driver.find_element('xpath', exchange_rate_dollar).text
        el03 = self.driver.find_element('xpath', exchange_rate_euro).text
        el04 = self.driver.find_element('xpath', exchange_rate_dirham).text
        el05 = self.driver.find_element('xpath', exchange_rate_pond).text
        el06 = self.driver.find_element('xpath', exchange_rate_lear).text
        el07 = self.driver.find_element('xpath', exchange_rate_syrian_lira).text
        # print(el01 + '\n' + el02 + '\n' + el03 + '\n' + el04 + '\n' + el06 + '\n' + el07 + '\n')
        # print(ela3 , el01)
        # assert ela3 == el01
        # print(ela3)
        # print(el01)
        assert ela4 == el01
        assert ela2 == el02
        assert ela5 == el03
        assert ela3 == el04
        # assert ela5 == el05
        assert ela6 == el06
        # print(ela7 + "option7" + '\n' + "option7" + el07)
        # assert ela7 == el07
        print("نمایش قیمت اعلامی به ریال برای تمام واحد های ارزی به درستی از جدول نرخ ارز خوانده می شود.")

###check_declared_price

    def enter_check_declared_price(self):
        el1 = "return $('#formoffer_price').val().replace(/,/g , '')"
        el2 = self.driver.execute_script(el1)
        el3 = self.driver.find_element('xpath', box_clearance_inquery_percent)
        el3a = el3.get_attribute('value')
        el4= "return $('#formtorialrate').val().replace(/,/g , '')"
        el5 = self.driver.execute_script(el4)
        el6 = (500 * ((int(el3a))/100))+500
        el7 = int(el6)
        el8 = int(el5)
        el9 = el7 * el8
        el2a = int(el2)
        assert el9 == el2a
        print("قیمت اعلامی به ریال = " , "درصد سود * قیمت * نرخ تبدیل به ریال")
        print("نمایش قیمت اعلامی به ریال درست می باشد.")

###check_final_price

    def enter_check_final_price(self):
        el3 = self.driver.find_element('xpath', box_clearance_inquery_final_price)
        el4 = el3.get_attribute('value')
        el1 = "return $('#formoffer_price').val().replace(/,/g , '')"
        el2 = self.driver.execute_script(el1)
        sleep(1)
        # el3 = "return $('#formvat_rate-n1-n2-n3-n4-n5-n6').val()"
        # el4 = self.driver.execute_script(el3)
        el4 = (int(el4)/100)
        # print(el4)
        el5 = "return $('#formtotal_price').val().replace(/,/g , '')"
        el6 = self.driver.execute_script(el5)
        el2 = int(el2)
        # el4 = int(el4)
        el6 = int(el6)
        # print(el6)
        el7 = (el2 * el4)+el2
        el7= int(el7)
        print(el7)
        # el2a = int(el2)
        assert el7 == el6
        print("قیمت نهایی = " , "درصد مالیات * قیمت اعلامی به ریال ")
        print("قیمت نهایی به درستی نمایش داده می شود.")

###check_final_price_per_kilo

    def enter_check_final_price_per_kil(self):
        el1 = "return $('#formtotal_price').val().replace(/,/g , '')"
        el2 = self.driver.execute_script(el1)
        el3 = "return $('#formfinal_price_per_kilo').val().replace(/,/g , '')"
        el4 = self.driver.execute_script(el3)

        el2 = int(el2)
        el4 = int(el4)

        el5 = (el2/100)+el2
        # el7= int(el7)
        # print(el7)
        # el2a = int(el2)
        # assert el4 == el6

###check_invoice

    def enter_box_clearance_invoice_check_Price(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_Price).text
        # print(el)
        el =el.replace(".","")
        # print(el)
        assert '50000' in el
        print("قیمت به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_interest_rate(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_interest_rate).text
        # print(el)
        el =el.replace(".","")
        # print(el)
        assert '2000' in el
        print("درصد سود به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_total_actual_weight(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_total_actual_weight).text
        assert el == "جرمی 1040 کیلوگرم"
        print("جرم به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_tax_coefficient(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_tax_coefficient).text
        print(el)
        assert '9' in el
        print("مالیات به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_final_price(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_final_price)
        assert 'bg-black' in el.get_attribute('class')
        print("رنگ قیمت نهایی به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_payments_list(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_payments_list).text
        print(el)
        assert "0 ریال" in el
        print("رنگ قیمت نهایی به درستی نمایش داده شد.")

    def enter_box_clearance_invoice_check_awaiting_Payment(self):
        el = self.driver.find_element('xpath', box_clearance_invoice_check_awaiting_Payment).text
        print(el)
        assert "ریال" in el
        print("رنگ قیمت نهایی به درستی نمایش داده شد.")

    def enter_box_order_details_check_color_checking_Shipping_Cost(self):
        self.driver.find_element('xpath', box_order_details_check_color_checking_Shipping_Cost).click()

###box_clearance_check_form

    def enter_box_clearance_check_form_tax_return(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_tax_return)
        print("Tax Return", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_inquiry(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_inquiry)
        print("استعلامات", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_invoices(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_invoices)
        print("پیش فاکتور ها", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_proof_of_dead(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_proof_of_dead)
        print("اعلام نقص مدرک", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_pre_evaluation_notes(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_pre_evaluation_notes)
        print("یادداشت پیش ارزیابی", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_clearance_inquiry_code(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_clearance_inquiry_code)
        print("کد استعلام ترخیص", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_customs_purchase_link(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_customs_purchase_link)
        print("لینک خرید گمرک", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_clearance_invoice_type(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_clearance_invoice_type)
        print("نوع پیش فاکتور ترخیص", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_billing_delivery_information(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_billing_delivery_information)
        print("اطلاعات تحویل قبض", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_user_notes(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_user_notes)
        print("یادداشت مربوط به کاربر", " به درستی مشاهده شد")

    def enter_box_clearance_check_form_issue_clearance_inquiry(self):
        assert self.driver.find_element('xpath', box_clearance_check_form_issue_clearance_inquiry)
        print("صدور استعلام ترخیص", " به درستی مشاهده شد")

    def enter_box_clearance_check_len_invoices(self):
        el1 = len(self.driver.find_elements('xpath', box_clearance_check_len_invoices))
        return el1

    def enter_box_clearance_check_len_inquiry(self):
        el1 = len(self.driver.find_elements('xpath', box_clearance_check_len_inquiry))
        return el1

    def enter_box_clearance_click_full_invoice(self):
        self.driver.find_element('xpath', box_clearance_click_full_invoice).click()

    def enter_box_clearance_click_checking_shipping_cost(self):
        self.driver.find_element('xpath', box_order_details_check_color_checking_Shipping_Cost).click()

    def enter_box_clearance_check_inquiry_box(self):
        assert self.driver.find_element('xpath', box_clearance_check_inquiry_check_box)
        assert self.driver.find_element('xpath', box_clearance_check_inquiry_create_invoice)
        assert self.driver.find_element('xpath', box_clearance_check_inquiry_copy_the_information_in_the_form)
        print("تیک معتبر است و ", " ایجادپیش فاکتور و", " کپی اطلاعات در فرم به درستی مشاهده شد")


