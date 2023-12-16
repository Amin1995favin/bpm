import unittest
import HtmlTestRunner
import datetime
import xmlrunner
import os


class Result:

    def run_res(test_suite):
        suite = unittest.TestLoader().loadTestsFromTestCase(test_suite)
        report_directory = "Test_Results"

        # Create the directory if it does not exist
        os.makedirs(report_directory, exist_ok=True)

        # Define the HTML report name with a timestamp
        report_name = os.path.join(report_directory,
                                   f'TestReport_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.html')

        # Open the HTML report file in binary write mode
        with open(report_name, 'wb') as report_file:
            # Create an instance of the HTMLTestRunner
            runner = HtmlTestRunner.HTMLTestRunner(output=report_file)

            # Run the test suite using the HTMLTestRunner
            runner.run(suite)
        quit()