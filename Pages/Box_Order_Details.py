from Locators import *
from time import sleep


class Box_Order_Details:
    def __init__(self, driver):
        self.driver = driver

###check_box_order_details

    def enter_check_box_order_details_form_details(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_details)
        print(" جزئیات سفارش  مشاهده شد.")

    def enter_check_box_order_details_form_order_goods(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_order_goods)
        print(" کالا های سفارش  مشاهده شد.")

    def enter_check_box_order_details_form_customer_declared_goods(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_customer_declared_goods)
        print(" کالا های اظهار شده توسط مشتری مشاهده شد.")

    def enter_check_box_order_details_form_all_order_files(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_all_order_files)
        print(" تمامی فایل های سفارش  مشاهده شد.")

    def enter_check_box_order_details_form_order_notes(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_order_notes)
        print(" یادداشت سفارش  مشاهده شد.")

    def enter_check_box_order_details_form_logs(self):
        assert self.driver.find_element('xpath', check_box_order_details_form_logs)
        print(" تغییر وضعیت سفارش  مشاهده شد.")

###check_box_order_details_data

    def enter_check_box_order_details_order_types(self):
        a = self.driver.find_element('xpath', check_box_order_details_order_type).text
        assert a == "عادی"
        print(" نوع سفارش به درستی مشاهده شد.")

    def enter_check_box_order_type_of_shipping(self):
        a = self.driver.find_element('xpath', check_box_order_type_of_shipping).text
        assert a == "هوایی"
        print("نوع حمل به درستی مشاهده شد.")

    def enter_check_box_order_details_other_services_invoice_type(self):
        a = self.driver.find_element('xpath', check_box_order_details_other_services_invoice_type).text
        print(a)
        assert a == "رسمی"
        print(" نوع پیش فاکتور حمل به درستی مشاهده شد.")

    def enter_check_box_order_details_total_volumetric_weight(self):
        a = self.driver.find_element('xpath', check_box_order_details_total_volumetric_weight).text
        assert a == "6.67"
        print(" جمع وزن حجمی به درستی مشاهده شد.")

    def enter_check_box_order_details_unit_of_value(self):
        a = self.driver.find_element('xpath', check_box_order_details_unit_of_value).text
        assert a == "ریال"
        print("  واحد ارزش به درستی مشاهده شد.")

    def enter_check_box_order_details_required_services(self):
        a = self.driver.find_element('xpath', check_box_order_details_required_services).text
        assert a == "حمل بین المللی / ترخیص"
        print("  خدمات موردنیاز به درستی مشاهده شد.")

    def enter_check_box_order_details_clearance_invoice_type(self):
        a = self.driver.find_element('xpath', check_box_order_details_clearance_invoice_type).text
        assert a == "رسمی"
        print(" نوع پیش فاکتور ترخیص به درستی مشاهده شد.")

    def enter_check_box_order_details_total_actual_weight(self):
        a = self.driver.find_element('xpath', check_box_order_details_total_actual_weight).text
        assert a == "1040"
        print("  جمع وزن جرمی  به درستی مشاهده شد.")

    def enter_check_box_order_details_total_chargeable_weight(self):
        a = self.driver.find_element('xpath', check_box_order_details_total_chargeable_weight).text
        assert a == "1040"
        print("  وزن قابل پرداخت سفارش به درستی مشاهده شد.")

    def enter_check_box_order_details_total_value(self):
        a = self.driver.find_element('xpath', check_box_order_details_total_value).text
        assert a == "800"
        print(" ارزش کل به درستی مشاهده شد.")

    def enter_check_box_order_details_order_owner(self):
        a = self.driver.find_element('xpath', check_box_order_details_order_owner).text
        assert a == "ملیکا کابلی Melika Kaboli"
        print(" صاحب سفارش به درستی مشاهده شد.")

    def enter_check_box_order_details_receivers_city(self):
        a = self.driver.find_element('xpath', check_box_order_details_receivers_city).text
        assert a == "Tehran - Iran"
        print(" شهر دریافت کننده به درستی مشاهده شد.")

    def enter_check_box_order_details_senders_city(self):
        a = self.driver.find_element('xpath', check_box_order_details_senders_city).text
        assert a == "Shenzhen - China"
        print(" شهر ارسال کننده به درستی مشاهده شد.")

    def enter_check_box_order_details_customer_manager(self):
        a = self.driver.find_element('xpath', check_box_order_details_customer_manager).text
        assert "زهرا پیروز" in a
        print(" مدیر مشتری به درستی مشاهده شد.")

    def enter_check_box_order_details_marketer(self):
        a = self.driver.find_element('xpath', check_box_order_details_marketer).text
        assert a == "رضا حسین زاده"
        print(" بازاریاب به درستی مشاهده شد.")

    def enter_check_box_order_details_creator(self):
        a = self.driver.find_element('xpath', check_box_order_details_creator).text
        assert a == "زهرا پیروز Zahra Pirooz"
        print(" ایجادکننده به درستی مشاهده شد.")

    def enter_check_box_order_details_branch_representation(self):
        a = self.driver.find_element('xpath', check_box_order_details_branch_representation).text
        assert a == "ایران - تهران |تهران - نمایندگی مرکزی"
        print(" شعبه | نمایندگی به درستی مشاهده شد.")

###check_box_order_details_order_goods

    def enter_check_box_order_details_order_goods1(self):
        a01 = self.driver.find_element('xpath', check_box_order_details_order_goods_product_name1).text
        assert a01 == "camera"
        a02 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_number1).text
        assert a02 == "عدد"
        a03 = self.driver.find_element('xpath', check_box_order_details_order_goods_quantity1).text
        assert a03 == "1,000"
        a04 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_weight1).text
        assert a04 == "1"
        a05 = self.driver.find_element('xpath', check_box_order_details_order_goods_sum_weight1).text
        assert a05 == "1,000"
        a06 = self.driver.find_element('xpath', check_box_order_details_order_goods_chargeable_weight1).text
        assert a06 == "1,000"
        a07 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_value1).text
        assert a07 == "ریال"
        a08 = self.driver.find_element('xpath', check_box_order_details_order_goods_cargo_whole_value1).text
        assert a08 == "ریال"
        print(" تمام بخش های کالای اول سفارش چک شد و صحیح می باشد.")

    def enter_check_box_order_details_order_goods2(self):
        a01 = self.driver.find_element('xpath', check_box_order_details_order_goods_product_name2).text
        assert a01 == "camera2"
        a02 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_number2).text
        assert a02 == "کارتن"
        a03 = self.driver.find_element('xpath', check_box_order_details_order_goods_quantity2).text
        assert a03 == "20"
        a04 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_weight2).text
        assert a04 == "2"
        a05 = self.driver.find_element('xpath', check_box_order_details_order_goods_sum_weight2).text
        assert a05 == "40"
        a06 = self.driver.find_element('xpath', check_box_order_details_order_goods_chargeable_weight2).text
        assert a06 == "40"
        a07 = self.driver.find_element('xpath', check_box_order_details_order_goods_unit_value2).text
        assert a07 == "ریال"
        a08 = self.driver.find_element('xpath', check_box_order_details_order_goods_cargo_whole_value2).text
        assert a08 == "ریال"
        print(" تمام بخش های کالای دوم سفارش چک شد و صحیح می باشد.")


