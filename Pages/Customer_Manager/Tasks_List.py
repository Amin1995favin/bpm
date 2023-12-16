from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from colorama import Fore


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


def customer_manager_my_tasks_check(self, element_locator):
    wait = WebDriverWait(self.driver, 20)
    scrolled = self.driver.find_element('xpath', element_locator)
    sleep(0.7)
    scrolled.location_once_scrolled_into_view
    sleep(0.7)
    a = self.driver.find_element('xpath', element_locator + "/small").text
    # print(a)
    # assert text1 in a
    print(" تکست باتن " + a + " به درستی نمایش داده می شود. ")
    element = wait.until(EC.element_to_be_clickable(('xpath', element_locator)))
    sleep(0.75)
    element.click()
    sleep(0.5)
    wait.until(EC.element_to_be_clickable(('xpath', clearance_my_tasks_update))).click()
    sleep(0.7)
    b = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div[1]/h4").text
    spa = self.driver.find_element('xpath', element_locator + "/span[1]").text
    spa = int(spa)
    if spa > 0:
        sleep(.5)
        c = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        spa = str(spa)
        if spa in c:
            print("تعداد نمایش داده شده روی باتن صحیح می باشد")
        else:
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(
                Fore.RED + " خطا!!!!!تعداد نمایش داده شده روی باتن و جدول کارتابل ==> " + "***" + b + "***" + " صحیح نمی باشد ")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
            print(Fore.RED + "##############################")
        # assert spa in c
    # print("مقدار روی کارتابل" + " به درستی نمایش داده می شود. ")
    # assert b == text2
    assert b == a
    print(" تایتل کارتابل " + b + " به درستی نمایش داده می شود. و برابر با تکست روی باتن است. ")


class Tasks_list:
    def __init__(self, driver):
        self.driver = driver

    def my_tasks_check_table(self, a, args):
        sleep(2)
        th = {}
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        if tr == 2:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', f"//table/thead/tr[2]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        elif tr == 1:
            for i in range(1, a):
                th[i] = self.driver.find_element('xpath', f"//table/thead/tr[1]/th[{i}]")
                sleep(1)
                th[i].location_once_scrolled_into_view
                th[i] = th[i].text
                sleep(1)
                # print(th[i])
                assert th[i] == args[i - 1]
            print("جدول به درستی نمایش داده شد.")
        print("_____________")

    def len_customer_manager(self):
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[1]/div/div/div[2]/a")) == 31  # فروش
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-4']/div[2]/div/div/div[2]/a")) == 2  # فروش
        assert len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li")) == 7  # تعداد بخش های کارتابل ها
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a")) == 5  # ترخیص
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a")) == 2  # انبار
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a")) == 3  #  مالی
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a")) == 2  #  دلیوری
        assert len(self.driver.find_elements('xpath', "//*[@id='nav-category-5']/div/div/div/div[2]/a")) == 6  #  مدیریت
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")

    def review_and_correct_order(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_review_and_correct_order)

    def need_to_issue_shipping_queries(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_need_to_issue_shipping_queries)

    def send_invoice_to_customer(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_send_invoice_to_customer)

    def conformation_by_customer(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_conformation_by_customer)

    def auto_need_pick_up_order(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_need_pick_up_order)

    def the_need_for_the_final_shipping_inquiry(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_the_need_for_the_final_shipping_inquiry)

    def fixing_discharge_clearance_defect(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_fixing_discharge_clearance_defect)

    def auto_need_shipping(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_need_shipping)

    def op_delivery_call(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_op_delivery_call)

    def check_payment_by_expert(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_check_payment_by_expert)

    def check_payment_by_expert_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_repack_request_costumer_manager)

    def request_costumer_manager(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_repack_request_costumer_manager)

    def request_costumer_manager_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_order_pickup)

    def auto_new_online_payment_experts(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_new_online_payment_experts)

    def auto_new_online_payment_experts_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_customer_completion_destination_order)

    def auto_defect_buy_information(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_defect_buy_information)

    def auto_defect_buy_information_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_new_online_payment_experts)

    def flight_delay_notification(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_flight_delay_notification)

    def flight_delay_notification_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_check_payment_by_expert)

    def information_shipping_orders_by_partner_company(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_information_shipping_orders_by_partner_company)

    def information_shipping_orders_by_partner_company_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_solve_defection_transport_invoice)

    def pending_to_specify_the_sender(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_pending_to_specify_the_sender)

    def complete_order_information(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_complete_order_information)

    def notify_customer_completion_destination_order(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_customer_completion_destination_order)

    def auto_chat_by_customer(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_chat_by_customer)

    def notify_order_pickup(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_order_pickup)

    def notify_order_pickup_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_settlement_problem)

    def settlement_problem(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_settlement_problem)

    def settlement_problem_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_defect_buy_information)

    def review_buy_requests(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_review_buy_requests)

    def review_buy_requests_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_complete_user_info_to_register_in_arian)

    def notify_of_buy(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_of_buy)

    def notify_of_buy_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_assign_money_to_invoices)

    def sales_claims(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_sales_claims)

    def sales_claims_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_review_buy_requests)

    def check_china_transaction(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_check_china_transaction)

    def check_china_transaction_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_information_shipping_orders_by_partner_company)

    def solve_defection_transport_invoice(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_solve_defection_transport_invoice)

    def solve_defection_transport_invoice_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_notify_of_buy)

    def complete_user_info_to_register_in_arian(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_complete_user_info_to_register_in_arian)

    def complete_user_info_to_register_in_arian_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_sales_claims)

    def assign_money_to_invoices(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_assign_money_to_invoices)

    def assign_money_to_invoices_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_pending_to_specify_the_sender)

    def auto_expert_customer_recovery(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_expert_customer_recovery)

    def auto_expert_customer_recovery_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_flight_delay_notification)

    def auto_pick_status_wrong_number(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_pick_status_wrong_number)

    def auto_pick_status_wrong_number_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_complete_order_information)

    def enter_clearance_information(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_enter_clearance_information)

    def enter_clearance_information_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_check_china_transaction)

    def awaiting_settlement(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_awaiting_settlement)

    def auto_orders_transport_batches(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_orders_transport_batches)

    def awaiting_settlement_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_auto_orders_transport_batches)

    def auto_orders_transport_batches_isfahan(self):
        customer_manager_my_tasks_check(self, customer_manager_my_tasks_awaiting_settlement)

    def enter_return_order_id(self):
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        return a

    def enter_customer_manager_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks)

    def enter_customer_manager_my_tasks_notify_order_in_dubai_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a[4]")

    def enter_customer_manager_my_tasks_notify_order_in_dubai_batch_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[6]//a[2]")

    def enter_customer_manager_update_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_update_my_tasks)

    def enter_customer_manager_date_filter(self, number):
        sleep(3)
        scrolled = self.driver.find_element('xpath', customer_manager_date_filter)
        sleep(3)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', customer_manager_date_filter, number)

    def enter_customer_manager_date_filter_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_date_filter_btn)

    def enter_customer_manager_my_tasks_review_and_correct_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_review_and_correct_order)

    def enter_customer_manager_my_tasks_correct_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_correct_order)

    def enter_customer_manager_my_tasks_assert_correct_order(self):
        a = len(self.driver.find_element('xpath', customer_manager_my_tasks_assert_correct_order))
        assert a == 1

    def enter_customer_manager_my_tasks_correct_order_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_correct_order_btn)

    ################### send_invoice_to_customer #########################

    def enter_customer_manager_my_tasks_send_invoice_to_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_send_invoice_to_customer)

    def enter_customer_manager_my_tasks_bill_delivery_to_customer_national_customs(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='nav-category-4']/div[1]/div/div/div[2]/a[19]")

    def enter_click_national_id_registration(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//tbody/tr[1]/td[3]/a[1]")

    def enter_national_id(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "//*[@id='formnationalcustoms_id']", text)

    def enter_the_name_of_the_owner_of_the_national_id(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "//*[@id='formnationalcustoms_id_owner']", text)

    def enter_english_name_of_the_national_id_holder(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', "//*[@id='formnationalcustoms_id_owner_en']", text)

    def enter_click_national_id_registration_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[2]/div/div/div[1]/div/div/form/div[6]/div/button")

    def enter_customer_manager_my_tasks_send_invoice_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_send_invoice_clearance)

    def enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_send_invoice_not_sent_to_the_customer)

    def enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer2(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[10]/div[2]/a[1]")

    def enter_customer_manager_my_tasks_send_invoice_clearance_not_sent_to_the_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_send_invoice_clearance_not_sent_to_the_customer)

    def enter_customer_manager_my_tasks_send_invoice_clearance_check(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div")
        assert self.driver.find_element('xpath', "//*[@id='maliapproval']/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='form_approvals_text']")
        assert self.driver.find_element('xpath', "//*[@id='pickuporder']/div[2]/form/button")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[1]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[1]/div/div/span/span[1]/span")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[1]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[1]/div/div/span/span[1]/span")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[2]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[7]/div/div[2]/form/div[3]/button")
        assert len(self.driver.find_elements('xpath', "//textarea")) == 1
        assert len(self.driver.find_elements('xpath', "//select")) == 7
        assert len(self.driver.find_elements('xpath', "//a[@class='btn btn-success btn-block']")) == 2
        assert len(self.driver.find_elements('xpath', "//button[@type='submit']")) == 4
        print("بخش پیش فاکتورها بررسی و تعداد بخش ها صحیح می باشد.")

    ################### conformation_by_customer #########################

    def enter_customer_manager_my_tasks_conformation_by_customer(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_conformation_by_customer)

    def enter_customer_manager_my_tasks_conformation_by_customer_no_customer_approval(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_conformation_by_customer_no_customer_approval)

    def enter_customer_manager_my_tasks_conformation_by_customer_approval(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_conformation_by_customer_approval)

    def enter_customer_manager_my_tasks_conformation_by_customer_approval2(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[10]/div[3]/a[1]")

    ################### auto_need_pick_up_order #########################

    def enter_customer_manager_my_tasks_auto_need_pick_up_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_auto_need_pick_up_order)

    def enter_customer_manager_my_tasks_click_auto_need_pick_up_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_click_auto_need_pick_up_order)

    def enter_customer_manager_my_tasks_click_auto_need_pick_up_order_page(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[1]/div[2]/div[10]/a")

    def enter_customer_manager_my_tasks_page_auto_need_pick_up_order(self):
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_page_auto_need_pick_up_order)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_page_auto_need_pick_up_order)

    ################### auto_need_shipping #########################

    def enter_customer_manager_my_tasks_auto_need_shipping(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_auto_need_shipping)

    def enter_customer_manager_my_tasks_click_need_shipping(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_click_need_shipping)

    def enter_customer_manager_my_tasks_need_shipping_form_approvals_text(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_need_shipping_form_approvals_text,
                                                          text)

    def enter_customer_manager_my_tasks_need_shipping_form_approvals_send(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_need_shipping_form_approvals_send)

    def enter_customer_manager_my_tasks_warehouses(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_warehouses)

    def enter_customer_manager_my_tasks_warehouses_need_to_batch_check_show(self):
        a = len(self.driver.find_element('xpath', customer_manager_my_tasks_warehouses_need_to_batch_check_show))
        assert a == 1
        print("سفارش در بخش در انتظار بچ موجود می باشد. ")

    def enter_customer_manager_my_tasks_warehouses_need_to_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_warehouses_need_to_batch)

    ################### my_tasks_op_delivery_call #########################

    def enter_customer_manager_my_tasks_op_delivery_call(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call)

    def enter_customer_manager_my_tasks_op_delivery_call_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call_click)

    def enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_call_clearing_type_fake)

    def enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_call_clearing_type_fake_option)

    def enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call_send_invoice_fake)

    def enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option)

    def enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option2)

    def enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_text_mali_fake,
                                                          text)

    def enter_customer_manager_my_tasks_op_delivery_call_date(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_date, text)

    def enter_customer_manager_my_tasks_op_delivery_call_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_name, text)

    def enter_customer_manager_my_tasks_op_delivery_call_mobile(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_mobile, text)

    def enter_customer_manager_my_tasks_op_delivery_call_mobile_error(self):
        a = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_mobile_error).text
        print(a)

    def enter_customer_manager_my_tasks_op_delivery_call_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_phone, text)

    def enter_customer_manager_my_tasks_op_delivery_call_phone_error(self):
        a = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_phone_error).text
        print(a)

    def enter_customer_manager_my_tasks_op_delivery_call_delivery_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call_delivery_type)

    def enter_customer_manager_my_tasks_op_delivery_call_delivery_type_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_call_delivery_type_option)

    def enter_customer_manager_my_tasks_op_delivery_call_form_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call_form_btn)

    def enter_customer_manager_my_tasks_op_delivery_call_form_address(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_form_address, text)

    def enter_customer_manager_my_tasks_op_delivery_call_form_address2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          "//*[@id='formdelivery_city']", text)

    def enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_call_descnotreg_location,
                                                          text)

    def enter_customer_manager_my_tasks_op_delivery_call_closed(self):
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_closed)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_call_closed)

    def enter_customer_manager_my_tasks_op_delivery_click_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_click_order)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_box_invoices)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_person(self):
        scrolled = self.driver.find_element('xpath', "//a[text()='انتخاب فاکتور']")
        sleep(.4)
        scrolled.location_once_scrolled_into_view
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_box_invoices_person)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_person_text(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_box_invoices_person_text,
                                                          text)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_person_option(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_box_invoices_person_option)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_company(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_op_delivery_box_invoices_company)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_company_text(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_op_delivery_box_invoices_company_text,
                                                          text)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_company_option(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_box_invoices_company_option)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_error(self):
        sleep(1)
        a = self.driver.find_element('xpath',
                                     customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_error).text
        print(a)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_confirmation(self):
        sleep(1)
        a = self.driver.find_element('xpath',
                                     customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_confirmation).text
        print(a)

    def enter_customer_manager_my_tasks_op_delivery_box_invoices_update_exchange(self):
        sleep(1)
        scrolled = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_box_invoices_update_exchange)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_box_invoices_update_exchange).click()
        sleep(1.5)

    ################### my_tasks_check_payment_by_expert #########################

    def enter_customer_manager_my_tasks_check_payment_by_expert(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_by_expert)

    def enter_customer_manager_my_tasks_check_payment_by_expert_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_by_expert_click)

    def enter_customer_manager_my_tasks_check_payment_by_expert_accept_link(self):
        scrolled = self.driver.find_element('xpath', customer_manager_my_tasks_check_payment_by_expert_accept_link)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_by_expert_accept_link)

    def enter_customer_manager_my_tasks_check_payment_by_expert_detail(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_check_payment_by_expert_detail,
                                                          text)

    def enter_customer_manager_my_tasks_check_payment_by_expert_btn(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_by_expert_btn)
        sleep(1)
        print("دریافت مبلغ مورد نظر تایید شد. ")
        sleep(1)

    def enter_customer_manager_my_tasks_check_payment_by_expert_presets(self):
        sleep(3)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_by_expert_presets)

    def enter_customer_manager_my_tasks_check_payment_amount1(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_check_payment_amount1, text)

    def enter_customer_manager_my_tasks_check_payment_total_amount1_check(self):
        a = self.driver.find_element('xpath', customer_manager_my_tasks_check_payment_total_amount).text
        assert a == "10,000,000"

    def enter_customer_manager_my_tasks_check_payment_total_amount2_check(self):
        a = self.driver.find_element('xpath', customer_manager_my_tasks_check_payment_total_amount).text
        assert a == "0"

    def enter_customer_manager_my_tasks_check_payment_amount2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          customer_manager_my_tasks_check_payment_amount2, text)

    def customer_manager_my_tasks_check_payment_amount_btn(self):
        sleep(1)
        scrolled = self.driver.find_element('xpath', customer_manager_my_tasks_check_payment_amount_btn)
        sleep(2)
        scrolled.location_once_scrolled_into_view
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', customer_manager_my_tasks_check_payment_amount_btn)
        sleep(2)

    def enter_customer_manager_my_tasks_clearance(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def enter_customer_manager_my_tasks_clearance_isfahan(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[3]/a").click()

    def need_clearance_inquiry(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[1]")

    def cleared_orders(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[2]")

    def need_final_clearance(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[3]")

    def need_final_clearance_urgency_in_auto_billed_order(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[4]")

    def auto_billed_order(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[5]")

    def need_final_clearance_urgency_in_auto_billed_order_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[4]")

    def auto_billed_order_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-1']/div/div/div/div[2]/a[5]")

    def enter_customer_manager_my_tasks_warehouse(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def enter_customer_manager_my_tasks_warehouse_yazd(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def enter_customer_manager_my_tasks_warehouse_isfahan(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()

    def transit_sea_pickup(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-3']/div[1]/div/div/div[2]/a")

    def auto_pickup_status_sending_to_the_warehouse(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")

    def auto_pickup_status_sending_to_the_warehouse_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")

    def auto_need_to_batch(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")

    def print_clearance_documents(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")

    def enter_customer_manager_my_tasks_financial(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[5]/a").click()

    def auto_new_payment(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-7']/div/div/div/div[2]/a[1]")

    def op_need_print_official_invoice(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-7']/div/div/div/div[2]/a[2]")

    def auto_wallet_refund(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-7']/div/div/div/div[2]/a[3]")

    def enter_customer_manager_my_tasks_delivery(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[6]/a").click()

    def op_ready_to_deliver(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-8']/div/div/div/div[2]/a[1]")

    def determine_driver(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-8']/div/div/div/div[2]/a[2]")

    def enter_customer_manager_my_tasks_manager(self):
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[7]/a").click()

    def arrived_op_in_batch_conflict(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[1]")

    def arrived_op_in_batch_conflict_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[5]")

    def arrived_op_in_batch_conflict_isfahan2(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[1]")

    def deliver_not_cleared_request(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[2]")

    def deliver_not_cleared_request_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[6]")

    def auto_wallet_refund_check_admin(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[3]")

    def auto_wallet_refund_check_admin_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[3]")

    def auto_new_discount_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[4]")

    def auto_new_discount(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[4]")

    def check_discount_per_kilo(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[5]")

    def check_discount_per_kilo_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[5]")

    def transport_is_accumulative(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[6]")

    def transport_is_accumulative_isfahan(self):
        customer_manager_my_tasks_check(self, "//*[@id='nav-category-5']/div/div/div/div[2]/a[6]")

    def len_customer_manager_my_task(self):
        a = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li"))
        clearance = len(self.driver.find_elements('xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a"))
        warehouse = len(self.driver.find_elements('xpath', "//*[@id='nav-category-3']/div/div/div/div[2]/a"))
        financial = len(self.driver.find_elements('xpath', "//*[@id='nav-category-7']/div/div/div/div[2]/a"))
        delivery = len(self.driver.find_elements('xpath', "//*[@id='nav-category-8']/div/div/div/div[2]/a"))
        customer = len(self.driver.find_elements('xpath', "//*[@id='nav-category-5']/div/div/div/div[2]/a"))
        assert a == 7
        assert clearance == 5
        assert warehouse == 2
        assert financial == 3
        assert delivery == 2
        assert customer == 6
        print("تعداد کارتابل های نمایشی صحیح می باشد")
        print("_____________")






