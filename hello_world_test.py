import pytest  
from hello_world import HelloWorld

#Test for basic requirements of prompt, text which matches exactly has rating of 1, text which "has no words in common" has rating of 0
def test_hello():
    HW = HelloWorld()
    assert HW.print_hello()=="Hello World"
test_hello()
