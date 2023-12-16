from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    sleep(0.5)
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


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Warehouses:
    def __init__(self, driver):
        self.driver = driver

    ################### Warehouses #########################

    def enter_click_warehouses(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_warehouses)
        # self.driver.find_element('xpath', click_warehouses).click()

    def enter_click_warehouse_china(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', click_warehouse_china)
        # self.driver.find_element('xpath', click_warehouse_china).click()

    def enter_warehouses_goods_loading_list(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list)

    def enter_warehouses_goods_loading_list_search(self, number):
        self.driver.find_element('xpath', warehouses_goods_loading_list_search).send_keys(number)

    def enter_warehouses_goods_loading_list_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_update)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_update).click()

    def enter_warehouses_goods_loading_list_order_loading_status(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_order_loading_status)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_order_loading_status).click()

    def enter_warehouses_goods_loading_list_order_loading_status_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_order_loading_status_option)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_order_loading_status_option).click()

    def enter_warehouses_goods_loading_list_order_loading_status_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_order_loading_status_option2)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_order_loading_status_option2).click()

    def enter_warehouses_goods_loading_list_order_loading_status_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_order_loading_status_update)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_order_loading_status_update).click()

    ################### called_and_not_answered #########################

    def enter_warehouses_goods_loading_list_called_and_not_answered(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_called_and_not_answered)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_called_and_not_answered).click()

    ################### on_the_way #########################

    def enter_warehouses_goods_loading_list_click_on_the_way(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_click_on_the_way)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_click_on_the_way).click()

    def enter_warehouses_goods_loading_list_cargo_pickup(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_cargo_pickup)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_cargo_pickup).click()

    def enter_warehouses_goods_loading_list_total_qty(self, number):
        sleep(1)
        self.driver.find_element('xpath', warehouses_goods_loading_list_total_qty).send_keys(number)

    def enter_warehouses_goods_loading_list_total_qty_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_total_qty_update)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_total_qty_update).click()

    def enter_warehouses_goods_loading_list_pickup_add1_from2(self):
        sleep(2)
        # wait = WebDriverWait(self.driver, 20)  # set a max wait time
        # element = wait.until(EC.element_to_be_clickable(
        #     ('xpath', warehouses_goods_loading_list_pickup_add1_from2)))
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_pickup_add1_from2)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2).click()
        sleep(1)

    def enter_warehouses_goods_loading_list_pickup_add1_from2_list(self):
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_list1)
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_list2)
        print("تعداد کالاهای نمایش داده شده صحیح می باشد. ")

    def enter_warehouses_goods_loading_list_pickup_add1_from2_list2(self):
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_list1)
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_list2)
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_list3)
        print("تعداد کالاهای نمایش داده شده صحیح می باشد و کالای قبلی اضافه شد. ")

    def enter_warehouses_goods_loading_list_pickup_add1_from2_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_pickup_add1_from2_update)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_update).click()

    def enter_warehouses_goods_loading_list_pickup_add1_from2_data(self):
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_pickup_add1_from2_data)
        sleep(2)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_data).click()

    def enter_warehouses_goods_loading_list_pickup_add1_from2_data2(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_pickup_add1_from2_data2)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_data2).click()

    def enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image(self):
        self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_exterior_image).send_keys(
            ROOT_DIR + "\\box.jpg")

    def enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image(self):
        self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_internal_image).send_keys(
            ROOT_DIR + "\\camera.jpg")

    def enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            warehouses_goods_loading_list_pickup_add1_from2_no_form_print)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_no_form_print).click()

    def enter_warehouses_goods_loading_list_pickup_check_add_barcode(self):
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_check_add_barcode1)
        assert self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_check_add_barcode2)
        print("تعداد دو بارکد به درستی اضافه شد. ")

    def enter_warehouses_goods_loading_list_pickup_check_disabled_add(self):
        a = self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_check_disabled_add)
        attr = a.get_attribute('class')
        assert 'disabled' in attr
        print("دکمه افزودن غیر فعال شد . ")

    def enter_warehouses_goods_loading_list_pickup_add_warehouses(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_goods_loading_list_pickup_add_warehouses)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add_warehouses).click()

    def enter_warehouses_goods_loading_list_pickup_success_add(self):
        a = self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_success_add)
        attr = a.get_attribute('class')
        assert 'alert-success' in attr
        print("عملیات بارگیری با موفقیت انجام شد. ")

    ################### check_no_batch ###################

    def enter_warehouses_show_order_id(self):
        a = self.driver.find_element('xpath', warehouses_show_order_id).text
        print(a)
        sleep(1)
        self.driver.find_element('xpath', "/html/body/div[1]/aside/section/div[2]/span[1]/span[1]/span/span[1]").click()
        sleep(1)
        self.driver.find_element('xpath', "/html/body/span/span/span[1]/input").send_keys(a)
        sleep(2)
        self.driver.find_element('xpath', "/html/body/span/span/span[2]/ul/li[1]").click()
        sleep(1)
        # self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/a/div").click()

    ################### orders_in_warehouse #########################

    def enter_warehouses_orders_in_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_orders_in_warehouse)

    def enter_warehouses_orders_in_warehouse_search(self, number):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_search)
        a.clear()
        a.send_keys(number)

    def enter_warehouses_orders_in_warehouse_order_id(self):
        el = self.driver.find_element('xpath', warehouses_orders_in_warehouse_order_id)
        assert 'rgb(255, 204, 204)' in el.get_attribute('style')
        print("رنگ پس زمینه قرمز می باشد. ")

    def enter_warehouses_orders_in_warehouse_check_allow_batching(self):
        el = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_allow_batching).text
        assert el == "No" or "خیر"
        print("اجازه بچ کردن خیر می باشد. ")

    ################### warehouses_orders_in_warehouse_check ###################

    # def enter_warehouses_orders_in_warehouse_check_order_id(self):
    #     a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).text

    def enter_warehouses_orders_in_warehouse_check_count(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_count).text
        assert a == "2"
        print("تعداد جعبه به درستی نمایش داده شد. ")

    def enter_warehouses_orders_in_warehouse_check_weight(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_actual_weight).text
        b = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_volumetric_weight).text
        c = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_chargeable_weight).text
        assert a == "4"
        assert b == "0.66"
        assert c == "4"
        print("وزن جرمی، وزن حجمی و وزن قابل پرداخت به درستی نمایش داده شدند. ")

    def enter_warehouses_orders_in_warehouse_check_allow_batching_yes(self):
        el = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_allow_batching)
        assert 'btn-success' in el.get_attribute('class')
        print("اجازه بچ کردن بله و به رنگ سبز می باشد. ")

    def enter_warehouses_orders_in_warehouse_click_order_id(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_check_order_id)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).click()
        sleep(1)

    def enter_warehouses_orders_in_warehouse_click_checkbox2(self):
        scrolled1 = self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox2)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_click_checkbox2)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox2).click()

    def enter_warehouses_orders_in_warehouse_click_checkbox1(self):
        scrolled1 = self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox1)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_click_checkbox1)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox1).click()
        sleep(1)

    def enter_warehouses_orders_in_warehouse_click_checkbox2_aue(self):
        scrolled1 = self.driver.find_element('xpath', "//*[@id='reload-boxop']/div//table/tbody/tr[2]/td[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='reload-boxop']/div//table/tbody/tr[2]/td[1]")
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox2).click()

    def enter_warehouses_orders_in_warehouse_click_checkbox1_aue(self):
        scrolled1 = self.driver.find_element('xpath', "//*[@id='reload-boxop']/div//table/tbody/tr[1]/td[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='reload-boxop']/div//table/tbody/tr[1]/td[1]")
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_checkbox1).click()
        sleep(1)

    def enter_warehouses_orders_in_warehouse_click_create_new_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_click_create_new_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_create_new_batch).click()

    def enter_warehouses_orders_in_warehouse_assert_create_new_batch(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_assert_create_new_batch).text
        # b = self.driver.find_element('xpath', warehouses_orders_in_warehouse_assert_not_checkbox2)
        # assert not b
        # sleep(.1)
        assert 'تعریف نشده' in a
        print("بچ جدید به درستی ایجاد شد و موقعیت به بچ تعریف نشده تغییر پیدا کرد. ")
        print("چک باکس دوم به درستی غیر فعال شد. ")

    def enter_warehouses_orders_in_warehouse_text_create_new_batch(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_text_create_new_batch).text

    def enter_warehouses_orders_in_warehouse_closed_tab_click_batch(self):
        scrolled1 = self.driver.find_element('xpath', warehouses_orders_in_warehouse_closed_tab_click_batch)
        scrolled1.location_once_scrolled_into_view
        sleep(.3)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_closed_tab_click_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_closed_tab_click_batch).click()

    def enter_warehouses_orders_in_warehouse_select_batch(self, x):
        # wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_select_batch)
        select_tag = self.driver.find_element('xpath', warehouses_orders_in_warehouse_select_batch)
        # select_elem = self.driver.find_element('xpath', warehouses_orders_in_warehouse_select_batch).click()
        # self.driver.find_element('xpath', '/html/body/div[7]/div/div/div/div[6]/div[2]/div/div/div/div/div/form/div[2]/select/option[@value=max(//select/option[@value])]').click()
        # options = self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div/div[6]/div[2]/div/div/div/div/div/form/div[2]/select/option[@value]")

        # options = self.driver.find_elements('tag name', "option")
        # sleep(1)
        # options[len(options) - 1].click()
        # sleep(1)
        select_object = Select(select_tag)
        options_list = select_object.options
        for option in options_list:
            if option.text == x:
                option.click()
                break

    def enter_warehouses_orders_in_warehouse_select_batch_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse)
        # a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_text_create_new_batch)
        # b = a.text
        # scrolled1 = self.driver.find_element('xpath', a)
        # scrolled1.location_once_scrolled_into_view
        # sleep(.3)
        # scrolled1.click()
        # a.click()

    def enter_warehouses_orders_in_warehouse_select_batch_btn(self):
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_select_batch_btn)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_select_batch_btn).click()

    def enter_warehouses_orders_in_warehouse_assert_create_add_batch(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_assert_create_add_batch).text
        # b = self.driver.find_element('xpath', warehouses_orders_in_warehouse_assert_not_checkbox2)
        # assert not b
        assert 'در بچ تعریف نشده' in a
        print("یه بچ مورد نظر به درستی اضافه شد و موقعیت به بچ تعریف نشده تغییر پیدا کرد. ")
        print("چک باکس اول به درستی غیر فعال شد. ")

    def enter_warehouses_orders_in_warehouse_check_form_batch(self):
        sleep(2)
        if self.driver.find_elements('xpath', warehouses_orders_in_warehouse_destination_batch
                                              and warehouses_orders_in_warehouse_estimated_time_batch
                                              and warehouses_orders_in_warehouse_waybill_number_batch
                                              and warehouses_orders_in_warehouse_type_batch
                                              and warehouses_orders_in_warehouse_search_batch
                                              and warehouses_orders_in_warehouse_contact_batch
                                              and warehouses_orders_in_warehouse_text_batch
                                     ):
            print("تمام المان های بسته تعریف نشده به درستی مشاهده شدند. ")
        else:
            print("Elements not found")

    def enter_warehouses_orders_in_warehouse_batch_check_order1(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_name_order1).text
        b = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_number_order1).text
        c = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_weight_order1).text
        d = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_chargeable_order1).text
        e = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_origin_order1).text
        f = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_destination_order1).text
        assert 'camera2' in a
        assert b == "1"
        assert c == "2"
        assert d == "2"
        assert e == "Shenzhen - China"
        assert f == "Tehran - Iran"
        print("کالای اول به درستی نمایش داده شد. ")

    def enter_warehouses_orders_in_warehouse_batch_check_order2(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_name_order2).text
        b = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_number_order2).text
        c = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_weight_order2).text
        d = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_chargeable_order2).text
        e = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_origin_order2).text
        f = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_destination_order2).text
        assert 'camera2' in a
        assert b == "1"
        assert c == "2"
        assert d == "2"
        assert e == "Shenzhen - China"
        assert f == "Tehran - Iran"
        print("کالای دوم به درستی نمایش داده شد. ")

    def enter_warehouses_orders_in_warehouse_click_batch(self):
        sleep(5)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_click_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_batch).click()

    def enter_customer_manager_menu_exchange_rates(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_menu_exchange_rates)
        # self.driver.find_element('xpath', customer_manager_menu_exchange_rates).click()

    def enter_warehouses_orders_in_warehouse_batch_customs_list(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_batch_customs_list)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_customs_list).click()

    def enter_warehouses_orders_in_warehouse_batch_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_batch_click)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_click).click()

    def enter_warehouses_orders_in_warehouse_replace_name_batch(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_replace_name_batch).text
        sleep(.2)
        b = a.replace("شماره بچ : تعریف نشده/@", "B")
        print(b)
        d = self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_name_batch).send_keys(b)

    def enter_warehouses_orders_in_warehouse_update_name_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_update_name_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_update_name_batch).click()

    def enter_warehouses_orders_in_warehouse_closed_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_closed_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_closed_batch).click()

    def enter_warehouses_orders_in_warehouse_waybill_number_batch(self, number):
        self.driver.find_element('xpath', warehouses_orders_in_warehouse_waybill_number_batch).send_keys(number)

    def enter_warehouses_orders_in_warehouse_exiting_and_sending_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_exiting_and_sending_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_exiting_and_sending_batch).click()

    def enter_warehouses_orders_in_warehouse_select_destination_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_destination_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_destination_batch).click()

    def enter_warehouses_orders_in_warehouse_select_option_destination_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            warehouses_orders_in_warehouse_select_option_destination_batch)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_select_option_destination_batch).click()

    def enter_warehouses_orders_in_warehouse_batch_shipping_international(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_orders_in_warehouse_batch_shipping_international)
        # self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_shipping_international).click()

    def enter_warehouses_orders_in_warehouse_batch_show_number(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_show_number).text
        sleep(.2)
        # b = a.replace("شماره بچ : ", "")
        # print(b)
        # return b
        return a
        # d = self.driver.find_element('xpath', warehouses_orders_in_warehouse_click_name_batch).send_keys(b)

    def enter_warehouses_orders_in_warehouse_batch_show_op_id1(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_show_op_id1).text
        return a

    def enter_warehouses_orders_in_warehouse_batch_show_tn(self):
        a = self.driver.find_element('xpath', "//table[@class='table  table-striped  table-hover  sort-table  dataTable no-footer']/tbody/tr[1]/td[2]/a[1]/span").text
        return a

    def enter_warehouses_orders_in_warehouse_batch_show_op_id2(self):
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_batch_show_op_id2).text
        return a

    ################### warehouses_menu_check ###################

    def enter_warehouses_menu_user_profile_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_user_profile)

    def enter_warehouses_menu_user_profile_language(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_user_profile_language)

    def enter_warehouses_menu_user_profile_language_en(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_user_profile_language_en)

    def enter_warehouses_menu_user_profile_language_fa(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_user_profile_language_fa)

    def enter_warehouses_menu_user_profile_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_user_profile_btn)

    def enter_warehouses_menu_check_element(self):
        if self.driver.find_elements('xpath', warehouses_menu_search
                                              and warehouses_menu_dashboard
                                              and warehouses_menu_my_tasks
                                              and warehouses_menu_inbox
                                              and warehouses_menu_information_and_training
                                              and warehouses_menu_orders
                                              and warehouses_menu_warehouses
                                              and warehouses_menu_receive_ordered_goods_by_scanning
                                              and warehouses_menu_batches
                                              and warehouses_menu_list_excel_output
                                              and warehouses_menu_user_profile
                                              and warehouses_menu_change_password
                                              and warehouses_menu_exit
                                     ):
            print("تمام المان ها به درستی مشاهده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_warehouses_menu_check_element_text(self):
        a01 = self.driver.find_element('xpath', warehouses_menu_dashboard).text
        a02 = self.driver.find_element('xpath', warehouses_menu_my_tasks).text
        a03 = self.driver.find_element('xpath', warehouses_menu_inbox).text
        a04 = self.driver.find_element('xpath', warehouses_menu_information_and_training).text
        a05 = self.driver.find_element('xpath', warehouses_menu_orders).text
        a06 = self.driver.find_element('xpath', warehouses_menu_warehouses).text
        a07 = self.driver.find_element('xpath', warehouses_menu_receive_ordered_goods_by_scanning).text
        a08 = self.driver.find_element('xpath', warehouses_menu_batches).text
        a09 = self.driver.find_element('xpath', warehouses_menu_list_excel_output).text
        a10 = self.driver.find_element('xpath', warehouses_menu_user_profile).text
        a11 = self.driver.find_element('xpath', warehouses_menu_change_password).text
        a12 = self.driver.find_element('xpath', warehouses_menu_exit).text
        assert 'Dashboard' in a01
        assert 'My Tasks' in a02
        # assert 'Inbox' in a03
        assert 'Information and training' in a03
        assert 'Orders' in a04
        assert 'Warehouses' in a05
        assert 'Receive ordered goods by scanning' in a06
        assert 'Batches' in a07
        assert 'List Excel output' in a09
        assert 'User Profile' in a10
        assert 'Change Password' in a11
        assert 'Exit' in a12
        print("تکست تمام المان ها به درستی مشاهده شدند. ")
        print("############################################")

    def enter_warehouses_menu_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_menu_my_tasks)

    def enter_warehouses_my_tasks_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_my_tasks_update)

    ################### warehouses_my_tasks_check ###################

    def enter_warehouses_my_tasks_check_element(self):
        if self.driver.find_elements('xpath', warehouses_my_tasks_orders_are_waiting_to_be_batched
                                              and warehouses_my_tasks_order_with_tax_returns
                                              and warehouses_my_tasks_sending_to_warehouse
                                              and warehouses_my_tasks_loading
                                              and warehouses_my_tasks_repack_request_origin_warehouse
                                              and warehouses_my_tasks_print_warehouse_documents
                                              and warehouses_my_tasks_confirmation_of_warehouse_goods_documents
                                              and warehouses_my_tasks_loaded
                                     ):
            print("تمام کارتابل های، کارتابل من به درستی مشاهده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_warehouses_my_tasks_orders_are_waiting_to_be_batched(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_my_tasks_orders_are_waiting_to_be_batched)

    def enter_warehouses_my_tasks_orders_are_waiting_to_be_batched_number(self):
        a = self.driver.find_element('xpath', warehouses_my_tasks_orders_are_waiting_to_be_batched_number).text
        return a

    def enter_warehouses_my_tasks_orders_are_waiting_to_be_batched_text_table(self):
        a = self.driver.find_element('xpath', warehouses_my_tasks_orders_are_waiting_to_be_batched_text_table).text
        return a

    ################### warehouses_create_batch ###################

    def enter_warehouses_create_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_create_batch)

    def enter_warehouses_create_batch_origin(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_create_batch_origin)

    def enter_warehouses_create_batch_origin_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_create_batch_origin_option)

    def enter_warehouses_create_batch_destination(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_create_batch_destination, text)

    def enter_warehouses_create_batch_destination_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_create_batch_destination_option)

    def enter_warehouses_create_batch_send(self):
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_create_batch_send)

    def enter_warehouses_create_batch_name(self):
        a = self.driver.find_element('xpath', warehouses_create_batch_name).text
        return a

    ################### warehouses_old_check ###################

    def enter_warehouses_old(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_old)

    def enter_warehouses_old_check(self):
        if self.driver.find_elements('xpath', warehouses_old_list_cargo_pickup
                                              and warehouses_old_list_on_the_way
                                              and warehouses_old_quantity_of_goods_by_weight
                                              and warehouses_old_load_the_goods_without_track_number
                                              and warehouses_old_list_of_newly_loaded_goods
                                              and warehouses_old_reprint_the_product_label
                                              and warehouses_old_check_the_goods_in_warehouse
                                              and warehouses_old_select_delivery_people_on_the_map
                                              and warehouses_old_check_table_batch
                                              and warehouses_old_check_table_orders_in_warehouse
                                              and warehouses_old_check_search_orders_in_warehouse
                                     ):
            print("تمام کارتابل های،انبار قدیم به درستی مشاهده شدند. ")
            print("############################################")
            print("تیبل ها به درستی نمایش داده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_warehouses_old_text_order_in_warehouse(self):
        a = self.driver.find_element('xpath', warehouses_old_click_order_in_warehouse).text
        return a

    def enter_warehouses_old_click_order_in_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_old_click_order_in_warehouse)

    def enter_warehouses_old_check_search_orders_in_warehouse(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          warehouses_old_check_search_orders_in_warehouse, text)

    def enter_warehouses_old_check_order_goods_in_warehouse(self):
        assert self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse)
        print("بررسی شد که حداقل یک کالا از این سفارش در انبار وجود دارد")

    def enter_warehouses_old_check_order_goods_in_warehouse_click_tr(self):
        if self.driver.find_elements('xpath', warehouses_old_check_order_goods_in_warehouse_tr1
                                              and warehouses_old_check_order_goods_in_warehouse_tr2
                                              and warehouses_old_check_order_goods_in_warehouse_tr3
                                     ):
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1).click()
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr2).click()
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr3).click()

        elif self.driver.find_elements('xpath', warehouses_old_check_order_goods_in_warehouse_tr1
                                                and warehouses_old_check_order_goods_in_warehouse_tr2
                                       ):
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1).click()
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr2).click()

        else:
            self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1).click()

    def enter_warehouses_old_check_order_goods_in_warehouse_no_batch(self):
        a = len(self.driver.find_elements('xpath', warehouses_old_check_order_goods_in_warehouse_no_batch))
        b = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_box).text
        print(a)
        print(b)
        # print(type(a))
        # print(type(b))
        sleep(1)
        b = int(b)
        assert a == b + 1
        print("بررسی شد که از کالاها حتما یکی در انبار می باشد")
        print("تعداد چک باکس های نمایش داده شده و انتخاب شده برابر می باشد.")

    def enter_warehouses_old_check_order_goods_in_warehouse_no_batch_select(self):
        a = len(self.driver.find_elements('xpath',
                                          "/html/body/div[7]/div/div/div/div[6]/div[1]/div[2]/div/div/table/tbody//tr[@class='selected-item']"))
        b = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_box).text
        print(a)
        print(b)
        # print(type(a))
        # print(type(b))
        sleep(1)
        b = int(b)
        assert a == b
        print("بررسی شد که از کالاها حتما یکی در انبار می باشد")
        print("تعداد چک باکس های نمایش داده شده و انتخاب شده برابر می باشد.")

    def enter_warehouses_old_check_order_goods_in_warehouse_btn(self):
        if self.driver.find_elements('xpath', warehouses_old_check_order_goods_in_warehouse_remove_the_suggested_batch
                                              and warehouses_old_check_order_goods_in_warehouse_select_batch
                                              and warehouses_old_check_order_goods_in_warehouse_add_to_batch
                                     ):
            print("باتن های پاپ آپ باز شده به درستی مشاهده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_warehouses_old_check_order_goods_in_warehouse_btn_red(self):
        sleep(1)
        buttons = self.driver.find_elements('xpath', warehouses_old_check_order_goods_in_warehouse_btn_red)
        sleep(1)
        if buttons:
            buttons[0].click()
            print("یک سفارش با بک گراند قرمز انتخاب شد.")
        else:
            print("هیچ ردیفی با بک گراند قرمز پیدا نشد.")

    def enter_warehouses_old_check_order_goods_in_warehouse_red_tn(self):
        tn = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_red_tn).text
        print(tn)
        return tn

    def enter_warehouses_old_check_order_goods_in_warehouse_close_order(self):
        sleep(1)
        scrolled = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_close_order)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_old_check_order_goods_in_warehouse_close_order)

    def enter_warehouses_old_check_order_goods_in_warehouse_remove_from_order(self):
        assert self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_remove_from_order)
        print(" حذف از سفارش به درستی نمایش داد می شود.")

    ################### warehouses_new_check ###################

    def enter_check_warehouses_china(self):
        if self.driver.find_elements('xpath', warehouses_goods_loading_list
                                              and warehouses_china_notifications
                                              and warehouses_china_negotiations
                                              and warehouses_china_warehouse_change
                                              and warehouses_china_going_to_the_old_warehouse
                                              and warehouses_china_create_a_new_batch
                                              and warehouses_china_wh_search
                                              # and warehouses_china_wh_search_btn
                                              and warehouses_china_goods_are_sending_to_warehouse_list
                                              and warehouses_china_load_the_goods_without_track_number
                                              and warehouses_china_check_the_goods_in_warehouse
                                              and warehouses_china_incoming_orders_to_the_warehouse
                                              and warehouses_china_outbound_orders_from_the_warehouse
                                              and warehouses_china_orders_in_warehouse
                                              and warehouses_china_latest_packages
                                              and warehouses_china_return_orders
                                              and warehouses_china_report_the_list_of_pickuped_orders
                                              and warehouses_china_goods_by_weight
                                              and warehouses_china_list_of_newly_loaded_goods

                                     ):
            print("اعلان ها، مذاکرات انبار، تغییر انبار، رفتن به انبار قدیم و ایجاد بچ جدید به درستی مشاهده شدند. ")
            print("باکس جستجو به درستی مشاهده شد.")
            print("باتن های بخش سفارش های در راه انبار به درستی مشاهده شد.")
            print("باتن های بخش در انتظار بررسی در انبار به درستی مشاهده شد.")
            print("باتن های بخش خروجی از انبار به درستی مشاهده شد.")
            print("باتن های بخش گزارش ها به درستی مشاهده شد.")
            print("############################################")
        else:
            print("Elements not found")
        print("############################################")

    def enter_warehouses_china_notifications(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_notifications)

    def enter_warehouses_china_assert(self, b):
        # a = self.driver.title
        # print(a)
        # assert a == b
        a = self.driver.current_url
        assert a == b
        print("به درستی وارد صفحه مورد نظر شد.")
        print("############################################")

    def enter_warehouses_china_negotiations(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_negotiations)

    def enter_warehouses_china_warehouse_change(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_warehouse_change)

    def enter_warehouses_china_going_to_the_old_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_going_to_the_old_warehouse)

    def enter_warehouses_china_create_a_new_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_create_a_new_batch)

    def enter_warehouses_china_orders_in_warehouse_tn(self):
        tn = self.driver.find_element('xpath', warehouses_china_orders_in_warehouse_tn).text
        print(tn)
        return tn

    def enter_warehouses_china_orders_in_warehouse_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_orders_in_warehouse_search,
                                                          text)

    def enter_warehouses_china_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_search, text + Keys.ENTER)

    def enter_warehouses_china_orders_in_warehouse_click_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_orders_in_warehouse_tn)

    def enter_warehouses_china_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_search_btn)

    def enter_warehouses_china_search_table_check(self):
        if self.driver.find_elements('xpath', warehouses_china_search_table_td1
                                              and warehouses_china_search_table_td2
                                              and warehouses_china_search_table_td3
                                              and warehouses_china_search_table_td4
                                              and warehouses_china_search_table_td5
                                              and warehouses_china_search_table_td6
                                     ):
            print("وضعیت دستور بارگیری، ")
            print("بارگیری، ")
            print("تایید حمل بین الملل، ")
            print("بچ های سفارش، ")
            print("مشاهده سفارش و ")
            print("وضعیت سفارش به درستی مشاهده شدند. ")
        else:
            print("Elements not found")

    def enter_warehouses_china_goods_loading_list_search_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_goods_loading_list_search_click)

    def enter_warehouses_china_goods_loading_list_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_goods_loading_list_search,
                                                          text)

    def enter_warehouses_china_goods_loading_list_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_goods_loading_list_search_btn)

    def enter_warehouses_china_goods_loading_list_search_pickup(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_goods_loading_list_search_pickup)

    def enter_warehouses_china_goods_loading_list_search_table(self):
        a = len(self.driver.find_elements('xpath', warehouses_china_goods_loading_list_search_table))
        assert a == 1

    def enter_warehouses_china_goods_are_sending_to_warehouse_list(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_goods_are_sending_to_warehouse_list)

    def enter_warehouses_china_goods_are_sending_to_warehouse_list_count(self):
        a = self.driver.find_element('xpath', warehouses_china_goods_are_sending_to_warehouse_list_count).text
        print(a)
        return a

    def enter_warehouses_china_goods_are_sending_to_warehouse_list_count2(self):
        a = self.driver.find_element('xpath', warehouses_china_goods_are_sending_to_warehouse_list_count2).text
        print(a)
        return a

    def enter_warehouses_china_goods_are_sending_to_warehouse_list_count3(self):
        a = self.driver.find_element('xpath', warehouses_china_goods_are_sending_to_warehouse_list_count3).text
        print(a)
        return a

    ################### load_the_goods_without_track_number_create ###################

    def enter_warehouses_china_load_the_goods_without_track_number(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_load_the_goods_without_track_number)

    def enter_load_the_goods_without_track_number_carriage_company(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_carriage_company, text)

    def enter_load_the_goods_without_track_number_carriage_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_carriage_number, text)

    def enter_load_the_goods_without_track_number_sender_city(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_sender_city)

    def enter_load_the_goods_without_track_number_sender_city_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_sender_city_name, text)

    def enter_load_the_goods_without_track_number_sender_city_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_sender_city_option)

    def enter_load_the_goods_without_track_number_receiver_city(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_receiver_city)

    def enter_load_the_goods_without_track_number_receiver_city_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_receiver_city_name, text)

    def enter_load_the_goods_without_track_number_receiver_city_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_receiver_city_option)

    def enter_load_the_goods_without_track_number_sender_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_sender_name, text)

    def enter_load_the_goods_without_track_number_sender_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_sender_phone, text)

    def enter_load_the_goods_without_track_number_receiver_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_receiver_name, text)

    def enter_load_the_goods_without_track_number_receiver_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          load_the_goods_without_track_number_receiver_phone, text)

    def enter_load_the_goods_without_track_number_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_submit)

    def enter_load_the_goods_without_track_number_weight(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', load_the_goods_without_track_number_weight,
                                                          text)

    def enter_load_the_goods_without_track_number_cbm(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', load_the_goods_without_track_number_cbm, text)

    def enter_load_the_goods_without_track_number_name_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', load_the_goods_without_track_number_name_en,
                                                          text)

    def enter_load_the_goods_without_track_number_new_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', load_the_goods_without_track_number_new_tn)

    ################### load_the_goods_without_track_number_check_order ###################

    def enter_load_the_goods_without_track_number_check_order_shipping_cost(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_shipping_cost)
        sleep(1)
        assert 'bg-navy' in el1.get_attribute('class')
        print("رنگ استعلام حمل خاکستری و غیرفعال می باشد.")

    def enter_load_the_goods_without_track_number_check_order_other_inquiries(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_other_inquiries)
        sleep(1)
        assert 'bg-navy' in el1.get_attribute('class')
        print("رنگ سایر استعلام ها خاکستری و غیرفعال می باشد.")

    def enter_load_the_goods_without_track_number_check_order_invoice(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_invoice)
        sleep(1)
        assert 'bg-navy' in el1.get_attribute('class')
        print("رنگ پیش فاکتور خاکستری و غیرفعال می باشد.")

    def enter_load_the_goods_without_track_number_check_order_payment(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_payment)
        sleep(1)
        assert 'bg-navy' in el1.get_attribute('class')
        print("رنگ پرداخت خاکستری و غیرفعال می باشد.")

    def enter_load_the_goods_without_track_number_check_order_cargo_pickup(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_cargo_pickup)
        sleep(1)
        assert 'bg-green-active' in el1.get_attribute('class')
        print("رنگ بارگیری کالا سبز می باشد.")

    def enter_load_the_goods_without_track_number_check_order_loaded_goods(self):
        el1 = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_loaded_goods)
        sleep(1)
        assert 'bg-green-active' in el1.get_attribute('class')
        print("رنگ کالاهای بارگیری شده سبز می باشد.")

    def enter_load_the_goods_without_track_number_check_order_sender_city(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_sender_city).text
        assert el == "Shenzhen - China"
        print(" شهر ارسال کننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_sender_city2(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[20]/div/div/div/span").text
        assert el == "Shenzhen - China"
        print(" شهر ارسال کننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_receiver_city(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_receiver_city).text
        assert el == "Tehran - Iran"
        print(" شهر دریافت  کننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_receiver_city2(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_sender_city).text
        assert el == "Tehran - Iran"
        print(" شهر دریافت  کننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_creator(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_creator).text
        assert el == "joemin joemin joemin joemin"
        print(" ایجادکننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_creator2(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[23]/div/div/div/span").text
        assert el == "joemin joemin joemin joemin"
        print(" ایجادکننده به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_description(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_description).text
        # assert el == "شخص ارسال کننده : زهرا پیروز : 0911 / کاربر دریافت کننده : ملیکا کابلی : 0912"
        assert el == "Sender (person) : زهرا پیروز : 0911 / Receiver user : ملیکا کابلی : 0912"
        print(" توضیحات به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_description2(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]/div[25]/div/div/div/span").text
        # assert el == "شخص ارسال کننده : زهرا پیروز : 0911 / کاربر دریافت کننده : ملیکا کابلی : 0912"
        assert el == "Sender (person) : زهرا پیروز : 0911 / Receiver user : ملیکا کابلی : 0912"
        print(" توضیحات به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_product_name(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_product_name).text
        assert el == "camera"
        print(" نام کالا به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_unit_number(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_unit_number).text
        # assert el == "عدد"
        assert el == "Number"
        print(" واحد تعداد به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_quantity(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_quantity).text
        assert el == "1"
        print(" تعداد به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_unit_weight(self):
        el = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_unit_weight).text
        assert el == "120"
        print(" وزن واحد(kg) به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_confirm_order_details(self):
        el = self.driver.find_element('xpath',
                                      load_the_goods_without_track_number_check_order_confirm_order_details).text
        # assert ' کاربر صاحب سفارش فاقد مدیر مشتری می باشد' in el
        assert 'Attention! The customer has no client manager.' in el
        print(" توضیحات تایید جزئیات سفارش به درستی نمایش داده می شود.")

    def enter_load_the_goods_without_track_number_check_order_details_of_this_order_are_approved(self):
        el = self.driver.find_element('xpath',
                                      load_the_goods_without_track_number_check_order_details_of_this_order_are_approved)
        assert "disabled" in el.get_attribute('disabled')
        print(" باتن تایید به درستی disabled  می باشد .")

    def enter_load_the_goods_without_track_number_check_order_tn(self):
        a = self.driver.find_element('xpath', load_the_goods_without_track_number_check_order_tn).text
        sleep(.2)
        return a

    ################### incoming_orders_to_the_warehouse ###################

    def enter_warehouses_china_incoming_orders_to_the_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_incoming_orders_to_the_warehouse)

    def enter_warehouses_china_incoming_orders_to_the_warehouse_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_incoming_orders_to_the_warehouse_tn)

    def enter_warehouses_china_tn_loaded_goods(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_tn_loaded_goods)

    def enter_warehouses_china_tn_loaded_goods_in_stock_china(self):
        a = len(self.driver.find_element('xpath', warehouses_china_tn_loaded_goods_in_stock_china))
        assert a >= 2
        print("حداقل یک مورد وجود دارد که در انبار چین موجود است.")

    ################### warehouses_china_latest_packages ###################

    def enter_warehouses_china_latest_packages(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_latest_packages)

    def enter_warehouses_china_latest_packages_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]").text
        assert self.driver.find_element('xpath', "//table/tbody/tr[1]")
        assert th1 == "No."
        assert th2 == "ID"
        assert th3 == "extra"
        assert th4 == "Status"
        assert th5 == "Estimated time of arrival"
        assert th6 == "Actual weight"
        assert th7 == "Locked"
        assert th8 == "Archived"
        assert th9 == "Smart kid"
        assert th10 == "Order number"
        assert th11 == "Order Product number"
        assert th12 == "PL"
        assert th13 == "PI"
        assert th14 == "Manifest"
        assert th15 == "Files"
        assert th16 == "AWB"
        print("جدول نمایش داده شده از آخرین بسته ها  صحیح می باشد.")
        print("حداقل یک ردیف نمایشی در جدول صحیح نمایش داده می شود.")

    def enter_warehouses_china_latest_packages_show_all(self):
        assert self.driver.find_element('xpath', warehouses_china_latest_packages_show_all)
        print("باتن show all  به درستی نمایش داده می شود.")
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_latest_packages_show_all)
        sleep(1)
        a = self.driver.current_url
        b = "http://testbpm.2ms.ir/warehouses/batch/140100002"
        assert a == b
        print("به درستی وارد صفحه نمایش همه بسته ها شد.")
        print("############################################")

    def enter_warehouses_china_latest_packages_click_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_latest_packages_click_batch)

    def enter_warehouses_china_latest_packages_check_batch(self):
        if self.driver.find_elements('xpath', warehouses_china_latest_packages_check_the_goods_of_this_batch
                                              and warehouses_china_latest_packages_unlock_the_batch
                                              and warehouses_china_latest_packages_exiting_warehouse_and_sending
                                              and warehouses_china_latest_packages_close_batch_edit
                                              and warehouses_china_latest_packages_shipping_International
                                              and warehouses_china_latest_packages_batch_received_at_the_destination
                                              and warehouses_china_latest_packages_excel_output
                                              and warehouses_china_latest_packages_select_the_desired_carton
                                              and warehouses_china_latest_packages_orders_table
                                              and warehouses_china_latest_packages_contact
                                              and warehouses_china_latest_packages_text
                                              and warehouses_china_latest_packages_send
                                     ):
            print("المان های نمایش داده شده در بچ به درستی قابل مشاهده می باشند. ")

        else:
            print("Elements not found")

    def enter_warehouses_china_latest_packages_exiting_warehouse_and_sending_check(self):
        a = self.driver.find_element('xpath', warehouses_china_latest_packages_exiting_warehouse_and_sending).text
        assert a == "Exiting warehouse and sending."
        print("باتن خروج از انبار و ارسال به گمرک به درستی غیر فعال می باشد..")

    ################### warehouses_china_report_the_list_of_pickuped_orders ###################

    def enter_warehouses_china_report_the_list_of_pickuped_orders(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_the_list_of_pickuped_orders)

    def enter_warehouses_china_report_orders_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[17]").text
        assert self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']//tbody/tr[1]")
        assert th1 == "No."
        assert th2 == "Time to add to the warehouse"
        assert th3 == "Track Number"
        assert th4 == "Number of packages"
        assert th5 == "Internal shipping tracking code"
        assert th6 == "Domestic shipping company"
        assert th7 == "weight (KG)"
        assert th8 == "vweight"
        assert th9 == "Dimensions"
        assert th10 == "Origin transaction cost"
        assert th11 == "Is Pure Battery?"
        assert th12 == "Is Include Battery?"
        assert th13 == "is brand"
        assert th14 == "description"
        assert th15 == "document"
        assert th16 == "History of Changes"
        assert th17 == "Edit"
        print("جدول نمایش داده شده از گزارش لیست سفارشات بارگیری شده  صحیح می باشد.")
        print("حداقل یک ردیف نمایشی در جدول صحیح نمایش داده می شود.")

    def enter_warehouses_china_report_orders_excel_output(self):
        assert self.driver.find_element('xpath', warehouses_china_report_orders_excel_output1)
        assert self.driver.find_element('xpath', warehouses_china_report_orders_excel_output2)
        print("خروجی اکسل به درستی نمایش داده می شود.")

    def enter_warehouses_china_report_orders_start_date(self, date):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_report_orders_start_date, date)

    def enter_warehouses_china_report_orders_end_date(self, date):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_report_orders_end_date, date)

    def enter_warehouses_china_report_orders_date_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_date_btn)

    def enter_warehouses_china_report_orders_table_len(self):
        a = len(self.driver.find_elements('xpath', warehouses_china_report_orders_table_len))
        return a

    def enter_warehouses_china_report_orders_click(self):
        self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").click()

    def enter_warehouses_china_report_orders_table_edit(self):
        sleep(1)
        edits = self.driver.find_elements('xpath', warehouses_china_report_orders_table_edit)
        sleep(1)
        if edits:
            edits[0].click()
        else:
            print("در هیچ ردیفی باتن ویرایش پیدا نشد.")

    def enter_warehouses_china_report_orders_table_edit_general_category(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_edit_general_category)

    def enter_warehouses_china_report_orders_table_edit_general_category_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_edit_general_category_option)

    def enter_warehouses_china_report_orders_table_edit_detailed_classification(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_edit_detailed_classification)

    def enter_warehouses_china_report_orders_table_edit_detailed_classification_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_edit_detailed_classification_option)

    def enter_warehouses_china_report_orders_table_edit_name(self, name):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_report_orders_table_edit_name, name)

    def enter_warehouses_china_report_orders_table_edit_name_en(self, name):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', warehouses_china_report_orders_table_edit_name_en, name)

    def enter_warehouses_china_report_orders_table_edit_btn(self):
        scrolled = self.driver.find_element('xpath', warehouses_china_report_orders_table_edit_btn)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_edit_btn)

    def enter_warehouses_china_report_orders_table_history(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_table_history)

    def enter_warehouses_china_report_orders_table_history_check(self):
        text1 = self.driver.find_element('xpath', "/html/body/div[9]/div/div/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[6]/span[1]").text
        text2 = self.driver.find_element('xpath', "/html/body/div[9]/div/div/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[6]/span[2]").text
        text3 = self.driver.find_element('xpath', "/html/body/div[9]/div/div/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[6]/span[3]").text
        text4 = self.driver.find_element('xpath', "/html/body/div[9]/div/div/div/section[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[6]/span[4]").text
        assert text1 == "new camera"
        assert text2 == "دوربین جدید"
        assert text3 == "Industrial equipment"
        assert text4 == "Bush bearings and bearings"
        print("تاریخچه نمایش داده صحیح می باشد.")

    def enter_warehouses_china_report_orders_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', warehouses_china_report_orders_tn)
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/a")
        print("به درستی وارد صفحه order مورد نظر شد.")
        self.driver.back()
        sleep(1)

    def enter_warehouses_china_click_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[2]/a[1]")

    def enter_warehouses_china_check_cargo_pickup(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a/div")
        assert 'info-box bg-orange-active' in el.get_attribute('class')

    def enter_warehouses_china_check_cargo_pickup2(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a/div")
        assert 'info-box bg-orange-active' in el.get_attribute('class')

    def enter_warehouses_china_check_cargo_pickup_chain_iran(self):
        el = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a/div")
        assert 'info-box bg-orange-active' in el.get_attribute('class')

    def enter_warehouses_china_click_cargo_pickup(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[11]/a/div")

    def enter_warehouses_china_click_cargo_pickup2(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a/div")

    def enter_warehouses_china_click_cargo_pickup_chain_iran(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[12]/a/div")

    def enter_warehouses_china_click_pickup(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div/div/div[1]/div/a")

    def enter_warehouses_china_check_chain_dubai(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[7]/span").text
        print(a)
        assert 'Dubai' in a
        print("بررسی شده که حتما مقصد دبی است. ")















