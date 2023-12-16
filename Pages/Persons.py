
from Locators import *
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(1)
    element.click()
    sleep(1)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(1)
    element.clear()
    sleep(1)
    element.send_keys(text)
    sleep(1)


class Persons:
    def __init__(self, driver):
        self.driver = driver

###persons

    def enter_click_persons(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_persons)
        # self.driver.find_element('xpath', click_persons).click()

    def enter_click_persons_financial(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_persons_financial)
        # self.driver.find_element('xpath', click_persons_financial).click()

###persons_create

    def enter_click_persons_create(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_persons_create)
        # self.driver.find_element('xpath', click_persons_create).click()

    def enter_assert_persons_create_check(self):
        a=self.driver.title
        # assert_persons_create_check = self.driver.find_element('xpath', persons_create_check).text
        # assert assert_persons_create_check == "ایجاد شخص "
        assert a == "اشخاص > ایجاد شخص | BPM"
        # print("شما با موفقیت وارد ", assert_persons_create_check, "شدید.")
        # print(a)

    def enter_persons_create_firstname(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_firstname, text)
        # el = self.driver.find_element('xpath', persons_create_firstname)
        # el.clear()
        # el.send_keys(name)

    def enter_persons_create_lastname(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_lastname, text)
        # el = self.driver.find_element('xpath', persons_create_lastname)
        # el.clear()
        # el.send_keys(name)

    def enter_persons_create_firstname_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_firstname_en, text)
        # el=self.driver.find_element('xpath', persons_create_firstname_en)
        # el.clear()
        # el.send_keys(name)

    def enter_persons_create_lastname_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_lastname_en, text)
        # el = self.driver.find_element('xpath', persons_create_lastname_en)
        # el.clear()
        # el.send_keys(name)

    def enter_persons_create_gender(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_gender)
        # self.driver.find_element('xpath', persons_create_gender).click()

    def enter_persons_create_gender_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_gender_option)
        # self.driver.find_element('xpath', persons_create_gender_option).click()

    def enter_persons_create_email(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_email, text)
        # self.driver.find_element('xpath', persons_create_email).send_keys(email)

    def enter_persons_create_non_iranian_nationals(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_non_iranian_nationals)
        # self.driver.find_element('xpath', persons_create_non_iranian_nationals).click()

    def enter_persons_create_non_iranian_nationals_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_non_iranian_nationals_option)
        # self.driver.find_element('xpath', persons_create_non_iranian_nationals_option).click()

    def enter_persons_create_non_iranian_nationals_option2(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_non_iranian_nationals_option2)
        # self.driver.find_element('xpath', persons_create_non_iranian_nationals_option2).click()

    def enter_persons_create_non_iranian_create_code_melli(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_non_iranian_create_code_melli, text)
        # el= self.driver.find_element('xpath', persons_create_non_iranian_create_code_melli)
        # el.clear()
        # el.send_keys(code)

    def enter_persons_create_code_melli(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_code_melli, text)
        # el= self.driver.find_element('xpath', persons_create_code_melli)
        # el.clear()
        # el.send_keys(code)

    def enter_persons_create_phone_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_phone_number, text)
        # el= self.driver.find_element('xpath', persons_create_phone_number)
        # el.clear()
        # el.send_keys(number)


    def random_phone_num_generator(self):
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)

        last = (str(random.randint(1, 9998)).zfill(4))
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))

        w= '{}-{}-{}'.format(989, second, last)
        return w
        # driver.find_element('xpath', persons_create_phone_number).send_keys(w)
        # self.driver.find_element('xpath', persons_create_phone_number).send_keys(w)

    # n = int(input("Enter Value of n: "))
    # for i in range(0, n):
    #     print(random_phone_num_generator())

    def enter_persons_create_phone_number2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_phone_number2, text)
        # self.driver.find_element('xpath', persons_create_phone_number2).send_keys(number)

    def enter_persons_create_phone1(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_phone1, text)
        # self.driver.find_element('xpath', persons_create_phone1).send_keys(number)

    def enter_persons_create_phone2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_phone2, text)
        # self.driver.find_element('xpath', persons_create_phone2).send_keys(number)

    def enter_persons_create_internal_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_internal_number, text)
        # self.driver.find_element('xpath', persons_create_internal_number).send_keys(number)

    def enter_persons_create_company_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_company_phone, text)
        # self.driver.find_element('xpath', persons_create_company_phone).send_keys(number)

    def enter_persons_create_company_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_company_name, text)
        # self.driver.find_element('xpath', persons_create_company_name).send_keys(name)

    def enter_persons_create_postalcode(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_postalcode, text)
        # self.driver.find_element('xpath', persons_create_postalcode).send_keys(code)

    def enter_persons_create_address(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_address, text)
        # self.driver.find_element('xpath', persons_create_address).send_keys(address)

    def enter_persons_create_agency(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_agency)
        # self.driver.find_element('xpath', persons_create_agency).click()

    def enter_persons_create_agency_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_agency_option)
        # self.driver.find_element('xpath', persons_create_agency_option).click()

    def enter_persons_create_expert_user(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_expert_user)
        # self.driver.find_element('xpath', persons_create_expert_user).click()

    def enter_persons_create_expert_user_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_expert_user_name, text)
        # self.driver.find_element('xpath', persons_create_expert_user_name).send_keys(name)

    def enter_persons_create_expert_user_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_expert_user_option)
        # self.driver.find_element('xpath', persons_create_expert_user_option).click()

    def enter_persons_create_how_find_us(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_how_find_us)
        # self.driver.find_element('xpath', persons_create_how_find_us).click()

    def enter_persons_create_how_find_us_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_how_find_us_option)
        # self.driver.find_element('xpath', persons_create_how_find_us_option).click()

    def enter_persons_create_marketer(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_marketer)
        # self.driver.find_element('xpath', persons_create_marketer).click()

    def enter_persons_create_marketer_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_marketer_name, text)
        # self.driver.find_element('xpath', persons_create_marketer_name).send_keys(name)

    def enter_persons_create_marketer_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_marketer_option)
        # self.driver.find_element('xpath', persons_create_marketer_option).click()

    def enter_persons_create_description(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', persons_create_description, text)
        # self.driver.find_element('xpath', persons_create_description).send_keys(text)

    def enter_persons_create_submit_btn(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_submit_btn)
        # self.driver.find_element('xpath', persons_create_submit_btn).click()

    def enter_persons_create_check_name(self):
        sleep(1.5)
        a = self.driver.find_element('xpath', persons_create_check_name).text
        assert 'کاربر تست / user test' in a
        print("نام بصورت:", a, "و صحیح می باشد.")

    def enter_persons_create_check_expert_user(self):
        a = self.driver.find_element('xpath', persons_create_check_expert_user).text
        assert "زهرا پیروز" in a
        print("مدیر مشتری بصورت:", a, "و صحیح می باشد.")

    def enter_persons_create_check_marketer(self):
        a= self.driver.find_element('xpath', persons_create_check_marketer).text
        assert a == "بازاریاب مارکتینگ"
        print("بازاریاب بصورت:", a, "و صحیح می باشد.")

    def enter_persons_create_check_agency(self):
        a= self.driver.find_element('xpath', persons_create_check_agency).text
        assert a == "تهران - نمایندگی مرکزی"
        print("نمایندگی بصورت:", a, "و صحیح می باشد.")

    def enter_persons_create_check_phone_number(self):
        a = self.driver.find_element('xpath', persons_create_check_phone_number).text
        assert a == "0212345678"
        print("تلفن بصورت:", a, "و صحیح می باشد.")

    def enter_persons_create_check_arian(self):
        assert self.driver.find_element('xpath', persons_create_check_arian)
        print(" انتقال کاربر به آرین مشاهده شد.")

    def enter_persons_create_check_connected_user(self):
        assert self.driver.find_element('xpath', persons_create_connected_user)
        # print(" کاربرمتصل مشاهده شد.")
        print(" اطلاعات فرد مشاهده شد.")

    # Enable/Disable
    def enter_persons_create_check_enable_disable(self):
        # Disabl
        el01= self.driver.find_element('xpath', persons_create_user_transactions)
        el02= self.driver.find_element('xpath', persons_create_user_payments)
        el03= self.driver.find_element('xpath', persons_create_payment_documents_in_Arian)
        el04= self.driver.find_element('xpath', persons_create_refund_requests)
        el05= self.driver.find_element('xpath', persons_create_doing)
        el06= self.driver.find_element('xpath', persons_create_just_downloaded)
        el07= self.driver.find_element('xpath', persons_create_delivered_not_settled)
        el08= self.driver.find_element('xpath', persons_create_delivered_and_settled)
        el09= self.driver.find_element('xpath', persons_create_canceled)
        # Enable
        el10= self.driver.find_element('xpath', persons_create_customer_indebtedness)
        el11= self.driver.find_element('xpath', persons_create_subscribed)
        el12= self.driver.find_element('xpath', persons_create_suspended)
        el13= self.driver.find_element('xpath', persons_create_list_all)
        # Disabl
        assert 'half-clear' in el01.get_attribute('class')
        assert 'half-clear' in el02.get_attribute('class')
        assert 'half-clear' in el03.get_attribute('class')
        assert 'half-clear' in el04.get_attribute('class')
        assert 'half-clear' in el05.get_attribute('class')
        assert 'half-clear' in el06.get_attribute('class')
        assert 'half-clear' in el07.get_attribute('class')
        assert 'half-clear' in el08.get_attribute('class')
        assert 'half-clear' in el09.get_attribute('class')
        # Enable
        assert 'half-clear' not in el10.get_attribute('class')
        assert 'half-clear' not in el11.get_attribute('class')
        assert 'half-clear' not in el12.get_attribute('class')
        assert 'half-clear' not in el13.get_attribute('class')
        print("تمامی Enable/Disable به درستی بررسی شدند.")

    def enter_persons_create_check_form(self):
        if self.driver.find_elements('xpath', persons_create_firstname and persons_create_lastname
                                     and persons_create_firstname_en and persons_create_lastname_en
                                     and persons_create_gender and persons_create_email
                                     and persons_create_non_iranian_nationals and persons_create_code_melli
                                     and persons_create_phone_number and persons_create_phone_number2
                                     and persons_create_phone1 and persons_create_phone2
                                     and persons_create_internal_number and persons_create_company_phone
                                     and persons_create_company_name and persons_create_postalcode
                                     and persons_create_address and persons_create_agency
                                     and persons_create_expert_user and persons_create_how_find_us
                                     and persons_create_marketer and persons_create_description
                                     ):
            print("Elements found")
        else:
            print("Elements not found")

    def enter_persons_create_check_selection(self):
        el1=len(self.driver.find_elements('xpath', persons_create_check_selection))
        el2=len(self.driver.find_elements('xpath', persons_create_check_input))
        el3=len(self.driver.find_elements('xpath', persons_create_check_text))
        el4=len(self.driver.find_elements('xpath', persons_create_check_select))
        sum_el= el1+el2+el3+el4
        # print(sum_el)
        assert sum_el == 44

###search_financial

    def enter_psp_search_select(self):
        wait_until_element_has_an_attribute(self, 'xpath', psp_search_select)
        # self.driver.find_element('xpath', psp_search_select).click()

    def enter_psp_search_select_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', psp_search_select_name, text)
        # self.driver.find_element('xpath', psp_search_select_name).send_keys(name)

    def enter_psp_search_select_option(self):
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', psp_search_select_option)
        # self.driver.find_element('xpath', psp_search_select_option).click()

    # def enter_psp_search_select_option2(self):
    #     self.driver.find_element('xpath', psp_search_select_option2).click()

    def enter_psp_search_show_financial(self):
        wait_until_element_has_an_attribute(self, 'xpath', psp_search_show_financial)
        # self.driver.find_element('xpath', psp_search_show_financial).click()

    def enter_financial_persons_create_check_form(self):
        if self.driver.find_elements('xpath', persons_create_firstname and persons_create_lastname
                                     and persons_create_firstname_en and persons_create_lastname_en
                                     and persons_create_gender and persons_create_email
                                     and persons_create_non_iranian_nationals and persons_create_code_melli
                                     and persons_create_phone_number and persons_create_phone_number2
                                     and persons_create_phone1 and persons_create_phone2
                                     and persons_create_internal_number and persons_create_company_phone
                                     and persons_create_company_name and persons_create_postalcode
                                     and persons_create_address and persons_create_how_find_us
                                     and persons_create_description
                                     ):
            print("Elements found")
        else:
            print("Elements not found")

    def enter_financial_persons_create_check_selection(self):
        el1=len(self.driver.find_elements('xpath', persons_create_check_selection))
        el2=len(self.driver.find_elements('xpath', persons_create_check_input))
        el3=len(self.driver.find_elements('xpath', persons_create_check_text))
        el4=len(self.driver.find_elements('xpath', persons_create_check_select))
        sum_el= el1+el2+el3+el4
        # print(sum_el)
        assert sum_el == 36

###connected_user

    def enter_persons_create_connected_user(self):
        wait_until_element_has_an_attribute(self, 'xpath', persons_create_connected_user)
        # self.driver.find_element('xpath', persons_create_connected_user).click()

    def enter_persons_create_check_user_btn(self):
        assert self.driver.find_element('xpath', persons_create_check_user_integration)
        print(" ادغام کاربر مشاهده شد.")
        assert self.driver.find_element('xpath', persons_create_check_login_to_user_account)
        print(" ورود به حساب کاربر مشاهده شد.")
        assert self.driver.find_element('xpath', persons_create_check_edit_user_information)
        print(" ویرایش اطلاعات کاربر مشاهده شد.")
        assert self.driver.find_element('xpath', persons_create_check_user_changes)
        print(" تغییرات کاربر مشاهده شد.")
        assert self.driver.find_element('xpath', persons_create_check_user_locations)
        print(" مکان های کاربر مشاهده شد.")
        assert self.driver.find_element('xpath', persons_create_check_persons_information)
        print(" اطلاعات فرد مشاهده شد.")

###check_enable

    def enter_persons_create_check_enable(self):
        # Enable
        el01= self.driver.find_element('xpath', persons_create_user_transactions1)
        el02= self.driver.find_element('xpath', persons_create_user_payments1)
        el03= self.driver.find_element('xpath', persons_create_payment_documents_in_Arian1)
        el04= self.driver.find_element('xpath', persons_create_refund_requests1)
        el05= self.driver.find_element('xpath', persons_create_doing1)
        el06= self.driver.find_element('xpath', persons_create_just_downloaded1)
        el07= self.driver.find_element('xpath', persons_create_delivered_not_settled1)
        el08= self.driver.find_element('xpath', persons_create_delivered_and_settled1)
        el09= self.driver.find_element('xpath', persons_create_canceled1)
        el10= self.driver.find_element('xpath', persons_create_customer_indebtedness1)
        el11= self.driver.find_element('xpath', persons_create_subscribed1)
        el12= self.driver.find_element('xpath', persons_create_suspended1)
        el13= self.driver.find_element('xpath', persons_create_list_all1)
        # Enable
        assert 'half-clear' not in el01.get_attribute('class')
        assert 'half-clear' not in el02.get_attribute('class')
        assert 'half-clear' not in el03.get_attribute('class')
        assert 'half-clear' not in el04.get_attribute('class')
        assert 'half-clear' not in el05.get_attribute('class')
        assert 'half-clear' not in el06.get_attribute('class')
        assert 'half-clear' not in el07.get_attribute('class')
        assert 'half-clear' not in el08.get_attribute('class')
        assert 'half-clear' not in el09.get_attribute('class')
        assert 'half-clear' not in el10.get_attribute('class')
        assert 'half-clear' not in el11.get_attribute('class')
        assert 'half-clear' not in el12.get_attribute('class')
        assert 'half-clear' not in el13.get_attribute('class')
        print("تمامی Enable به درستی بررسی شدند.")

    def enter_persons_create_check_inventory(self):
        el = self.driver.find_element('xpath', persons_create_check_inventory)
        attr = el.get_attribute('class')
        assert 'bg-gray' in attr
        print("کاربر فاقد اعتبار به رنگ خاکستری می باشد.")

    def enter_persons_create_check_records(self):
        el =  self.driver.find_element('xpath', persons_create_check_records)
        attr = el.get_attribute('class')
        assert 'col-lg-6  col-md-6 col-sx-12 ' in attr
        print("سوابق قراردادها به رنگ خاکستری می باشد.")

################### create_order_create_person #########################

    def enter_click_create_order_create_person(self):
        wait_until_element_has_an_attribute(self, 'xpath', click_create_order_create_person)
        # self.driver.find_element('xpath', click_create_order_create_person).click()

    def enter_create_order_create_person_phon1(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', create_order_create_person_phon1, text)

    def enter_assert_create_order_create_person_representation(self):
        sleep(1)
        a = self.driver.find_element('xpath', create_order_create_person_representation).get_attribute('value')
        print(a)
        assert a == "Alborz Agency"
        print("نمایندگی به درستی نمایش داده می شود.")

    def enter_create_order_create_person_language(self):
        wait_until_element_has_an_attribute(self, 'xpath', create_order_create_person_language)

    def enter_create_order_create_person_language_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', create_order_create_person_language_option)

    def enter_create_order_create_person_submit(self):
        sleep(2)
        scrolled = self.driver.find_element('xpath', create_order_create_person_submit)
        sleep(2)
        scrolled.location_once_scrolled_into_view
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', create_order_create_person_submit)

    def enter_create_order_create_person_check_form(self):
        if self.driver.find_elements('xpath', persons_create_firstname
                                     and persons_create_lastname
                                     and persons_create_firstname_en
                                     and persons_create_lastname_en
                                     and persons_create_gender
                                     and persons_create_email
                                     and persons_create_non_iranian_nationals
                                     and persons_create_code_melli
                                     and create_order_create_person_phon1
                                     and persons_create_phone_number2
                                     and persons_create_phone1
                                     and persons_create_phone2
                                     and persons_create_company_phone
                                     and persons_create_company_name
                                     and persons_create_postalcode
                                     and persons_create_address
                                     and persons_create_how_find_us
                                     and persons_create_description
                                     and create_order_create_person_language
                                     ):
            print("تمامی فیلد های فرم مشاهده شدند")
        else:
            print("فیلد های فرم به درستی مشاهده نشدند")

    def enter_create_order_create_person_check_selection(self):
        el1 = len(self.driver.find_elements('xpath', persons_create_check_input))
        el2 = len(self.driver.find_elements('xpath', persons_create_check_select))
        sum_el = el1+el2
        print(sum_el)
        assert sum_el == 21

################### new_person #########################

    def enter_new_person_first_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_first_name, text)

    def enter_new_person_last_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_last_name, text)

    def enter_new_person_first_name_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_first_name_en, text)

    def enter_new_person_last_name_en(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_last_name_en, text)

    def enter_new_person_codemelli(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_codemelli, text)

    def enter_new_person_gender(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_gender)

    def enter_new_person_gender_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_gender_option)

    def enter_new_person_email(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_email, text)

    def enter_new_person_how_find_us(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_how_find_us)

    def enter_new_person_how_find_us_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_how_find_us_option)

    def enter_new_person_new_password(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_new_password, text)

    def enter_new_person_new_password_repeat(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_new_password_repeat, text)

    def enter_new_person_gender2(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_gender2)

    def enter_new_person_gender2_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_gender2_option)

    def enter_new_person_language(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_language)

    def enter_new_person_language_option(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_language_option)

    def enter_new_person_mobile2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_mobile2, text)

    def enter_new_person_phone1(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_phone1, text)

    def enter_new_person_phone2(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_phone2, text)

    def enter_new_person_postalcode(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_postalcode, text)

    def enter_new_person_address(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', new_person_address, text)

    def enter_new_person_btn(self):
        scrolled = self.driver.find_element('xpath', new_person_btn)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', new_person_btn)

    def enter_new_person_check_form(self):
        if self.driver.find_elements('xpath', persons_create_firstname
                                     and new_person_first_name
                                     and new_person_last_name
                                     and new_person_first_name_en
                                     and new_person_last_name_en
                                     and new_person_codemelli
                                     and new_person_gender
                                     and new_person_email
                                     and new_person_how_find_us
                                     and new_person_new_password
                                     and new_person_new_password_repeat
                                     and new_person_gender2
                                     and new_person_language
                                     and new_person_mobile2
                                     and new_person_phone1
                                     and new_person_phone2
                                     and new_person_postalcode
                                     and new_person_address
                                     and new_person_btn
                                     ):
            print("تمامی فیلد های فرم مشاهده شدند")
        else:
            print("فیلد های فرم به درستی مشاهده نشدند")

    def enter_new_person_profile_edit(self):
        wait_until_element_has_an_attribute(self, 'xpath', new_person_profile_edit)








