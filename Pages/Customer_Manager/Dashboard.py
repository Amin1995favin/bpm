from Locators import *


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    ################### click_dashboard ###################

    def enter_customer_manager_click_dashboard(self):
        self.driver.find_element('xpath', customer_manager_menu_dashboard).click()

    ################### dashboard_track_orders ###################

    def enter_customer_manager_dashboard_click_track_orders(self):
        self.driver.find_element('xpath', customer_manager_dashboard_track_orders).click()
