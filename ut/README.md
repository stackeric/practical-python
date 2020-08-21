## Python unittest

test case, test suite,test loader, test runner


### 1. Basic TestCase
```python
import unittest


class IntegerArithmeticTestCase(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':

    unittest.main()

```

* import unittest module
* define a class inherits from unittest TestCase
* run tests with main function

### 2. The Main

```python
    main = TestProgram
    class TestProgram(object):
        pass
```

* main is a alias name for TestProgram class
* run main() just return an TestProgram instance
* after new TestProgram instance, __init__ func will be be executed
  
```python
    self.module = __import__(module)
    self.parseArgs(argv)
    self.runTests()
```
* default module args is __main__, after __import__("__main__) ,self.module is current executed file
* parseArgs  load testcases and return Test suite
* runTests run test tests one by one by testRunner

### 3. parseArgs

```python
    self.createTests()
```
* if run with directory  parseArgs will run  _do_discovery function to load all case from specified directory
* other wise ,just run createTests which return test to run

#### 3.1 createTests

* now createTests with default args 

```python
    def createTests(self, from_discovery=False, Loader=None):
        if self.testNames is None:
            self.test = self.testLoader.loadTestsFromModule(self.module)
```
#### 3.2 loadTestsFromModule

* on step TestProgram self.module is current executed file
  
```python
tests = []
for name in dir(module):
    obj = getattr(module, name)
    if isinstance(obj, type) and issubclass(obj, case.TestCase):
        tests.append(self.loadTestsFromTestCase(obj))
```

* loop all module attrs, if obj is an class and is subclass of TestCase add test to list tests 

#### 3.3 loadTestsFromTestCase 

```python
    testCaseNames = self.getTestCaseNames(testCaseClass)
    loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames))
```

* first get TestCases Name from class
```python
class IntegerArithmeticTestCase(TestCase):

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

```
* in this cases , testCaseNames is [testAdd,testMultiply],then construct them to TestSuite
* map(testCaseClass, testCaseNames) create two TestCase instance with args methodName by testCaseNames
* loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames)) create TestSuite instances by testcase instances  created by map function
* loadTestsFromTestCase return TestSuite with testcase
* createTests is over ,now we have test suite with two testcases

### 4. runTests

#### 4.1 runTests

```python
self.testRunner = runner.TextTestRunner
self.result = testRunner.run(self.test)
```

* function runTests first create a default  runner.TextTestRunner instance
* then run self.test created by parseArgs

#### 4.2 testRunner run

* first create and register TextTestResult instance which store test result

```python
    result = self._makeResult()
    registerResult(result)
```
* then run self.test

```python
    test(result)
```
* now test is an instance of TestSuite,  instance can be call ?you must specify an __call__ method  
* TestSuite do have an attribute inherite from BaseTestSuite
```python
    def __call__(self, *args, **kwds):
        return self.run(*args, **kwds)
```
* test(result) means call TestSuite run method with args result

```python
    def run(self, result, debug=False):
```

#### 4.3 TestSuite run

```python
    for index, test in enumerate(self):
        self._tearDownPreviousClass(test, result)
        self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__
        test(result)
        self._tearDownPreviousClass(None, result)
        self._handleModuleTearDown(result)
        return result
```
* self is TestSuite themself
* enumerate will call  TestSuite __iter__ method 

```python
    def __iter__(self):
        return iter(self._tests)
```
* so we get all testcases 
* before and after run testcases ,we run setup&teardown methods
* test current is instance of TestCase, like TestSuite,when call test(result),we call instance class __call__

#### 4.4 TestCase run
```python
    def __call__(self, *args, **kwds):
        return self.run(*args, **kwds)
```

* so call test(result) just run TestCase run method
  
```python
    def run(self, result=None):
        result.startTest(self)
        testMethod = getattr(self, self._testMethodName)
        self._addSkip(result, self, skip_why)
        outcome = _Outcome(result)
        self._callSetUp()
        self._callTestMethod(testMethod)
        self._callTearDown()
        result.addSuccess(self)
        result.stopTest(self)
```
* testMethod here is func testAdd or testMultiply
* then process skip setup 
* _Outcome is a result collector with contextmanager
* _callTestMethod run real testcases 

```python
    def _callTestMethod(self, method):
        method()
```
* call testcase function directly

### 5. Result

* let's come back
* after testcase run, we get testcase run result
* after teardown testcase ,we return TestSuite Run loop
```python
    for index, test in enumerate(self):
```
* after  finish TestSuite loop, we tearDown testsuit class and return the result to runner
* after finish testsuit run in runner , we get exec time, log Error if exist,stream all results.
* now we come back to runTests and exit all program

### 6. Others

* typically, we run test cases in a directory
* in this way ,parseArgs will call _do_discovery and scan all directory cases

```python
    def _do_discovery(self, argv, Loader=None):
        self.start = '.'
        self.pattern = 'test*.py'
        self.top = None
        if argv is not None:
            # handle command line args for test discovery
            if self._discovery_parser is None:
                # for testing
                self._initArgParsers()
            self._discovery_parser.parse_args(argv, self)

        self.createTests(from_discovery=True, Loader=Loader)
``` 