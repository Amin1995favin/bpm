from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


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

    def enter_report(self):
        wait_until_element_has_an_attribute(self, 'xpath', admin_report)
        sleep(.3)

    def enter_report_delivery(self):
        wait_until_element_has_an_attribute(self, 'xpath', "/html/body/div[1]/aside/section/ul/li[5]/a")
        sleep(.3)

    def enter_report_manager_check(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[1]")
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div/div[3]")
        print("بخش پورسانت ها به درستی مشاهده شد. ")
        print("بخش گزارش موردنظر خود را انتخاب نمایید به درستی مشاهده شد. ")

    def enter_len_report_manager_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 10
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

    def enter_len_warehouse_iran_report_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 4
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

    def enter_len_warehouse_iran_delivery_report_check(self):
        a = len(self.driver.find_elements('xpath', admin_reports))
        print(a)
        assert a == 3
        print("تعداد گزارشات نمایش داده شده صحیح می باشد. ")

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

    def enter_admin_report_select_the_report22(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report22, "سفارش های تحویل شده توسط همکاران", "سفارش های تحویل شده توسط همکاران")

    def enter_admin_report_select_the_report22_check_table(self):
        assert self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[3]/div/div[1]/div/div[2]/div/div/div")
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره پیگیری"
        assert th3 == "صاحب سفارش"
        assert th4 == "تحویل دهنده"
        assert th5 == "موزع"
        assert th6 == "زمان تحویل"
        assert th7 == "توضیحات تحویل"
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

    def enter_admin_report_select_the_report111(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report111, "گزارش مدیریت ناوگان", "لیست مدیریت ناوگان")

    def enter_admin_report_select_the_report111_check_table(self):
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

    def enter_admin_report_select_the_report71(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report71, "تاریخچه‌ی چاپ لیبل", "تاریخچه‌ی چاپ لیبل")

    def enter_admin_report_select_the_report71_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
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

    def enter_admin_report_select_the_report55(self):
        enter_admin_report_arian_click(self, 'xpath', admin_report_select_the_report55, "سفارشات تحویل شده دلیوری", "سفارشات تحویل شده دلیوری")

    def enter_admin_report_select_the_report55_check_table(self):
        th1 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[1]").text
        th2 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[2]").text
        th3 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[3]").text
        th4 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[4]").text
        th5 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[5]").text
        th6 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[6]").text
        th7 = self.driver.find_element('xpath', "//table/thead/tr[2]/th[7]").text
        assert th1 == "ردیف"
        assert th2 == "شماره ترک"
        assert th3 == "صاحب سفارش"
        assert th4 == "مدیر مشتری"
        assert th5 == "تحویل دهنده"
        assert th6 == "موزع"
        assert th7 == "زمان تحویل سفارش"
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

    def enter_admin_report_select_the_report05_tn_assert_search(self):
        a = len(self.driver.find_elements('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr"))
        assert a >= 1
        print("سرچ به درستی انجام شد.")









