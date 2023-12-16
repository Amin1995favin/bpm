from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
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


class My_Tasks:
    def __init__(self, driver):
        self.driver = driver

    def enter_clearance_my_tasks(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks)

    def enter_clearance_my_tasks_auto_billed_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a[9]")

    def enter_clearance_my_tasks_new_auto_billed_order(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a[11]")

    def enter_clearance_my_tasks_new_auto_billed_order_click(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[3]/a[1]")

    def enter_clearance_my_tasks_need_clearance_inquiry(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_clearance_inquiry)

    def enter_clearance_my_tasks_update(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_update)

    def enter_clearance_my_tasks_search(self, text):
        sleep(1)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', clearance_my_tasks_search, text)

    def enter_clearance_my_tasks_search_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_search_btn)

    ################### clearance_my_tasks_need_to_issue #########################

    def enter_clearance_my_tasks_need_to_issue(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_to_issue)

    def enter_clearance_my_tasks_click_bill(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//tbody/tr[1]/td[11]/a")

    def enter_clearance_my_tasks_click_bill_delivery(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='box-seltn']/div/table/tbody/tr/td[4]/div/a[2]")

    def enter_clearance_my_tasks_need_to_issue2(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[1]/select")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[1]/select/option[2]")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[2]/button")

    def enter_clearance_my_tasks_need_to_issue3(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[1]/select")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[1]/select/option[2]")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[5]/form/div/div[2]/button")

    def enter_clearance_my_tasks_need_to_issue4(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/form/div/div[1]/select")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/form/div/div[1]/select/option[2]")
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]/div/div/div[2]/div[4]/form/div/div[2]/button")
    #
    # def enter_clearance_my_tasks_need_to_issue_check(self):
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[1]/div/div" )
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[2]/div/div")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[3]/div/div")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[4]/a")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[1]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[2]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[3]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[2]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[3]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[4]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[5]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[6]")
    #     assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[2]/div[2]/a")
    #     assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[15]/a")
    #     assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//select")) == 4
    #     assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//input")) == 28
    #     assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//textarea")) == 3
    #     assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//button")) == 8
    #     # assert a+b+c+d == 43
    #     print("بررسی فرم ترخیص انجام شد.")

    def enter_clearance_my_tasks_need_to_issue_check(self):
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[1]/div/div" )
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[2]/div/div")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[3]/div/div")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[4]/a")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[1]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[2]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[3]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[2]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[3]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[4]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[5]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[2]/div[6]")
        assert self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div[5]/div/div/div[1]/div[2]/div[2]/a")
        assert self.driver.find_element('xpath', "//*[@id='boxclearanceinqueryForm']/div/div[15]/a")
        assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//select")) == 4
        assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//input")) == 32
        assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//textarea")) == 2
        assert len(self.driver.find_elements('xpath', "/html/body/div[7]/div/div/div//button")) == 8
        # assert a+b+c+d == 43
        print("بررسی فرم ترخیص انجام شد.")

    def enter_clearance_my_tasks_need_to_issue_price(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', clearance_my_tasks_need_to_issue_price, text)

    def enter_clearance_my_tasks_need_to_issue_price_unit(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_to_issue_price_unit)

    def enter_clearance_my_tasks_need_to_issue_price_unit_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_to_issue_price_unit_option)

    def enter_clearance_my_tasks_need_to_issue_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_to_issue_btn)

    def enter_clearance_manager_my_tasks_assert_need_to_issue(self):
        a = len(self.driver.find_element('xpath', clearance_manager_my_tasks_assert_need_to_issue))
        assert a == 1

    ################### clearance_my_tasks_final_clearance #########################

    def enter_clearance_my_tasks_need_final_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_need_final_clearance)

    def enter_clearance_my_tasks_final_clearance(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance)

    def enter_clearance_my_tasks_final_clearance_text_issue(self):
        scrolled = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_text_issue)
        scrolled.location_once_scrolled_into_view
        a = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_text_issue).text
        print(a)
        assert 'منتظر تایید گمرک است' in a

    def enter_clearance_my_tasks_final_clearance_loaded_goods(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_loaded_goods)

    def enter_clearance_my_tasks_final_clearance_customs_approval(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_customs_approval)

    def enter_clearance_my_tasks_final_clearance_customs_approval_error(self):
        a = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_customs_approval_error).text
        print(a)
        assert ' ارزش کالا' in a

    def enter_clearance_my_tasks_final_clearance_record_the_value_of_goods(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_record_the_value_of_goods)

    def enter_clearance_my_tasks_final_clearance_record_the_value(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          clearance_my_tasks_final_clearance_record_the_value, text)

    def enter_clearance_my_tasks_final_clearance_record_the_value_send(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_record_the_value_send)

    def enter_clearance_my_tasks_final_clearance_checkbox_order(self):
        scrolled = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_checkbox_order)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_checkbox_order)

    def enter_clearance_my_tasks_final_clearance_category(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_category)

    def enter_clearance_my_tasks_final_clearance_category_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_category_option)

    def enter_clearance_my_tasks_final_clearance_category_send(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_final_clearance_category_send)

    def enter_clearance_my_tasks_notification_closure_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_notification_closure_batch)

    def enter_clearance_my_tasks_notification_closure_batch_click_batch(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_notification_closure_batch_click_batch)

    def enter_clearance_my_tasks_notification_closure_batch_manifests(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_notification_closure_batch_manifests)

    def enter_clearance_bill_delivery_to_customer_receipt_documents(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='nav-category-1']/div/div/div/div[2]/a[8]")

    def enter_clearance_bill_delivery_to_customer_receipt_documents_click_upload_file(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//tbody/tr[1]/td[3]/a[1]")

    def enter_clearance_bill_delivery_to_customer_receipt_documents_click_upload_file_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[7]/div/div/div/section[2]/div/div/div[1]/div/div/form/div[2]/div/button")

    def enter_clearance_bill_delivery_to_customer_receipt_documents_click_choose_file(self):
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='formreceiptdocumentsclearance']").send_keys(ROOT_DIR + "\\box.jpg")

    def enter_clearance_my_tasks_notification_closure_batch_manifests_dubai(self, batch):
        self.driver.find_element('xpath', "/html/body/div[1]/aside/section/ul/li[9]/a").click()
        sleep(1)
        self.driver.find_element('xpath', "/html/body/div[1]/aside/section/ul/li[9]/ul/li[1]/a").click()
        self.driver.find_element('xpath', "//*[@id='dateFilter']/div[2]/input").send_keys(batch)
        self.driver.find_element('xpath', "//*[@id='dateFilter']/div[2]/button").click()
        self.driver.find_element('xpath', "//table/tbody/tr[1]/td[2]/a").click()
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_notification_closure_batch_manifests)

    def enter_clearance_my_tasks_notification_closure_batch_manifests_edite(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            clearance_my_tasks_notification_closure_batch_manifests_edite)

    def enter_clearance_my_tasks_notification_closure_batch_manifests_declared_value(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          clearance_my_tasks_notification_closure_batch_manifests_declared_value,
                                                          text)

    def enter_clearance_my_tasks_notification_closure_batch_manifests_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_my_tasks_notification_closure_batch_manifests_btn)

    def enter_clearance_warehouses(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_warehouses)

    def enter_clearance_warehouses_dubai(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/a")
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[7]/ul/li/a")

    def enter_clearance_warehouses_psp(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_warehouses_psp)

    def enter_clearance_warehouses_psp_receipt_confirmation(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_warehouses_psp_receipt_confirmation)

    def enter_clearance_warehouses_dubai_receive_confirm_box(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/a")

    def enter_clearance_warehouses_psp_evaluation_of_goods_received(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_warehouses_psp_evaluation_of_goods_received)

    def enter_clearance_warehouses_psp_receipt_confirmation_op_id(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          clearance_warehouses_psp_receipt_confirmation_op_id, text)

    def enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', clearance_warehouses_psp_receipt_confirmation_op_id_btn)

    def enter_clearance_warehouses_psp_evaluation_of_goods_received_check_declared_value(self):
        a = self.driver.find_element('xpath',
                                     clearance_warehouses_psp_evaluation_of_goods_received_check_declared_value).text
        assert a == "100"

    def enter_clearance_warehouses_psp_evaluation_of_goods_received_price(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath',
                                                          clearance_warehouses_psp_evaluation_of_goods_received_price,
                                                          text)

    def enter_clearance_warehouses_psp_evaluation_of_goods_received_price_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            clearance_warehouses_psp_evaluation_of_goods_received_price_btn)

    def enter_clearance_warehouses_psp_evaluation_of_goods_received_price_msg(self):
        a = self.driver.find_element('xpath', clearance_warehouses_psp_evaluation_of_goods_received_price_msg).text
        print(a)
        assert '110' in a

    def enter_clearance_warehouses_psp_evaluation_of_goods_received_price_msg2(self):
        a = self.driver.find_element('xpath', clearance_warehouses_psp_evaluation_of_goods_received_price_msg).text
        print(a)
        assert 'قبض شده ها' in a



