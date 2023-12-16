from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from colorama import Fore


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
    print(Fore.GREEN + " تایتل " + b + " به درستی نمایش داده می شود.  ")
    print("________________________________")


class Report:
    def __init__(self, driver):
        self.driver = driver

    def enter_report(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report)
        sleep(.3)

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

    def enter_report_manager_check(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[5]")
        print("بخش پورسانت ها به درستی مشاهده شد. ")
        print("گزارش های مدیریتی آرین به درستی مشاهده شد. ")
        print("بخش گزارش موردنظر خود را انتخاب نمایید به درستی مشاهده شد. ")
        print("گزارش های مطابق با سیستم قدیم به درستی مشاهده شد. ")

    def enter_len_report_manager_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 164
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

    def enter_len_report_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 152
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

    def enter_admin_report_select_the_report147(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report147, "پاداش مدیر مشتریان", "پاداش مدیر مشتریان")

    def enter_admin_report_select_the_report147_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='all-order']")
        assert self.driver.find_element('xpath', "//*[@id='settle_order']")
        assert self.driver.find_element('xpath', "//*[@id='has_payment_order']")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "نمایندگی"
        assert th4 == "نام مدیر نمایندگی"
        assert th5 == "مجموع سود ترخیص ریالی"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report15_agency_id(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id_option)
        sleep(0.3)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_select_the_report15_agency_id_btn)

    def enter_admin_report_select_the_report146(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report146, "گزارش پورسانت مسئول انبار", "گزارش پورسانت مسئول انبار")

    def enter_admin_report_select_the_report146_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/a")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "انباردار"
        assert th3 == "تعداد کارتن"
        assert th4 == "مبلغ اولیه پاداش"
        assert th5 == "پاداش نهایی"
        print("جدول  وضریب ریالی و باتن تاثیر نظر به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report149(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report149, "گزارش پورسانت تحویل دهندگان سفارش", "گزارش پورسانت تحویل دهندگان سفارش")

    def enter_admin_report_select_the_report149_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[2]/div/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/a")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
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

    def enter_admin_report_select_the_report_new(self):
        enter_admin_report_arian_click(self, 'xpath', "//*[text()='گزارش پورسانت نمایندگی ها(جدید)']", "گزارش پورسانت نمایندگی ها(جدید)", "گزارش پورسانت نمایندگی ها(جدید)")

    def enter_admin_report_select_the_report_new_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        assert th1 == "ردیف"
        assert th2 == "نمایندگی"
        assert th3 == "پورسانت (ریال)"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report150(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report150, "گزارش پورسانت بازاریاب خارجی", "گزارش پورسانت بازاریاب خارجی")

    def enter_admin_report_select_the_report150_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report151(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report151, "گزارش پورسانت بازاریاب تلفنی", "گزارش پورسانت بازاریاب تلفنی")

    def enter_admin_report_select_the_report151_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "نام بازاریاب"
        assert th3 == "پورسانت (ریال)"
        assert th4 == "تعداد سفارش"
        print("جدول و جمع کل پورسانت ها به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report152(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report152, "گزارش پورسانت بازاریاب حضوری", "گزارش پورسانت بازاریاب حضوری (جدید)")

    def enter_admin_report_select_the_report152_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
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
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[2]/div/div[2]")
        print("جدول محاسبه پورسانت به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_arian_management_report1(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report1, "سندهای فروش آرین", "گزارش سندهای فروش ثبت شده در آرین")

    def enter_admin_report_arian_management_report1_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
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
        a = extract_number(text, 0)
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_arian_management_report2_search, a)
        sleep(2)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report2_search_btn)
        sleep(1)

    def enter_admin_report_arian_management_report3(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report3, "فاکتورهای ارسال نشده به آرین", "فاکتورهای ارسال نشده به آرین")

    def enter_admin_report_arian_management_report3_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
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
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report8, "صاحب سفارشان فاقد شناسه آرین", "صاحب سفارشان فاقد شناسه آرین")

    def enter_admin_report_arian_management_report8_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "نام و نام خانوادگی"
        assert th3 == "کدملی"
        assert th4 == "موبایل1"
        assert th5 == "موبایل2"
        assert th6 == "تلفن ثابت 1"
        print("جدول نمایش داده شده صحیح می باشد.")

    def enter_admin_report_arian_management_report9(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_arian_management_report9, "مانیتورینگ آرین", "مانیتورینگ آرین")

    def enter_admin_report_arian_management_report9_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div/div[1]/div[1]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div/div[1]/div[2]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div/div[2]/div[1]/div")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div/div[2]/div[2]/div")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "نوع تراکنش"
        assert th3 == "وضعیت درخواست http"
        assert th4 == "شناسه دریافتی"
        assert th5 == "موجودیت مرتبط"
        print(" نمودارها و جدول نمایش داده شده صحیح می باشد.")

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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "وضعیت"
        assert th4 == "مبلغ"
        assert th5 == "حساب"
        assert th6 == "توضیحات"
        assert th7 == "زمان پرداخت"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        assert th8 == "ایجادکننده"
        assert th9 == "شماره حساب/کارت پرداخت کننده"
        assert th10 == "نام صاحب حساب پرداخت کننده"
        assert th11 == "علت عدم انتخاب موارد مشابه"
        assert th12 == "موبایل"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report11(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report11, "اتصال ها به درگاه", "اتصال ها به درگاه")

    def enter_admin_report_select_the_report11_check_table(self):
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[1]/div[1]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[1]/div[2]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[2]/div[1]/div")
        assert self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div[2]/div[2]/div")
        th1 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr[2]/th[11]").text
        assert th1 == "ردیف"
        assert th2 == "بانک"
        assert th3 == "نوع پرداخت"
        assert th4 == "وضعیت مقدار برگشتی"
        assert th5 == "شماره پیگیری بانک"
        assert th6 == "مبلغ"
        assert th7 == "کارت"
        assert th8 == "پرداخت متصل"
        assert th9 == "پیش فاکتور ها"
        assert th10 == "موجودیت مرتبط"
        assert th11 == "زمان ایجاد"
        print("جدول ها و بخش های دیگر به درستی نمایش داده شدند.")
        print("________________________________")

    def enter_admin_report_select_the_report33(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report33, "کالاهای تحویل شده با تایید مدیریت", "کالاهای تحویل شده با تایید مدیریت")

    def enter_admin_report_select_the_report33_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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

    def enter_admin_report_select_the_report31(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report31, "گزارش صاحبان پیش‌فاکتور سفارش", "گزارش صاحبان پیش‌فاکتور سفارش")

    def enter_admin_report_select_the_report31_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
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

    def enter_admin_report_select_the_report21(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report21, "گزارش صاحبان سفارش", "گزارش صاحبان سفارش")

    def enter_admin_report_select_the_report21_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نام انگلیسی صاحب سفارش"
        assert th3 == "صاحب سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "ارزش فاکتورهای تایید شده(میلیون تومان)"
        assert th6 == "پرداخت های تایید شده(میلیون تومان)"
        assert th7 == "تعداد سفارش"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report115(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report115, "گزارش سفارشات تحویل شده کالاپیک", "لیست گزارش سفارشات تحویل شده کالاپیک")

    def enter_admin_report_select_the_report115_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        scrolled1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]")
        sleep(0.5)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره قیض"
        assert th3 == "شماره ترک"
        assert th4 == "وزن جرمی (KG)"
        assert th5 == "وزن حجمی (KG)"
        assert th6 == "تعداد کالای تحویل شده"
        assert th7 == "ترک فرعی"
        assert th8 == "هزینه محاسبه شده کالاپیک (ریال)"
        assert th9 == "اضافه مسیر (ریال)"
        scrolled2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]")
        sleep(0.5)
        scrolled2.location_once_scrolled_into_view
        sleep(0.5)
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]").text
        assert th10 == "جمع کل (ریال)"
        assert th11 == "صاحب پیش فاکتور"
        assert th12 == "شماره بچ"
        assert th13 == "زمان تحویل"
        assert th14 == "شهر"
        assert th15 == "آدرس"
        assert th16 == "زمان ایجاد"
        print("جدول و نمودار به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report76(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report76, "سفارش های تحویل شده", "سفارش های تحویل شده")

    def enter_admin_report_select_the_report76_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='final-tarkhis-data']")
        scrolled1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]")
        sleep(0.5)
        scrolled1.location_once_scrolled_into_view
        sleep(0.5)
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
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[17]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[17]").text
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

    def enter_admin_report_select_the_report02_tn(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[2]/a[1]").text
        return a

    def enter_admin_report_reports_search_tn(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', admin_report_arian_management_report2_search, text)
        sleep(1)
        wait_until_element_has_an_attribute(self, 'xpath', admin_report_arian_management_report2_search_btn)
        sleep(1)

    def enter_admin_report_select_the_report22_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table table-center']/tbody/tr"))
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report79(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report79, "گزارش فاکتور های پرداخت شده با اصلاح..", "گزارش فاکتور های پرداخت شده با اصلاح سابقه")

    def enter_admin_report_select_the_report79_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "کاربر ثبت کننده"
        assert th5 == "زمان ثبت"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        assert th6 == "قیمت نهایی"
        assert th7 == "مبلغ پرداخت شده"
        assert th8 == "توضیحات"
        print("جدول2 به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report23(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report23, "فاکتورهای تسعیر ارز ایجاد شده", "لیست فاکتورهای تسعیر ارز ایجاد شده")

    def enter_admin_report_select_the_report23_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "صاحب پیش فاکتور"
        assert th4 == "نوع پیش فاکتور"
        assert th5 == "نرخ ارز اولیه"
        assert th6 == "نرخ ارز جدید"
        assert th7 == "مبلغ فاکتور تسعیر"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report36(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report36, "ترک های فاکتور نخورده", "ترک های فاکتور نخورده")

    def enter_admin_report_select_the_report36_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره بسته"
        assert th3 == "سفارش"
        assert th4 == "ثبت در سیستم مالی"
        assert th5 == "تغییرات سفارش‌های تسویه شده"
        assert th6 == "نیاز به چاپ فاکتور رسمی"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        assert th7 == "فاکتور رسمی بعد از چاپ"
        assert th8 == "وزن سفارش (KG)"
        assert th9 == "کالای سفارش"
        assert th10 == "خدمات موردنیاز"
        assert th11 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report20(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report20, "پیش فاکتور های حمل صادر شده", "لیست پیش فاکتور های حمل صادر شده")

    def enter_admin_report_select_the_report20_check_table(self):
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
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
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

    def enter_admin_report_select_the_report26_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a == 1
        print("سرچ به درستی انجام شد.")

    def enter_admin_report_select_the_report133(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report133, "پرداخت هایی که از طریق دستگاه پوز دوبار..", "پرداخت هایی که از طریق دستگاه پوز دوبار ثبت شده")

    def enter_admin_report_select_the_report133_check_table(self):
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

    def enter_admin_report_select_the_report82(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report82, "درخواست های عودت وجه - مالی", "لیست درخواست های عودت وجه - مالی")

    def enter_admin_report_select_the_report82_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر"
        assert th3 == "مبلغ"
        assert th4 == "واحد"
        assert th5 == "زمان تغییرات"
        assert th6 == "مدیر مشتری"
        assert th7 == "فایل"
        assert th8 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report_fleet_costs(self):
        enter_admin_report_arian_click(self, 'xpath', "//*[text()='هزینه های ناوگان']", "هزینه های ناوگان", "هزینه های ناوگان")

    def enter_admin_report_select_the_report_fleet_costs_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[2]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "نوع هزینه"
        assert th3 == "مبلغ هزینه (ریال)"
        assert th4 == "توضیحات"
        assert th5 == "کیلومتر"
        assert th6 == "تاریخ انجام"
        assert th7 == "شخص انجام دهنده"
        print("نمودارها و جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report144(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report144, "سفارش های دارای پیش فاکتور سود منفی", "سفارش های دارای پیش فاکتور سود منفی")

    def enter_admin_report_select_the_report144_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "خدمات موردنیاز"
        assert th4 == "پیش فاکتور های سود منفی"
        assert th5 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report17(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report17, "گزارش هزینه ها و فروش بچ ها", "گزارش هزینه ها و فروش بچ ها")

    def enter_admin_report_select_the_report17_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='chart-lastthreemonth']")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "کل وزن قابل پرداخت"
        assert th3 == "شماره بسته"
        assert th4 == "موقعیت"
        assert th5 == "مبدا"
        assert th6 == "مقصد"
        assert th7 == "هزینه بچ"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
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

    def enter_admin_report_select_the_report49(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report49, "گزارش مالی ترخیص", "گزارش مالی ترخیص")

    def enter_admin_report_select_the_report49_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[4]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
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

    def enter_admin_report_select_the_report61(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report61, "فاکتورهای ایجاد شده به تفکیک خدمات", "لیست فاکتورهای ایجاد شده به تفکیک خدمات")

    def enter_admin_report_select_the_report61_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='op-location-info']")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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

    def enter_admin_report_select_the_report53(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report53, "گزارش پرداخت های دارای اطلاعات غلط", "گزارش پرداخت های دارای اطلاعات غلط")

    def enter_admin_report_select_the_report53_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[11]").text
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

    def enter_admin_report_select_the_report27(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report27, "سفارش های تسویه نشده", "سفارش های تسویه نشده")

    def enter_admin_report_select_the_report27_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "مدیر مشتری"
        assert th4 == "صاحب سفارش"
        assert th5 == "زمان تحویل سفارش"
        assert th6 == "دلار"
        assert th7 == "یورو"
        assert th8 == "یوان"
        assert th9 == "درهم امارات"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        assert th10 == "لیر ترکیه"
        assert th11 == "لیر سوریه"
        assert th12 == "ریال"
        assert th13 == "ریال*"
        assert th14 == "هزینه های ثبت نشده"
        assert th15 == "سفارش تسویه شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report59(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report59, "گزارش تراکنش های ثبت چین فاقد پیش فاکتور", "گزارش تراکنش های ثبت چین فاقد پیش فاکتور")

    def enter_admin_report_select_the_report59_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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

    def enter_admin_report_select_the_report54(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report54, "فاکتورهای رسمی مشتریان دارای کیف پول..", "لیست فاکتورهای رسمی مشتریان دارای کیف پول منفی")

    def enter_admin_report_select_the_report54_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[9]").text
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

    def enter_admin_report_select_the_report113(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report113, "فاکتورهایی که مبلغ باقیمانده منفی دارند", "لیست فاکتورهایی که مبلغ باقیمانده منفی دارند")

    def enter_admin_report_select_the_report113_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[9]").text
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

    def enter_admin_report_select_the_report18(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report18, "گزارش سفارشات تسویه شده اصلاح سابقه‌دار", "گزارش سفارشات تسویه شده اصلاح سابقه‌دار")

    def enter_admin_report_select_the_report18_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        assert th8 == "ایجادکننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report28(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report28, "سفارش هایی که تسویه شده اند اما بارگیری..", "سفارش هایی که تسویه شده اند اما بارگیری نشده")

    def enter_admin_report_select_the_report28_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "سفارش تسویه شده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report109(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report109, "فاکتورهای غیرمعتبر دارای موجودی", "فاکتورهای غیرمعتبر دارای موجودی")

    def enter_admin_report_select_the_report109_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "درصد مالیات"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        assert th5 == "پرداخت شده (در واحد)"
        assert th6 == "عنوان فاکتور"
        assert th7 == "کاربر ثبت کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report138(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report138, "فاکتورهایی که پس از چاپ فاکتور رسمی نام..", "لیست فاکتورهایی که پس از چاپ فاکتور رسمی نام صاحب فاکتور تغییر کرده")

    def enter_admin_report_select_the_report138_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "صاحب سفارش"
        assert th3 == "پرداخت شده (در واحد)"
        assert th4 == "شماره پیگیری"
        assert th5 == "شماره پیش فاکتور"
        assert th6 == "کاربر ثبت کننده"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th7 == "زمان ثبت"
        assert th8 == "قیمت نهایی"
        assert th9 == "توضیحات"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report66(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report66, "گزارش درآمد و هزینه ترخیص دارای ترک فرعی", "لیست گزارش درآمد و هزینه ترخیص دارای ترک فرعی")

    def enter_admin_report_select_the_report66_check_table(self):
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

    def enter_admin_report_select_the_report64(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report64, "گزارش درآمد و هزینه حمل دارای ترک فرعی", "لیست گزارش درآمد و هزینه حمل دارای ترک فرعی")

    def enter_admin_report_select_the_report64_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
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

    def enter_admin_report_select_the_report140(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report140, "سفارشها با فاکتور رسمی که نرخ ارز آنها..", "سفارشها با فاکتور رسمی که نرخ ارز آنها تغییر کرده")

    def enter_admin_report_select_the_report140_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "ایجادکننده"
        assert th9 == "کاربر تایید کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report134(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report134, "تراکنش های ثبت سفارش", "لیست تراکنش های ثبت سفارش")

    def enter_admin_report_select_the_report134_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "شماره بچ"
        assert th4 == "نوع تراکنش"
        assert th5 == "نوع هزینه / دریافت"
        assert th6 == "مبلغ تراکنش"
        assert th7 == "پیش فاکتورهای یوانی"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
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

    def enter_admin_report_select_the_report125(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report125, "صورتحساب مالی نمایندگی ها", "صورتحساب مالی نمایندگی ها")

    def enter_admin_report_select_the_report125_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "دریافت کننده"
        assert th4 == "ارسال کننده"
        assert th5 == "وزن سفارش (KG)"
        assert th6 == "کالای سفارش"
        assert th7 == "خدمات موردنیاز"
        assert th8 == "تعداد پیش فاکتور های حمل رسمی"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[23]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
        th15 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[15]").text
        th16 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]").text
        th17 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[17]").text
        th18 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[18]").text
        th19 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[19]").text
        th20 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[20]").text
        th21 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[21]").text
        th22 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[22]").text
        th23 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[23]").text
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

    def enter_admin_report_select_the_report75_tn(self):
        sleep(1)
        buttons = self.driver.find_elements('xpath', "//table/tbody/tr/td[2]/a[@class='btn btn-sm btn-block btn-info tn-linkedin mb-2 btn-social']")
        sleep(1)
        if buttons:
            a = buttons[0].text
            return a
        else:
            print("هیچ Tn پیدا نشد.")

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

    def enter_admin_report_select_the_report08(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report08, "تبدیل ارزهای انجام شده", "لیست تبدیل ارزهای انجام شده")

    def enter_admin_report_select_the_report08_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[13]").text
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

    def enter_admin_report_select_the_report145(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report145, "فاکتور های تایید شده توسط مدیر مشتری", "فاکتور های تایید شده توسط مدیر مشتری")

    def enter_admin_report_select_the_report145_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
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

    def enter_admin_report_select_the_report136(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report136, "هزینه و فروش", "گزارش هزینه و فروش سفارش ها")

    def enter_admin_report_select_the_report136_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "شماره بچ"
        assert th4 == "هزینه حمل"
        assert th5 == "فاکتور حمل"
        assert th6 == "درآمد حمل"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[16]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
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

    def enter_admin_report_select_the_report123(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report123, "هزینه و فروش سفارشهای کنسل شده بعد از..", "هزینه و فروش سفارشهای کنسل شده بعد از بارگیری")

    def enter_admin_report_select_the_report123_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "هزینه سایر"
        assert th4 == "فاکتور سایر"
        assert th5 == "درآمد سایر"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report116(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report116, "تراکنش های تکراری چین", "لیست 'گزارش تراکنش های تکراری چین'")

    def enter_admin_report_select_the_report116_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "وضعیت"
        assert th3 == "مبلغ"
        assert th4 == "حساب"
        assert th5 == "توضیحات"
        assert th6 == "توضیحات تاییدیه"
        assert th7 == "شماره سفارش"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        assert th8 == "زمان پرداخت"
        assert th9 == "ایجادکننده"
        assert th10 == "شماره حساب/کارت پرداخت کننده"
        assert th11 == "نام صاحب حساب پرداخت کننده"
        assert th12 == "علت عدم انتخاب موارد مشابه"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report108(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report108, "سفارش هایی که وارد تسویه نهایی نشده اند", "سفارش هایی که وارد تسویه نهایی نشده اند")

    def enter_admin_report_select_the_report108_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "وزن قابل پرداخت سفارش (kg)"
        assert th5 == "مقدار بدهی به ریال"
        assert th6 == "مشکل تسویه دارد"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        assert th7 == "خدمات موردنیاز"
        assert th8 == "مدیر مشتری"
        assert th9 == "بازاریاب"
        assert th10 == "ایجادکننده"
        assert th11 == "زمان ایجاد"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report110(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report110, "گزارش سفارش های تسویه شده فاقد فاکتور..", "سفارش های تسویه شده فاقد پیش فاکتور به ازای خدمت")

    def enter_admin_report_select_the_report110_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
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

    def enter_admin_report_select_the_report120(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report120, "گزارش پیش‌ فاکتورهایی که چندبار در آرین..", "گزارش پیش‌ فاکتورهایی که چندبار در آرین ثبت شده اند")

    def enter_admin_report_select_the_report120_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        assert th1 == "ردیف"
        assert th2 == "جزئیات سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "درصد مالیات"
        assert th5 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th6 == "عنوان فاکتور"
        assert th7 == "کاربر ثبت کننده"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report40(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report40, "مغایرت فاکتورهای حمل", "مغایرت فاکتورهای حمل")

    def enter_admin_report_select_the_report96(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report96, "سفارش های لغو شده دارای فاکتور پرداخت..", "سفارش های لغو شده دارای فاکتور پرداخت شده")

    def enter_admin_report_select_the_report96_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[2]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div/div[1]/a[3]")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[9]").text
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
        th1 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[1]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیش فاکتور اولیه"
        assert th3 == "قیمت نهایی اولیه"
        assert th4 == "شماره پیش فاکتور ثانویه"
        assert th5 == "قیمت نهایی ثانویه"
        assert th6 == "عنوان"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report03(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report03, "مغایرت قیمت برند در فاکتور حمل",
                                       "مغایرت قیمت برند در فاکتور حمل")

    def enter_admin_report_select_the_report03_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "سفارش"
        assert th3 == "شماره پیش فاکتور"
        assert th4 == "قیمت اعلامی"
        assert th5 == "قیمت نهایی (با نرخ تبدیل خام)"
        assert th6 == "پرداخت شده (در واحد)"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        assert th7 == "قیمت هر کیلو کالای برند"
        assert th8 == "قیمت جدید"
        assert th9 == "مغایرت"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")

    def enter_admin_report_select_the_report92(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report92, "بدهی های کیف پول کاربران", "لیست بدهی های کیف پول کاربران")

    def enter_admin_report_select_the_report92_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "مشتریان"
        assert th3 == "مدیر مشتریان"
        assert th4 == "موبایل1"
        assert th5 == "دلار"
        assert th6 == "یورو"
        scrolled = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]")
        sleep(0.5)
        scrolled.location_once_scrolled_into_view
        sleep(0.5)
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        th8 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[8]").text
        th9 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[9]").text
        th10 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[10]").text
        th11 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[11]").text
        th12 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[12]").text
        th13 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[13]").text
        th14 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[14]").text
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

    def enter_admin_report_select_the_report88(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report88, "دلیل رد کردن پرداخت", "دلیل رد کردن پرداخت")

    def enter_admin_report_select_the_report88_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        assert th1 == "ردیف"
        assert th2 == "کاربر مرتبط"
        assert th3 == "مبلغ"
        assert th4 == "ایجادکننده"
        assert th5 == "علت لغو"
        assert th6 == "توضیحات تایید / عدم تایید"
        print("جدول به درستی نمایش داده شد.")
        print("________________________________")






















































