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


class Orders_Create:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_feather_light_content(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_feather_light_content)

    def enter_click_feather_light_content2(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_feather_light_content2)

    def enter_click_orders(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_orders)

    def enter_click_orders_syria(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[6]/a")

    def enter_click_orders_id(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_orders_id)

    def enter_click_orders_id_tn(self, text):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_orders_list_all_orders)
        sleep(0.3)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "//*[@id='dateFilter']/div[2]/input", text)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='dateFilter']/div[2]/button")
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', click_orders_id)

    def enter_click_orders_doing_open(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_orders_doing_open)

    def enter_click_new_orders_create(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_new_orders_create)

    def enter_click_orders_create(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_orders_create)

    def enter_click_orders_check_len(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[1]/div/a"))
        assert a == 9
        print("تعداد نوبار درست است. ")
        assert len(self.driver.find_elements('xpath', "//input")) == 3
        assert len(self.driver.find_elements('xpath', "//select")) == 4
        assert len(self.driver.find_elements('xpath', "//button[@class='btn btn-success btn-sm btn-block mt-2']")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[2]/div/div/div/div/div[2]/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/div[2]/div/div/div/div/div[2]/span")) == 1
        print("تعداد باتن ها و input ها درست است. ")
        print("..................................................")

    def enter_delivery_manager_click_orders_check_len(self):
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

    def enter_orders_create_name_check(self):
        assert self.driver.find_element('xpath', orders_create_name_select)
        assert self.driver.find_element('xpath', orders_create_check_transport)
        assert self.driver.find_element('xpath', orders_create_check_clearance)
        assert self.driver.find_element('xpath', "//*[@id='chooseservices']/form/div[1]/div/div/div[4]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/p/a")
        assert self.driver.find_element('xpath', "//*[@id='buy']")
        assert self.driver.find_element('xpath', "//*[@id='chooseservices']/form/div[2]/div/div/button")
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//input")) == 4
        print("تمام قسمت های انتخاب خدمات موردنیاز صحیح نمایش داده می شود.")

    def enter_orders_create_name_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_name_select)

    def enter_orders_create_name_select_text(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_name_select_text, text)

    def enter_orders_create_name_select_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_name_select_option)

    def enter_orders_create_name_select_option_text(self):
        a = self.driver.find_element('xpath', orders_create_name_select_option_text).text
        # assert a == "کاربر تست"
        print("کاربر: ", a, "به درستی نمایش داده شد.")

    def enter_orders_create_check_transport(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_check_transport)

    def enter_orders_create_check_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_check_clearance)

    def enter_orders_create_chooseservices(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_chooseservices)

    def enter_orders_create_choose_services_check(self):
        if self.driver.find_elements('xpath', "//*[@id='orderproductsholder']/div[3]/a"and "//*[@id='formorder_type-n1']"
                                        and "//*[@id='formtransport_type-n1']" and "//*[@id='formtotalweight-n1']"
                                        and "//*[@id='formtotalvweight-n1']" and "//*[@id='formtotalcweight-n1']"
                                        and "//*[@id='formtotalprice-n1']" and "//*[@id='formpriceunit-n1']"
                                        and "//*[@id='formsenders_count-n1']" and "//*[@id='formmustpaybeforetransport-n1']"
                                        and "//*[@id='formsenders_description-n1']" and "//*[@id='formpay_in_china-n1']"
                                        and "//*[@id='formis_areaone-n1']"
                                        and "//*[@id='information']/div/div/form/div[2]/div[2]/div[1]/div/div/span/span[1]/span"
                                        and "//*[@id='select2-formsender_p-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[2]/div[3]/div[1]/div[3]/a"
                                        and "//*[@id='select2-formsender_c-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/div[3]/a"
                                        and "//*[@id='select2-formreceiver_city-n1-container']"
                                        and "//*[@id='select2-formreceiver_p-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[3]/div[4]/div[1]/div[3]/a"
                                        and "//*[@id='select2-formreceiver_c-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[3]/div[4]/div[2]/div[3]/a"
                                        and "//*[@id='information']/div/div/form/div[2]/div[3]/div[1]/button"
                                        and "//*[@id='information']/div/div/form/div[2]/div[3]/div[3]/button"
                                        and "//*[@id='formsubbill-n1']"
                                        and "//*[@id='formfactorrasmi_transport-n1']"
                                        and "//*[@id='formneed_clearance_inquery-n1']"
                                        and "//*[@id='formclearance_youan_invoice_request-n1']"
                                        and "//*[@id='formfactorrasmi-n1']"
                                        and "//*[@id='information']/div/div/form/div[6]/div[1]/button"
                                        and "//*[@id='select2-forminvoiceto_p-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[5]/div[3]/div[1]/a"
                                        and "//*[@id='select2-forminvoiceto_c-n1-container']"
                                        and "//*[@id='information']/div/div/form/div[5]/div[3]/div[3]/a"
                                    ):
            print("همه بخش ها دیده شدند.")
        else:
            print("Elements not found")
        assert len(self.driver.find_elements('xpath', "//select")) == 22
        assert len(self.driver.find_elements('xpath', "//input")) == 10
        assert len(self.driver.find_elements('xpath', "//*[@id='information']/div/div//button")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@class='btn btn-success btn-block btn_create_person']")) == 6
        print("تمام بخش های تکمیل اطلاعات سفارش به درستی مشاهده شدند و تعداد آنان صحیح می باشد.")

    ################## Completion_of_information #########################

    def enter_orders_create_information_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_type)

    def enter_orders_create_information_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_type_option)

    def enter_orders_create_information_transport(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_transport)

    def enter_orders_create_information_transport_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_transport_option)

    def enter_orders_create_information_senders(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_information_senders, text)

    def enter_orders_create_information_must_pay_before_transport(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_must_pay_before_transport)

    def enter_orders_create_information_must_pay_before_transport_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_must_pay_before_transport_option)

    def enter_orders_create_information_description(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_information_description, text)

    def enter_orders_create_information_pay_in_china(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_pay_in_china)

    def enter_orders_create_information_pay_in_china_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_pay_in_china_option)

    def enter_orders_create_information_area_one(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_area_one)

    ################## information_sender #########################

    def enter_orders_create_information_sender_city(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_sender_city)

    def enter_orders_create_information_sender_name_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_sender_name_select)

    def enter_orders_create_information_sender_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_information_sender_name, text)

    def enter_orders_create_information_sender_name_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_sender_name_option)

    ################## information_receiver #########################

    def enter_orders_create_information_receiver_city(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_receiver_city)

    def enter_orders_create_information_receiver_city_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_information_receiver_city_name,
                                                          text)

    def enter_orders_create_information_receiver_city_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_receiver_city_option)

    def enter_orders_create_information_receiver_name_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_receiver_name_select)

    def enter_orders_create_information_receiver_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_information_receiver_name, text)

    def enter_orders_create_information_receiver_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_receiver_option)

    ################## factor #########################

    def enter_orders_create_information_sub_bill(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_sub_bill)

    def enter_orders_create_information_sub_bill_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_sub_bill_option)

    def enter_orders_create_information_factor_rasmi_transport(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi_transport)

    def enter_orders_create_information_factor_rasmi_transport_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi_transport_option)

    def enter_orders_create_information_factor_rasmi_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi_clearance)

    def enter_orders_create_information_factor_rasmi_clearance_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi_clearance_option)

    def enter_orders_create_information_need_clearance_inquery(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_need_clearance_inquery)

    def enter_orders_create_information_need_clearance_inquery_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_need_clearance_inquery_option)

    def enter_orders_create_information_clearance_youan_invoice_request(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_clearance_youan_invoice_request)

    def enter_orders_create_information_clearance_youan_invoice_request_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            orders_create_information_clearance_youan_invoice_request_option)

    def enter_orders_create_information_factor_rasmi(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi)

    def enter_orders_create_information_factor_rasmi_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_factor_rasmi_option)

    def enter_orders_create_information_invoice_to_container(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_invoice_to_container)

    def enter_orders_create_information_invoice_to_container_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          orders_create_information_invoice_to_container_name, text)

    def enter_orders_create_information_invoice_to_container_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_invoice_to_container_option)

    def enter_orders_create_information_goback(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_goback)

    def enter_orders_create_information_approve(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_approve)

    def enter_orders_create_information_approve2(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_information_approve2)

    ################## review #########################

    def enter_orders_create_next_review(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_next_review)

    ################## check_the_order #########################

    def enter_click_checking_the_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_checking_the_order)

    def enter_check_the_order_approved(self):
        wait_until_element_has_an_attribute(self, 'xpath', check_the_order_approved)

    ################## clearance_inquiry #########################

    def enter_click_clearance_inquiry(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_clearance_inquiry)

    def enter_clearance_inquiry_cargo_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_cargo_clearance)

    def enter_clearance_inquiry_cargo_clearance_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_cargo_clearance_option)

    def enter_clearance_inquiry_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_type)

    def enter_clearance_inquiry_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_type_option)

    def enter_clearance_inquiry_price(self, number):
        self.driver.find_element('xpath', clearance_inquiry_price).send_keys(number)

    def enter_clearance_inquiry_price_unit(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_price_unit)

    def enter_clearance_inquiry_price_unit_option1(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_price_unit_option1)

    def enter_clearance_inquiry_comment(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', clearance_inquiry_comment, text)

    def enter_clearance_inquiry_form_save(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_inquiry_form_save)

    ################## other_inquiries #########################

    def enter_click_other_inquiries(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_other_inquiries)

    def enter_click_other_inquiries_check(self):
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert '(استعلام حمل)' in self.driver.find_element('xpath', "//table/tbody/tr/td[2]/a[1]").text
        print("بررسی شد که فقط یک فاکتور وجود داشته باشد و آن هم برای حمل می باشد")

    def enter_click_other_inquiries_check_chain_iran(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div//table/tbody/tr")) == 1
        # assert '(استعلام حمل)' in self.driver.find_element('xpath', "//table/tbody/tr/td[2]/a[1]").text
        print("بررسی شد که فقط یک فاکتور وجود داشته باشد و آن هم برای حمل می باشد")

    def enter_other_inquiries_services_invoice_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_services_invoice_type)

    def enter_other_inquiries_services_invoice_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_services_invoice_type_option)

    def enter_other_inquiries_services_invoice_type_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_services_invoice_type_update)

    def enter_other_inquiries_pre_factor_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_pre_factor_type)

    def enter_other_inquiries_price(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', other_inquiries_price, text)

    def enter_other_inquiries_price_unit(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_price_unit)

    def enter_other_inquiries_price_unit_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_price_unit_option)

    def enter_other_inquiries_description(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', other_inquiries_description, text)

    def enter_other_inquiries_save_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', other_inquiries_save_submit)

    ################### orders_create_check #########################

    def enter_orders_create_check_data(self):
        assert self.driver.find_element('xpath', click_create_order_product)
        print(" ایجاد کالای سفارش مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_type)
        print(" نوع سفارش مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_transport)
        print(" نوع حمل مشاهده شد.")
        el1 = self.driver.find_element('xpath', orders_create_check_total_weight)
        sleep(1)
        assert '' in el1.get_attribute('disabled')
        assert '0' in el1.get_attribute('value')
        print(" جمع وزن جرمی (kg) مشاهده شد.")
        el2 = self.driver.find_element('xpath', orders_create_check_total_v_weight)
        sleep(0.1)
        assert '' in el2.get_attribute('disabled')
        assert '0' in el2.get_attribute('value')
        print(" جمع وزن حجمی (kg) مشاهده شد.")
        el3 = self.driver.find_element('xpath', orders_create_check_total_c_weight)
        sleep(0.1)
        assert '' in el3.get_attribute('disabled')
        assert '0' in el3.get_attribute('value')
        print(" وزن قابل پرداخت سفارش (kg) مشاهده شد.")
        el4 = self.driver.find_element('xpath', orders_create_check_total_price)
        sleep(0.1)
        assert '' in el4.get_attribute('disabled')
        print(" ارزش کل مشاهده شد.")
        el5 = self.driver.find_element('xpath', orders_create_check_price_unit)
        sleep(0.1)
        assert '' in el5.get_attribute('disabled')
        print(" واحد ارزش مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_senders)
        print(" تعداد ارسال کنندگان مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_must_pay_before_transport)
        print(" هزینه قبل از حمل بین الملل پرداخت شود؟ مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_description)
        print(" توضیحات برای ارسال کنندگان مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_pay_in_china)
        print(" آیا هزینه در چین پرداخت میشود؟ مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_area_one)
        print(" آیا سفارش حوزه یک است؟ مشاهده شد.")

    def enter_orders_create_check_data_sender(self):
        assert self.driver.find_element('xpath', orders_create_information_sender_city)
        print(" شهر ارسال کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_name_select)
        print(" شخص ارسال کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_add)
        print(" اضافه کردن شخص ارسال کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_new_persons)
        print("ایجاد شخص مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_company)
        print(" شرکت ارسال کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_company_add)
        print(" اضافه کردن شرکت ارسال کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_sender_new_company)
        print(" ایجاد شرکت مشاهده شد.")

    def enter_orders_create_check_data_receiver(self):
        assert self.driver.find_element('xpath', orders_create_information_receiver_city)
        print(" شهر دریافت کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_receiver_name_select)
        print(" شخص دریافت کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_receiver_new_persons)
        print("ایجاد شخص مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_receiver_company)
        print(" شرکت دریافت کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_receiver_new_company)
        print(" ایجاد شرکت مشاهده شد.")

    def enter_orders_create_check_data_factor(self):
        assert self.driver.find_element('xpath', orders_create_information_sub_bill)
        print("صدور بارنامه فرعی مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_rasmi_transport)
        print("نوع پیش فاکتور حمل مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_rasmi_clearance)
        print("نوع پیش فاکتور ترخیص مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_need_clearance_inquery)
        print("استعلام ترخیص قبل از بارگیری نیاز است؟ مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_clearance_youan_invoice_request)
        print("درخواست صدور استعلام ترخیص یوانی مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_rasmi)
        print("نوع پیش فاکتور سایر خدمات کننده مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_invoice_to_container)
        print("پیش فاکتور به نام فرد مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_new_persons)
        print(" ایجاد شخص مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_company)
        print("پیش فاکتور به نام شرکت مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_factor_new_company)
        print(" ایجاد شرکت مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_goback)
        print(" تغییر خدمات مشاهده شد.")
        assert self.driver.find_element('xpath', orders_create_information_approve)
        print(" ادامه مشاهده شد.")

    def enter_orders_create_check_sender_city_btn(self):
        el1 = self.driver.find_element('xpath', orders_create_information_sender_city_btn).text
        self.driver.find_element('xpath', orders_create_information_sender_city_btn).click()
        el2 = self.driver.find_element('xpath', orders_create_information_sender_city_check_name).text
        print("############################################")
        assert el1 in el2
        print("شهر ارسال کننده انتخابی با شهر نمایشی برابر باشد.")

    def enter_orders_create_check_sender_city_btn2(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_city-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_city-n1-results']/li[1]").click()
        print("شهر ارسال کننده انتخاب شد.")

    def enter_orders_create_sender_person(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_p-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_p-n1-results']/li[1]").click()
        print("شخص ارسال کننده انتخاب شد.")

    def enter_orders_create_receiver_person(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_p-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_p-n1-results']/li[1]").click()
        print("شخص دریافت کننده انتخاب شد.")

    def enter_orders_create_sender_person2(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_p-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formsender_p-n1-results']/li[2]").click()
        print("شخص ارسال کننده انتخاب شد.")

    def enter_orders_create_receiver_person2(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_p-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_p-n1-results']/li[2]").click()
        print("شخص دریافت کننده انتخاب شد.")

    def enter_orders_create_check_receiver_city_btn(self):
        el1 = self.driver.find_element('xpath', orders_create_information_receiver_city_btn).text
        self.driver.find_element('xpath', orders_create_information_receiver_city_btn).click()
        el2 = self.driver.find_element('xpath', orders_create_information_receiver_city_check_name).text
        print("############################################")
        assert el1 in el2
        print("شهر دریافت کننده انتخابی با شهر نمایشی برابر باشد.")

    def enter_orders_create_check_receiver_city_btn2(self, text):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_city-n1-container']").click()
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "/html/body/span/span/span[1]/input", text)
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='select2-formreceiver_city-n1-results']/li[1]").click()
        print("شهر دریافت کننده انتخاب شد.")

    ################## create_order_product #########################

    def enter_click_create_order_product(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_create_order_product)

    def enter_orders_create_category_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_category_select)

    def enter_orders_create_category_select_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_category_select_option)

    def enter_orders_create_detailed_classification_of_goods(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_detailed_classification_of_goods)

    def enter_orders_create_detailed_classification_of_goods_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_detailed_classification_of_goods_option)

    def enter_orders_create_form_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_name, text)

    def enter_orders_create_form_name_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_name_en, text)

    def enter_orders_create_form_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_type)

    def enter_orders_create_form_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_type_option)

    def enter_orders_create_form_quantity(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_quantity)

    def enter_orders_create_form_quantity_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_quantity_option)

    def enter_orders_create_form_quantity_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_quantity_number, text)

    def enter_orders_create_form_one_weight(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_one_weight, text)

    def enter_orders_create_form_weight(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_weight, text)

    def enter_orders_create_form_length(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_length, text)

    def enter_orders_create_form_width(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_width, text)

    def enter_orders_create_form_height(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_height, text)

    def enter_orders_create_form_cbm(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_cbm, text)

    def enter_orders_create_form_v_weight(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_v_weight, text)

    def enter_orders_create_form_quantity_in_box(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_quantity_in_box, text)

    def enter_orders_create_form_price_unit(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_price_unit)

    def enter_orders_create_form_price_unit_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_price_unit_option)

    def enter_orders_create_form_price_unit_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_form_price_unit_option2)

    def enter_orders_create_form_one_price(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_one_price, text)

    def enter_orders_create_form_price(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_price, text)

    def enter_orders_create_HSCODE(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_HSCODE)

    def enter_orders_create_HSCODE_option(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_HSCODE_option)

    def enter_orders_create_form_part_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_part_number, text)

    def enter_orders_create_form_buy_url(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_buy_url, text)

    def enter_orders_create_form_text(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_text, text)

    def enter_orders_create_form_country(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', orders_create_form_country, text)

    def enter_orders_create_submit_information(self):
        wait_until_element_has_an_attribute(self, 'xpath', orders_create_submit_information)

    ################## create_order_product_check_form #########################

    def enter_create_order_product_check_form(self):
        if self.driver.find_elements('xpath',
                                     orders_create_category_select and orders_create_detailed_classification_of_goods
                                     and orders_create_form_name and orders_create_form_name_en
                                     and orders_create_form_type and orders_create_form_quantity
                                     and orders_create_form_quantity_number and orders_create_form_one_weight
                                     and orders_create_form_weight and orders_create_form_length
                                     and orders_create_form_width and orders_create_form_height
                                     and orders_create_form_cbm and orders_create_form_v_weight
                                     and orders_create_form_quantity_in_box and orders_create_form_price_unit
                                     and orders_create_form_one_price and orders_create_form_price
                                     and orders_create_HSCODE and orders_create_form_part_number
                                     and orders_create_form_buy_url and orders_create_form_text
                                     and orders_create_form_country and orders_create_submit_information
                                     ):
            print("Elements found")
        else:
            print("Elements not found")

    def enter_create_order_product_check_selection(self):
        el1 = len(self.driver.find_elements('xpath', create_order_product_check_input))
        el2 = len(self.driver.find_elements('xpath', create_order_product_check_select))
        el3 = len(self.driver.find_elements('xpath', orders_create_form_text))
        sum_el = el1 + el2 + el3
        # print(sum_el)
        assert sum_el == 25
        print("تعداد المان های در فرم بررسی شد.")

    def enter_create_order_product_check_passed(self):
        self.driver.refresh()
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "//*[@id='orderproductsholder']/div[3]/a")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        el1 = self.driver.find_element('xpath', orders_create_check_total_weight)
        el2 = self.driver.find_element('xpath', orders_create_check_total_v_weight)
        el3 = self.driver.find_element('xpath', orders_create_check_total_c_weight)
        el4 = self.driver.find_element('xpath', orders_create_check_total_price)
        el5 = self.driver.find_element('xpath', orders_create_check_price_unit)
        sleep(1)
        assert '1000' in el1.get_attribute('value')
        assert '0' in el2.get_attribute('value')
        assert '1000' in el3.get_attribute('value')
        assert '' in el4.get_attribute('value')
        assert 'rial' in el5.get_attribute('value')
        print("دیتای مشاهده شده درست می باشد.")

    def enter_create_order_product_check_passed2(self):
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', orders_create_information_type)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        el1 = self.driver.find_element('xpath', orders_create_check_total_weight)
        el2 = self.driver.find_element('xpath', orders_create_check_total_v_weight)
        el3 = self.driver.find_element('xpath', orders_create_check_total_c_weight)
        el4 = self.driver.find_element('xpath', orders_create_check_total_price)
        el5 = self.driver.find_element('xpath', orders_create_check_price_unit)
        assert '1040' in el1.get_attribute('value')
        assert '6.67' in el2.get_attribute('value')
        assert '1040' in el3.get_attribute('value')
        assert '800' in el4.get_attribute('value')
        assert 'rial' in el5.get_attribute('value')
        print("دیتای مشاهده شده درست می باشد.")

    def enter_create_order_product_check_all_data(self):
        el01 = self.driver.find_element('xpath', product_check_branch_representation).text
        el02 = self.driver.find_element('xpath', product_check_required_services).text
        el03 = self.driver.find_element('xpath', product_check_senders_city).text
        el04 = self.driver.find_element('xpath', product_check_receivers_city).text
        el05 = self.driver.find_element('xpath', product_check_transportation_invoice_type).text
        el06 = self.driver.find_element('xpath', product_check_type_of_shipping).text
        el07 = self.driver.find_element('xpath', product_check_clearance_invoice_type).text
        el08 = self.driver.find_element('xpath', product_check_clearance_inquiry_required).text
        el09 = self.driver.find_element('xpath', product_check_other_services_invoice_type).text
        el10 = self.driver.find_element('xpath', product_check_total_actual_weight).text
        el11 = self.driver.find_element('xpath', product_check_total_volumetric_weight).text
        el12 = self.driver.find_element('xpath', product_check_total_chargeable_weight).text
        el13 = self.driver.find_element('xpath', product_check_total_value).text
        el14 = self.driver.find_element('xpath', product_check_unit_of_value).text
        assert el01 == "ایران - تهران |تهران - نمایندگی مرکزی"
        assert el02 == "حمل بین المللی / ترخیص"
        assert el03 == "Shenzhen - China"
        assert el04 == "Tehran - Iran"
        assert el05 == "رسمی"
        assert el06 == "هوایی"
        assert el07 == "رسمی"
        assert el08 == "بله"
        assert el09 == "رسمی"
        assert el10 == "1040"
        assert el11 == "6.67"
        assert el12 == "1040"
        assert el13 == "800"
        assert el14 == "ریال"
        print("بازبینی نهایی انجام و درستی اطلاعات یررسی شد.")

    def enter_create_order_product_check_all_data2(self):
        el15 = self.driver.find_element('xpath', "//*[@id='review']/div[1]/p").text
        el01 = self.driver.find_element('xpath', product_check_branch_representation).text
        el02 = self.driver.find_element('xpath', product_check_required_services).text
        assert self.driver.find_element('xpath', "//*[@id='review']/div[2]/div/form/div[4]/div/div").text == "Melika Kaboli ملیکا کابلی"
        el03 = self.driver.find_element('xpath', product_check_senders_city).text
        assert self.driver.find_element('xpath', "//*[@id='review']/div[2]/div/form/div[7]/div/div").text == "Melika Kaboli ملیکا کابلی"
        assert self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[22]/div/div").text == "6.67"
        el04 = self.driver.find_element('xpath', product_check_receivers_city).text
        el05 = self.driver.find_element('xpath', product_check_transportation_invoice_type).text
        el06 = self.driver.find_element('xpath', product_check_type_of_shipping).text
        el08 = self.driver.find_element('xpath', product_check_clearance_inquiry_required).text
        el09 = self.driver.find_element('xpath', product_check_other_services_invoice_type).text
        el10 = self.driver.find_element('xpath', product_check_total_actual_weight).text
        el11 = self.driver.find_element('xpath', product_check_total_volumetric_weight).text
        assert el15 == "سفارش چین به دبی است تیک ترخیص برداشته شد!"
        assert el01 == "ایران - تهران |تهران - نمایندگی مرکزی"
        assert el02 == "حمل بین المللی"
        assert el03 == "Shenzhen - China"
        assert el04 == "Dubai - United Arab Emirates"
        assert el05 == "غیر رسمی"
        assert el06 == "هوایی"
        assert el08 == "1040"
        assert el09 == "1040"
        assert el10 == "800"
        assert el11 == "ریال"
        print("بازبینی نهایی انجام و درستی اطلاعات یررسی شد.")

    def enter_create_order_product_check_chain_iran_all_data2(self):
        # el15 = self.driver.find_element('xpath', "//*[@id='review']/div[1]/p").text
        el01 = self.driver.find_element('xpath', product_check_branch_representation).text
        el02 = self.driver.find_element('xpath', product_check_required_services).text
        assert self.driver.find_element('xpath', "//*[@id='review']/div[1]/div/form/div[4]/div/div").text == "Melika Kaboli ملیکا کابلی"
        el03 = self.driver.find_element('xpath', product_check_senders_city).text
        assert self.driver.find_element('xpath', "//*[@id='review']/div[1]/div/form/div[7]/div/div").text == "Melika Kaboli ملیکا کابلی"
        assert self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[25]/div/div").text == "6.67"
        el04 = self.driver.find_element('xpath', product_check_receivers_city).text
        el05 = self.driver.find_element('xpath', product_check_transportation_invoice_type).text
        el06 = self.driver.find_element('xpath', product_check_type_of_shipping).text
        el08 = self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[24]/div/div").text
        el09 = self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[25]/div/div").text
        el10 = self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[27]/div/div").text
        el11 = self.driver.find_element('xpath', "//*[@id='review']/div/div/form/div[28]/div/div").text
        # assert el15 == "سفارش چین به دبی است تیک ترخیص برداشته شد!"
        assert el01 == "ایران - تهران |تهران - نمایندگی مرکزی"
        assert el02 == "حمل بین المللی / ترخیص"
        assert el03 == "Shenzhen - China"
        assert el04 == "Tehran - Iran"
        assert el05 == "غیر رسمی"
        assert el06 == "هوایی"
        assert el08 == "1040"
        assert el09 == "6.67"
        assert el10 == "800"
        assert el11 == "ریال"
        print("بازبینی نهایی انجام و درستی اطلاعات یررسی شد.")

    def enter_product_final_order_confirmation(self):
        wait_until_element_has_an_attribute(self, 'xpath', product_final_order_confirmation)

    def enter_product_check_color_checking_the_order(self):
        el1 = self.driver.find_element('xpath', product_checking_the_order)
        sleep(1)
        assert 'bg-orange-active' in el1.get_attribute('class')
        print("رنگ بررسی سفارش نارنچی می باشد.")

    def enter_product_click_checking_the_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', product_checking_the_order)

    def enter_product_details_of_this_order_are_approved(self):
        sleep(.2)
        scrolled1 = self.driver.find_element('xpath', product_details_of_this_order_are_approved)
        sleep(0.7)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', product_details_of_this_order_are_approved)

    def enter_product_error_details_of_this_order_are_approved(self):
        assert self.driver.find_element('xpath', product_error_details_of_this_order_are_approved)
        el = self.driver.find_element('xpath', product_error_details_of_this_order_are_approved).text
        print(el)

    def enter_product_click_edit_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', product_click_edit_order)

    def enter_box_order_details_check_color_btn(self):
        el01 = self.driver.find_element('xpath', box_order_details_check_color_checking_order)
        el02 = self.driver.find_element('xpath', box_order_details_check_color_checking_negotiations)
        el03 = self.driver.find_element('xpath', box_order_details_check_color_checking_barcode_maker)
        el04 = self.driver.find_element('xpath', box_order_details_check_color_checking_order_files)
        el05 = self.driver.find_element('xpath', box_order_details_check_color_checking_Shipping_Cost)
        el06 = self.driver.find_element('xpath', box_order_details_check_color_checking_clearance_inquiry)
        el07 = self.driver.find_element('xpath', box_order_details_check_color_checking_other_inquiries)
        el08 = self.driver.find_element('xpath', box_order_details_check_color_checking_invoice)
        el09 = self.driver.find_element('xpath', box_order_details_check_color_checking_payment)
        el10 = self.driver.find_element('xpath', box_order_details_check_color_checking_cargo_pickup)
        el11 = self.driver.find_element('xpath', box_order_details_check_color_checking_Loaded_goods)
        el12 = self.driver.find_element('xpath', box_order_details_check_color_checking_order_accounting)
        el13 = self.driver.find_element('xpath', box_order_details_check_color_checking_invoice_discount)
        el14 = self.driver.find_element('xpath', box_order_details_check_color_checking_order_changes)
        el15 = self.driver.find_element('xpath', box_order_details_check_color_checking_order_information_in_arian)
        el16 = self.driver.find_element('xpath', box_order_details_check_color_checking_general_status_of_cargo)
        assert 'info-box bg-green-active' in el01.get_attribute('class')
        assert 'info-box bg-light-blue' in el02.get_attribute('class')
        assert 'info-box bg-light-blue' in el03.get_attribute('class')
        assert 'info-box bg-red-active' in el04.get_attribute('class')
        assert 'info-box bg-light-blue' in el05.get_attribute('class')
        assert 'info-box bg-light-blue' in el06.get_attribute('class')
        assert 'info-box bg-light-blue' in el07.get_attribute('class')
        assert 'info-box bg-light-blue' in el08.get_attribute('class')
        assert 'info-box bg-light-blue' in el09.get_attribute('class')
        assert 'info-box bg-navy' in el10.get_attribute('class')
        assert 'info-box bg-light-blue' in el11.get_attribute('class')
        assert 'info-box bg-light-blue' in el12.get_attribute('class')
        assert 'info-box bg-light-blue' in el13.get_attribute('class')
        assert 'info-box bg-light-blue' in el14.get_attribute('class')
        assert 'info-box bg-light-blue' in el15.get_attribute('class')
        assert 'info-box bg-light-blue' in el16.get_attribute('class')
        print("رنگ دکمه بررسی سفارش سبز." + "\n", "رنگ دکمه فایل های سفارش قرمز." + "\n",
              "رنگ دکمه بارگیری کالا سورمه ای." + "\n", "مابقی رنگ ها آبی می باشد.")

    def enter_box_order_details_check_log(self):
        el1 = self.driver.find_element('xpath', box_order_details_check_log1).text
        el2 = self.driver.find_element('xpath', box_order_details_check_log2).text
        el3 = self.driver.find_element('xpath', box_order_details_check_status).text
        assert 'زهرا پیروز Zahra Pirooz' in el1
        assert 'جزئیات سفارش مورد تایید قرار گرفت' in el2
        assert 'در حال انجام' in el3
        print("لاگ تغییر وضعیت سفارش درست می باشد." + "\n" + "وضعیت سفارش در حال انجام می باشد.")
        # print(el1 + "\n" + el2 + "\n" + el3 + "\n")

    def enter_product_check_edit_order(self):
        assert self.driver.find_element('xpath', product_click_edit_order)
        print("دکمه ویرایش سفارش مشاهده شد. ")

    def enter_click_box_clearance_inquiry(self):
        self.driver.find_element('xpath', box_order_details_check_color_checking_clearance_inquiry).click()

    def enter_check_box_clearance_inquery_check(self):
        el = len(self.driver.find_elements('xpath', box_clearance_inquery_check))
        # print(el)
        assert el == 3
        print("اطلاعات تحویل قبض به درستی نمایش داده می شود. ")

    def enter_menu_search(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_menu_search)

    def enter_menu_search_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', customer_manager_menu_search_name, text)

    def enter_menu_search_option(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_menu_search_option)

    def enter_search_tn(self, text):
        sleep(0.5)
        self.driver.find_element('xpath', "/html/body/div[1]/aside/section/div[2]/span[1]/span[1]/span/span[1]").click()
        sleep(0.5)
        self.driver.find_element('xpath', "/html/body/span/span/span[1]/input").send_keys(text)
        sleep(2)
        self.driver.find_element('xpath', "/html/body/span/span/span[2]/ul/li").click()

    def enter_click_box_invoices(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a")

    def enter_click_box_invoices2(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_invoices)

    def enter_order_click_box_invoices(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a")

    def enter_click_box_op(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a")

    def enter_check_op_in_warehouses(self):
        sleep(1)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[3]/a[1]")
        b = self.driver.find_element('xpath', "//table/tbody/tr[2]/td[3]/a[1]")
        assert 'btn btn-sm btn-block' in a.get_attribute('class')
        assert 'btn btn-sm btn-block' in b.get_attribute('class')
        print("موقعیت به انبار دبی تغییر کرد. ")

    def enter_check_admin_orders_doing_open(self):
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 17
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/a")) == 3
        print("تعداد به درستی مشاهده شد. ")
        assert "بررسی سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        print("بررسی سفارش", "به درستی مشاهده شد.")
        assert "مذاکرات" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a").text)
        print("مذاکرات", "به درستی مشاهده شد.")
        assert "بارکد ساز" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        print("بارکد ساز", "به درستی مشاهده شد.")
        assert "فایل های سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        print("فایل های سفارش", "به درستی مشاهده شد.")
        assert "استعلام حمل" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        print("استعلام حمل", "به درستی مشاهده شد.")
        assert "استعلام ترخیص" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        print("استعلام ترخیص", "به درستی مشاهده شد.")
        assert "سایر استعلام ها" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a").text)
        print("سایر استعلام ها", "به درستی مشاهده شد.")
        assert "پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a").text)
        print("پیش فاکتور", "به درستی مشاهده شد.")
        assert "پرداخت" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a").text)
        print("پرداخت", "به درستی مشاهده شد.")
        assert "بارگیری کالا" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a").text)
        print("بارگیری کالا", "به درستی مشاهده شد.")
        assert "کالاهای بارگیری شده" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[13]/a").text)
        print("کالاهای بارگیری شده", "به درستی مشاهده شد.")
        assert "تراکنش های سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[14]/a").text)
        print("تراکنش های سفارش", "به درستی مشاهده شد.")
        assert "تخفیف پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[15]/a").text)
        print("تخفیف پیش فاکتور", "به درستی مشاهده شد.")
        assert "تغییرات سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[16]/a").text)
        print("تغییرات سفارش", "به درستی مشاهده شد.")
        assert "اطلاعات سفارش در آرین" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[17]/a").text)
        print("اطلاعات سفارش در آرین", "به درستی مشاهده شد.")
        assert "هزینه ها و درآمدها" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[18]/a").text)
        print("هزینه ها و درآمدها", "به درستی مشاهده شد.")
        assert "وضعیت کلی بار" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[19]/a").text)
        print("وضعیت کلی بار", "به درستی مشاهده شد.")
        print("..................................................")

    def enter_check_account_chain_orders_doing_open(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 15
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/a")) == 3
        print("تعداد به درستی مشاهده شد. ")
        assert "Checking the order" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        print("Checking the order", "به درستی مشاهده شد.")
        assert "Negotiations" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a").text)
        print("Negotiations", "به درستی مشاهده شد.")
        assert "Barcode maker" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        print("Barcode maker", "به درستی مشاهده شد.")
        assert "Order files" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        print("Order files", "به درستی مشاهده شد.")
        assert "Shipping Cost" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        print("Shipping Cost", "به درستی مشاهده شد.")
        assert "Clearance inquiry" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        print("Clearance inquiry", "به درستی مشاهده شد.")
        assert "Other inquiries" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a").text)
        print("Other inquiries", "به درستی مشاهده شد.")
        assert "Invoice" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a").text)
        print("Invoice", "به درستی مشاهده شد.")
        assert "Payment" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a").text)
        print("Payment", "به درستی مشاهده شد.")
        assert "Cargo pickup" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a").text)
        print("Cargo pickup", "به درستی مشاهده شد.")
        assert "Loaded goods" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[13]/a").text)
        print("Loaded goods", "به درستی مشاهده شد.")
        # assert "Order Accounting" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[14]/a").text)
        # print("Order Accounting", "به درستی مشاهده شد.")
        assert "invoice discount" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[15]/a").text)
        print("invoice discount", "به درستی مشاهده شد.")
        assert "Order changes" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[16]/a").text)
        print("Order changes", "به درستی مشاهده شد.")
        assert "General status of cargo" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[17]/a").text)
        print("General status of cargo", "به درستی مشاهده شد.")
        print("..................................................")

    def enter_check_customer_manager_orders_doing_open(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 16
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/a")) == 3
        print("تعداد به درستی مشاهده شد. ")
        print(self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        assert "بررسی سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        print("بررسی سفارش", "به درستی مشاهده شد.")
        assert "مذاکرات" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a").text)
        print("مذاکرات", "به درستی مشاهده شد.")
        assert "بارکد ساز" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        print("بارکد ساز", "به درستی مشاهده شد.")
        assert "فایل های سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        print("فایل های سفارش", "به درستی مشاهده شد.")
        assert "استعلام حمل" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        print("استعلام حمل", "به درستی مشاهده شد.")
        assert "استعلام ترخیص" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        print("استعلام ترخیص", "به درستی مشاهده شد.")
        assert "سایر استعلام ها" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a").text)
        print("سایر استعلام ها", "به درستی مشاهده شد.")
        assert "پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a").text)
        print("پیش فاکتور", "به درستی مشاهده شد.")
        assert "پرداخت" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a").text)
        print("پرداخت", "به درستی مشاهده شد.")
        assert "بارگیری کالا" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a").text)
        print("بارگیری کالا", "به درستی مشاهده شد.")
        assert "کالاهای بارگیری شده" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[13]/a").text)
        print("کالاهای بارگیری شده", "به درستی مشاهده شد.")
        assert "تراکنش های سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[14]/a").text)
        print("تراکنش های سفارش", "به درستی مشاهده شد.")
        assert "تخفیف پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[15]/a").text)
        print("تخفیف پیش فاکتور", "به درستی مشاهده شد.")
        assert "تغییرات سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[16]/a").text)
        print("تغییرات سفارش", "به درستی مشاهده شد.")
        assert "اطلاعات سفارش در آرین" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[17]/a").text)
        print("اطلاعات سفارش در آرین", "به درستی مشاهده شد.")
        assert "وضعیت کلی بار" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[18]/a").text)
        # print("هزینه ها و درآمدها", "به درستی مشاهده شد.")
        print("وضعیت کلی بار", "به درستی مشاهده شد.")
        # assert "وضعیت کلی بار" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[19]/a").text)
        print("..................................................")

    def enter_check_delivery_manager_orders_doing_open(self):
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 15
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 6
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/a")) == 3
        print("تعداد به درستی مشاهده شد. ")
        print(self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        assert "بررسی سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        print("بررسی سفارش", "به درستی مشاهده شد.")
        assert "مذاکرات" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a").text)
        print("مذاکرات", "به درستی مشاهده شد.")
        assert "پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        print("پیش فاکتور", "به درستی مشاهده شد.")
        # assert "بارکد ساز" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        # print("بارکد ساز", "به درستی مشاهده شد.")
        # assert "فایل های سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        # print("فایل های سفارش", "به درستی مشاهده شد.")
        # assert "استعلام حمل" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        # print("استعلام حمل", "به درستی مشاهده شد.")
        # assert "استعلام ترخیص" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        # print("استعلام ترخیص", "به درستی مشاهده شد.")
        # assert "سایر استعلام ها" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a").text)
        # print("سایر استعلام ها", "به درستی مشاهده شد.")
        # assert "پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a").text)
        # print("پیش فاکتور", "به درستی مشاهده شد.")
        # assert "پرداخت" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a").text)
        assert "پرداخت" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        print("پرداخت", "به درستی مشاهده شد.")
        # assert "بارگیری کالا" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a").text)
        assert "بارگیری کالا" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        print("بارگیری کالا", "به درستی مشاهده شد.")
        # assert "کالاهای بارگیری شده" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[13]/a").text)
        assert "کالاهای بارگیری شده" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        print("کالاهای بارگیری شده", "به درستی مشاهده شد.")
        # assert "تراکنش های سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[14]/a").text)
        # print("تراکنش های سفارش", "به درستی مشاهده شد.")
        # assert "تخفیف پیش فاکتور" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[15]/a").text)
        # print("تخفیف پیش فاکتور", "به درستی مشاهده شد.")
        # assert "تغییرات سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[16]/a").text)
        # print("تغییرات سفارش", "به درستی مشاهده شد.")
        # assert "وضعیت کلی بار" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[17]/a").text)
        # print("وضعیت کلی بار", "به درستی مشاهده شد.")
        print("..................................................")

    def enter_check_clearance_manager_orders_doing_open(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/a")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/a")) == 3
        print("تعداد به درستی مشاهده شد. ")
        print(self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        assert "بررسی سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/a").text)
        print("بررسی سفارش", "به درستی مشاهده شد.")
        assert "مذاکرات" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a").text)
        print("مذاکرات", "به درستی مشاهده شد.")
        assert "فایل های سفارش" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/a").text)
        print("فایل های سفارش", "به درستی مشاهده شد.")
        assert "استعلام حمل" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/a").text)
        print("استعلام حمل", "به درستی مشاهده شد.")
        assert "استعلام ترخیص" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/a").text)
        print("استعلام ترخیص", "به درستی مشاهده شد.")
        assert "سایر استعلام ها" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/a").text)
        print("سایر استعلام ها", "به درستی مشاهده شد.")
        assert "پیش فاکتور" in  (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[9]/a").text)
        print("پیش فاکتور", "به درستی مشاهده شد.")
        assert "کالاهای بارگیری شده" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[10]/a").text)
        print("کالاهای بارگیری شده", "به درستی مشاهده شد.")
        assert "تغییرات سفارش" in (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a").text)
        print("تغییرات سفارش", "به درستی مشاهده شد.")
        print("..................................................")

    def enter_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 17
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 10
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 37
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//input")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 1
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 17
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 36
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 16
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 35
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 15
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 27
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_marketing_manager_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 6
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 32
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 15
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 32
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]//input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "Order type"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "Required services"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "Type of shipping"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "Transportation invoice type"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "Sub-Bill of Lading Issuance"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "Clearance inquiry required?"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "Clearance invoice type"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "Other services invoice type"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "Total actual weight (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "Total volumetric weight (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "Total chargeable weight (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "Inco terms"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "Total value"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "Unit of value"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "Order owner"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "Invoice to person"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "Invoice to company"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "Sender (person)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "Sender (company)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "Receiver (person)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "Receiver (company)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "Sender's city"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "Receiver's city"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "Order Registration Date"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "Creator"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "Is the order from China registered?"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "Description"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "Customer manager"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "coordinator"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "Destination coordinator"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "Branch | Representation"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "attached file"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_clearance_manager_checking_the_order(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div/a")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 26
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist100']/div[1]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist2']/div[1]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='oplist1']/div[1]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='orderstatus']//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div/div[1]//a")) == 0
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[1]/div/a").text) == "ویرایش سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[1]/div/div/label/span").text) == "نوع سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[2]/div/div/label/span").text) == "خدمات موردنیاز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[3]/div/div/label/span").text) == "نوع حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[4]/div/div/label/span").text) == "نوع پیش فاکتور حمل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[5]/div/div/label/span").text) == "صدور بارنامه فرعی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[6]/div/div/label/span").text) == "استعلام ترخیص قبل از بارگیری نیاز است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[7]/div/div/label/span").text) == "نوع پیش فاکتور ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[8]/div/div/label/span").text) == "نوع پیش فاکتور سایر خدمات"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[9]/div/div/label/span").text) == "جمع وزن جرمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[10]/div/div/label/span").text) == "جمع وزن حجمی (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[11]/div/div/label/span").text) == "وزن قابل پرداخت سفارش (kg)"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[12]/div/div/label/span").text) == "اینکو ترمز"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[13]/div/div/label/span").text) == "ارزش کل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[14]/div/div/label/span").text) == "واحد ارزش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[15]/div/div/label/span").text) == "صاحب سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[16]/div/div/label/span").text) == "پیش فاکتور به نام فرد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[17]/div/div/label/span").text) == "پیش فاکتور به نام شرکت"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[18]/div/div/label/span").text) == "شخص ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[19]/div/div/label/span").text) == "شرکت ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/label/span").text) == "شخص دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[21]/div/div/label/span").text) == "شرکت دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[22]/div/div/label/span").text) == "شهر ارسال کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/label/span").text) == "شهر دریافت کننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[24]/label/span").text) == "تاریخ ثبت سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/label/span").text) == "ایجادکننده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[26]/div/div/label/span").text) == "آیا سفارش از چین ثبت شده است؟"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[27]/div/div/label/span").text) == "توضیحات"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[28]/div/div/label/span").text) == "مدیر مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[29]/div/div/label/span").text) == "هماهنگ کننده مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[30]/div/div/label/span").text) == "هماهنگ کننده مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[31]/div/div/label/span").text) == "شعبه | نمایندگی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[32]/div/div/label/span").text) == "فایل پیوست"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_check_box_chat(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) >= 22
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[2]/div/div/span/span[1]/span")
        print("مخاطب* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext-n1']")
        print("متن* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[5]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_box_chat(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 20
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[2]/div/div/span/span[1]/span")
        print("مخاطب* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext-n1']")
        print("متن* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[5]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_marketing_check_box_chat(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 25
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[2]/div/div/span/span[1]/span")
        print("مخاطب* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext-n1']")
        print("متن* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[5]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_chat(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 21
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[2]/div/div/span/span[1]/span")
        print("مخاطب* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext-n1']")
        print("متن* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[5]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_clearance_manager_check_box_chat(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 4
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 19
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[2]/div/div/span/span[1]/span")
        print("مخاطب* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext-n1']")
        print("متن* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxChatForm']/div/div/form/div[5]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_click_box_barcode(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_barcode)

    def enter_click_box_order_obligation(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_order_obligation)

    def enter_check_box_order_obligation(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) >= 20
        assert self.driver.find_element('xpath', "//*[@id='formtitle']")
        print("عنوان فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formverified']")
        print("تایید شده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/div[2]/form/div[4]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_order_obligation(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 21
        assert self.driver.find_element('xpath', "//*[@id='formtitle']")
        print("عنوان فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/div[2]/form/div[3]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_check_box_order_obligation(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 22
        assert self.driver.find_element('xpath', "//*[@id='formtitle']")
        print("عنوان فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/div[2]/form/div[3]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_order_obligation(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 20
        assert self.driver.find_element('xpath', "//*[@id='formtitle']")
        print("عنوان فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/div[2]/form/div[3]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_clearance_manager_check_box_order_obligation(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 8
        assert len(self.driver.find_elements('xpath', "//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']//a")) == 14
        assert self.driver.find_element('xpath', "//*[@id='formtitle']")
        print("عنوان فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfile']")
        print("فایل* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/div[2]/form/div[3]/div/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_transporter_inquery(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_click_box_transporter_inquery)

    def enter_check_box_transporter_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]//input")) == 17
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='reasons']")
        print("اعلام نقص مدرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='send-problem']")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد ارز* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formperkilo']")
        print(" تخفیف در هر کیلو* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtransport_priceunit']")
        print(" واحد ارز فاکتور حمل " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/div/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='transportForm']/div/b/div[2]/div/div/div/div[1]")
        print(" همکار*" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice_approved']")
        print(" قیمت مصوب " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice']")
        print(" قیمت* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice_per_kilo']")
        print(" قیمت هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit-n1']")
        print(" واحد " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formcomment']")
        print(" توضیحات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fullinvoice']")
        print(" صدور پیش فاکتور برای این استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='transportForm']/div/b/div[11]/a")
        print("  وارد کردن قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpercent']")
        print(" درصد سود " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formoffer_price']")
        print(" قیمت اعلامی به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formvat_rate-n1']")
        print(" ضریب مالیات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtorialrate']")
        print(" نرخ تبدیل به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfinal_price_per_kilo']")
        print(" قیمت نهایی هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtotal_price']")
        print(" قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formact_date']")
        print("تاریخ موثر " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='transportForm']/b/button")
        print(" ثبت اطلاعات " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_transporter_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//button")) == 1
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد ارز* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formperkilo']")
        print(" تخفیف در هر کیلو* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtransport_priceunit']")
        print(" واحد ارز فاکتور حمل " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/div/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_transporter_inquery2(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//input")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد ارز* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formperkilo']")
        print(" تخفیف در هر کیلو* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtransport_priceunit']")
        print(" واحد ارز فاکتور حمل " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[8]/div/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_transporter_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//input")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[6]//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]//button")) == 1
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد ارز* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formperkilo']")
        print(" تخفیف در هر کیلو* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtransport_priceunit']")
        print(" واحد ارز فاکتور حمل " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div[2]/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[7]/div/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_click_box_clearance_inquery(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_clearance_inquery)

    def enter_check_box_clearance_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) ==3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div/div")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[2]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//input")) == 18
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//a")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[2]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[2]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]//button")) == 1
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//input")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[6]//input")) == 2
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a")
        print("لیست کالاهای بارگیری شده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[2]/div[2]/a")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[3]/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[4]/div/div/span/span[1]/span")
        print(" ترخیص کار* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formclearance_type']")
        print(" نوع ترخیص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice']")
        print(" قیمت* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice_per_kilo']")
        print(" قیمت به ازای هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formcomment']")
        print(" توضیحات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='forminquiry_documents']")
        print(" مدارک استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fullinvoice']")
        print(" صدور پیش فاکتور برای این استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[15]/a")
        print("  وارد کردن قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpercent']")
        print(" درصد سود " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formoffer_price']")
        print(" قیمت اعلامی به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formvat_rate']")
        print(" ضریب مالیات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtorialrate']")
        print(" نرخ تبدیل به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfinal_price_per_kilo']")
        print(" قیمت نهایی هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtotal_price']")
        print(" قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formact_date']")
        print("تاریخ موثر " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/button")
        print("ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='reasons']")
        print(" اعلام نقص مدرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='send-problem']")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='des_evaluator_manifest']")
        print(" یادداشت پیش ارزیابی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/button")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/div[2]/form/div[1]/input")
        print(" کد استعلام ترخیص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/div[2]/form/div[2]/div/button")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[1]/select")
        print(" درصد تعرفه " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[2]/button")
        print(" ذخیره " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formclearance_buylink']")
        print(" لینک خرید گمرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[6]/form/div/div[2]/button")
        print(" ذخیره " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_check_box_clearance_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) ==3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[2]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//input")) == 18
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[2]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[2]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[6]//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[6]//input")) == 0
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a")
        print("لیست کالاهای بارگیری شده " + " + ")
        # assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[2]/div[2]/a")
        # print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[1]/div[2]/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[4]/div/div/span/span[1]/span")
        print(" ترخیص کار* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formclearance_type']")
        print(" نوع ترخیص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice']")
        print(" قیمت* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice_per_kilo']")
        print(" قیمت به ازای هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formcomment']")
        print(" توضیحات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='forminquiry_documents']")
        print(" مدارک استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fullinvoice']")
        print(" صدور پیش فاکتور برای این استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[14]/a")
        print("  وارد کردن قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpercent']")
        print(" درصد سود " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formoffer_price']")
        print(" قیمت اعلامی به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formvat_rate']")
        print(" ضریب مالیات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtorialrate']")
        print(" نرخ تبدیل به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfinal_price_per_kilo']")
        print(" قیمت نهایی هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtotal_price']")
        print(" قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formact_date']")
        print("تاریخ موثر " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/button")
        print("ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='reasons']")
        print(" اعلام نقص مدرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='send-problem']")
        print(" بروزرسانی " + " + ")
        # assert self.driver.find_element('xpath', "//*[@id='des_evaluator_manifest']")
        # print(" یادداشت پیش ارزیابی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/button")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div//div[2]/form/div/input")
        print(" کد استعلام ترخیص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/button")
        print(" بروزرسانی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/form/div/div[1]/select")
        print(" درصد تعرفه " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/form/div/div[2]/button")
        print(" ذخیره " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formclearance_buylink']")
        print(" لینک خرید گمرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[2]/button")
        print(" ذخیره " + " : به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_clearance_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//select")) == 0
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 5
        # assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 10
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0

    def enter_admin_click_box_other_service_inquery(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_check_order_invoice)

    def enter_check_box_other_service_inquery(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//input")) == 13
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//textarea")) == 1
        assert self.driver.find_element('xpath', "//*[@id='fastinvoice']/div/div[1]/div/div[2]/div")
        print(" سوییچ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formotherinquery_type']")
        print(" نوع پیش فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice']")
        print(" قیمت* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print(" واحد " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtext']")
        print(" توضیحات خدمت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formattachment']")
        print(" پیوست فایل " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fullinvoice']")
        print(" صدور پیش فاکتور برای این استعلام " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fastinvoice']/div/div[2]/form/div/a")
        print("  وارد کردن قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpercent']")
        print(" درصد سود " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formoffer_price']")
        print(" قیمت اعلامی به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formvat_rate']")
        print(" ضریب مالیات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtorialrate']")
        print(" نرخ تبدیل به ریال " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formfinal_price_per_kilo']")
        print(" قیمت نهایی هر کیلو " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formtotal_price']")
        print(" قیمت نهایی " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formact_date']")
        print("تاریخ موثر " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='fastinvoice']/div/div[2]/form/button")
        print("ثبت اطلاعات " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_invoices(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_box_invoices)

    def enter_check_box_invoices(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 30
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert 'برای تایید حمل فاکتور های حمل بین المللی و ترخیص باید تایید شوند' == (self.driver.find_element('xpath', "//*[@id='msg-holder']").text)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='form_approvals_text']")
        print("تاییدیه بارگیری کالا توسط گمرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[1]/a")
        print("انتخاب فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام فرد" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[2]/a")
        print(" ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[2]/a")
        print(" ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[3]/button")
        print("تغییر صاحب پیش فاکتور " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_invoices(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 25
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 7
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert 'برای تایید حمل فاکتور های حمل بین المللی و ترخیص باید تایید شوند' == (self.driver.find_element('xpath', "//*[@id='msg-holder']").text)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='form_approvals_text']")
        print("تاییدیه بارگیری کالا توسط گمرک " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[1]/a")
        print("انتخاب فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام فرد" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[2]/a")
        print(" ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[2]/a")
        print(" ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[3]/button")
        print("تغییر صاحب پیش فاکتور " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_check_box_invoices(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 25
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 6
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert 'شما دسترسی ایجاد برای حمل بین الملل را ندارید' == (self.driver.find_element('xpath', "//*[@id='msg-holder']").text)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        # assert self.driver.find_element('xpath', "//*[@id='form_approvals_text']")
        # print("تاییدیه بارگیری کالا توسط گمرک " + " + ")
        # assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        # print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[1]/a")
        print("انتخاب فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام فرد" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[2]/a")
        print(" ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[2]/a")
        print(" ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[3]/button")
        print("تغییر صاحب پیش فاکتور " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_box_invoices(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 25
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 6
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert 'In order to validate the invoices, invoices must be confirmed' == (self.driver.find_element('xpath', "//*[@id='msg-holder']").text)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[1]/a")
        print("انتخاب فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام فرد" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[2]/a")
        print(" ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[2]/a")
        print(" ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[3]/button")
        print("تغییر صاحب پیش فاکتور " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_invoices(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 24
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div")) == 6
        assert len(self.driver.find_elements('xpath', "//table/tbody/tr")) == 1
        assert 'شما دسترسی ایجاد برای حمل بین الملل را ندارید' == (self.driver.find_element('xpath', "//*[@id='msg-holder']").text)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]//button")) == 2
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[1]/a")
        print("انتخاب فاکتور " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام فرد" + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[1]/div[2]/a")
        print(" ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        print("پیش فاکتور به نام شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[2]/div[2]/a")
        print(" ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/div/div[2]/form/div[3]/button")
        print("تغییر صاحب پیش فاکتور " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_payment(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_check_order_cargo_pickup)

    def enter_check_box_payment(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[1]//a")) == 17
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[3]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[4]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[5]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[6]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//button")) == 1
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_payment(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[1]//a")) == 12
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[3]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[4]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[5]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[6]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//button")) == 1
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_payment(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div")) == 9
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[1]//a")) == 11
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[3]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[4]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[5]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[6]/div/div[2]/div[2]/div")) == 8
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='paymentList']/div[9]//button")) == 1
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_order_loaded_goods(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_check_order_loaded_goods)

    def enter_check_order_loaded_goods(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//button")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//a")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//button")) == 1
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/div/div/select")
        print(" انبار بارگیری کننده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='form_pickup_text']")
        print("توضیحات لازم را درباره این تاییدیه وارد نمایید " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formhas_tax_return']")
        print(" آیا بازگشت مالیاتی دارد؟ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='internal_carriage']/div/form/button")
        print(" ثبت اطلاعات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[1]/button")
        print(" + " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[1]/div[1]/span/span[1]/span")
        print("شخص ارسال کننده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[1]/div[3]/a")
        print("  ایجاد شخص " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[3]/button")
        print(" + " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[3]/div[1]/span/span[1]/span")
        print(" شرکت ارسال کننده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/div/div[3]/div[3]/div[3]/a")
        print("  ایجاد شرکت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/form/button")
        print("ثبت اطلاعات " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_order_loaded_goods(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//button")) == 0
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/div/div/select")
        print(" انبار بارگیری کننده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='form_pickup_text']")
        print("توضیحات لازم را درباره این تاییدیه وارد نمایید " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formhas_tax_return']")
        print(" آیا بازگشت مالیاتی دارد؟ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='internal_carriage']/div/form/button")
        print(" ثبت اطلاعات " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_order_loaded_goods(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//a")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]//button")) == 0
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/div/div/select")
        print(" انبار بارگیری کننده " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='form_pickup_text']")
        print("توضیحات لازم را درباره این تاییدیه وارد نمایید " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        print("ارسال دستور بارگیری " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formhas_tax_return']")
        print(" آیا بازگشت مالیاتی دارد؟ " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='internal_carriage']/div/form/button")
        print(" ثبت اطلاعات " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_op(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_op)

    def enter_check_box_op(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']/div")) == 7
        assert len(self.driver.find_elements('xpath', "//*[@id='fatherdiv']/div")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']//a")) == 4
        assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[7]/div[1]/div[1]/a")
        print("  ثبت ارزش کالا " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[7]/div[1]/div[1]/div")
        print("تغییر اطلاعات بارگیری " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_op(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='fatherdiv']/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']//a")) == 1
        # assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[6]/div[1]/div[1]/a")
        # print("  ثبت ارزش کالا " + " + ")
        # assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[6]/div[1]/div[1]/div")
        # print("تغییر اطلاعات بارگیری " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_check_box_op(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='fatherdiv']/div")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']//a")) == 1
        # assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[6]/div[1]/div[1]/a")
        # print("  ثبت ارزش کالا " + " + ")
        # assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[6]/div[1]/div[1]/div")
        # print("تغییر اطلاعات بارگیری " + " به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_clearance_manager_check_box_op(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']/div")) == 6
        assert len(self.driver.find_elements('xpath', "//*[@id='fatherdiv']/div")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']//a")) == 4
        assert self.driver.find_element('xpath', "//*[@id='opinfobox']/div[6]/div[1]/div[1]/a")
        print("  ثبت ارزش کالا " + " + ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_box_op(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']/div")) == 6
        assert len(self.driver.find_elements('xpath', "//*[@id='fatherdiv']/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='opinfobox']//a")) == 1
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_china_transaction(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_tn_loaded_goods)

    def enter_check_box_china_transaction(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//input")) == 6
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div")) == 2
        assert self.driver.find_element('xpath', "//*[@id='formchinatransaction_type']")
        print("نوع تراکنش " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formotherinquery_type']")
        print("نوع هزینه / دریافت " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formprice']")
        print("قیمت* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formpriceunit']")
        print("واحد* " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formdescription']")
        print("توضیحات " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='formattach']")
        print("فایل پیوست " + " + ")
        assert self.driver.find_element('xpath', "//*[@id='add_chinatransaction']/div/div[2]/form/div[12]/div/button")
        print(" ثبت اطلاعات " + " به درستی مشاهده شدند . ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_china_transaction(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]//textarea")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div")) == 2
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_invoices_discount(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_invoices_discount)

    def enter_check_box_invoices_discount(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/select")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/textarea")) == 0
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_logs(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_logs)

    def enter_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 14
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "تاریخچه زمان انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "تاریخچه انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "تاریخچه پیامک های ارسالی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) == "تاریخچه تغییرات سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "تاریخچه تغییرات کالاهای سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "تاریخچه تاییدیه های سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "تاریخچه افزودن توضیحات بر روی وظیفه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "تغییرات پیش فاکتور"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "تاریخچه هماهنگی با مشتری برای تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[10]/a/div/div/span").text) == "تاریخچه تغییرات ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[11]/a/div/div/span").text) == "تاریخچه چاپ فاکتور رسمی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[12]/a/div/div/span").text) == "تاریخچه درخواست های مرجوعی کالا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[13]/a/div/div/span").text) == "آپدیت ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[14]/a/div/div/span").text) == "تاریخچه تغییرات هزینه قبض"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 9
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "History of Tasks"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "Order confirmation history"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "History of adding a description on the task"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) == "invoice changes"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "Customer coordination history for delivery"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "Official invoice printing history"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "History of goods return requests"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "clearance update"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "customs bill change history"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_customer_manager_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 11
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "تاریخچه انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "تاریخچه پیامک های ارسالی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "تاریخچه تغییرات کالاهای سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) == "تاریخچه تاییدیه های سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "تاریخچه افزودن توضیحات بر روی وظیفه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "تغییرات پیش فاکتور"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "تاریخچه هماهنگی با مشتری برای تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "تاریخچه چاپ فاکتور رسمی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "تاریخچه درخواست های مرجوعی کالا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[10]/a/div/div/span").text) == "آپدیت ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[11]/a/div/div/span").text) == "تاریخچه تغییرات هزینه قبض"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 9
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "تاریخچه انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "تاریخچه تاییدیه های سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "تاریخچه افزودن توضیحات بر روی وظیفه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) == "تغییرات پیش فاکتور"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "تاریخچه هماهنگی با مشتری برای تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "تاریخچه چاپ فاکتور رسمی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "تاریخچه درخواست های مرجوعی کالا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "آپدیت ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "تاریخچه تغییرات هزینه قبض"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_delivery_manager_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 9
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "تاریخچه انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "تاریخچه تاییدیه های سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "تاریخچه افزودن توضیحات بر روی وظیفه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) =="تغییرات پیش فاکتور"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "تاریخچه هماهنگی با مشتری برای تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "تاریخچه چاپ فاکتور رسمی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "تاریخچه درخواست های مرجوعی کالا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "آپدیت ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "تاریخچه تغییرات هزینه قبض"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_clearance_manager_check_box_logs(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/a")) == 11
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]/a/div/div/span").text) == "تاریخچه انجام وظایف"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/a/div/div/span").text) == "تاریخچه تغییرات کالاهای سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/a/div/div/span").text) == "تاریخچه تاییدیه های سفارش"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/a/div/div/span").text) == "تاریخچه افزودن توضیحات بر روی وظیفه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]/a/div/div/span").text) == "تغییرات پیش فاکتور"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[6]/a/div/div/span").text) == "تاریخچه هماهنگی با مشتری برای تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/a/div/div/span").text) == "تاریخچه تغییرات ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[8]/a/div/div/span").text) == "تاریخچه چاپ فاکتور رسمی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[9]/a/div/div/span").text) == "تاریخچه درخواست های مرجوعی کالا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[10]/a/div/div/span").text) == "آپدیت ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[11]/a/div/div/span").text) == "تاریخچه تغییرات هزینه قبض"
        print("تمامی تعییرات به درستی مشاهده شدند. ")
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_arian(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_arian)

    def enter_check_box_arian(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_financial_manager_check_box_arian(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_financial(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_financial)

    def enter_check_box_financial(self):
        sleep(3)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 4
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 0
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_admin_click_box_track_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_box_track_order)

    def enter_check_box_track_order(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='pageHolder']/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 22
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/a[1]").text) == "شرکت حمل - psp"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/a[2]").text) == "شماره بارنامه"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[1]/div/div[2]/a[1]").text) == "مرسوله آماده حمل نیست"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[1]/div/div[2]/a[2]").text) == "سفارش لغو شده است"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[1]").text) == "ارسال کننده در انتظار اقدام مشتری"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[2]").text) == "در راه تحویل به انبار مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[3]").text) == "ورود کالا به انبار مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[4]").text) == "در انتظار حمل در مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[5]").text) == "آماده ارسال در مبدا"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[6]").text) == "در حال حمل بین المللی"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[7]").text) == "رسیدن مرسوله به گمرک مقصد - منتظر ارزیابی گمرک"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[8]").text) == "منتظر تایید گمرک مبداء"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[1]").text) == "در انتظار ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[2]").text) == "در حال ارزیابی ترخیص"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[3]").text) == "ترخیص شده"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[4]").text) == "قبض شدن در انبار گمرک"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[5]").text) == "ارزیابی کالا در گمرک مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[1]").text) == "ورود کالا به انبار مقصد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[2]").text) == "آماده سازی جهت تحویل"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[3]").text) == "در حال توزیع"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[1]").text) == "تحویل داده شد"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[2]").text) == "تحویل برای ارسال به شهرستان"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[3]").text) == "تحویل قبض گمرک به مشتری"
        print("تعداد navbar  و بقیه موارد درست است. ")

    def enter_account_chain_check_box_track_order(self):
        sleep(1)
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[1]/div[1]/div/div/a")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='pageHolder']/div")) == 2
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div")) == 5
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//a")) == 22
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//button")) == 1
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//input")) == 3
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div//textarea")) == 0
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/a[1]").text) == "Shipping company - psp"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/a[2]").text) == "AWB number"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[1]/div/div[2]/a[1]").text) == "Cargo is not ready to carry"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[1]/div/div[2]/a[2]").text) == "Order Canceled"
        # assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[1]").text) == "The sender is waiting for the customer's action"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[1]").text) == "waiting for customer comfirm"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[2]").text) == "On the way to delivery to the PSP's warehouse"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[3]").text) == "Cargo Received at PSP’s warehouse in the Country of origin"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[4]").text) == "Waiting for shipment to origin"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[5]").text) == "Customer comfirmed and ready for send out"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[6]").text) == "During the international shipping"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[7]").text) == "Arrival to destination customs"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[2]/div/div[2]/a[8]").text) == "Waitng for china custom"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[1]").text) == "Received at Destination Airport"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[2]").text) == "Doing custome clearance"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[3]").text) == "Ready to Deliver. Waiting for Receiver."
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[4]").text) == "Doing Customs Clearance"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[3]/div/div[2]/a[5]").text) == "Evaluation of goods at the destination customs"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[1]").text) == "Cargo Received at PSP’s warehouse in the Destination Country"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[2]").text) == "Ready to Deliver."
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[4]/div/div[2]/a[3]").text) == "Distributing"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[1]").text) == "Customer signed the cargo"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[2]").text) == "Delivered"
        assert (self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]/div/div[5]/div/div[2]/a[3]").text) == "Customer will do Customs Clearance himself. Documents of cargo Delivered."
        print("تعداد navbar  و بقیه موارد درست است. ")

    def check_table(self, path, a, args):
        sleep(2)
        th = {}
        tr = len(self.driver.find_elements('xpath', path))
        if tr == 2:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', path+f"[2]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        elif tr == 1:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', path+f"[1]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        elif tr >= 3:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', path+f"[1]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        print("_____________")
