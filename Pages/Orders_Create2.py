from Locators import *


class Orders_Create:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_orders(self):
        self.driver.find_element('xpath', click_orders).click()

    def enter_click_new_orders_create(self):
        self.driver.find_element('xpath', click_new_orders_create).click()

    def enter_click_orders_create(self):
        self.driver.find_element('xpath', click_orders_create).click()

    def enter_orders_create_name_select(self):
        self.driver.find_element('xpath', orders_create_name_select).click()

    def enter_orders_create_name_select_text(self, name):
        self.driver.find_element('xpath', orders_create_name_select_text).send_keys(name)

    def enter_orders_create_name_select_option(self):
        self.driver.find_element('xpath', orders_create_name_select_option).click()

    def enter_orders_create_name_select_option_text(self):
        a= self.driver.find_element('xpath', orders_create_name_select_option_text).text
        # assert a == "کاربر تست"
        print("کاربر: ", a , "به درستی نمایش داده شد.")

    def enter_orders_create_check_transport(self):
        self.driver.find_element('xpath', orders_create_check_transport).click()

    def enter_orders_create_check_clearance(self):
        self.driver.find_element('xpath', orders_create_check_clearance).click()

    def enter_orders_create_chooseservices(self):
        self.driver.find_element('xpath', orders_create_chooseservices).click()

    def enter_orders_create_products_holder(self):
        self.driver.find_element('xpath', click_create_order_product).click()

    def enter_orders_create_category_select(self):
        self.driver.find_element('xpath', orders_create_category_select).click()

    def enter_orders_create_category_select_option(self):
        self.driver.find_element('xpath', orders_create_category_select_option).click()

    def enter_orders_create_form_name(self, name):
        self.driver.find_element('xpath', orders_create_form_name).send_keys(name)

    def enter_orders_create_form_name_en(self, name):
        self.driver.find_element('xpath', orders_create_form_name_en).send_keys(name)

    def enter_orders_create_form_type(self):
        self.driver.find_element('xpath', orders_create_form_type).click()

    def enter_orders_create_form_type_option(self):
        self.driver.find_element('xpath', orders_create_form_type_option).click()

    def enter_orders_create_form_quantity(self):
        self.driver.find_element('xpath', orders_create_form_quantity).click()

    def enter_orders_create_form_quantity_option(self):
        self.driver.find_element('xpath', orders_create_form_quantity_option).click()

    def enter_orders_create_form_quantity_number(self, number):
        self.driver.find_element('xpath', orders_create_form_quantity_number).send_keys(number)

    def enter_orders_create_form_one_weight(self, number):
        self.driver.find_element('xpath', orders_create_form_one_weight).send_keys(number)

    def enter_orders_create_form_length(self, number):
        self.driver.find_element('xpath', orders_create_form_length).send_keys(number)

    def enter_orders_create_form_width(self, number):
        self.driver.find_element('xpath', orders_create_form_width).send_keys(number)

    def enter_orders_create_form_height(self, number):
        self.driver.find_element('xpath', orders_create_form_height).send_keys(number)

    def enter_orders_create_form_quantity_in_box(self, number):
        self.driver.find_element('xpath', orders_create_form_quantity_in_box).send_keys(number)

    def enter_orders_create_form_price_unit(self):
        self.driver.find_element('xpath', orders_create_form_price_unit).click()

    def enter_orders_create_form_price_unit_option(self):
        self.driver.find_element('xpath', orders_create_form_price_unit_option).click()

    def enter_orders_create_form_one_price(self, number):
        self.driver.find_element('xpath', orders_create_form_one_price).send_keys(number)

    def enter_orders_create_form_price(self, number):
        self.driver.find_element('xpath', orders_create_form_price).send_keys(number)

    def enter_orders_create_HSCODE(self):
        self.driver.find_element('xpath', orders_create_HSCODE).click()

    def enter_orders_create_HSCODE_option(self):
        self.driver.find_element('xpath', orders_create_HSCODE_option).click()

    def enter_orders_create_form_part_number(self, number):
        self.driver.find_element('xpath', orders_create_form_part_number).send_keys(number)

    def enter_orders_create_form_buy_url(self, url):
        self.driver.find_element('xpath', orders_create_form_buy_url).send_keys(url)

    def enter_orders_create_form_text(self, text):
        self.driver.find_element('xpath', orders_create_form_text).send_keys(text)

    def enter_orders_create_form_country(self, country):
        self.driver.find_element('xpath', orders_create_form_country).send_keys(country)

    def enter_orders_create_submit_information(self):
        self.driver.find_element('xpath', orders_create_submit_information).click()

###Completion_of_information


    def enter_orders_create_information_type(self):
        self.driver.find_element('xpath', orders_create_information_type).click()

    def enter_orders_create_information_type_option(self):
        self.driver.find_element('xpath', orders_create_information_type_option).click()

    def enter_orders_create_information_transport(self):
        self.driver.find_element('xpath', orders_create_information_transport).click()

    def enter_orders_create_information_transport_option(self):
        self.driver.find_element('xpath', orders_create_information_transport_option).click()

    def enter_orders_create_information_senders(self, number):
        self.driver.find_element('xpath', orders_create_information_senders).send_keys(number)

    def enter_orders_create_information_must_pay_before_transport(self):
        self.driver.find_element('xpath', orders_create_information_must_pay_before_transport).click()

    def enter_orders_create_information_must_pay_before_transport_option(self):
        self.driver.find_element('xpath', orders_create_information_must_pay_before_transport_option).click()

    def enter_orders_create_information_description(self, text):
        self.driver.find_element('xpath', orders_create_information_description).send_keys(text)

    def enter_orders_create_information_pay_in_china(self):
        self.driver.find_element('xpath', orders_create_information_pay_in_china).click()

    def enter_orders_create_information_pay_in_china_option(self):
        self.driver.find_element('xpath', orders_create_information_pay_in_china_option).click()

    def enter_orders_create_information_area_one(self):
        self.driver.find_element('xpath', orders_create_information_area_one).click()


###information_sender


    def enter_orders_create_information_sender_city(self):
        self.driver.find_element('xpath', orders_create_information_sender_city).click()

    def enter_orders_create_information_sender_name_select(self):
        self.driver.find_element('xpath', orders_create_information_sender_name_select).click()

    def enter_orders_create_information_sender_name(self, name):
        self.driver.find_element('xpath', orders_create_information_sender_name).send_keys(name)

    def enter_orders_create_information_sender_name_option(self):
        self.driver.find_element('xpath', orders_create_information_sender_name_option).click()

###information_receiver


    def enter_orders_create_information_receiver_city(self):
        self.driver.find_element('xpath', orders_create_information_receiver_city).click()

    def enter_orders_create_information_receiver_city_name(self, name):
        self.driver.find_element('xpath', orders_create_information_receiver_city_name).send_keys(name)

    def enter_orders_create_information_receiver_city_option(self):
        self.driver.find_element('xpath', orders_create_information_receiver_city_option).click()

    def enter_orders_create_information_receiver_name_select(self):
        self.driver.find_element('xpath', orders_create_information_receiver_name_select).click()

    def enter_orders_create_information_receiver_name(self, name):
        self.driver.find_element('xpath', orders_create_information_receiver_name).send_keys(name)

    def enter_orders_create_information_receiver_option(self):
        self.driver.find_element('xpath', orders_create_information_receiver_option).click()

###factor

    def enter_orders_create_information_sub_bill(self):
        self.driver.find_element('xpath', orders_create_information_sub_bill).click()

    def enter_orders_create_information_sub_bill_option(self):
        self.driver.find_element('xpath', orders_create_information_sub_bill_option).click()

    def enter_orders_create_information_factor_rasmi_transport(self):
        self.driver.find_element('xpath', orders_create_information_factor_rasmi_transport).click()

    def enter_orders_create_information_factor_rasmi_transport_option(self):
        self.driver.find_element('xpath', orders_create_information_factor_rasmi_transport_option).click()

    def enter_orders_create_information_factor_rasmi_clearance(self):
        self.driver.find_element('xpath', orders_create_information_factor_rasmi_clearance).click()

    def enter_orders_create_information_need_clearance_inquery(self):
        self.driver.find_element('xpath', orders_create_information_need_clearance_inquery).click()

    def enter_orders_create_information_need_clearance_inquery_option(self):
        self.driver.find_element('xpath', orders_create_information_need_clearance_inquery_option).click()

    def enter_orders_create_information_clearance_youan_invoice_request(self):
        self.driver.find_element('xpath', orders_create_information_clearance_youan_invoice_request).click()

    def enter_orders_create_information_clearance_youan_invoice_request_option(self):
        self.driver.find_element('xpath', orders_create_information_clearance_youan_invoice_request_option).click()

    def enter_orders_create_information_factor_rasmi(self):
        self.driver.find_element('xpath', orders_create_information_factor_rasmi).click()

    def enter_orders_create_information_factor_rasmi_option(self):
        self.driver.find_element('xpath', orders_create_information_factor_rasmi_option).click()

    def enter_orders_create_information_invoice_to_container(self):
        self.driver.find_element('xpath', orders_create_information_invoice_to_container).click()

    def enter_orders_create_information_invoice_to_container_name(self, name):
        self.driver.find_element('xpath', orders_create_information_invoice_to_container_name).send_keys(name)

    def enter_orders_create_information_invoice_to_container_option(self):
        self.driver.find_element('xpath', orders_create_information_invoice_to_container_option).click()

    def enter_orders_create_information_goback(self):
        self.driver.find_element('xpath', orders_create_information_goback).click()

    def enter_orders_create_information_approve(self):
        self.driver.find_element('xpath', orders_create_information_approve).click()

###review

    def enter_orders_create_next_review(self):
        self.driver.find_element('xpath', orders_create_next_review).click()

###check_the_order

    def enter_click_checking_the_order(self):
        self.driver.find_element('xpath', click_checking_the_order).click()

    def enter_check_the_order_approved(self):
        self.driver.find_element('xpath', check_the_order_approved).click()

###clearance_inquiry

    def enter_click_clearance_inquiry(self):
        self.driver.find_element('xpath', click_clearance_inquiry).click()

    def enter_clearance_inquiry_cargo_clearance(self):
        self.driver.find_element('xpath', clearance_inquiry_cargo_clearance).click()

    def enter_clearance_inquiry_cargo_clearance_option(self):
        self.driver.find_element('xpath', clearance_inquiry_cargo_clearance_option).click()

    def enter_clearance_inquiry_type(self):
        self.driver.find_element('xpath', clearance_inquiry_type).click()

    def enter_clearance_inquiry_type_option(self):
        self.driver.find_element('xpath', clearance_inquiry_type_option).click()

    def enter_clearance_inquiry_Price(self, number):
        self.driver.find_element('xpath', clearance_inquiry_Price).send_keys(number)

    def enter_clearance_inquiry_Price_unit(self):
        self.driver.find_element('xpath', clearance_inquiry_Price_unit).click()

    def enter_clearance_inquiry_comment(self, comment):
        self.driver.find_element('xpath', clearance_inquiry_comment).send_keys(comment)

    def enter_clearance_inquiry_form_save(self):
        self.driver.find_element('xpath', clearance_inquiry_form_save).click()

###other_inquiries

    def enter_click_other_inquiries(self):
        self.driver.find_element('xpath', click_other_inquiries).click()

    def enter_other_inquiries_services_invoice_type(self):
        self.driver.find_element('xpath', other_inquiries_services_invoice_type).click()

    def enter_other_inquiries_services_invoice_type_option(self):
        self.driver.find_element('xpath', other_inquiries_services_invoice_type_option).click()

    def enter_other_inquiries_services_invoice_type_update(self):
        self.driver.find_element('xpath', other_inquiries_services_invoice_type_update).click()

    def enter_other_inquiries_pre_factor_type(self):
        self.driver.find_element('xpath', other_inquiries_pre_factor_type).click()

    def enter_other_inquiries_price(self, price):
        self.driver.find_element('xpath', other_inquiries_price).send_keys(price)

    def enter_other_inquiries_price_unit(self):
        self.driver.find_element('xpath', other_inquiries_price_unit).click()

    def enter_other_inquiries_price_unit_option(self):
        self.driver.find_element('xpath', other_inquiries_price_unit_option).click()

    def enter_other_inquiries_description(self, comment):
        self.driver.find_element('xpath', other_inquiries_description).send_keys(comment)

    def enter_other_inquiries_save_submit(self):
        self.driver.find_element('xpath', other_inquiries_save_submit).click()




