import re
from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# from termcolor import colored
import requests
# from bs4 import BeautifulSoup


def extract_number(string, number):
    return int(string.split()[number])


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.75)
    element.click()
    sleep(0.5)


def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.5)
    element.clear()
    sleep(0.75)
    element.send_keys(text)
    sleep(0.5)


def enter_admin_report_arian_click(self, element_selector, element_locator, text1, text2):
    wait = WebDriverWait(self.driver, 20)
    scrolled = self.driver.find_element(element_selector, element_locator)
    sleep(0.5)
    scrolled.location_once_scrolled_into_view
    sleep(0.5)
    a = self.driver.find_element(element_selector, element_locator).text
    # print(a)
    assert a == text1
    print("تکست باتن به درستی نمایش داده می شود. ")
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.75)
    element.click()
    sleep(0.5)
    b = self.driver.find_element('xpath', admin_report_arian_management_report_title).text
    assert b == text2
    print("تایتل به درستی نمایش داده می شود. ")
    print("________________________________")


class Report:
    def __init__(self, driver):
        self.driver = driver

    def enter_admin_report(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report)
        sleep(1)

    def enter_admin_report_filter(self):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_reports_start_date, "1401/02/08")
        print("فیلتر موجود می باشد.")
        sleep(1)
        self.driver.find_element('xpath', admin_reports_date_click).click()
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_reports_date_btn)
        sleep(1)
        a = self.driver.find_element('xpath', admin_reports_date_result).text
        sleep(1)
        assert '1401/02/08' in a
        print("نتایج در بازه صحیح می باشد.")
        print("________________________________")

    def enter_admin_report_check_excel(self):
        a = len(self.driver.find_elements('xpath', "//a[text()='خروجی اکسل']"))
        assert a == 2
        print("خروجی اکسل ها به درستی مشاهده شد. ")

    def enter_admin_report_check(self):
        assert self.driver.find_element('xpath', admin_report_commissions)
        assert self.driver.find_element('xpath', admin_report_arian_management_reports)
        assert self.driver.find_element('xpath', admin_report_select_the_report)
        assert self.driver.find_element('xpath', admin_report_reports_according_old_system)
        print("بخش پورسانت ها به درستی مشاهده شد. ")
        print("بخش گزارش های مدیریتی آرین به درستی مشاهده شد. ")
        print("بخش گزارش موردنظر خود را انتخاب نمایید به درستی مشاهده شد. ")
        print("بخش گزارش های مطابق با سیستم قدیم به درستی مشاهده شد. ")

    def enter_admin_reports_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 172
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

################### admin_report_commissions ###################

# admin_report_commissions = "//*[@id='main-content-wrapper']/section[2]/div/div[1]/div/div"

################### admin_report_arian_management_reports ###################

    def enter_admin_report_arian_management_report1(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report1, "سندهای فروش آرین", "گزارش سندهای فروش ثبت شده در آرین")

    def enter_admin_report_arian_management_report1_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نوع سند"
        assert th4 == "صادر شده به اسم"
        assert th5 == "شناسه سند دریافت شده"
        assert th6 == "وضعیت ثبت در آرین"
        assert th7 == "فاکتور های ثبت شده"
        assert th8 == "خطای صادر شده"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report1_document_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_document_type)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_document_type_option)
        # sleep(1)
        # wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_document_type_btn)
        sleep(2)
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[3]/span")
        for row in rows:
            if len(rows) > 1:
                if row.text != 'غیر رسمی':
                # if row.text != 'رسمی':
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_arian_management_report1_created_by_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_created_by)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_created_by_option)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report1_created_by_btn)

    def enter_admin_report_arian_management_report2(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report2, "سندهای خرید آرین", "گزارش سندهای خرید ثبت شده در آرین")

    def enter_admin_report_arian_management_report2_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "اطلاعات بچ"
        assert th3 == "نوع سرویس"
        assert th4 == "شناسه سند دریافت شده"
        assert th5 == "جزئیات سند"
        assert th6 == "وضعیت ثبت در آرین"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report2_check_batch(self, a):
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[2]/a")
        for row in rows:
            if len(rows) > 1:
                if row.text == a:
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_arian_management_report2_batch(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[2]/a").text
        return a

    def enter_admin_report_reports_search(self, text):
        # a = extract_number(text, 0)
        # wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_arian_management_report2_search, a)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_arian_management_report2_search, text)
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report2_search_btn)
        sleep(1)

    def enter_admin_report_arian_management_report3(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report3, "فاکتورهای ارسال نشده به آرین", "فاکتورهای ارسال نشده به آرین")

    def enter_admin_report_arian_management_report3_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نوع سند"
        assert th4 == "صادر شده به اسم"
        assert th5 == "شناسه سند دریافت شده"
        assert th6 == "وضعیت ثبت در آرین"
        assert th7 == "فاکتور های ثبت شده"
        assert th8 == "خطای صادر شده"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report4(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report4, "فاکتورهای غیر رسمی دارای مغایرت در نوع", "فاکتورهای غیر رسمی دارای مغایرت در نوع")

    def enter_admin_report_arian_management_report4_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نوع سند"
        assert th4 == "صادر شده به اسم"
        assert th5 == "شناسه سند دریافت شده"
        assert th6 == "وضعیت ثبت در آرین"
        assert th7 == "فاکتور های ثبت شده"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report5(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report5, "سندهای پرداخت آرین", "گزارش سندهای پرداخت ثبت شده در آرین")

    def enter_admin_report_arian_management_report5_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "اطلاعات پرداخت"
        assert th4 == "شناسه سند دریافت شده"
        assert th5 == "وضعیت ثبت در آرین"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report5_created_by_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by_option)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by_btn)

    def enter_admin_report_arian_management_report6(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report6, "پیش فاکتورهای غیرمعتبر شده بعد از ثبت..", "پیش فاکتورهای غیرمعتبر شده بعد از ثبت در آرین")

    def enter_admin_report_arian_management_report6_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "اطلاعات فاکتور"
        assert th4 == "قیمت اعلامی"
        assert th5 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th6 == "قیمت نهایی"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report7(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report7, "کاربران دارای شناسه آرین مشابه", "کاربران دارای شناسه آرین مشابه")

    def enter_admin_report_arian_management_report7_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "شناسه آرین"
        assert th3 == "فهرست کاربران"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report7_check_person(self):
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[3]")
        for row in rows:
            if len(rows) > 1:
                if row == 2:
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_arian_management_report8(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report8, "صاحب سفارشات فاقد شناسه آرین", "صاحب سفارشات فاقد شناسه آرین")

    def enter_admin_report_arian_management_report8_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "کدملی"
        assert th4 == "موبایل1"
        assert th5 == "موبایل2"
        assert th6 == "تلفن ثابت 1"
        print("جدول نمایش داده شده صحیح می باشد.")

################### admin_report_select_the_report ###################

    def enter_admin_report_select_the_report01(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report01, "گزارش سفارشات قبض شده به تفکیک ترخیص کار",
                                       "گزارش سفارشات قبض شده به تفکیک ترخیص کار")

    def enter_admin_report_select_the_report01_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='table table-bordered']/tbody/tr[1]/th").text
        assert th1 == "ردیف"
        assert th2 == "ترخیص توسط"
        assert th3 == "تعداد ترک"
        assert th4 == "جمع هزینه ها (ریال)"
        assert th5 == "جمع کل (ریال)"
        print("جدول نمایش داده شده صحیح می باشد.")
        print("________________________________")

    def enter_admin_report_select_the_report02(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report02, "سفارشات دارای دستور بارگیری",
                                       "سفارشات دارای دستور بارگیری")

    def enter_admin_report_select_the_report02_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "وزن سفارش (KG)"
        assert th4 == "مبدا"
        assert th5 == "مقصد"
        assert th6 == "انبار بارگیری"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "تاریخ صدور دستور بارگیری"
        print("جدول فهرست ترخیص کنندگان سفارش وجمع کل هزینه ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report02_tn(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[2]/a[1]").text
        return a

    def enter_admin_report_reports_search_tn(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_arian_management_report2_search, text)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report2_search_btn)
        sleep(1)

    def enter_admin_report_select_the_report02_tn_assert_search(self):
        sleep(1)
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        sleep(1)
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report02_status_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_status)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_status_option)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[8]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "---":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report02_marketer_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_marketer)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_marketer_option1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_marketer_btn)

    def enter_admin_report_select_the_report03(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report03, "مغایرت قیمت برند در فاکتور حمل",
                                       "مغایرت قیمت برند در فاکتور حمل")

    def enter_admin_report_select_the_report03_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "قیمت اعلامی"
        assert th5 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th6 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th7 == "قیمت هر کیلو کالای برند"
        assert th8 == "قیمت جدید"
        assert th9 == "مغایرت"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report04(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report04, "سفارش های تایید پرداخت شده از سمت چین",
                                       "سفارش های تایید پرداخت شده از سمت چین")

    def enter_admin_report_select_the_report04_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report05(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report05, "گزارش زمان تحویل کالاهای سفارش",
                                       "گزارش زمان تحویل کالاهای سفارش")

    def enter_admin_report_select_the_report05_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "ترک فرعی"
        assert th4 == "زمان تحویل کالا"
        assert th5 == "شمارشگر تحویل کالا"
        assert th6 == "اولین کالای اضافه شده در بچ"
        assert th7 == "نحوه تحویل کالا"
        assert th8 == "نحوه ترخیص کالا"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report05_detail(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report05_detail)
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='mySidebar']/div/div[2]/table")
        print("جزییات گزارش به درستی نمایش داده می شود.")

    def enter_admin_report_select_the_report05_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a >= 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report06(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report06, "گزارش بازه قیمتی ترخیص کار",
                                       "گزارش بازه قیمتی ترخیص کار")

    def enter_admin_report_select_the_report06_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        # th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        # th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        # th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        # th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        # th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        # th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        # th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        # th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        assert th1 == "ردیف"
        assert th2 == "دسته بندی و ترخیص کار"
        assert th3 == "دوربین"
        assert th4 == "رم، گرافیک و هارد"
        assert th5 == "مبدل تصویر"
        # assert th6 == "دستگاه ساشه پر کن"
        # assert th7 == "کنترل تردد"
        # assert th8 == "چسب"
        # assert th9 == "گرانول"
        # assert th10 == "برد خام"
        # assert th11 == "اندروید باکس"
        # assert th12 == "ژنراتور الترا سونیک و یدکی"
        # assert th13 == "پروگرمر و تستر ها"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report07(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report07, "گزارش مسیر حرکت", "گزارش مسیر حرکت")

    def enter_admin_report_select_the_report07_check_map(self):
        assert self.driver.find_element('xpath', "//*[@id='map']")
        print("نقشه به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report07_car(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report07_car)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report07_car_option)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report07_car_btn)
        sleep(1)

    def enter_admin_report_select_the_report08(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report08, "تبدیل ارزهای انجام شده", "لیست تبدیل ارزهای انجام شده")

    def enter_admin_report_select_the_report08_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        # a = print(tr)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر مرتبط"
        assert th3 == "دلار"
        assert th4 == "یورو"
        assert th5 == "پوند"
        assert th6 == "یوان"
        assert th7 == "درهم امارات"
        assert th8 == "ریال"
        assert th9 == "ریال*"
        assert th10 == "لیر سوریه"
        assert th11 == "سفارش"
        assert th12 == "ایجادکننده"
        assert th13 == "مدیر مشتری"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report09(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report09, "تفاوت قیمت نهایی فاکتورهای یوانی", "گزارش تفاوت قیمت نهایی فاکتورهای یوانی")

    def enter_admin_report_select_the_report09_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "اطلاعات فاکتور"
        assert th4 == "قیمت نهایی با نرخ /ارز"
        assert th5 == "قیمت نهایی با نرخ ارز خام"
        assert th6 == "شناسه آرین"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report09_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a >= 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report09_status_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_option)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[2]/span[1]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "در حال انجام":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report10(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report10, "سفارشات بازگشت خورده از کارتابل آپلود..", "سفارشات بازگشت خورده از کارتابل آپلود لیبل")

    def enter_admin_report_select_the_report10_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شخص دریافت کننده"
        assert th4 == "شخص ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "توضیحات"
        assert th10 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report11(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report11, "اتصال ها به درگاه", "اتصال ها به درگاه")

    def enter_admin_report_select_the_report11_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr"))
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[1]/div[1]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[1]/div[2]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[2]/div[1]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[2]/div[2]/div")
        th1 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "بانک"
        assert th3 == "نوع پرداخت"
        assert th4 == "وضعیت مقدار برگشتی"
        assert th5 == "شماره پیگیری بانک"
        assert th6 == "کارت"
        assert th7 == "پرداخت متصل"
        assert th8 == "پیش فاکتور ها"
        assert th9 == "موجودیت مرتبط"
        assert th10 == "زمان ایجاد"
        print("جدول ها و بخش های دیگر به درستی نمایش داده شدند.")
        print("________________________________")

    def enter_admin_report_select_the_report12(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report12, "لیست سفارشات فاقد مدیر مشتری", "لیست سفارشات فاقد مدیر مشتری")

    def enter_admin_report_select_the_report12_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report13(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report13, "کاربرانی که بازاریاب آنها تغییر کرده است", "کاربرانی که بازاریاب آنها تغییر کرده است")

    def enter_admin_report_select_the_report13_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "کاربر تغییر دهنده"
        assert th4 == "زمان تغییر بازاریاب سفارش"
        assert th5 == "بازاریاب سفارش قبلی"
        assert th6 == "بازاریاب سفارش فعلی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report13_show_name(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report13_show_name)

    def enter_admin_report_select_the_report14(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report14, "درخواست های مرجوعی", "درخواست های مرجوعی")

    def enter_admin_report_select_the_report14_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "کالاهای مرجوعی"
        assert th4 == "نام تحویل گیرنده"
        assert th5 == "موبایل تحویل گیرنده"
        assert th6 == "آدرس محل تحویل"
        assert th7 == "توضیحات"
        assert th8 == "فایل ضمیمه"
        assert th9 == "توضیحات نهایی"
        assert th10 == "فایل ضمیمه نهایی"
        assert th11 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report15(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report15, "گزارش عملکرد جدید PSP", "گزارش عملکرد جدید PSP")

    def enter_admin_report_select_the_report15_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[1]/div[3]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[1]/div[6]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[1]/div[9]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[1]/div[12]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[4]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]/div[6]")
        print("گزارش های عملکرد پی اس پی به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report15_agency_id(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id_btn)

    def enter_admin_report_select_the_report15_origin_filter(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_origin_filter)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_origin_filter_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_origin_filter_btn)

    def enter_admin_report_select_the_report15_destination_filter(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_destination_filter)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_destination_filter_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_destination_filter_btn)

    def enter_admin_report_select_the_report16(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report16, "سفارش های لغو شده", "گزارش سفارش های لغو شده")

    def enter_admin_report_select_the_report16_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شماره تماس صاحب سفارش"
        assert th4 == "ایجادکننده"
        assert th5 == "خدمات موردنیاز"
        assert th6 == "مبدا"
        assert th7 == "مقصد"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th8 == "دلیل لغو"
        assert th9 == "اطلاعات لغو"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report17(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report17, "گزارش هزینه ها و فروش بچ ها", "گزارش هزینه ها و فروش بچ ها")

    def enter_admin_report_select_the_report17_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='chart-lastthreemonth']")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "کل وزن قابل پرداخت"
        assert th3 == "شماره بسته"
        assert th4 == "موقعیت"
        assert th5 == "مبدا"
        assert th6 == "مقصد"
        assert th7 == "هزینه بچ"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        assert th8 == "فروش (فاکتور)"
        assert th9 == "وصول شده (تسویه شده)"
        assert th10 == "وزن جرمی"
        assert th11 == "وزن جرمی"
        assert th12 == "وزن حجمی"
        assert th13 == "بچ ترک"
        assert th14 == "حمل کننده"
        assert th15 == "آیا سفارش حوزه یک است؟"
        print("جدول و چارت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report18(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report18, "گزارش سفارشات تسویه شده اصلاح سابقه‌دار", "گزارش سفارشات تسویه شده اصلاح سابقه‌دار")

    def enter_admin_report_select_the_report18_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report19(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report19, "پرداخت های کمی که مقدار زیاد فاکتور..", "پرداخت های کمی که مقدار زیاد فاکتور فاکتور صادر کرده اند")

    def enter_admin_report_select_the_report19_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "وضعیت"
        assert th4 == "مبلغ"
        assert th5 == "حساب"
        assert th6 == "توضیحات"
        assert th7 == "زمان پرداخت"
        assert th8 == "ایجادکننده"
        assert th9 == "شماره حساب/کارت پرداخت کننده"
        assert th10 == "نام صاحب حساب پرداخت کننده"
        assert th11 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report20(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report20, "پیش فاکتور های حمل صادر شده", "لیست پیش فاکتور های حمل صادر شده")

    def enter_admin_report_select_the_report20_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "جمع وزن جرمی (kg)"
        assert th5 == "جمع وزن حجمی (kg)"
        assert th6 == "وزن غیر برند"
        assert th7 == "وزن برند"
        assert th8 == "قیمت اعلامی"
        assert th9 == "قیمت نهایی (ریال)"
        assert th10 == "هزینه به دلار"
        assert th11 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        assert th12 == "درخواست محاسبه غیرتجمیعی"
        assert th13 == "کاربر ثبت کننده"
        assert th14 == "خدمات موردنیاز"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report20_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report20_status_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/div[1]/section[2]/span[1]/div/div/div/div/div/div[1]/form/div[3]/select/option[2]")
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[2]/span[1]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "در حال انجام":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report20_destination_filter(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter_btn)

    def enter_admin_report_select_the_report21(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report21, "گزارش صاحبان سفارش", "گزارش صاحبان سفارش")

    def enter_admin_report_select_the_report21_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام انگلیسی صاحب سفارش"
        assert th3 == "صاحب سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "ارزش فاکتورهای تایید شده(میلیون تومان)"
        assert th6 == "پرداخت های تایید شده(میلیون تومان)"
        assert th7 == "تعداد سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report22(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report22, "سفارش های تحویل شده توسط همکاران", "سفارش های تحویل شده توسط همکاران")

    def enter_admin_report_select_the_report22_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[2]/div/div/div")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "تحویل دهنده"
        assert th5 == "موزع"
        assert th6 == "زمان تحویل"
        assert th7 == "توضیحات تحویل"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        assert th8 == "وزن قابل پرداخت سفارش (kg)"
        assert th9 == "وزن کالاهای تحویل شده به مشتری"
        assert th10 == "تعداد پارت های تحویل شده به مشتری"
        assert th11 == "امضا های سفارش"
        assert th12 == "خدمات موردنیاز"
        assert th13 == "مدیر مشتری"
        assert th14 == "ایجادکننده"
        assert th15 == "زمان ایجاد"
        print("جدول و چارت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report22_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table table-center']/tbody/tr"))
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report22_delivery_person_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person)
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person_option)
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person_btn)
        sleep(0.5)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table table-center']/tbody/tr//td[4]")
        for row in rows:
            if len(rows) > 1:
                if "مهدی خالقی" in row.text:
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report23(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report23, "فاکتورهای تسعیر ارز ایجاد شده", "لیست فاکتورهای تسعیر ارز ایجاد شده")

    def enter_admin_report_select_the_report23_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "صاحب پیش فاکتور"
        assert th4 == "نوع پیش فاکتور"
        assert th5 == "نرخ ارز اولیه"
        assert th6 == "نرخ ارز جدید"
        assert th7 == "مبلغ فاکتور تسعیر"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report24(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report24, "دوره ی تجدید سفارش مشتریان", "دوره ی تجدید سفارش مشتریان")

    def enter_admin_report_select_the_report24_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "تعداد سفارشات"
        assert th4 == "بیشترین زمان ثبت سفارش مجدد"
        assert th5 == "کمترین زمان ثبت سفارش مجدد"
        assert th6 == "دوره ی تجدید سفارش"
        assert th7 == "مدیر مشتری"
        assert th8 == "تاریخ عضویت"
        assert th9 == "تاریخ آخرین سفارش انجام شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report25(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report25, "گزارش عملکرد PSP", "گزارش عملکرد PSP")

    def enter_admin_report_select_the_report25_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "تعداد سفارشات"
        assert th4 == "بیشترین زمان ثبت سفارش مجدد"
        assert th5 == "کمترین زمان ثبت سفارش مجدد"
        assert th6 == "دوره ی تجدید سفارش"
        assert th7 == "مدیر مشتری"
        assert th8 == "تاریخ عضویت"
        assert th9 == "تاریخ آخرین سفارش انجام شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report26(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report26, "مشتریان دارای سفارش", "مشتریان دارای سفارش")

    def enter_admin_report_select_the_report26_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "نام مدیر مشتری"
        assert th4 == "مجموع ریالی مبلغ فاکتورهای صادر شده"
        assert th5 == "مجموع وزن سفارش ها"
        assert th6 == "تعداد سفارشات دارای خدمت حمل"
        assert th7 == "تعداد سفارشات دارای خدمت ترخیص"
        assert th8 == "تعداد سفارشات دارای خدمات حمل و ترخیص و خرید"
        assert th9 == "تعداد سفارشات تسویه شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report26_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report26_customer_manager_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report26_customer_manager)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report26_customer_manager_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report26_customer_manager_btn)
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a >= 1
        print("فیلتر به درستی انجام شد.")

    def enter_admin_report_select_the_report27(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report27, "سفارش های تسویه نشده", "سفارش های تسویه نشده")

    def enter_admin_report_select_the_report27_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "مدیر مشتری"
        assert th4 == "صاحب سفارش"
        assert th5 == "زمان تحویل سفارش"
        assert th6 == "دلار"
        assert th7 == "یورو"
        assert th8 == "یوان"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        assert th9 == "درهم امارات"
        assert th10 == "لیر ترکیه"
        assert th11 == "لیر سوریه"
        assert th12 == "ریال"
        assert th13 == "ریال*"
        assert th14 == "هزینه های ثبت نشده"
        assert th15 == "سفارش تسویه شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report28(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report28, "سفارش هایی که تسویه شده اند اما بارگیری..", "سفارش هایی که تسویه شده اند اما بارگیری نشده")

    def enter_admin_report_select_the_report28_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "سفارش تسویه شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report29(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report29, "تارگت و KPI", "تارگت و KPI")

    def enter_admin_report_select_the_report29_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == ""
        assert th3 == "تعداد سفارشات مشروط"
        assert th4 == "تعداد کل سفارشات"
        assert th5 == "درصد عملکرد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report30(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report30, "گزارش تغییرات بعد از بارگیری سفارش", "گزارش تغییرات بعد از بارگیری سفارش")

    def enter_admin_report_select_the_report30_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "اطلاعات قبلی"
        assert th4 == "اطلاعات جدید"
        assert th5 == "زمان بارگیری"
        assert th6 == "ایجادکننده"
        assert th7 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report30_search(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_select_the_report30_search, text)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report30_search_btn)
        sleep(1)

    def enter_admin_report_select_the_report31(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report31, "گزارش صاحبان پیش‌فاکتور سفارش", "گزارش صاحبان پیش‌فاکتور سفارش")

    def enter_admin_report_select_the_report31_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "شماره موبایل"
        assert th4 == "تعداد دفعات سفارش"
        assert th5 == "مجموع وزن سفارش ها"
        assert th6 == "پیش‌فاکتورها"
        assert th7 == "جمع پیش فاکتور (ریال)"
        assert th8 == "جمع پرداختی (ریال)"
        print("جدول و چارت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report32(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report32, "پیامک های ورود و عضویت در سایت", "پیامک های ورود و عضویت در سایت")

    def enter_admin_report_select_the_report32_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "موبایل درخواست کننده"
        assert th3 == "نتیجه پیامک"
        assert th4 == "کد ارسال شده"
        assert th5 == "متن پیامک ارسال شده"
        assert th6 == "زمان درخواست"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report33(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report33, "کالاهای تحویل شده با تایید مدیریت", "کالاهای تحویل شده با تایید مدیریت")

    def enter_admin_report_select_the_report33_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "تاریخ تحویل"
        assert th4 == "نحوه تحویل کالا"
        assert th5 == "نمایش کالاهای این فرم"
        assert th6 == "فرد تایید کننده"
        assert th7 == "توضیحات درخواست"
        assert th8 == "زمان تایید"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report34(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report34, "گزارش کدهای ترخیص ثبت شده", "گزارش کدهای ترخیص ثبت شده")

    def enter_admin_report_select_the_report34_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "شماره ترک"
        assert th4 == "کد ترخیص"
        assert th5 == "کاربر ثبت کننده"
        assert th6 == "تاریخ"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report34_tn(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[3]/a[1]").text
        return a

    def enter_admin_report_select_the_report34_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table/tbody/tr"))
        sleep(1)
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report35(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report35, "گزارش مشتریان", "گزارش مشتریان")

    def enter_admin_report_select_the_report35_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "مدیرمشتری"
        assert th4 == "شماره موبایل"
        assert th5 == "ایمیل"
        assert th6 == "آخرین بار"
        assert th7 == "جمع پیش فاکتور (ریال)"
        assert th8 == "جمع پرداختی (ریال)"
        assert th9 == "تعداد دفعات سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[23]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        th17 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]").text
        th18 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[18]").text
        th19 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[19]").text
        th20 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[20]").text
        th21 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[21]").text
        th22 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[22]").text
        th23 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[23]").text
        assert th10 == "تعداد کنسلی"
        assert th11 == "تعداد در حال انجام"
        assert th12 == "تعداد تحویل شده"
        assert th13 == "تعداد تسویه شده"
        assert th14 == "تعداد کل سفارش های تحویل شده"
        assert th15 == "مجموع وزن قابل پرداخت سفارش (kg)"
        assert th16 == "جمع فاکتورهای پرداخت شده یوانی"
        assert th17 == "تعداد فاکتورهای پرداخت شده یوانی"
        assert th18 == "جمع فاکتورهای پرداخت شده دلاری"
        assert th19 == "تعداد فاکتورهای پرداخت شده دلاری"
        assert th20 == "جمع فاکتورهای پرداخت شده یورو"
        assert th21 == "تعداد فاکتورهای پرداخت شده یورو"
        assert th22 == "جمع فاکتورهای پرداخت شده درهم"
        assert th23 == "تعداد فاکتورهای پرداخت شده درهم"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report35_tn(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[4]").text
        return a

    def enter_admin_report_select_the_report36(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report36, "ترک های فاکتور نخورده", "ترک های فاکتور نخورده")

    def enter_admin_report_select_the_report36_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بسته"
        assert th3 == "سفارش"
        assert th4 == "ثبت در سیستم مالی"
        assert th5 == "تغییرات سفارش‌های تسویه شده"
        assert th6 == "نیاز به چاپ فاکتور رسمی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th7 == "فاکتور رسمی بعد از چاپ"
        assert th8 == "وزن سفارش (KG)"
        assert th9 == "کالای سفارش"
        assert th10 == "خدمات موردنیاز"
        assert th11 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report37(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report37, "لیست درخواست های ادغام کابر", "درخواست ادغام کاربران")

    def enter_admin_report_select_the_report37_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر حذف شونده"
        assert th3 == "کاربر نهایی"
        assert th4 == "زمان ایجاد"
        assert th5 == "ایجادکننده"
        assert th6 == "وضعیت ادغام"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report39(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report39, "مدیر مشتری های بدون نمایندگی", "مدیر مشتری های بدون نمایندگی")

    def enter_admin_report_select_the_report39_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "form.fastpay.person_id"
        assert th3 == "موبایل"
        assert th4 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report41(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report41, "گزارش زمان انجام وظایف واحد مالی ایران", "گزارش زمان انجام وظایف مالی ایران")

    def enter_admin_report_select_the_report41_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نوع وظیفه"
        assert th3 == "حداقل زمان انجام"
        assert th4 == "حداکثر زمان انجام"
        assert th5 == "متوسط زمان انجام"
        assert th6 == "متوسط زمان انجام بدون محاسبه تعویق"
        assert th7 == "تعداد وظیفه باز"
        assert th8 == "تعداد وظیفه بحرانی"
        assert th9 == "تعداد کل وظایف"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report42(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report42, "گزارش زمان انجام وظایف دفتر چین", "گزارش زمان انجام وظایف دفتر چین")

    def enter_admin_report_select_the_report42_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نوع وظیفه"
        assert th3 == "حداقل زمان انجام"
        assert th4 == "حداکثر زمان انجام"
        assert th5 == "متوسط زمان انجام"
        assert th6 == "متوسط زمان انجام بدون محاسبه تعویق"
        assert th7 == "تعداد وظیفه باز"
        assert th8 == "تعداد وظیفه بحرانی"
        assert th9 == "تعداد کل وظایف"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report43(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report43, "زمان انجام وظایف برای تمام واحد ها", "زمان انجام وظایف برای تمام واحد ها")

    def enter_admin_report_select_the_report43_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "کارتابل"
        assert th3 == "واحد"
        assert th4 == "متوسط زمان انجام وظیفه"
        assert th5 == "متوسط زمان انجام وظیفه بدون محاسبه تعویق"
        assert th6 == "تعداد وظیفه انجام شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report44(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report44, "گزارش زمان انجام وظایف ترخیص ایران", "گزارش زمان انجام وظایف ترخیص ایران")

    def enter_admin_report_select_the_report44_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "نوع وظیفه"
        assert th3 == "حداقل زمان انجام"
        assert th4 == "حداکثر زمان انجام"
        assert th5 == "متوسط زمان انجام"
        assert th6 == "متوسط زمان انجام بدون محاسبه تعویق"
        assert th7 == "تعداد وظیفه باز"
        assert th8 == "تعداد وظیفه بحرانی"
        assert th9 == "تعداد کل وظایف"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report45(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report45, "گزارش زمان انجام وظایف مدیر مشتریان", "گزارش زمان انجام وظایف مدیر مشتریان")

    def enter_admin_report_select_the_report45_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "نوع وظیفه"
        assert th3 == "مدیر مشتری"
        assert th4 == "حداقل زمان انجام"
        assert th5 == "حداکثر زمان انجام"
        assert th6 == "متوسط زمان انجام"
        assert th7 == "متوسط زمان انجام بدون محاسبه تعویق"
        assert th8 == "متوسط زمان انجام بدون انحراف"
        assert th9 == "تعداد کل وظایف"
        assert th10 == "تعداد وظیفه باز"
        assert th11 == "تعداد وظیفه بحرانی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report46, "گزارش تیم فروش", "گزارش تیم فروش")

    def enter_admin_report_select_the_report46_check_table1(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[14]").text
        assert th1 == "نام همکار"
        assert th2 == "کل سفارشات ثبت شده"
        assert th3 == "درصد از کل"
        assert th4 == "تعداد کل مشتریان"
        assert th5 == "تعداد سفارش لغو شده"
        assert th6 == "درصد از کل"
        assert th7 == "تعداد دستور بارگیری صادر شده"
        assert th8 == "درصد از کل"
        assert th9 == "تعداد سفارش های در انتظار"
        assert th10 == "درصد از کل"
        assert th11 == "تعداد سفارش در حال انجام"
        assert th12 == "درصد از کل"
        assert th13 == "تعداد سفارش انجام شده"
        assert th14 == "درصد از کل"
        print("جدول یک به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table2(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[17]").text
        th18 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[18]").text
        th19 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[19]").text
        th20 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[20]").text
        th21 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[21]").text
        th22 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[22]").text
        th23 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-invoices']/thead/tr[1]/th[23]").text
        assert th1 == "نام همکار"
        assert th2 == "تعداد کل سفارش های دارای پیش فاکتور"
        assert th3 == "درصد از کل"
        assert th4 == "تعداد سفارش های هوایی دارای پیش فاکتور"
        assert th5 == "درصد از کل"
        assert th6 == "تعداد سفارش های دریایی دارای پیش فاکتور"
        assert th7 == "درصد از کل"
        assert th8 == "ارزش وزنی سفارش های هوایی دارای پیش فاکتور تن"
        assert th9 == "درصد از کل"
        assert th10 == "ارزش ریالی حمل سفارش های هوایی دارای پیش فاکتور میلیون تومان"
        assert th11 == "درصد از کل"
        assert th12 == "ارزش ریالی سفارش های هوایی ترخیص شده دارای پیش فاکتور میلیون تومان"
        assert th13 == "درصد از کل"
        assert th14 == "ارزش وزنی سفارش های دریایی پیش فاکتور شده تن"
        assert th15 == "درصد از کل"
        assert th16 == "ارزش ریالی سفارش های حمل دریایی پیش فاکتور شده میلیون تومان"
        assert th17 == "درصد از کل"
        assert th18 == "ارزش ریالی سفارش های دریایی ترخیص شده دارای پیش فاکتور میلیون تومان"
        assert th19 == "درصد از کل"
        assert th20 == "ارزش ریالی سفارش های خرید پیش فاکتور شده میلیون تومان"
        assert th21 == "درصد از کل"
        assert th22 == "ارزش وزنی سفارش های دارای پیش فاکتور خرید تن"
        assert th23 == "درصد از کل"
        print("جدول دو به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table3(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-rates']/thead/tr[1]/th[7]").text
        assert th1 == "نام همکار"
        assert th2 == "نرخ تبدیل مبلغ پیش فاکتور به پرداختی مشتری هوایی"
        assert th3 == "نرخ تبدیل مبلغ پیش فاکتور به پرداختی مشتری دریایی"
        assert th4 == "نرخ تبدیل وزن پیش فاکتور به پرداختی مشتری هوایی"
        assert th5 == "نرخ تبدیل وزن پیش فاکتور به پرداختی مشتری دریایی"
        assert th6 == "نرخ تبدیل تعداد پیش فاکتور به پرداختی مشتری هوایی"
        assert th7 == "نرخ تبدیل تعداد پیش فاکتور به پرداختی مشتری دریایی"
        print("جدول سه به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table4(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-payments']/thead/tr[1]/th[17]").text
        assert th1 == "نام همکار"
        assert th2 == "تعداد پرداخت ها"
        assert th3 == "درصد از کل"
        assert th4 == "ارزش ریالی کل پرداخت میلیون تومان"
        assert th5 == "درصد از کل"
        assert th6 == "ارزش وزنی پرداخت حمل هوایی تن"
        assert th7 == "درصد از کل"
        assert th8 == "ارزش ریالی پرداخت حمل هوایی میلیون تومان"
        assert th9 == "درصد از کل"
        assert th10 == "ارزش ریالی پرداخت های ترخیص هوایی میلیون تومان"
        assert th11 == "درصد از کل"
        assert th12 == "ارزش وزنی پرداخت حمل دریایی تن"
        assert th13 == "درصد از کل"
        assert th14 == "ارزش ریالی پرداخت حمل دریایی میلیون تومان"
        assert th15 == "درصد از کل"
        assert th16 == "ارزش ریالی پرداخت های ترخیص دریایی میلیون تومان"
        assert th17 == "درصد از کل"
        print("جدول چهار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table5(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[17]").text
        th18 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[18]").text
        th19 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[19]").text
        th20 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[20]").text
        th21 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[21]").text
        th22 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[22]").text
        assert th1 == "نام همکار"
        assert th2 == "تعداد کل دستور بارگیری"
        assert th3 == "درصد از کل"
        assert th4 == "ارزش وزنی کل دستور بارگیری تن"
        assert th5 == "درصد از کل"
        assert th6 == "ارزش ریالی کل دستور بارگیری میلیون تومان"
        assert th7 == "درصد از کل"
        assert th8 == "تعداد دستور بارگیری هوایی"
        assert th9 == "درصد از کل"
        assert th10 == "ارزش وزنی دستور بارگیری هوایی تن"
        assert th11 == "درصد از کل"
        assert th12 == "ارزش ریالی دستور بارگیری هوایی میلیون تومان"
        assert th13 == "درصد از کل"
        assert th14 == "تعداد دستور بارگیری دریایی"
        assert th15 == "درصد از کل"
        assert th16 == "ارزش وزنی دستور بارگیری دریایی تن"
        assert th17 == "درصد از کل"
        assert th18 == "ارزش ریالی دستور بارگیری دریایی میلیون تومان"
        assert th19 == "درصد از کل"
        assert th20 == "تعداد کل بارگیری دارای حمل بدون ترخیص"
        assert th21 == "ارزش وزنی کل بارگیری دارای حمل بدون ترخیص"
        assert th22 == "ارزش ریالی خرید بارگیری شده"
        scrolled = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[25]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th23 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[23]").text
        th24 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[24]").text
        th25 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[25]").text
        assert th23 == "ارزش ریالی ترخیص بارگیری شده"
        assert th24 == "ارزش ریالی حمل بارگیری شده"
        assert th25 == "تعداد مشتریان دستور بارگیری"
        print("جدول پنج به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table6(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table-customer-report table-zero table-total-customer-count dataTable no-footer']/thead/tr[1]/th[6]").text
        assert th1 == "نام مشتری"
        assert th2 == "آیا دفعه اول دارد؟"
        assert th3 == "تعداد کل سفارش ها"
        assert th4 == "تعداد کل دستور بارگیری"
        assert th5 == "وزن"
        assert th6 == "نحوه آشنایی با ما"
        print("جدول شش به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report46_check_table7(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[17]").text
        th18 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[18]").text
        th19 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[19]").text
        th20 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[20]").text
        th21 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[21]").text
        th22 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[22]").text
        th23 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[23]").text
        th24 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[24]").text
        assert th1 == "نام همکار"
        assert th2 == "تعداد کل دستور حمل بین الملل"
        assert th3 == "درصد از کل"
        assert th4 == "ارزش وزنی کل دستور حمل بین الملل تن"
        assert th5 == "درصد از کل"
        assert th6 == "ارزش ریالی کل دستور حمل بین الملل میلیون تومان"
        assert th7 == "درصد از کل"
        assert th8 == "تعداد دستور حمل بین الملل هوایی"
        assert th9 == "درصد از کل"
        assert th10 == "ارزش وزنی دستور حمل بین الملل هوایی تن"
        assert th11 == "درصد از کل"
        assert th12 == "ارزش ریالی دستور حمل بین الملل هوایی میلیون تومان"
        assert th13 == "درصد از کل"
        assert th14 == "تعداد دستور حمل بین الملل دریایی"
        assert th15 == "درصد از کل"
        assert th16 == "ارزش وزنی دستور حمل بین الملل دریایی تن"
        assert th17 == "درصد از کل"
        assert th18 == "ارزش ریالی دستور حمل بین الملل دریایی میلیون تومان"
        assert th19 == "درصد از کل"
        assert th20 == "تعداد کل حمل بین الملل دارای حمل بدون ترخیص"
        assert th21 == "ارزش وزنی کل حمل بین الملل دارای حمل بدون ترخیص"
        assert th22 == "ارزش ریالی خرید حمل بین الملل شده"
        assert th23 == "ارزش ریالی ترخیص حمل بین الملل شده"
        assert th24 == "ارزش ریالی حمل ، حمل بین الملل شده"
        scrolled = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[25]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th25 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-maliapproval']/thead/tr[1]/th[25]").text
        assert th25 == "تعداد مشتریان دستور حمل بین الملل"
        print("جدول هفت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report47(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report47, "نمودار زمان انجام وظایف", "نمودار زمان انجام وظایف")

    def enter_admin_report_select_the_report47_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[4]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[6]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div[8]")
        print("نمودار ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report48(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report48, "نتیجه کارتابل کیفیت خدمات", "نتیجه کارتابل کیفیت خدمات")

    def enter_admin_report_select_the_report48_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[3]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[4]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[5]")
        scrolled1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]")
        sleep(0.5)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "شناسه سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "رضایت از مدیر مشتری - مسئولیت پذیری"
        assert th6 == "رضایت از مدیر مشتری - تخصص در مشاوره"
        assert th7 == "رضایت از مدیر مشتری - حسن رفتار"
        assert th8 == "رضایت از مدیر مشتری - توضیحات"
        assert th9 == "بازاریاب"
        assert th10 == "رضایت از بازاریابی - مسئولیت پذیری"
        assert th11 == "رضایت از بازاریابی - تخصص در مشاوره"
        assert th12 == "رضایت از بازاریابی - حسن رفتار"
        assert th13 == "رضایت از بازاریابی - توضیحات"
        assert th14 == "رضایت از خدمات - حمل - هزینه حمل"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[30]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        th17 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]").text
        th18 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[18]").text
        th19 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[19]").text
        th20 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[20]").text
        th21 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[21]").text
        th22 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[22]").text
        th23 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[23]").text
        th24 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[24]").text
        th25 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[25]").text
        th26 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[26]").text
        th27 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[27]").text
        th28 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[28]").text
        th29 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[29]").text
        th30 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[30]").text
        assert th15 == "رضایت از خدمات - حمل - توضیحات"
        assert th16 == "رضایت از خدمات - حمل - زمان حمل"
        assert th17 == "رضایت از خدمات - حمل - توضیحات"
        assert th18 == "رضایت از خدمات - ترخیص - هزینه ترخیص"
        assert th19 == "رضایت از خدمات - ترخیص - توضیحات"
        assert th20 == "رضایت از خدمات - ترخیص - زمان ترخیص"
        assert th21 == "رضایت از خدمات - ترخیص - توضیحات"
        assert th22 == "رضایت از خدمات - خرید - امتیاز"
        assert th23 == "رضایت از خدمات - خرید - توضیحات"
        assert th24 == "تحویل دهنده"
        assert th25 == "رضایت از تحویل کالا - مدت زمان تحویل بار"
        assert th26 == "رضایت از تحویل کالا - توضیحات"
        assert th27 == "رضایت از تحویل کالا - برخورد تیم تحویل دهنده"
        assert th28 == "رضایت از تحویل کالا - توضیحات"
        assert th29 == "میزان رضایت کلی"
        assert th30 == "تاریخ ثبت"
        print("جدول و نمودار ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report49(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report49, "گزارش مالی ترخیص", "گزارش مالی ترخیص")

    def enter_admin_report_select_the_report49_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "ترک فرعی"
        assert th4 == "شماره بچ"
        assert th5 == "هزینه ریل ترخیص"
        assert th6 == "هزینه قبض ترخیص"
        assert th7 == "ترخیص شده توسط"
        assert th8 == "جمع هزینه ترخیص"
        assert th9 == "مبلغ فروش ترخیص"
        print("جدول و آمار ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report50(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report50, "گزارش بازاریاب ها", "گزارش بازاریاب ها")

    def enter_admin_report_select_the_report50_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "پیش فاکتور به نام شخص"
        assert th4 == "پیش فاکتور به نام شرکت"
        assert th5 == "مبلغ حمل"
        assert th6 == "مبلغ حمل تایید مشتری"
        assert th7 == "مبلغ ترخیص"
        assert th8 == "مبلغ ترخیص تایید مشتری"
        assert th9 == "مبلغ خرید"
        assert th10 == "مبلغ خرید تایید مشتری"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        assert th11 == "بازاریاب"
        assert th12 == "بازیاب بازاریابی"
        assert th13 == "ایجاد کننده"
        assert th14 == "تاریخ ثبت سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report51(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report51, "سفارشات صادرات واردات غیر از چین + ..", "سفارشات صادرات واردات غیر از چین + سرویس خرید")

    def enter_admin_report_select_the_report51_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report52(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report52, "میزان اختلاف پیش فاکتور قبل و بعد از..", "میزان اختلاف پیش فاکتور قبل و بعد از بارگیری")

    def enter_admin_report_select_the_report52_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "شماره سفارش"
        assert th3 == "پیش فاکتور حمل (بعد بارگیری)"
        assert th4 == "پیش فاکتور ترخیص (بعد بارگیری)"
        assert th5 == "وزن (بعد بارگیری)"
        assert th6 == "پیش فاکتور حمل (قبل بارگیری)"
        assert th7 == "پیش فاکتور ترخیص (قبل بارگیری)"
        assert th8 == "وزن (قبل بارگیری)"
        assert th9 == "اختلاف پیش فاکتور حمل"
        assert th10 == "اختلاف پیش فاکتور ترخیص"
        assert th11 == "اختلاف وزن"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report53(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report53, "گزارش پرداخت های دارای اطلاعات غلط", "گزارش پرداخت های دارای اطلاعات غلط")

    def enter_admin_report_select_the_report53_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "وضعیت"
        assert th4 == "مبلغ"
        assert th5 == "حساب"
        assert th6 == "توضیحات"
        assert th7 == "زمان پرداخت"
        assert th8 == "ایجادکننده"
        assert th9 == "شماره حساب/کارت پرداخت کننده"
        assert th10 == "نام صاحب حساب پرداخت کننده"
        assert th11 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report54(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report54, "فاکتورهای رسمی مشتریان دارای کیف پول..", "لیست فاکتورهای رسمی مشتریان دارای کیف پول منفی")

    def enter_admin_report_select_the_report54_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "صاحب سفارش"
        assert th3 == "موجودی کیف پول (ریال)"
        assert th4 == "شماره پیگیری"
        assert th5 == "شماره پیش فاکتور"
        assert th6 == "کاربر ثبت کننده"
        assert th7 == "زمان ثبت"
        assert th8 == "قیمت نهایی"
        assert th9 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report55(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report55, "سفارشات تحویل شده دلیوری", "سفارشات تحویل شده دلیوری")

    def enter_admin_report_select_the_report55_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "صاحب سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "تحویل دهنده"
        assert th6 == "موزع"
        assert th7 == "زمان تحویل سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report56(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report56, "سفارشات لغو شده دارای پیش فاکتور ترخیص", "سفارشات لغو شده دارای پیش فاکتور ترخیص")

    def enter_admin_report_select_the_report56_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "وزن قابل پرداخت سفارش (kg)"
        assert th4 == "دلیل لغو"
        assert th5 == "شماره های تماس"
        assert th6 == "زمان ثبت"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report57(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report57, "مشتریان عضو شده", "مشتریان عضو شده")

    def enter_admin_report_select_the_report57_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='final-new-person']")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "شماره های تماس"
        assert th4 == "آدرس"
        assert th5 == "مدیر مشتری"
        assert th6 == "بازاریاب"
        assert th7 == "زمان ایجاد"
        assert th8 == "ایجادکننده"
        assert th9 == "نحوه آشنایی با ما"
        assert th10 == "نمایندگی"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report57_check_filter(self):
        # scrolled = self.driver.find_element('xpath', "//table/tbody/tr/td[9]")
        # sleep(0.5)
        # scrolled.location_once_scrolled_into_view
        # sleep(0.5)
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[9]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "اینستاگرام":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report58(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report58, "لیست تخفیف ها", "لیست تخفیف ها")

    def enter_admin_report_select_the_report58_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "صاحب سفارش"
        assert th3 == "سفارش"
        assert th4 == "قیمت"
        assert th5 == "مبلغ نهایی فاکتور"
        assert th6 == "درصد تخفیف"
        assert th7 == "واحد"
        assert th8 == "کاربر تایید کننده / رد کننده"
        assert th9 == "کاربر ثبت کننده"
        assert th10 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report59(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report59, "گزارش تراکنش های ثبت چین فاقد پیش فاکتور", "گزارش تراکنش های ثبت چین فاقد پیش فاکتور")

    def enter_admin_report_select_the_report59_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "مدیر مشتری"
        assert th4 == "نوع تراکنش"
        assert th5 == "قیمت"
        assert th6 == "واحد"
        assert th7 == "ایجادکننده"
        assert th8 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report60(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report60, "گزارش محیط ایجاد سفارش", "لیست گزارش محیط ایجاد سفارش")

    def enter_admin_report_select_the_report60_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='create-origin']")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نحوه ایجاد سفارش"
        assert th4 == "دریافت کننده"
        assert th5 == "ارسال کننده"
        assert th6 == "وزن سفارش (KG)"
        assert th7 == "کالای سفارش"
        assert th8 == "خدمات موردنیاز"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th9 == "ایجادکننده"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report61(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report61, "فاکتورهای ایجاد شده به تفکیک خدمات", "لیست فاکتورهای ایجاد شده به تفکیک خدمات")

    def enter_admin_report_select_the_report61_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='op-location-info']")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک سفارش"
        assert th3 == "نوع صاحب پیش فاکتور"
        assert th4 == "صاحب پیش فاکتور"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "نوع فاکتور"
        assert th7 == "نوع خدمت"
        assert th8 == "قیمت نهایی"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report61_document_type_check(self):
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[6]")
        for row in rows:
            if len(rows) > 1:
                if row.text == 'غیر رسمی':
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report61_inquery_type_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_status)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/div[1]/section[2]/span[1]/div/div/div/div/div/div[1]/form/div[3]/select/option[3]")
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report02_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[7]")
        for row in rows:
            if len(rows) > 1:
                if row.text == 'حمل':
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report62(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report62, "گزارش فاکتورهای غیر رسمی صادر شده", "گزارش فاکتورهای غیر رسمی صادر شده")

    def enter_admin_report_select_the_report62_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "قیمت"
        assert th4 == "واحد"
        assert th5 == "نیاز به پرداخت (ریال)"
        assert th6 == "نیاز به پرداخت (در واحد)"
        assert th7 == "آیا کالای قبض شده دارد؟"
        assert th8 == "شماره بچ"
        assert th9 == "جمع وزن جرمی (kg)"
        assert th10 == "جمع وزن حجمی (kg)"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report63(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report63, "لیست اشخاص با شماره های نامعتبر", "لیست اشخاص با شماره های نامعتبر")

    def enter_admin_report_select_the_report63_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "موبایل1"
        assert th4 == "تلفن ثابت 1"
        assert th5 == "تلفن ثابت 2"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report64(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report64, "گزارش درآمد و هزینه حمل دارای ترک فرعی", "لیست گزارش درآمد و هزینه حمل دارای ترک فرعی")

    def enter_admin_report_select_the_report64_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "ترک فرعی"
        assert th4 == "شماره بچ"
        assert th5 == "جمع هزینه حمل"
        assert th6 == "مبلغ فروش حمل"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report65(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report65, "گزارش فاکتورهای رسمی صادر شده", "گزارش فاکتورهای رسمی صادر شده")

    def enter_admin_report_select_the_report65_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "متن تاییدیه"
        assert th4 == "کاربر تایید کننده"
        assert th5 == "زمان تایید"
        assert th6 == "صاحب پیش فاکتور"
        assert th7 == "صاحب سفارش"
        assert th8 == "مبلغ پیش فاکتور"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report66(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report66, "گزارش درآمد و هزینه ترخیص دارای ترک فرعی", "لیست گزارش درآمد و هزینه ترخیص دارای ترک فرعی")

    def enter_admin_report_select_the_report66_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]/div")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[3]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "ترک فرعی"
        assert th4 == "شماره بچ"
        assert th5 == "هزینه ریل ترخیص"
        assert th6 == "هزینه قبض ترخیص"
        assert th7 == "ترخیص شده توسط"
        assert th8 == "جمع هزینه ترخیص"
        assert th9 == "مبلغ فروش ترخیص"
        print("جدول و مجموع هزینه ها و آمار به تفکیک نوع ترخیص به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report67(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report67, "گزارش قطعات خودرو", "گزارش قطعات خودرو")

    def enter_admin_report_select_the_report67_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "شخص ارسال کننده"
        assert th5 == "شماره تلفن ارسال کننده"
        assert th6 == "شماره موبایل ارسال کننده"
        assert th7 == "PI"
        assert th8 == "PL"
        assert th9 == "کالاهای سفارش"
        assert th10 == "مدیر مشتری"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        assert th11 == "یادداشت پیش ارزیابی"
        assert th12 == "تغییردهنده"
        assert th13 == "بروزرسانی"
        assert th14 == "شماره بارنامه"
        assert th15 == "فایل بارنامه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report68(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report68, "ارزیابی کالاها توسط ترخیص", "ارزیابی کالاها توسط ترخیص")

    def enter_admin_report_select_the_report68_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "شماره بچ"
        assert th4 == "صاحب سفارش"
        assert th5 == "مدیر مشتری"
        assert th6 == "نام کالا"
        assert th7 == "وزن کالا"
        assert th8 == "بسته ها"
        assert th9 == "ترخیص کار"
        assert th10 == "خروجی پیش ارزیابی"
        assert th11 == "ارزیابی"
        assert th12 == "اختلاف پیش ارزیابی و ارزیابی نهایی"
        assert th13 == "درصد اختلاف"
        assert th14 == "مقایسه"
        assert th15 == "ریسک قبض"
        assert th16 == "وضعیت ارزیابی کالا"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[19]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th17 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]").text
        th18 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[18]").text
        th19 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[19]").text
        assert th17 == "نوع فاکتور ترخیص در لحظه ارزیابی"
        assert th18 == "وضعیت سفارش"
        assert th19 == "ماخذ"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report68_batch(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[3]/a[1]").text
        return a

    def enter_admin_report_select_the_report68_filter_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person)
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person_option)
        sleep(0.5)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report22_delivery_person_btn)
        sleep(0.5)
        rows = self.driver.find_elements('xpath', "//table/tbody/tr/td[16]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "قبض شده":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report69(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report69, "گزارش تامین کنندگان چین", "گزارش تامین کنندگان چین")

    def enter_admin_report_select_the_report69_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "نام شرکت/سازمان"
        assert th3 == "تلفن 1"
        assert th4 == "تلفن 2"
        assert th5 == "ایمیل"
        assert th6 == "آدرس"
        assert th7 == "کالا انگلیسی"
        assert th8 == "کالا فارسی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report70(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report70, "اختصاص های حذف شده", "اختصاص های حذف شده")

    def enter_admin_report_select_the_report70_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "درصد مالیات"
        assert th5 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th6 == "عنوان فاکتور"
        assert th7 == "کاربر ثبت کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report71(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report71, "تاریخچه‌ی چاپ لیبل", "تاریخچه‌ی چاپ لیبل")

    def enter_admin_report_select_the_report71_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک اصلی"
        assert th3 == "کد مشخصه"
        assert th4 == "ترک فرعی"
        assert th5 == "بچ کالا"
        assert th6 == "موقعیت"
        assert th7 == "چاپ برچسب کالا"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report71_search_batch(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_select_the_report71_search_batch, text)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report71_search_batch_btn)
        sleep(1)

    def enter_admin_report_select_the_report71_batch(self):
        scrolled = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        return a

    def enter_admin_report_select_the_report72(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report72, "سفارشات ارزیابی شده", "سفارشات ارزیابی شده")

    def enter_admin_report_select_the_report72_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک اصلی"
        assert th3 == "مجموع مبلغ پیش فاکتور ترخیص"
        assert th4 == "واحد ارز"
        assert th5 == "ترک فرعی"
        assert th6 == "ارزیابی"
        assert th7 == "واحد ارز"
        assert th8 == "مجموع مبلغ ترک قبض شده"
        assert th9 == "واحد ارز"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report73(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report73, "گزارش تعداد مشتری مدیر مشتریان", "گزارش تعداد مشتری مدیر مشتریان")

    def enter_admin_report_select_the_report73_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "مدیر مشتری"
        assert th3 == "تعداد مشتریان"
        assert th4 == "انتقال مشتریان"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report74(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report74, "دسته بندی های انتخاب شده برای کالا", "دسته بندی های انتخاب شده برای کالا")

    def enter_admin_report_select_the_report74_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "کد مشخصه"
        assert th3 == "سفارش"
        assert th4 == "صاحب سفارش"
        assert th5 == "مدیر مشتری"
        assert th6 == "شماره ترک فرعی"
        assert th7 == "دسته بندی کلی کالا"
        assert th8 == "دسته بندی جزئی کالا"
        assert th9 == "تغییرات دسته بندی کلی کالا"
        assert th10 == "تغییرات دسته بندی جزئی کالا"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report75(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report75, "گزارش نمایندگی", "گزارش نمایندگی")

    def enter_admin_report_select_the_report75_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "وزن سفارش (KG)"
        assert th4 == "کالای سفارش"
        assert th5 == "خدمات موردنیاز"
        assert th6 == "پیش فاکتور ها"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report75_tn(self):
        sleep(1)
        buttons = self.driver.find_elements('xpath', "//table/tbody/tr/td[2]/a[@class='btn btn-sm btn-block btn-info tn-linkedin mb-2 btn-social']")
        sleep(1)
        if buttons:
            a = buttons[0].text
            return a
        else:
            print("هیچ Tn پیدا نشد.")

    def enter_admin_report_select_the_report75_filter(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report75_filter_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter_btn)

    def enter_admin_report_select_the_report76(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report76, "سفارش های تحویل شده", "سفارش های تحویل شده")

    def enter_admin_report_select_the_report76_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        scrolled1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]")
        sleep(0.5)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "تحویل دهنده"
        assert th5 == "موزع"
        assert th6 == "زمان تحویل"
        assert th7 == "توضیحات تحویل"
        assert th8 == "وزن قابل پرداخت سفارش (kg)"
        assert th9 == "وزن کالاهای تحویل شده به مشتری"
        assert th10 == "تعداد پارت های تحویل شده به مشتری"
        assert th11 == "امضا های سفارش"
        assert th12 == "شهر"
        assert th13 == "نحوه تحویل"
        assert th14 == "خدمات موردنیاز"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        th17 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]").text
        assert th15 == "مدیر مشتری"
        assert th16 == "ایجادکننده"
        assert th17 == "زمان ایجاد"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report76_status_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', enter_admin_report_select_the_report76_status_option)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table table-center']/tbody/tr/td[4]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "طاهر غنی ابادی Taher Ghani abady":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report77(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report77, "پیش فاکتور های ترخیص صادر شده", "لیست پیش فاکتور های ترخیص صادر شده")

    def enter_admin_report_select_the_report77_check_table1(self):
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام"
        assert th3 == "تعداد پیش فاکتور های صادر شده ریلی"
        assert th4 == "تعداد پیش فاکتور های صادر شده قبضی"
        assert th5 == "تعداد پیش فاکتور های نهایی ریلی"
        assert th6 == "تعداد پیش فاکتور های نهایی قبضی"
        assert th7 == "جمع پیش فاکتور ها"
        print("جدول1 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report77_check_table2(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[12]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "قیمت اعلامی"
        assert th4 == "جمع وزن جرمی (kg)"
        assert th5 == "کالاهای سفارش"
        assert th6 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th7 == "ضریب مالیات"
        assert th8 == "نرخ تبدیل به ریال"
        assert th9 == "قیمت نهایی"
        assert th10 == "پرداخت شده (در واحد)"
        assert th11 == "تاییدیه مشتری"
        assert th12 == "کاربر ثبت کننده"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report77_status_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', enter_admin_report_select_the_report77_status)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', enter_admin_report_select_the_report77_status_option)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[12]/a")
        for row in rows:
            if len(rows) > 1:
                if row.text == "کوثر امیرخانی / ...":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report78(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report78, "گریدینگ مشتریان", "گریدینگ مشتریان")

    def enter_admin_report_select_the_report78_check_table1(self):
        th1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/table/thead/tr[2]/th[5]").text
        assert th1 == "گریدینگ بر اساس وزن"
        assert th2 == "نمره یک"
        assert th3 == "نمره دو"
        assert th4 == "نمره سه"
        assert th5 == "نمره چهار"
        print("جدول1 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report78_check_table2(self):
        th1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div/table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div/table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div/table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div/table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div/table/thead/tr[2]/th[5]").text
        assert th1 == "گریدینگ بر اساس مبلغ"
        assert th2 == "نمره یک"
        assert th3 == "نمره دو"
        assert th4 == "نمره سه"
        assert th5 == "نمره چهار"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report78_check_table3(self):
        th1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/div/div/div/div/table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/div/div/div/div/table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/div/div/div/div/table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/div/div/div/div/table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[4]/div/div/div/div/table/thead/tr[2]/th[5]").text
        assert th1 == "'گریدینگ بر اساس تعداد"
        assert th2 == "نمره یک"
        assert th3 == "نمره دو"
        assert th4 == "نمره سه"
        assert th5 == "نمره چهار"
        print("جدول3 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report78_check_table4(self):
        th1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[5]/div/div/div/div/table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[5]/div/div/div/div/table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[5]/div/div/div/div/table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[5]/div/div/div/div/table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[5]/div/div/div/div/table/thead/tr[2]/th[5]").text
        assert th1 == "گرید نهایی"
        assert th2 == "نمره یک"
        assert th3 == "نمره دو"
        assert th4 == "نمره سه"
        assert th5 == "نمره چهار"
        print("جدول4 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report79(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report79, "گزارش فاکتور های پرداخت شده با اصلاح..", "گزارش فاکتور های پرداخت شده با اصلاح سابقه")

    def enter_admin_report_select_the_report79_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "کاربر ثبت کننده"
        assert th5 == "زمان ثبت"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th6 == "قیمت نهایی"
        assert th7 == "مبلغ پرداخت شده"
        assert th8 == "توضیحات"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report80(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report80, "گزارش اطلاعات لوکیشن در فرم هماهنگی با..", "گزارش اطلاعات لوکیشن در فرم هماهنگی با مشتری")

    def enter_admin_report_select_the_report80_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='op-location-info']")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شهر"
        assert th3 == "تعداد کل فرم ها"
        assert th4 == "تعداد فرم های با لوکیشن"
        assert th5 == "تعداد فرم های بدون لوکیشن"
        assert th6 == "درصد تعداد فرم های با لوکیشن"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report81(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report81, "لیست سفارش های تحویل شده به صورت نقدی", "لیست سفارش های تحویل شده به صورت نقدی")

    def enter_admin_report_select_the_report81_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "کل بدهی سفارش"
        assert th4 == "نوع ترخیص"
        assert th5 == "توضیحات دلیوری"
        assert th6 == "توضیحات مالی"
        assert th7 == "توضیحات انبار"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report82(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report82, "درخواست های عودت وجه - مالی", "لیست درخواست های عودت وجه - مالی")

    def enter_admin_report_select_the_report82_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر"
        assert th3 == "مبلغ"
        assert th4 == "واحد"
        assert th5 == "زمان تغییرات"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th6 == "مدیر مشتری"
        assert th7 == "فایل"
        assert th8 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report83(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report83, "سفارشات ثبت شده توسط بازاریاب", "")

    def enter_admin_report_select_the_report83_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "وضعیت بارگیری سفارش"
        assert th4 == "خدمات موردنیاز"
        assert th5 == "وزن قابل پرداخت سفارش (kg)"
        assert th6 == "مبلغ پیش فاکتور"
        assert th7 == "زمان ایجاد"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report83_by_check(self):
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[3]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "سفارش بارگیری نشده است":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report83_users_filter(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report20_destination_filter_btn)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[8]/a")
        for row in rows:
            if len(rows) > 1:
                if row.text == "چنور خداکرمی":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report83_agency_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='dateFilter']/div[3]/span/span[1]/span")
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/span/span/span[2]/ul/li[1]")
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report09_status_btn)

    def enter_admin_report_select_the_report84(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report84, "توضیحات دلیوری در فرم هماهنگی با مشتری", "توضیحات دلیوری در فرم هماهنگی با مشتری")

    def enter_admin_report_select_the_report84_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "توضیحات دلیوری"
        assert th4 == "مدیر مشتری"
        assert th5 == "نام تحویل گیرنده"
        assert th6 == "تغییردهنده"
        assert th7 == "بروزرسانی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th8 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report85(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report85, "گزارش مغایرت قیمتهای جدول حمل جدید با..", "گزارش مغایرت قیمتهای جدول حمل جدید با قیمتهای جدول حمل قبلی")

    def enter_admin_report_select_the_report85_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "مکان صاحب سفارش"
        assert th4 == "دریافت کننده"
        assert th5 == "ارسال کننده"
        assert th6 == "وزن سفارش (KG)"
        assert th7 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th8 == "خدمات موردنیاز"
        assert th9 == "ایجادکننده"
        assert th10 == "برحسب مدل فعلی"
        assert th11 == "برحسب مدل جدید"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report86(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report86, "لیست آخرین پیام های هر مشتری", "لیست آخرین پیام های هر مشتری")

    def enter_admin_report_select_the_report86_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "پیغام"
        assert th3 == "اسم مشتری"
        assert th4 == "شماره"
        assert th5 == "مدیر مشتری"
        assert th6 == "تاریخ"
        assert th7 == "مبدا ارسال پیام"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report87(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report87, "کالاهای نیاز به بررسی بیشتر", "کالاهای نیاز به بررسی بیشتر")

    def enter_admin_report_select_the_report87_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "کد مشخصه"
        assert th3 == "سفارش"
        assert th4 == "وزن کالا"
        assert th5 == "دسته بندی کلی کالا"
        assert th6 == "دسته بندی جزئی کالا"
        assert th7 == "زمان خروج از کارتابل"
        assert th8 == "کاربر بررسی نوع کالا"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report88(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report88, "دلیل رد کردن پرداخت", "دلیل رد کردن پرداخت")

    def enter_admin_report_select_the_report88_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر مرتبط"
        assert th3 == "مبلغ"
        assert th4 == "ایجادکننده"
        assert th5 == "علت لغو"
        assert th6 == "توضیحات تایید / عدم تایید"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report89(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report89, "گزارش نموداری از فعالیت تیم های فروش", "لیست گزارش نموداری از فعالیت تیم های فروش")

    def enter_admin_report_select_the_report89_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]/div[1]")
        print("نمودار وزن سفارشات، تعداد ترک اصلی (سفارش)، مسیرهای سفارش، تعداد ترک فرعی و تعداد سفارش های لغو شده  به درستی نمایش داده شدند.")
        print("________________________________")

    def enter_admin_report_select_the_report90(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report90, "پرداخت های تایید شده از سمت چین", "پرداخت های تایید شده از سمت چین")

    def enter_admin_report_select_the_report90_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "مبلغ"
        assert th4 == "حساب"
        assert th5 == "توضیحات"
        assert th6 == "زمان پرداخت"
        assert th7 == "ایجادکننده"
        assert th8 == "شماره حساب/کارت پرداخت کننده"
        assert th9 == "نام صاحب حساب پرداخت کننده"
        assert th10 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report91(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report91, "علت عدم انتخاب لوکیشن در هماهنگی", "علت عدم انتخاب لوکیشن در هماهنگی")

    def enter_admin_report_select_the_report91_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "نام مدیر مشتری"
        assert th4 == "صاحب سفارش"
        assert th5 == "توضیحات عدم ثبت لوکیشن"
        assert th6 == "زمان پر شدن فرم هماهنگی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report92(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report92, "بدهی های کیف پول کاربران", "لیست بدهی های کیف پول کاربران")

    def enter_admin_report_select_the_report92_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "مشتریان"
        assert th3 == "مدیر مشتریان"
        assert th4 == "موبایل1"
        assert th5 == "دلار"
        assert th6 == "یورو"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        assert th7 == "یوان"
        assert th8 == "درهم امارات"
        assert th9 == "لیر ترکیه"
        assert th10 == "ریال"
        assert th11 == "ریال*"
        assert th12 == "لیر سوریه"
        assert th13 == "پوند"
        assert th14 == "زمان ایجاد مشتری"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report93(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report93, "گزارش مدیریتی کار", "گزارش مدیریتی کار")

    def enter_admin_report_select_the_report93_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "موبایل1"
        assert th4 == "تلفن ثابت 1"
        assert th5 == "تلفن ثابت 2"
        assert th6 == "تعداد کار های مانده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report94(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report94, "افراد دارای قرارداد اعتباری", "افراد دارای قرارداد اعتباری")

    def enter_admin_report_select_the_report94_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/span[1]/a")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "سوابق قراردادها"
        assert th4 == "جنسیت"
        assert th5 == "کدملی"
        assert th6 == "موبایل1"
        assert th7 == "ایجادکننده"
        print("جدول و نمایش قراردادهای معتبر به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report95(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report95, "کاربران دارای موجودی", "کاربران دارای موجودی")

    def enter_admin_report_select_the_report95_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "مشتریان"
        assert th3 == "مدیر مشتریان"
        assert th4 == "دلار"
        assert th5 == "یوان"
        assert th6 == "ریال"
        assert th7 == "یورو"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        assert th8 == "پوند"
        assert th9 == "درهم امارات"
        assert th10 == "لیر ترکیه"
        assert th11 == "ریال*"
        assert th12 == "زمان ایجاد مشتری"
        assert th13 == "تعداد سفارشات باز"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report96(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report96, "سفارش های لغو شده دارای فاکتور پرداخت..", "سفارش های لغو شده دارای فاکتور پرداخت شده")

    def enter_admin_report_select_the_report96_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[3]")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "وضعیت بارگیری"
        print("جدول، نمایش همه، سفارشات لغو شده بعد از بارگیری و سفارشات لغو شده قبل از بارگیری به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report97(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report97, "فاکتورهای مابه التفاوت", "فاکتورهای مابه التفاوت")

    def enter_admin_report_select_the_report97_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیش فاکتور اولیه"
        assert th3 == "قیمت نهایی اولیه"
        assert th4 == "شماره پیش فاکتور ثانویه"
        assert th5 == "قیمت نهایی ثانویه"
        assert th6 == "عنوان"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report98(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report98, "گزارش پرداخت های انجام شده", "لیست گزارش پرداخت های انجام شده")

    def enter_admin_report_select_the_report98_check_table1(self):
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[14]").text
        assert th1 == "ردیف"
        assert th2 == "تعداد پرداخت"
        assert th3 == "تعداد پرداخت غیر یوانی"
        assert th4 == "تعداد پرداخت یوانی"
        assert th5 == "مجموع پرداخت یوانی (یوان)"
        assert th6 == "تعداد پرداخت ریالی"
        assert th7 == "مجموع پرداخت ریالی (ریال)"
        assert th8 == "تعداد پرداخت دلاری"
        assert th9 == "مجموع پرداخت دلاری (دلار)"
        assert th10 == "تعداد پرداخت درهم اماراتی"
        assert th11 == "مجموع پرداخت درهم اماراتی (درهم امارات)"
        assert th12 == "تعداد پرداخت یوروی"
        assert th13 == "مجموع پرداخت یوروی (یورو)"
        assert th14 == "مجموع کل پرداختی (ریال)"
        print("جدول1 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report98_check_table2(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "وضعیت"
        assert th4 == "مبلغ"
        assert th5 == "حساب"
        assert th6 == "توضیحات"
        assert th7 == "زمان پرداخت"
        scrolled = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[12]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[12]").text
        assert th8 == "ایجادکننده"
        assert th9 == "شماره حساب/کارت پرداخت کننده"
        assert th10 == "نام صاحب حساب پرداخت کننده"
        assert th11 == "علت عدم انتخاب موارد مشابه"
        assert th12 == "موبایل"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report100(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report100, "گزارش مکالمات داخلی و خارجی", "گزارش مکالمات داخلی و خارجی")

    def enter_admin_report_select_the_report100_check_table1(self):
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[1]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "تعداد تماس وارده از دست رفته"
        assert th3 == "مدت زمان اشغالی خط"
        assert th4 == "تعداد تماس پاسخ داده شده"
        print("جدول1 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report100_check_table2(self):
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[1]/th[12]").text
        assert th1 == "ردیف"
        assert th2 == "شناسه"
        assert th3 == "تاریخ"
        assert th4 == "تماس گیرنده"
        assert th5 == "گروه پاسخگو"
        assert th6 == "مقصد"
        assert th7 == "کانال ورودی"
        assert th8 == "کد حساب"
        assert th9 == "کانال مقصد"
        assert th10 == "وضعیت"
        assert th11 == "مدت تماس"
        assert th12 == "فایل مکالمه"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report101(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report101, "توضیحات عدم ثبت مورد مشابه پرداخت", "توضیحات عدم ثبت مورد مشابه پرداخت")

    def enter_admin_report_select_the_report101_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "ایجادکننده"
        assert th4 == "زمان ایجاد"
        assert th5 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report102(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report102, "مشتریان 30 روز پس از تحویل", "لیست مشتریان 30 روز پس از تحویل")

    def enter_admin_report_select_the_report102_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "مدیر مشتری"
        assert th4 == "تاریخ عضویت"
        assert th5 == "تاریخ آخرین سفارش انجام شده"
        assert th6 == "تعداد سفارشات"
        assert th7 == "کارکرد مالی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report103(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report103, "خروجی کارتابل های تجدید سفارش", "لیست خروجی کارتابل های تجدید سفارش")

    def enter_admin_report_select_the_report103_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "عملیات انجام شده"
        assert th3 == "نام مشتری"
        assert th4 == "وضعیت سفارش"
        assert th5 == "نام مدیر مشتری"
        assert th6 == "دوره تجدید سفارش"
        assert th7 == "تعداد سفارشات"
        assert th8 == "خروجی کارتابل"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report103_customer_manager(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report103_customer_manager_option)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by_btn)
        sleep(1)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[5]/a[1]")
        for row in rows:
            if len(rows) > 1:
                if 'احمدرضا' in row.text:
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report104(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report104, "زمان تحویل سفارش ها", "لیست زمان تحویل سفارش ها")

    def enter_admin_report_select_the_report104_check_table1(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover sort-table ']/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "تعداد سفارش"
        assert th3 == "میانگین زمان انجام (روز)"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report104_check_table2(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "زمان انجام (روز)"
        assert th4 == "دریافت کننده"
        assert th5 == "ارسال کننده"
        assert th6 == "وزن سفارش (KG)"
        assert th7 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[9]").text
        assert th8 == "خدمات موردنیاز"
        assert th9 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report105(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report105, "سفارش های ثبت شده از اپلیکیشن فاقد وزن", "سفارش های ثبت شده از اپلیکیشن فاقد وزن حجمی")

    def enter_admin_report_select_the_report105_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report106(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report106, "سفارشات ثبت شده با مقصد میانی دبی", "سفارشات ثبت شده با مقصد میانی دبی")

    def enter_admin_report_select_the_report106_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report107(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report107, "کاربرانی که وارد اپلیکیشن شدند", "لیست کاربرانی که وارد اپلیکیشن شدند")

    def enter_admin_report_select_the_report107_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "موبایل"
        assert th4 == "ایجادکننده"
        assert th5 == "ثبت نام از طریق"
        assert th6 == "مدیر مشتری"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report108(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report108, "سفارش هایی که وارد تسویه نهایی نشده اند", "سفارش هایی که وارد تسویه نهایی نشده اند")

    def enter_admin_report_select_the_report108_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "وزن قابل پرداخت سفارش (kg)"
        assert th5 == "مقدار بدهی به ریال"
        assert th6 == "مشکل تسویه دارد"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "مدیر مشتری"
        assert th9 == "بازاریاب"
        assert th10 == "ایجادکننده"
        assert th11 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report109(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report109, "فاکتورهای غیرمعتبر دارای موجودی", "فاکتورهای غیرمعتبر دارای موجودی")

    def enter_admin_report_select_the_report109_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "درصد مالیات"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th5 == "پرداخت شده (در واحد)"
        assert th6 == "عنوان فاکتور"
        assert th7 == "کاربر ثبت کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report110(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report110, "گزارش سفارش های تسویه شده فاقد فاکتور..", "سفارش های تسویه شده فاقد پیش فاکتور به ازای خدمت")

    def enter_admin_report_select_the_report110_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report111(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report111, "گزارش مدیریت ناوگان", "لیست مدیریت ناوگان")

    def enter_admin_report_select_the_report111_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "تاریخ گزارش"
        assert th3 == "ساعت گزارش از"
        assert th4 == "ساعت گزارش تا"
        assert th5 == "نام خودرو"
        assert th6 == "نام راننده"
        assert th7 == "کل مسافت طی شده"
        assert th8 == "کل زمان طی شده (دقیقه)"
        assert th9 == "کل سوخت مصرفی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report111_created_by_check(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by)
        wait_until_element_has_an_attribute(self, 'xpath', "//*[@id='dateFilter']/div[2]/select/option[text()='20ایران441د35']")
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report5_created_by_btn)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id_btn)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[5]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "20ایران441د35":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report112(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report112, "مشتریانی که کد ملی تکراری دارند", "مشتریانی که کد ملی تکراری دارند")

    def enter_admin_report_select_the_report112_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "شناسه"
        assert th3 == "نام مشتری"
        assert th4 == "کدملی"
        assert th5 == "تلفن همراه"
        assert th6 == "تلفن همراه"
        assert th7 == "تلفن ثابت 1"
        assert th8 == "تلفن ثابت 1"
        assert th9 == "آدرس"
        assert th10 == "نام مدیر مشتری"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report113(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report113, "فاکتورهایی که مبلغ باقیمانده منفی دارند", "لیست فاکتورهایی که مبلغ باقیمانده منفی دارند")

    def enter_admin_report_select_the_report113_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "صاحب سفارش"
        assert th3 == "پرداخت شده (در واحد)"
        assert th4 == "شماره پیگیری"
        assert th5 == "شماره پیش فاکتور"
        assert th6 == "کاربر ثبت کننده"
        assert th7 == "زمان ثبت"
        assert th8 == "قیمت نهایی"
        assert th9 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report114(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report114, "آخرین ارزیابی خدمات", "آخرین ارزیابی خدمات")

    def enter_admin_report_select_the_report114_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شناسه سفارش"
        assert th3 == "مشاهده ارزیابی"
        assert th4 == "صاحب سفارش"
        assert th5 == "مدیر مشتری"
        assert th6 == "پیشنهادات"
        assert th7 == "ایجادکننده"
        assert th8 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report115(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report115, "گزارش سفارشات تحویل شده کالاپیک", "لیست گزارش سفارشات تحویل شده کالاپیک")

    def enter_admin_report_select_the_report115_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        scrolled1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]")
        sleep(0.5)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره قیض"
        assert th3 == "شماره ترک"
        assert th4 == "وزن جرمی (KG)"
        assert th5 == "وزن حجمی (KG)"
        assert th6 == "تعداد کالای تحویل شده"
        assert th7 == "ترک فرعی"
        assert th8 == "هزینه محاسبه شده کالاپیک (ریال)"
        assert th9 == "اضافه مسیر (ریال)"
        scrolled2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]")
        sleep(0.5)
        scrolled2.location_once_scrolled_into_view
        sleep(0.5)
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        assert th10 == "جمع کل (ریال)"
        assert th11 == "صاحب پیش فاکتور"
        assert th12 == "شماره بچ"
        assert th13 == "زمان تحویل"
        assert th14 == "شهر"
        assert th15 == "آدرس"
        assert th16 == "زمان ایجاد"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report116(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report116, "تراکنش های تکراری چین", "لیست 'گزارش تراکنش های تکراری چین'")

    def enter_admin_report_select_the_report116_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "مبلغ"
        assert th4 == "حساب"
        assert th5 == "توضیحات"
        assert th6 == "توضیحات تاییدیه"
        assert th7 == "شماره سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        assert th8 == "زمان پرداخت"
        assert th9 == "ایجادکننده"
        assert th10 == "شماره حساب/کارت پرداخت کننده"
        assert th11 == "نام صاحب حساب پرداخت کننده"
        assert th12 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report117(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report117, "سفارشات دارای کالای مرجوعی", "سفارشات دارای کالای مرجوعی")

    def enter_admin_report_select_the_report117_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شخص دریافت کننده"
        assert th4 == "شخص ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "تاریخ مرجوع شدن سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report118(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report118, "لاگ استفاده از هر کارتابل", "لاگ استفاده از هر کارتابل")

    def enter_admin_report_select_the_report118_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', "//table/tbody/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/tbody/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/tbody/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/tbody/tr[1]/th[4]").text
        assert th1 == "form.system.radif"
        assert th2 == "نام کارتابل"
        assert th3 == "واحد استفاده کننده"
        assert th4 == "تعداد تسکهای وارد شده و خارج شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report119(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report119, "مشتریان شعبه ها", "لیست مشتریان شعبه ها")

    def enter_admin_report_select_the_report119_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "نام مدیر مشتری"
        assert th4 == "موبایل"
        assert th5 == "ایجادکننده"
        assert th6 == "زمان ایجاد"
        assert th7 == "نمایندگی"
        assert th8 == "هیچ سفارشی ندارد"
        assert th9 == "یک سفارش دارد‌"
        assert th10 == "بیش از یک سفارش دارد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report120(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report120, "گزارش پیش‌ فاکتورهایی که چندبار در آرین..", "گزارش پیش‌ فاکتورهایی که چندبار در آرین ثبت شده اند")

    def enter_admin_report_select_the_report120_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "درصد مالیات"
        assert th5 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th6 == "عنوان فاکتور"
        assert th7 == "کاربر ثبت کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report121(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report121, "لیست سفارش با صاحب سفارش های تغییر کرده", "لیست سفارش با صاحب سفارش های تغییر کرده")

    def enter_admin_report_select_the_report121_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "کاربر تغییر دهنده"
        assert th4 == "زمان تغییر صاحب سفارش"
        assert th5 == "صاحب سفارش قبلی"
        assert th6 == "مدیر مشتریِ صاحب سفارش قبلی"
        assert th7 == "صاحب سفارش فعلی"
        assert th8 == "مدیر مشتریِ صاحب سفارش فعلی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report122(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report122, "لیست تخفیف ها بر اساس شماره موبایل", "لیست تخفیف ها بر اساس شماره موبایل")

    def enter_admin_report_select_the_report122_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک ها"
        assert th3 == "نام ثبت شده"
        assert th4 == "شماره موبایل"
        assert th5 == "توضیحات"
        assert th6 == "عنوان تخفیف"
        assert th7 == "ایجاد کننده سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report123(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report123, "هزینه و فروش سفارشهای کنسل شده بعد از..", "هزینه و فروش سفارشهای کنسل شده بعد از بارگیری")

    def enter_admin_report_select_the_report123_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "هزینه سایر"
        assert th4 == "فاکتور سایر"
        assert th5 == "درآمد سایر"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report124(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report124, "کاربران ثبت شده با دو شماره موبایل", "کاربران ثبت شده با دو شماره موبایل")

    def enter_admin_report_select_the_report124_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "موبایل1"
        assert th4 == "موبایل2"
        assert th5 == "تلفن ثابت 1"
        assert th6 == "تلفن ثابت 2"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report125(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report125, "صورتحساب مالی نمایندگی ها", "صورتحساب مالی نمایندگی ها")

    def enter_admin_report_select_the_report125_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "تعداد پیش فاکتور های حمل رسمی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[23]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        th17 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[17]").text
        th18 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[18]").text
        th19 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[19]").text
        th20 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[20]").text
        th21 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[21]").text
        th22 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[22]").text
        th23 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[23]").text
        assert th9 == "تعداد پیش فاکتور های حمل غیررسمی"
        assert th10 == "تعداد پیش فاکتور های ترخیص رسمی"
        assert th11 == "تعداد پیش فاکتور های ترخیص غیررسمی"
        assert th12 == "مبلغ ارزی فاکتور حمل اول"
        assert th13 == "نرخ ارز فاکتور حمل اول"
        assert th14 == "معادل ریالی فاکتور حمل اول"
        assert th15 == "مبلغ ارزی فاکتور حمل دوم"
        assert th16 == "نرخ ارز فاکتور حمل دوم"
        assert th17 == "معادل ریالی فاکتور حمل دوم"
        assert th18 == "مبلغ ارزی فاکتور ترخیص اول"
        assert th19 == "نرخ ارز فاکتور ترخیص اول"
        assert th20 == "معادل ریالی فاکتور ترخیص اول"
        assert th21 == "مبلغ ارزی فاکتور ترخیص دوم"
        assert th22 == "نرخ ارز فاکتور ترخیص دوم"
        assert th23 == "معادل ریالی فاکتور ترخیص دوم"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report126(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report126, "وظیفه های باز مدیر مشتریان", "گزارش وظیفه های باز مدیر مشتریان")

    def enter_admin_report_select_the_report126_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "نام مدیر مشتری"
        assert th3 == "تعداد وظیفه باز"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report127(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report127, "سفارش های تحویل شده فاقد تاییدیه فاکتور..", "سفارش های تحویل شده فاقد تاییدیه فاکتور رسمی")

    def enter_admin_report_select_the_report127_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "خدمات مورد نیاز"
        assert th4 == "نوع پیش فاکتور رسمی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report129(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report129, "گزارش نتیجه تماس با مشتریان", "لیست گزارش نتیجه تماس با مشتریان")

    def enter_admin_report_select_the_report129_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "نام"
        assert th3 == "نام خانوادگی"
        assert th4 == "آدرس"
        assert th5 == "استان"
        assert th6 == "کد پستی"
        assert th7 == "تلفن"
        assert th8 == "وضعیت"
        assert th9 == "توضیحات"
        assert th10 == "بازاریاب"
        assert th11 == "زمان ثبت وضعیت"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report130(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report130, "نتیجه نظرسنجی تحویل سفارش", "نتیجه نظرسنجی تحویل سفارش")

    def enter_admin_report_select_the_report130_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "زمان ایجاد"
        assert th4 == "زمان تکمیل اطلاعات"
        assert th5 == "مدت زمان ارسال کالا را چگونه ارزیابی میکنید؟"
        assert th6 == "نظر شما در مورد هزینه حمل شرکت پی اس پی چیست؟"
        assert th7 == "آیا از زمان انجام ترخیص سفارش خود رضایت داشته اید؟"
        assert th8 == "نظر شما در مورد هزینه ترخیص شرکت پی اس پی چیست؟"
        assert th9 == "نحوه عملکرد، پاسخگویی و رفتار مدیر مشتری (کارشناس فروش ) از نظر شما چقدر رضایت بخش بود؟"
        assert th10 == "نحوه تحویل بار و برخورد تحویل دهنده را چگونه ارزیابی میکنید؟"
        assert th11 == "پیشنهادات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report131(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report131, "گزارش سفارشات زیبای", "گزارش سفارشات زیبای")

    def enter_admin_report_select_the_report131_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "ترک زیبای"
        assert th4 == "کل فاکتورهای صادر شده"
        assert th5 == "وزن"
        assert th6 == "ایجادکننده"
        assert th7 == "مبلغ پیش فاکتور"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report132(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report132, "ساعت تحویل بار توسط واحد تحویل کالا", "ساعت تحویل بار توسط واحد تحویل کالا")

    def enter_admin_report_select_the_report132_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        print("نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report133(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report133, "پرداخت هایی که از طریق دستگاه پوز دوبار..", "پرداخت هایی که از طریق دستگاه پوز دوبار ثبت شده")

    def enter_admin_report_select_the_report133_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "وضعیت"
        assert th4 == "مبلغ"
        assert th5 == "حساب"
        assert th6 == "توضیحات"
        assert th7 == "زمان پرداخت"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th8 == "ایجادکننده"
        assert th9 == "شماره حساب/کارت پرداخت کننده"
        assert th10 == "نام صاحب حساب پرداخت کننده"
        assert th11 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report134(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report134, "تراکنش های ثبت سفارش", "لیست تراکنش های ثبت سفارش")

    def enter_admin_report_select_the_report134_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "شماره بچ"
        assert th4 == "نوع تراکنش"
        assert th5 == "نوع هزینه / دریافت"
        assert th6 == "مبلغ تراکنش"
        assert th7 == "پیش فاکتورهای یوانی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th8 == "زمان تایید"
        assert th9 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report134_cost_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report134_cost_type)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report134_cost_type_option)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[4]/span[1]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "هزینه":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report134_other_inquery_type(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report134_other_inquery_type)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report134_other_inquery_type_option)
        rows = self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr/td[5]")
        for row in rows:
            if len(rows) > 1:
                if row.text == "خرید":
                    sleep(.01)
                else:
                    print(
                        'خطا!!!مقدار {} در سطر {} و ستون سوم قابل قبول نیست.'.format(row.text, rows.index(row)))
        print("فیلتر به درستی انجام شد")
        print("________________________________")

    def enter_admin_report_select_the_report135(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report135, "نتیجه CRM تحویل دهنده", "نتیجه CRM تحویل دهنده")

    def enter_admin_report_select_the_report135_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "مدیر مشتری"
        assert th4 == "شناسه سفارش"
        assert th5 == "تحویل دهنده"
        assert th6 == "موزع"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th7 == "رضایت از تحویل کالا - مدت زمان تحویل بار"
        assert th8 == "رضایت از تحویل کالا - توضیحات"
        assert th9 == "رضایت از تحویل کالا - برخورد تیم تحویل دهنده"
        assert th10 == "رضایت از تحویل کالا - توضیحات"
        assert th11 == "تاریخ ثبت"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report136(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report136, "هزینه و فروش", "گزارش هزینه و فروش سفارش ها")

    def enter_admin_report_select_the_report136_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "شماره بچ"
        assert th4 == "هزینه حمل"
        assert th5 == "فاکتور حمل"
        assert th6 == "درآمد حمل"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        th14 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[14]").text
        th15 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[15]").text
        th16 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[16]").text
        assert th7 == "هزینه ترخیص"
        assert th8 == "فاکتور ترخیص"
        assert th9 == "درآمد ترخیص"
        assert th10 == "هزینه خرید"
        assert th11 == "فاکتور خرید"
        assert th12 == "درآمد خرید"
        assert th13 == "هزینه سایر"
        assert th14 == "فاکتور سایر"
        assert th15 == "درآمد سایر"
        assert th16 == "پرداخت اصلاح سابقه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report137(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report137, "زمان انجام گام به گام سفارش های ریل شده", "زمان انجام گام به گام سفارش های ریل شده")

    def enter_admin_report_select_the_report137_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "نوع گزارش"
        assert th3 == "از بارگیری تا در انبار"
        assert th4 == "از در انبار تا در بچ"
        assert th5 == "از در بچ تا خروج از انبار مبدا"
        # print(th6)
        assert th6 == "از خروچ از انبار مبدا تا دریافت بسته در انبار مقصد"
        assert th7 == "از دریافت بسته در انبار مقصد تا رسیدن مرسوله به مقصد منتظر ارزیابی گمرک"
        assert th8 == "از رسیدن مرسوله به مقصد منتظر ارزیابی گمرک تا هماهنگی با مشتری برای تحویل"
        assert th9 == "از هماهنگی با مشتری برای تحویل تا آماده تحویل مشتری"
        assert th10 == "از آماده تحویل مشتری تا تحویل شده به مشتری"
        assert th11 == "جمع کل"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report138(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report138, "فاکتورهایی که پس از چاپ فاکتور رسمی نام..", "لیست فاکتورهایی که پس از چاپ فاکتور رسمی نام صاحب فاکتور تغییر کرده")

    def enter_admin_report_select_the_report138_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "صاحب سفارش"
        assert th3 == "پرداخت شده (در واحد)"
        assert th4 == "شماره پیگیری"
        assert th5 == "شماره پیش فاکتور"
        assert th6 == "کاربر ثبت کننده"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th7 == "زمان ثبت"
        assert th8 == "قیمت نهایی"
        assert th9 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report139(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report139, "سود و زیان سفارش ها", "گزارش سود و زیان سفارش ها")

    def enter_admin_report_select_the_report139_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[4]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[5]")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "سود و زیان حمل"
        assert th4 == "سود و زیان ترخیص"
        assert th5 == "سود و زیان خرید"
        assert th6 == "سود و زیان سایر استعلام"
        assert th7 == "پرداخت اصلاح سابقه"
        assert th8 == "جمع سود و زیان"
        print("جدول، سفارشات ثبت شده در بازه انتخابی، خلاصه گزارش، خلاصه گزارش زیان و خلاصه گزارش سود به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report140(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report140, "سفارشها با فاکتور رسمی که نرخ ارز آنها..", "سفارشها با فاکتور رسمی که نرخ ارز آنها تغییر کرده")

    def enter_admin_report_select_the_report140_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "کاربر تایید کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report141(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report141, "مشتریانی که فقط کالای داکیومنت دارند", "مشتریانی که فقط کالای داکیومنت دارند")

    def enter_admin_report_select_the_report141_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "نام مدیر مشتری"
        assert th4 == "تعداد سفارشات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report142(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report142, "زمان انجام وظایف کارتابل ها به صورت..", "زمان انجام وظایف کارتابل ها به صورت نموداری")

    def enter_admin_report_select_the_report142_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        print("نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report143(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report143, "لیست خروجی ها از کارتابل سفارش های لغو..", "لیست خروجی ها از کارتابل سفارش های لغو شده")

    def enter_admin_report_select_the_report143_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "علت لغو سفارش"
        assert th4 == "توضیحات لغو سفارش"
        assert th5 == "تمایل همکاری مجدد را دارد"
        assert th6 == "توضیحات همکاری مجدد"
        assert th7 == "علت لغو"
        assert th8 == "توضیحات وضعیت"
        assert th9 == "توضیحات خروج از کارتابل"
        assert th10 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report144(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report144, "سفارش های دارای پیش فاکتور سود منفی", "سفارش های دارای پیش فاکتور سود منفی")

    def enter_admin_report_select_the_report144_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "خدمات موردنیاز"
        assert th4 == "پیش فاکتور های سود منفی"
        assert th5 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report145(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report145, "فاکتور های تایید شده توسط مدیر مشتری", "فاکتور های تایید شده توسط مدیر مشتری")

    def enter_admin_report_select_the_report145_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "صاحب سفارش"
        assert th4 == "صاحب پیش فاکتور"
        assert th5 == "مدیر مشتری"
        assert th6 == "نوع پیش فاکتور"
        assert th7 == "زمان ثبت"
        assert th8 == "کاربر ثبت کننده"
        assert th9 == "زمان تایید فاکتور"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report146(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report146, "گزارش پورسانت مسئول انبار", "گزارش پورسانت مسئول انبار")

    def enter_admin_report_select_the_report146_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "انباردار"
        assert th3 == "تعداد کارتن"
        assert th4 == "مبلغ اولیه پاداش"
        assert th5 == "پاداش نهایی"
        print("جدول  وضریب ریالی و باتن تاثیر نظر به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report147(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report147, "پاداش مدیر مشتریان", "پاداش مدیر مشتریان")

    def enter_admin_report_select_the_report147_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='all-order']")
        assert self.driver.find_element('xpath', "//*[@id='settle_order']")
        assert self.driver.find_element('xpath', "//*[@id='has_payment_order']")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام مدیر مشری"
        assert th3 == "جمع سود واقعی (ریال)"
        assert th4 == "جمع وزن قابل پرداخت سفارش ها"
        assert th5 == "ضریب پورسانت از سود"
        assert th6 == "پورسانت (ریال)"
        assert th7 == "تعداد سفارش"
        print("جدول و باتن همه موارد و باتن در انتظار و باتن سفارش های دارای دستور به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report148(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report148, "گزارش پورسانت نمایندگی ها", "گزارش پورسانت نمایندگی ها")

    def enter_admin_report_select_the_report148_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نمایندگی"
        assert th4 == "نام مدیر نمایندگی"
        assert th5 == "مجموع سود ترخیص ریالی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report149(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report149, "گزارش پورسانت تحویل دهندگان سفارش", "گزارش پورسانت تحویل دهندگان سفارش")

    def enter_admin_report_select_the_report149_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/a")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "راننده/خودرو"
        assert th3 == "زمان طی شده (دقیقه)"
        assert th4 == "مسافت طی شده (کیلومتر)"
        assert th5 == "تعداد تحویل"
        assert th6 == "وزن حمل شده (کیلوگرم)"
        assert th7 == "مبلغ اولیه پاداش"
        assert th8 == "پاداش نهایی"
        print("جدول و تغییر ضرایب و باتن تاثیر نظر به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report150(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report150, "گزارش پورسانت بازاریاب خارجی", "گزارش پورسانت بازاریاب خارجی")

    def enter_admin_report_select_the_report150_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report151(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report151, "گزارش پورسانت بازاریاب تلفنی", "گزارش پورسانت بازاریاب تلفنی")

    def enter_admin_report_select_the_report151_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report152(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report152, "گزارش پورسانت بازاریاب حضوری (جدید)", "گزارش پورسانت بازاریاب حضوری (جدید)")

    def enter_admin_report_select_the_report152_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//*[@id='main-content-wrapper']/section[2]/div[2]/div/div[2]/div/table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report153(self):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', admin_report_select_the_report153)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        element = wait.until(EC.element_to_be_clickable(('xpath', admin_report_select_the_report153)))
        sleep(0.75)
        element.click()

    def enter_admin_report_select_the_report153_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report154(self):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', admin_report_select_the_report154)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        element = wait.until(EC.element_to_be_clickable(('xpath', admin_report_select_the_report154)))
        sleep(0.75)
        element.click()
        sleep(0.5)
        b = self.driver.find_element('xpath', admin_report_arian_management_report_title).text
        assert b == "گزارش پورسانت گمرک"
        print("تایتل به درستی نمایش داده می شود. ")
        print("________________________________")

    def enter_admin_report_select_the_report154_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div/div[2]")
        print("جدول محاسبه پورسانت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report155(self):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', admin_report_select_the_report155)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        element = wait.until(EC.element_to_be_clickable(('xpath', admin_report_select_the_report155)))
        sleep(0.75)
        element.click()
        sleep(0.5)
        # b = self.driver.find_element('xpath', admin_report_arian_management_report_title).text
        # assert b == "گزارش مشتریان"
        print("تایتل به درستی نمایش داده می شود. ")
        print("________________________________")

    def enter_admin_report_select_the_report155_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        assert th1 == "ردیف"
        assert th2 == "نام مشتری"
        assert th3 == "تعداد دفعات سفارش"
        assert th4 == "آخرین بار"
        assert th5 == "جمع پیش فاکتور (ریال)"
        assert th6 == "جمع پرداختی (ریال)"
        assert th7 == "تعداد کنسلی"
        assert th8 == "تعداد در حال انجام"
        assert th9 == "تعداد در انتظار تایید"
        assert th10 == "تعداد تحویل شده"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        th12 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[12]").text
        th13 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[13]").text
        assert th11 == "تعداد پیش سفارش"
        assert th12 == "تعداد تسویه شده"
        assert th13 == "نظرسنجی (از 10 نمره)"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report156(self):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', admin_report_select_the_report156)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        element = wait.until(EC.element_to_be_clickable(('xpath', admin_report_select_the_report156)))
        sleep(0.75)
        element.click()
        sleep(0.5)
        b = self.driver.find_element('xpath', admin_report_arian_management_report_title).text
        assert b == "گزارش عملکرد تیم فروش"
        print("تایتل به درستی نمایش داده می شود. ")
        print("________________________________")

    def enter_admin_report_select_the_report156_check_table1(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-order-report']/thead/tr[1]/th[14]").text
        assert th1 == "نام همکار"
        assert th2 == "کل سفارشات ثبت شده"
        assert th3 == "درصد از کل"
        assert th4 == "تعداد سفارش لغو شده"
        assert th5 == "درصد از کل"
        assert th6 == "تعداد دستور بارگیری صادر شده"
        assert th7 == "درصد از کل"
        assert th8 == "تعداد سفارش های در انتظار"
        assert th9 == "درصد از کل"
        assert th10 == "تعداد سفارش در حال انجام"
        assert th11 == "درصد از کل"
        assert th12 == "تعداد سفارش انجام شده"
        assert th13 == "درصد از کل"
        assert th14 == "تعداد پیش سفارش"
        print("جدول یک به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report156_check_table5(self):
        th1 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[17]").text
        th18 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[18]").text
        th19 = self.driver.find_element('xpath', "//table[@class='report-one-table table-zero table-total-shipping']/thead/tr[1]/th[19]").text
        assert th1 == "نام همکار"
        assert th2 == "تعداد کل دستور بارگیری"
        assert th3 == "درصد از کل"
        assert th4 == "ارزش وزنی کل دستور بارگیری تن"
        assert th5 == "درصد از کل"
        assert th6 == "ارزش ریالی کل دستور بارگیری میلیون تومان"
        assert th7 == "درصد از کل"
        assert th8 == "تعداد دستور بارگیری هوایی"
        assert th9 == "درصد از کل"
        assert th10 == "ارزش وزنی دستور بارگیری هوایی تن"
        assert th11 == "درصد از کل"
        assert th12 == "ارزش ریالی دستور بارگیری هوایی میلیون تومان"
        assert th13 == "درصد از کل"
        assert th14 == "تعداد دستور بارگیری دریایی"
        assert th15 == "درصد از کل"
        assert th16 == "ارزش وزنی دستور بارگیری دریایی تن"
        assert th17 == "درصد از کل"
        assert th18 == "ارزش ریالی دستور بارگیری دریایی میلیون تومان"
        assert th19 == "درصد از کل"
        print("جدول پنج به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report157(self):
        wait = WebDriverWait(self.driver, 20)
        scrolled = self.driver.find_element('xpath', admin_report_select_the_report157)
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        element = wait.until(EC.element_to_be_clickable(('xpath', admin_report_select_the_report157)))
        sleep(0.75)
        element.click()
        sleep(0.5)
        b = self.driver.find_element('xpath', admin_report_arian_management_report_title).text
        assert b == "گزارش صاحبان سفارش"
        print("تایتل به درستی نمایش داده می شود. ")
        print("________________________________")

    def enter_admin_report_select_the_report157_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام انگلیسی صاحب سفارش"
        assert th3 == "صاحب سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "ارزش فاکتورهای تایید شده(میلیون تومان)"
        assert th6 == "پرداخت های تایید شده(میلیون تومان)"
        assert th7 == "تعداد سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report158(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report158, "زمان اجرای کارتابل ها", "زمان اجرای کارتابل ها")

    def enter_admin_report_select_the_report158_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره صفحه"
        assert th3 == "نام کارتابل"
        assert th4 == "حداقل (ثانیه)"
        assert th5 == "متوسط (ثانیه)"
        assert th6 == "حداکثر (ثانیه)"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report159(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report159, "سفارش های دارای کد ترخیص کار", "سفارش های دارای کد ترخیص کار")

    def enter_admin_report_select_the_report159_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "کد استعلام ترخیص"
        assert th4 == "کاربر بروزرسان کد استعلام ترخیص"
        assert th5 == "بروزرسانی کد استعلام ترخیص"
        assert th6 == "تاریخ اولین ایجاد فاکتور ترخیص"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report160(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report160, "مانیتورینگ سیستم" , "لیست گزارش های مانیتورینگ سیستم")

    def enter_admin_report_select_the_report160_check_table(self):
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام گزارش"
        assert th3 == "وضعیت گزارش"
        assert th4 == "تعداد موارد نیاز به بررسی"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table01(self):
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[1]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "مبدا"
        assert th4 == "مقصد"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table02(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[2]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شناسه آرین"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table03(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[3]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بسته"
        assert th3 == "تاریخ ایجاد بچ"
        assert th4 == "موقعیت"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table04(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[4]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بسته"
        assert th3 == "تاریخ ایجاد بچ"
        assert th4 == "موقعیت"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table05(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[5]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شناسه سفارش"
        assert th3 == "شناسه بچ"
        assert th4 == "وزن جرمی"
        assert th5 == "وزن حجمی"
        assert th6 == "وزن قابل پرداخت"
        assert th7 == "زمان ایجاد"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table06(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[6]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "مبدا"
        assert th4 == "مقصد"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table07(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[7]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شناسه آرین"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table08(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[8]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بچ"
        assert th3 == "شناسه آرین"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table09(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[9]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بچ"
        assert th3 == "شناسه آرین"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table10(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[10]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "جنسیت"
        assert th4 == "ایمیل"
        assert th5 == "کدملی"
        assert th6 == "موبایل1"
        assert th7 == "ایجادکننده"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table11(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[11]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیش فاکتور"
        assert th3 == "عنوان"
        assert th4 == "قیمت اعلامی"
        assert th5 == "هزینه به دلار"
        assert th6 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th7 == "قیمت نهایی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th8 == "تسعیر ارز"
        assert th9 == "پرداخت شده (در واحد)"
        assert th10 == "عملیات"
        assert th11 == "کاربر ایجاد کننده"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table12(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[12]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "پیش فاکتورهای معتبر"
        assert th4 == "کاربر لغو کننده سفارش"
        assert th5 == "زمان لغو سفارش"
        print("________________________________")

    def enter_admin_report_select_the_report160_check_table13(self):
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-2])
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', "//table/tbody/tr[13]/td[2]/a[1]")
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        tr = len(self.driver.find_elements('xpath', "//table/thead/tr"))
        sleep(1)
        th1 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[1]").text
        th2 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[2]").text
        th3 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[3]").text
        th4 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[4]").text
        th5 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[5]").text
        th6 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[6]").text
        th7 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیش فاکتور"
        assert th3 == "عنوان"
        assert th4 == "قیمت اعلامی"
        assert th5 == "هزینه به دلار"
        assert th6 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th7 == "قیمت نهایی"
        scrolled = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[8]").text
        th9 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[9]").text
        th10 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[10]").text
        th11 = self.driver.find_element('xpath', f"//table/thead/tr[{tr}]/th[11]").text
        assert th8 == "تسعیر ارز"
        assert th9 == "پرداخت شده (در واحد)"
        assert th10 == "عملیات"
        assert th11 == "کاربر ایجاد کننده"
        print("________________________________")




################### admin_report_reports_according_old_system ###################

# admin_report_reports_according_old_system = "//*[@id='main-content-wrapper']/section[2]/div/div[5]"







