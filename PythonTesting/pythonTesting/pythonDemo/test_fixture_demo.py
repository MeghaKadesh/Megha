import pytest



@pytest.mark.usefixtures("setup")
class TestExample:
    def test_megha(self):
        print("Hello world")
    def test_megha1(self):
        print(" Hi Megha")
    def test_megha3(self):
        print("hiiii")
    def test_megha4(self):
        print("hi ")
