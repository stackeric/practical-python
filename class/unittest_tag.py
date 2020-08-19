#### you want Tag func to your unittest

#### so you write a decorator , and a __tag__ to testcase
import unittest

DefultTag = {"All"}


def tag(*any_tag):

    def wrap(func):
        if not hasattr(func, "__tag__"):
            tags = DefultTag
            tags.update(any_tag)
            setattr(func, "__tag__", tags)
        else:
            getattr(func, "__tag__").update(any_tag)
        return func

    return wrap

#### then you write a testcase and decorator it with tag


@tag("V1", "V2")
def test_func(self):
    pass

#### now you want to run all test case with tag V1


run_tag = {"V1"}


class TestTag(unittest.TestCase):

    @tag("V1")
    def test_create_1(self):
        print("test_create_1")

    @tag("V2")
    def test_create_2(self):
        print("test_create_1")


#### bug, all case include, you have to filter case by tag
#### when ?
#### at test case runtime ,good
#### or at test case creation time
#### how ?
#### metaclass.
#### now define a metaclass

class Meta(type):
    def __new__(cls, clsname, bases, attrs):
        funcs, cases = filter_test_case(attrs)
        for test_case in cases.values():
            if hasattr(test_case, "__tag__") and len(
                getattr(test_case, "__tag__") & run_tag
            ):
                funcs.update(create_case(test_case))
            else:
                continue
        return super(Meta, cls).__new__(cls, clsname, bases, funcs)

#### ok now put it on your unitest


class TestCaseWithTag(unittest.TestCase, metaclass=Meta):
    pass

#### patch or  inheritance 

#### patch
unittest.TestCase = TestCaseWithTag

#### run it again, only test_create_1 include
#### perfect!

run_tag = {"V1"}


class TestTag(unittest.TestCase):
#### class TestTag(TestCaseWithTag): 

    @tag("V1")
    def test_create_1(self):
        print("test_create_1")

    @tag("V2")
    def test_create_2(self):
        print("test_create_1"
