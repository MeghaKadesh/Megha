# any pytest file start with test_
#pytest method name should be start with test or end with test
#any code should be wrapped in method only
#method name should have sense.
# -k stands for methods name execution
# -s for logs in output (print the output in console)
# -v stands for more info like metadata
#you can run specific file with  py.test <file name> -v -s
#you can run full package with py.test
# you can mark (tag) tests @pytest.mark.smoke and run with -m
# you can skip test with @pytest.mark.skip  and run py.test
#you can run testcase but not to see the  status output  @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize
# fixture and make it available to all test cases(fixture name into parameters of method)
#datadrievn and parameterization can be done with return statments in tuple format
# when you define fixture scope class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")
@pytest.mark.xfail
def test_CreditCard():
    print("GoodMorning")