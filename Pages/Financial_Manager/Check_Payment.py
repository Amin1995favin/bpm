from time import sleep

from Locators import *
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def wait_until_element_has_an_attribute(self, element_selector, element_locator, timeout=10):
    for i in range(timeout * 5):
        try:
            element = self.driver.find_element(element_selector, element_locator)
            element.click()
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute is not: " + str(element_locator))


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

    def enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder(self):
        wait_until_element_has_an_attribute(self, 'xpath',
                                            delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder)

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer).click()

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file(self):
        scrolled = self.driver.find_element('xpath',
                                            delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file)
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file)\
            .send_keys(ROOT_DIR + "\\box.jpg")

    def enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn).click()

    def enter_delivery_my_task_deliver_to_customer_order_id(self):
        self.driver.find_element('xpath', delivery_my_task_deliver_to_customer_order_id).click()





