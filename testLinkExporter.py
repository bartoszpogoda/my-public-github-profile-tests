import testlink
from unittest import (
    TestLoader,
    TextTestRunner)
import os

from myGhProfileTests import *
from jsonTestResult import JsonTestResult

# Note:
#
# Before execution following ENV variables should be set to override testlink defaults
#
# set TESTLINK_API_PYTHON_SERVER_URL=http://192.168.1.100/lib/api/xmlrpc/v1/xmlrpc.php
# set TESTLINK_API_PYTHON_DEVKEY=4d1******************1cc
#
#

if __name__ == '__main__':

    with open(os.devnull, 'w') as null_stream:

        # TestLink context
        platformname = 'SeleniumWD/Firefox'
        testcaseid = 'my-gh-2'

        # new a runner and overwrite resultclass of runner
        runner = TextTestRunner(stream=null_stream)
        runner.resultclass = JsonTestResult

        # create a testsuite
        suite = TestLoader().loadTestsFromTestCase(MyPublicGithubProfileTests)

        # run the testsuite, measure time
        start = datetime.now().timestamp()
        result = runner.run(suite)
        end = datetime.now().timestamp()

        # evaluate summary result. 'f'ailed if any failure or error, 'p'assed otherwise
        summary_result = 'p' if len(result.failures) + len(result.errors) == 0 else 'f'

        # extract names of test method which passed
        passedTestNames = list(map(lambda test: test._testMethodName, result.successes))

        steps = [
            {
                'step_number': 1,
                'result': 'p' if 'test_my_name' in passedTestNames else 'f',
                'notes': ''
            }, {
                'step_number': 2,
                'result': 'p' if 'test_more_than_5_followers' in passedTestNames else 'f',
                'notes': ''
            }, {
                'step_number': 3,
                'result': 'p' if 'test_java_dominance' in passedTestNames else 'f',
                'notes': ''
            }, {
                'step_number': 4,
                'result': 'p' if 'test_commits_last_week' in passedTestNames else 'f',
                'notes': ''
            }
        ]

        # Send results to TestLink
        tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
        tls.reportTCResult(None,
                           2,
                           None,
                           summary_result,
                           result.jsonify(),
                           guess=True,
                           testcaseexternalid=testcaseid,
                           platformname=platformname,
                           execduration=(end - start) / 60,
                           timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"),
                           steps=steps)

