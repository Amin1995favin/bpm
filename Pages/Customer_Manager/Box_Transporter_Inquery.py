from Locators import *
from time import sleep
from unidecode import unidecode


class Box_Transporter_Inquery:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_box_transporter_inquery(self):
        self.driver.find_element('xpath', click_box_transporter_inquery).click()

    ################### box_transporter_inquery_check_form ###################

    def enter_box_transporter_inquery_check_table_results(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_results)
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_results_data)
        print("نتایج ", " به درستی مشاهده شد و دیتا هم موجود است")

    def enter_box_transporter_inquery_check_table_invoice_forwarding_factors(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_invoice_forwarding_factors)
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_invoice_forwarding_factors_data)
        print("پیش فاکتور های استعلام حمل", " به درستی مشاهده شد و دیتا هم موجود است")

    def enter_box_transporter_inquery_check_table_list_of_shipping_discounts_per_kilo(self):
        assert self.driver.find_element('xpath',
                                        box_transporter_inquery_check_table_list_of_shipping_discounts_per_kilo)
        print("فهرست تخفیف های حمل در هر کیلو", " به درستی مشاهده شد")

    def enter_box_transporter_inquery_check_table_estimated_transportation_cost(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_estimated_transportation_cost)
        print("تخمین قیمت حمل", " به درستی مشاهده شد")

    def enter_box_transporter_inquery_check_table_request_a_discount_on_shipping_per_kilo(self):
        assert self.driver.find_element('xpath',
                                        box_transporter_inquery_check_table_request_a_discount_on_shipping_per_kilo)
        print("درخواست تخفیف حمل به ازای هر کیلو", " به درستی مشاهده شد")

    def enter_box_transporter_inquery_check_table_currency_of_invoice_shipping(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_currency_of_invoice_shipping)
        print("واحد ارزی فاکتور حمل", " به درستی مشاهده شد")

    def enter_box_transporter_inquery_check_table_transportation_invoice_type(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_table_transportation_invoice_type)
        print("نوع پیش فاکتور حمل", " به درستی مشاهده شد")

    ################### box_transporter_inquery_check_datetime ###################

    def enter_box_transporter_inquery_price_unit_select(self):
        self.driver.find_element('xpath', box_transporter_inquery_price_unit_select).click()

    def enter_box_transporter_inquery_price_unit_option(self):
        self.driver.find_element('xpath', box_transporter_inquery_price_unit_option).click()

    def enter_box_transporter_inquery_price_unit_option2(self):
        self.driver.find_element('xpath', box_transporter_inquery_price_unit_option2).click()

    def enter_box_transporter_inquery_per_kilo(self, number):
        a = self.driver.find_element('xpath', box_transporter_inquery_per_kilo)
        a.clear()
        a.send_keys(number)

    def enter_box_transporter_inquery_per_kilo_submit(self):
        self.driver.find_element('xpath', box_transporter_inquery_per_kilo_submit).click()

    def enter_box_transporter_inquery_check_datetime_create(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_datetime_create).text
        a = unidecode(a)
        return a

    def enter_box_transporter_inquery_click_the_record_is_valid(self, a=1):
        for i in range(a):
            try:
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid).click()
                # return
                break
            except:
                print('\n')

    def enter_box_transporter_inquery_check_the_record_is_valid(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_the_record_is_valid)
        print("رکورد معتبر است دیده شد.")

    def enter_box_transporter_inquery_check_awaiting_approval(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_awaiting_approval)
        print("در انتظار تایید دیده شد.")

    def enter_box_transporter_inquery_check_discount_per_kilo(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_discount_per_kilo).text
        assert a == "50000"
        print("قیمت به درستی نمایش داده شد.")

    def enter_box_transporter_inquery_check_currency_unit(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_currency_unit).text
        print(a)
        assert a == "ریال"
        print("واحد ارز به درستی نمایش داده شد.")

    def enter_box_transporter_inquery_check_error_currency_unit(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_error_currency_unit)
        print(
            " امکان درخواست تخفیف در واحد برای پیش فاکتور حمل وجود ندارد. چراکه در حال حاضر تخفیف درجریانی وجود دارد.")

    def enter_box_transporter_inquery_check_saved_currency_unit(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_saved_currency_unit)
        print("رکورد جدید با موفقیت  ذخیره شد.")

    def enter_box_transporter_inquery_check_error_discount_per_kil(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_error_discount_per_kil)
        print("اعداد منفی را نمی توان وارد کرد.")

    def enter_box_transporter_inquery_check_is_it_valid(self):
        sleep(1)
        self.driver.find_element('xpath', box_transporter_inquery_check_is_it_valid).click()
        print("رکورد غیر معتبر شد.")
        sleep(1)
        self.driver.find_element('xpath', box_transporter_inquery_check_is_it_valid).click()
        print("رکورد معتبر شد.")

    def enter_box_transporter_inquery_check_table_invoice_click_forwarding_factors(self):
        self.driver.find_element('xpath', box_transporter_inquery_check_table_invoice_click_forwarding_factors).click()
        sleep(1)

    def enter_box_transporter_inquery_check_view_invoice(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_view_invoice)
        assert 'bg-orange' in a.get_attribute('class')
        print("رنگ نمایش پیش فاکتور نارتجی می باشد.")

    def enter_box_transporter_inquery_click_view_invoice(self):
        sleep(1)
        self.driver.find_element('xpath', box_transporter_inquery_check_view_invoice).click()

    def enter_box_transporter_inquery_invoice_to_person(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_to_person).click()

    def enter_box_transporter_inquery_invoice_to_person_option(self):
        sleep(1)
        self.driver.find_element('xpath', box_transporter_inquery_invoice_to_person_option).click()

    def enter_box_transporter_inquery_invoice_to_company_name(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_to_company_name).click()

    def enter_box_transporter_inquery_invoice_to_company_name_option(self):
        sleep(1)
        self.driver.find_element('xpath', box_transporter_inquery_invoice_to_company_name_option).click()

    def enter_box_transporter_inquery_view_invoice_submit(self):
        self.driver.find_element('xpath', box_transporter_inquery_view_invoice_submit).click()

    def enter_box_transporter_inquery_view_invoice_error(self):
        sleep(1)
        assert self.driver.find_element('xpath', box_transporter_inquery_view_invoice_error)
        print("فاکتور نمی تواند همزمان به نام شخص و نام شرکت باشد")

    ################### box_transporter_inquery_invoice_check_action ###################

    def enter_box_transporter_inquery_invoice_action_invoice_valid(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_invoice_action_invoice_valid)
        assert 'btn-success' in a.get_attribute('class')
        print("رنگ نمایش فاکتور معتبر است سبز می باشد.")

    def enter_box_transporter_inquery_invoice_action_invoice_not_sent(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_invoice_action_invoice_not_sent)
        assert 'btn-info' in a.get_attribute('class')
        print("رنگ نمایش به مشتری ارسال نشده آبی می باشد.")

    def enter_box_transporter_inquery_invoice_action_invoice_no_approval(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_invoice_action_invoice_no_approval)
        assert 'btn-info' in a.get_attribute('class')
        print("رنگ نمایش فاقد تاییدیه مشتری آبی می باشد.")

    ################### box_transporter_inquery_check_invoice_type ###################

    def enter_click_to_box_transporter_inquery(self):
        self.driver.find_element('xpath', click_to_box_transporter_inquery).click()

    def enter_box_transporter_inquery_click_invoice_type(self):
        self.driver.find_element('xpath', box_transporter_inquery_click_invoice_type).click()

    def enter_box_transporter_inquery_invoice_type_option1(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_type_option1).click()

    def enter_box_transporter_inquery_invoice_type_option2(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_type_option2).click()

    def enter_box_transporter_inquery_invoice_type_update(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_type_update).click()

    def enter_box_transporter_inquery_invoice_check_tax_coefficient1(self):
        sleep(1)
        a = self.driver.find_element('xpath', box_transporter_inquery_invoice_check_tax_coefficient1).text
        assert a == "9"
        print("مالیات در فاکتور رسمی به درستی به مقدار 9 درصد نمایش داده شد.")

    def enter_box_transporter_inquery_invoice_check_tax_coefficient2(self):
        sleep(1)
        a = self.driver.find_element('xpath', box_transporter_inquery_invoice_check_tax_coefficient2).text
        assert a == "0"
        print("مالیات در فاکتور غیر رسمی به درستی به مقدار 0 درصد نمایش داده شد.")

    def enter_box_transporter_inquery_invoice_transport_price_unit(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_transport_price_unit).click()

    def enter_box_transporter_inquery_invoice_transport_price_unit_option(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_transport_price_unit_option).click()

    def enter_box_transporter_inquery_invoice_transport_price_unit_submit(self):
        self.driver.find_element('xpath', box_transporter_inquery_invoice_transport_price_unit_submit).click()

    ################### box_transporter_inquery_check_paid ###################

    def enter_box_transporter_inquery_check_paid1(self):
        assert self.driver.find_element('xpath', box_transporter_inquery_check_paid1)
        print("روی در انتظار پرداخت نمی توان کلیک کرد")

    def enter_box_transporter_inquery_check_paid2(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_paid2).text
        return a

    def enter_box_transporter_inquery_check_paid3(self):
        a = self.driver.find_element('xpath', box_transporter_inquery_check_paid3).text
        assert 'دلار' in a
        print("واحد ارز فاکتور حمل به درستی تغییر داده شد.")
