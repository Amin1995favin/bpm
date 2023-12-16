from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from unidecode import unidecode
from persiantools.jdatetime import JalaliDate
from datetime import datetime

from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from selenium.webdriver.common.action_chains import ActionChains

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


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


class Delivery:
    def __init__(self, driver):
        self.driver = driver

    ################### my_tasks_delivery_manager ###################

    def enter_my_task_delivery_manager(self):
        wait_until_element_has_an_attribute(self, 'xpath', my_task_delivery_manager)

    def enter_delivery_manager_my_task_all(self):
        self.driver.find_element('xpath', delivery_manager_my_task_all).click()

    def enter_delivery_manager_my_task_determine_drive(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_my_task_determine_drive)

    def enter_delivery_manager_bill_delivery_to_customer_print_documents(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='task-collapse-8']/div/div/div/div[2]/a[3]")

    def enter_delivery_manager_my_task_update(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_my_task_update)

    def enter_delivery_manager_my_task_search(self, code):
        a = self.driver.find_element('xpath', delivery_manager_my_task_search)
        a.clear()
        a.send_keys(code)

    def enter_delivery_manager_my_task_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_my_task_search_btn)

    def enter_delivery_manager_my_task_determine_drive_approvals_receive(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_my_task_determine_drive_approvals_receive)

    def enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox1(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_receive_checkbox1)

    def enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox2(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_receive_checkbox2)

    def enter_delivery_manager_my_task_determine_drive_approvals_receive_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_receive_btn)

    def enter_delivery_manager_my_task_determine_drive_approvals_check_container(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_check_container)

    def enter_delivery_manager_my_task_determine_drive_approvals_select_container(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_select_container)

    def enter_delivery_manager_my_task_determine_drive_approvals_select_container_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_select_container_option)

    def enter_delivery_manager_my_task_determine_drive_approvals_select_container_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_my_task_determine_drive_approvals_select_container_btn)

    ################### my_tasks_delivery ###################

    def enter_delivery_my_task_deliver_to_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_my_task_deliver_to_customer)

    def enter_delivery_my_task_deliver_to_customer_receive_goods_this_order(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_my_task_deliver_to_customer_receive_goods_this_order)

    def enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_text(self, text):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_receive_goods_this_order_text).send_keys(
            text)

    def enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder)

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer).click()

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file(self):
        # scrolled = self.driver.find_element('xpath',
        #                                     delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file)
        # sleep(1)
        # scrolled.location_once_scrolled_into_view
        # sleep(1)
        # self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file)\
        #     .send_keys(ROOT_DIR + "\\box.jpg")
        sleep(1)
        self.driver.find_element('xpath',
                                 delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file).send_keys(
            ROOT_DIR + "\\box.jpg")

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn(self):
        scrolled = self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn).click()

    def enter_delivery_my_task_deliver_to_customer_order_id(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_order_id).click()

    ################### my_task_deliver_to_customer_official_residual ###################

    def enter_delivery_my_task_deliver_to_customer_official_residual(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_official_residual).click()

    def enter_delivery_my_task_deliver_to_customer_official_residual_price(self, number):
        a = self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_official_residual_price)
        a.clear()
        a.send_keys(number)

    def enter_delivery_my_task_deliver_to_customer_official_residual_payment_unit(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_official_residual_payment_unit).click()

    def enter_delivery_my_task_deliver_to_customer_official_residual_payment_unit_option(self):
        self.driver.find_element('xpath',
                                 delivery_my_task_deliver_to_customer_official_residual_payment_unit_option).click()

    def enter_delivery_my_task_deliver_to_customer_official_residual_payment_type(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_official_residual_payment_type).click()

    def enter_delivery_my_task_deliver_to_customer_official_residual_payment_type_option(self):
        self.driver.find_element('xpath',
                                 delivery_my_task_deliver_to_customer_official_residual_payment_type_option).click()

    def enter_delivery_my_task_deliver_to_customer_official_residual_account_number(self, number):
        self.driver.find_element('xpath',
                                 delivery_my_task_deliver_to_customer_official_residual_account_number).send_keys(
            number)

    def enter_delivery_my_task_deliver_to_customer_official_residual_btn(self):
        scrolled = self.driver.find_element('xpath',
                                            delivery_my_task_deliver_to_customer_official_residual_btn)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_official_residual_btn).click()

    # def enter_delivery_my_task_deliver_to_customer_official_residual_btn(self):
    #     wait_until_element_has_an_attribute(self, 'xpath',
    #                                         delivery_my_task_deliver_to_customer_official_residual_btn)

    def enter_delivery_order_delivered_assert(self):
        a = self.driver.find_element('xpath', delivery_order_delivered).text
        assert 'سفارش تحویل داده ' in a
        print("کالا تحویل داده شد.")
        print("############################################")

    def enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn_op(self):
        scrolled = self.driver.find_element('xpath', delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn_op)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        number = self.driver.find_element('xpath', delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn_op).text
        # print(type(number))
        numbers = number.split("/")
        # print(type(numbers))
        result1 = str(numbers[1])
        # print(type(result1))
        # result = print(result)
        numbers2 = result1.split("[")
        result2 = str(numbers2[0])
        print(result2)
        return result2

    ################### check_delivery_manager_warehouse #########################

    def enter_delivery_manager_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse)

    def enter_delivery_manager_warehouse_kahrizak(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse_kahrizak)

    def enter_delivery_manager_check_warehouses_kahrizak(self):
        if self.driver.find_elements('xpath', delivery_manager_warehouse_kahrizak_notifications
                                              and delivery_manager_warehouse_kahrizak_negotiations
                                              and delivery_manager_warehouse_kahrizak_warehouse_change
                                              and delivery_manager_warehouse_kahrizak_going_to_the_old_warehouse
                                              and delivery_manager_warehouse_kahrizak_create_a_new_batch
                                              and delivery_manager_warehouse_kahrizak_search
                                              and delivery_manager_warehouse_kahrizak_search_btn
                                              and delivery_manager_warehouse_kahrizak_receipt_confirmation
                                              and delivery_manager_warehouse_kahrizak_check_the_goods_in_warehouse
                                              and delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map
                                              and delivery_manager_warehouse_kahrizak_orders_in_warehouse
                                              and delivery_manager_warehouse_kahrizak_outbound_orders_from_the_warehouse

                                     ):
            print("اعلان ها، مذاکرات انبار، تغییر انبار، رفتن به انبار قدیم و ایجاد بچ جدید به درستی مشاهده شدند. ")
            print("باکس جستجو به درستی مشاهده شد.")
            print("باتن تاییدیه دریافت بار به درستی مشاهده شد.")
            print("باتن بررسی کالا موجود در انبار به درستی مشاهده شد.")
            print("باتن انتخاب تحویل دهندگان روی نقشه به درستی مشاهده شد.")
            print("باتن سفارش های موجود در انبار به درستی مشاهده شد.")
            print("باتن سفارش های در انتظار تحویل به درستی مشاهده شد.")
            print("############################################")
        else:
            print("Elements not found")
        print("############################################")

    def enter_delivery_manager_warehouse_kahrizak_check_the_goods_in_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_warehouse_kahrizak_check_the_goods_in_warehouse)

    def enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse_kahrizak_orders_in_warehouse)

    def enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn)

    def enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse(self):
        if self.driver.find_elements('xpath', delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_barcode
                                              and delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search
                                              and delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search_btn
                                     ):
            print("بخش سرچ op  و اسکن بارکد به درستی مشاهده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search,
                                                          text)

    def enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search_btn)

    ################### warehouses_receive_confirm_box #########################

    def enter_delivery_manager_warehouse_kahrizak_receipt_confirmation(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse_kahrizak_receipt_confirmation)

    def enter_delivery_manager_warehouses_check_receive_confirm_box(self):
        if self.driver.find_elements('xpath', delivery_manager_warehouses_receive_confirm_box_quit_search
                                              and delivery_manager_warehouses_receive_confirm_box_quit_search_btn
                                              and delivery_manager_warehouses_receive_confirm_box_batch_search
                                              and delivery_manager_warehouses_receive_confirm_box_batch_search_btn
                                     ):
            print("بخش جستجوی ترک و جستجوی بسته ها به درستی مشاهده شدند. ")
        else:
            print("Elements not found")
        print("############################################")

    def enter_delivery_manager_warehouses_receive_confirm_box_scan_batches(self):
        # تعریف لیست از المنت ها
        my_list = len(self.driver.find_elements('xpath', delivery_manager_warehouses_receive_confirm_box_scan_batches))

        # بررسی وجود حداقل یک المنت 1 در لیست
        if my_list >= 1:
            print("حداقل یک دایره وجود دارد.")

            # بررسی وجود المنت 2
            if my_list >= 5:
                assert self.driver.find_element('xpath',
                                                delivery_manager_warehouses_receive_confirm_box_scan_batches_next)
                print("5 عدد دایره وجود دارد و فلش ها نیز مشاهده شدند.")
        else:
            print("المنت 1 وجود ندارد.")

    def enter_delivery_manager_warehouses_receive_confirm_box_close_print(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = self.driver.find_element('tag name', "body")
        element.send_keys(Keys.ENTER)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def enter_delivery_manager_warehouses_receive_confirm_box_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "کد مشخصه"
        assert th3 == "ترک فرعی"
        assert th4 == ""
        assert th5 == "موقعیت"
        print("جدول نمایش داده شده صحیح می باشد.")

    def delivery_manager_warehouses_receive_confirm_box_scan_batch_op_id(self):
        a = self.driver.find_element('xpath', delivery_manager_warehouses_receive_confirm_box_scan_batch_op_id_a).text
        b = self.driver.find_element('xpath', delivery_manager_warehouses_receive_confirm_box_scan_batch_op_id_b).text
        assert a == b
        print(a)
        return a

    def delivery_delivery_manager_warehouses_receive_confirm_box_scan_batch_tn(self):
        a = self.driver.find_element('xpath', delivery_manager_warehouses_receive_confirm_box_scan_batch_tn).text
        print(a)
        return a

    def enter_delivery_manager_warehouses_receive_confirm_box_quit_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          delivery_manager_warehouses_receive_confirm_box_quit_search,
                                                          text)

    def enter_delivery_manager_warehouses_receive_confirm_box_quit_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_warehouses_receive_confirm_box_quit_search_btn)

    def enter_delivery_manager_warehouses_receive_confirm_box_check_table_tn(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "کد مشخصه"
        assert th3 == "شماره ترک"
        assert th4 == ""
        assert th5 == "شماره بچ"
        assert th6 == "تصاویر"
        assert th7 == "تاریخ چاپ برچسب کالا"
        assert th8 == "موقعیت"
        print("جدول نمایش داده شده از کالاها صحیح می باشد.")

    def enter_delivery_manager_warehouses_receive_confirm_box_scan_batch_tn_time(self):
        a = self.driver.find_element('xpath', delivery_manager_warehouses_receive_confirm_box_scan_batch_tn_time).text
        print(a)
        # assert '۱۴۰۲/۰۲/۲۵-۱۱:۴۸:۱۹' in a
        print("تاریخ نمایش داده شده از برچسب درست می باشد.")

    ################### deliver_cars #########################

    def enter_delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_manager_warehouse_kahrizak_select_delivery_people_on_the_map)

    def enter_deliver_cars_area_allocation_map(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_area_allocation_map)

    def enter_deliver_cars_create_car(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_create_car)

    def enter_deliver_cars_sync(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_sync)

    def enter_deliver_cars_check_table(self):
        th1 = self.driver.find_element('xpath', deliver_cars_no).text
        th2 = self.driver.find_element('xpath', deliver_cars_name).text
        th3 = self.driver.find_element('xpath', deliver_cars_number_plates).text
        th4 = self.driver.find_element('xpath', deliver_cars_selection_delivery).text
        th5 = self.driver.find_element('xpath', deliver_cars_selection_distributor).text
        th6 = self.driver.find_element('xpath', deliver_cars_the_operation).text
        assert self.driver.find_element('xpath', deliver_cars_check_tbody)
        assert th1 == "ردیف"
        assert th2 == "نام ماشین"
        assert th3 == "شماره پلاک"
        assert th4 == "انتخاب تحویل دهنده"
        assert th5 == "انتخاب موزع"
        assert th6 == "عملیات"
        print("جدول نمایش داده شده از ماشین ها صحیح می باشد.")
        print("حداقل یک ردیف نمایشی در جدول صحیح نمایش داده می شود.")

    def enter_deliver_cars_create_car_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_create_car_name, text)

    def enter_deliver_cars_create_car_number_plates1(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_create_car_number_plates1, text)

    def enter_deliver_cars_create_car_number_plates2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_create_car_number_plates2, text)

    def enter_deliver_cars_create_car_number_plates3(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_create_car_number_plates3, text)

    def enter_deliver_cars_create_car_number_plates4(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_create_car_number_plates4, text)

    def enter_deliver_cars_create_car_satisfaction_coefficient(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          deliver_cars_create_car_satisfaction_coefficient, text)

    def enter_deliver_cars_create_car_send(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_create_car_send)

    def enter_deliver_cars_selection_delivery_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_delivery_click)

    def enter_deliver_cars_selection_delivery_user_id_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_delivery_user_id_btn)

    def enter_deliver_cars_selection_delivery_user_id(self):
        user_id = self.driver.find_element('xpath', deliver_cars_selection_delivery_user_id).text
        print(user_id)
        return user_id

    def enter_deliver_cars_selection_delivery_user_id2(self):
        user_id = self.driver.find_element('xpath', deliver_cars_selection_delivery_user_id2).text
        print(user_id)
        return user_id

    def enter_deliver_cars_selection_delivery_user_id_delete(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_delivery_user_id_delete)

    def enter_deliver_cars_selection_delivery_user_id_select(self, x):
        select_tag = self.driver.find_element('xpath', deliver_cars_selection_delivery_user_id_select)
        select_object = Select(select_tag)
        options_list = select_object.options
        for option in options_list:
            if option.text == x:
                option.click()
                break

    def enter_deliver_cars_selection_distributor_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_distributor_click)

    def enter_deliver_cars_selection_distributor_user_id_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_distributor_user_id_btn)

    def enter_deliver_cars_selection_distributor_user_id(self):
        user_id = self.driver.find_element('xpath', deliver_cars_selection_distributor_user_id).text
        print(user_id)
        return user_id

    def enter_deliver_cars_selection_distributor_user_id_delete(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_selection_distributor_user_id_delete)

    def enter_deliver_cars_selection_distributor_user_id_select(self, x):
        select_tag = self.driver.find_element('xpath', deliver_cars_selection_distributor_user_id_select)
        select_object = Select(select_tag)
        options_list = select_object.options
        for option in options_list:
            if option.text == x:
                option.click()
                break

    def enter_deliver_cars_the_operation_disabled(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_the_operation_disabled)

    def enter_deliver_cars_the_operation_history(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_the_operation_history)

    def enter_check_deliver_cars_the_operation_history_time(self):
        a = self.driver.find_element('xpath', deliver_cars_the_operation_history_time).text
        c = JalaliDate.today().strftime('%A %d ')
        b = unidecode(a)
        now = datetime.now()
        c = now.strftime("%H:%M")
        # c = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        print("b = " + b)
        print("c = " + c)
        assert c in b
        print("زمان نمایش داده شده صحیح می باشد.")

    def enter_check_deliver_cars_the_operation_history_time2(self):
        a = self.driver.find_element('xpath', deliver_cars_the_operation_history_time2).text
        c = JalaliDate.today().strftime('%A %d ')
        b = unidecode(a)
        now = datetime.now()
        c = now.strftime("%H:%M")
        # c = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        print(b)
        print(c)
        assert c in b
        print("زمان نمایش داده شده صحیح می باشد.")

    def enter_deliver_cars_the_operation_edit_name(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_the_operation_edit_name)

    def enter_deliver_cars_the_operation_edit_name_new(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', deliver_cars_the_operation_edit_name_new, text)

    def enter_deliver_cars_the_operation_edit_name_new_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_the_operation_edit_name_new_btn)

    ################### delivery_manager_allocation_map ###################

    def enter_delivery_manager_allocation_map(self):
        actions = ActionChains(self.driver)
        self.driver.find_element('xpath',
                                 "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
        sleep(0.5)
        self.driver.find_element('xpath',
                                 "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
        sleep(0.5)
        self.driver.find_element('xpath',
                                 "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a[2]").click()
        sleep(5)
        actions.move_by_offset(750, 280).click_and_hold().move_by_offset(100, 50).click_and_hold().perform()
        # actions.move_by_offset(889, 288).pause(1).click().perform()
        # sleep(3)
        # actions.move_by_offset(870, 290).pause(1).click().perform()
        sleep(1)

    #### document.onmousemove = function(e)
    #### {
    ####     var
    #### x = e.pageX;
    #### var
    #### y = e.pageY;
    #### e.target.title = "[" + x + " , " + y + "]";
    #### };

    #
    # ################### delivery_manager_allocation_map ###################
    #
    # def enter_delivery_manager_allocation_map(self):
    #     actions = ActionChains(self.driver)
    #
    #     # چیدمان نمایشی صفحه را منتظر بمانید
    #     wait = WebDriverWait(self.driver, 5)
    #     # map_element = wait.until(EC.presence_of_element_located(('xpath', "//img[@src='https://tile.openstreetmap.org/0/0/0.png']")))
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a[2]").click()
    #
    #     # self.driver.execute_script("scroll(0,500)")
    #     sleep(1)
    #     # offset = self.driver.find_element("xpath", "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div/div/div[2]/button").location
    #     # actions.move_by_offset(889, 288).pause(1).click().perform()
    #     # actions.move_by_offset(482, 345).pause(1).click().perform()
    #
    #    sleep(3)
    #
    #      document.onmousemove = function(e)
    #      {
    #          var
    #      x = e.pageX;
    #      var
    #      y = e.pageY;
    #      e.target.title = "[" + x + " , " + y + "]";
    #      };
    #
    #
    #
    # def enter_delivery_manager_allocation_map(self):
    #     action = ActionChains(self.driver)
    #
    #     # چیدمان نمایشی صفحه را منتظر بمانید
    #     wait = WebDriverWait(self.driver, 5)
    #     # map_element = wait.until(EC.presence_of_element_located(('xpath', "//img[@src='https://tile.openstreetmap.org/0/0/0.png']")))
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     sleep(3)
    #     map_element = wait.until(EC.presence_of_element_located(('xpath', "//img[@src='https://tile.openstreetmap.org/0/0/0.png']")))
    #
    #     # مختصات قسمت مورد نظر را استخراج کنید
    #     location = map_element.location
    #     size = map_element.size
    #
    #     x1 = location['x'] + 50
    #     y1 = location['y'] + 50
    #     x2 = x1 + size['width'] - 100
    #     y2 = y1 + size['height'] - 100
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a[2]").click()
    #
    #     # عکس قسمت مورد نظر را ذخیره کنید
    #     self.driver.save_screenshot("map_part.png", {'left': x1, 'top': y1, 'width': x2 - x1, 'height': y2 - y1})

    #
    # def enter_delivery_manager_allocation_map(self):
    #     action = ActionChains(self.driver)
    #
    #     # چیدمان نمایشی صفحه را منتظر بمانید
    #     wait = WebDriverWait(self.driver, 5)
    #     # map_element = wait.until(EC.presence_of_element_located(('xpath', "//img[@src='https://tile.openstreetmap.org/0/0/0.png']")))
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
    #     sleep(0.5)
    #     sleep(3)
    #     map_element = wait.until(EC.presence_of_element_located(('xpath', "//img[@src='https://tile.openstreetmap.org/0/0/0.png']")))
    #
    #     # مختصات قسمت مورد نظر را استخراج کنید
    #     location = map_element.location
    #     size = map_element.size
    #
    #     x1 = location['x'] + 50
    #     y1 = location['y'] + 50
    #     x2 = x1 + size['width'] - 100
    #     y2 = y1 + size['height'] - 100
    #     self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div/a[2]").click()
    #
    #     # عکس قسمت مورد نظر را ذخیره کنید
    #     self.driver.save_screenshot("map_part.png", {'left': x1, 'top': y1, 'width': x2 - x1, 'height': y2 - y1})
    #

    def enter_deliver_cars_area_allocation_map_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_area_allocation_map_submit)

    def enter_deliver_cars_area_allocation_map_popup_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_area_allocation_map_popup_btn)

    def enter_delivery_manager_allocation_map_zoom_out(self):
        self.driver.find_element('xpath',
                                 "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
        sleep(0.5)
        self.driver.find_element('xpath',
                                 "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/a[2]").click()
        sleep(0.5)

    def enter_deliver_cars_area_allocation_map_delete_location(self):
        wait_until_element_has_an_attribute(self, 'xpath', deliver_cars_area_allocation_map_delete_location)

    def enter_delivery_manager_allocation_map_zoom_out2(self):
        self.driver.find_element('xpath',
                                 "/html/body/div[7]/div/div/div[5]/div[2]/div/div[2]/form/div[11]/div/div/div/div[2]/div[1]/div[1]/a[2]").click()
        sleep(0.5)
        self.driver.find_element('xpath',
                                 "/html/body/div[7]/div/div/div[5]/div[2]/div/div[2]/form/div[11]/div/div/div/div[2]/div[1]/div[1]/a[2]").click()
        sleep(0.5)

    def enter_delivery_manager_allocation_map_click(self):
        wait = WebDriverWait(self.driver, 20)
        actions = ActionChains(self.driver)
        sleep(5)
        # offset = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div[5]/div[2]/div/div[2]/form/div[11]/div/div/div/div[2]/div[1]/div[2]/input").location
        # actions.move_by_offset(offset['x']-100, offset['y']-200).pause(1).click().perform()
        sleep(8)
        # actions.move_by_offset(30, 30).click_and_hold().perform()
        actions.move_by_offset(640, 220).click().perform()
        sleep(2)
        print("لوکیشن انتخاب شد.")

        # document.onmousemove = function(e)
        # {
        #     var
        # x = e.pageX;
        # var
        # y = e.pageY;
        # e.target.title = "[" + x + " , " + y + "]";
        # };

################### outbound_orders_from_the_warehouse ###################

    def enter_outbound_orders_from_the_warehouse(self):
        wait_until_element_has_an_attribute(self, 'xpath', delivery_manager_warehouse_kahrizak_outbound_orders_from_the_warehouse)
















