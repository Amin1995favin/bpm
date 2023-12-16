import jsonpickle
import sys
import unittest
from pymongo import MongoClient
import datetime


class Mongodb:

    def run_tests_and_insert_into_mongodb(Test , type_name):
        collection_name = "log_test"
        suite = unittest.TestLoader().loadTestsFromTestCase(Test)

        runner = unittest.TextTestRunner(stream=None, verbosity=2)

        result = runner.run(suite)

        e = datetime.datetime.now()

        test_results_json = {
            "type": type_name,
            "errors_len": len(result.failures),
            "errors": jsonpickle.decode(jsonpickle.encode(result.errors, unpicklable=False)),
            "failures": jsonpickle.decode(jsonpickle.encode(result.failures, unpicklable=False)),
            "skipped": jsonpickle.decode(jsonpickle.encode(result.skipped, unpicklable=False)),
            "messages": Test.tests_texts,
            "tests_run": result.testsRun,
            "was_successful": result.wasSuccessful(),
            "time": e.strftime("%Y-%m-%d %H:%M:%S"),
        }

        client = MongoClient('localhost', 27017)

        db = client['BPM']

        collection = db[collection_name]

        collection.insert_one(test_results_json)
        sys.exit()
