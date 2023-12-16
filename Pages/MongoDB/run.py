from time import sleep

import schedule


class Run:

    def run_selenium_script(Test):

        print("aaaaaaaaaaaaaaaa")

        while True:
            schedule.run_pending()
            schedule.every(10).seconds.do(Test)

            print("ccccccccccccccccccc")
            Test()
            sleep(5)
