from Locators import *


class Box_Other_Service_Inquery:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_box_other_service_inquery(self):
        self.driver.find_element('xpath', click_box_other_service_inquery).click()

    def enter_box_other_service_inquery_check_record(self):
        assert self.driver.find_element('xpath', box_other_service_inquery_check_record)
        print("نتایج ", " به درستی مشاهده شد")

    def enter_box_other_service_inquery_check_other_services_invoice_type(self):
        assert self.driver.find_element('xpath', box_other_service_inquery_check_other_services_invoice_type)
        print("نوع پیش فاکتور سایر خدمات", " به درستی مشاهده شد")

    def enter_box_other_service_inquery_check_other_inquiries(self):
        assert self.driver.find_element('xpath', box_other_service_inquery_check_other_inquiries)
        print("سایر استعلام ها", " به درستی مشاهده شد")

    ################### create_other_inquiries ###################

    def enter_box_other_service_inquery_other_inquery_type(self):
        self.driver.find_element('xpath', box_other_service_inquery_other_inquery_type).click()

    def enter_box_other_service_inquery_other_inquery_type_option(self):
        self.driver.find_element('xpath', box_other_service_inquery_other_inquery_type_option).click()

    def enter_box_other_service_inquery_price(self, number):
        self.driver.find_element('xpath', box_other_service_inquery_price).send_keys(number)

    def enter_box_other_service_inquery_price_unit(self):
        self.driver.find_element('xpath', box_other_service_inquery_price_unit).click()

    def enter_box_other_service_inquery_price_unit_option(self):
        self.driver.find_element('xpath', box_other_service_inquery_price_unit_option).click()

    def enter_box_other_service_inquery_submit(self):
        self.driver.find_element('xpath', box_other_service_inquery_submit).click()
