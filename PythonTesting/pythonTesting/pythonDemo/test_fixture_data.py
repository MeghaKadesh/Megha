import pytest



@pytest.mark.usefixtures("dataLoad")


class TestExample:
    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])
        #print(dataLoad)


    def test_browser(self,browser):
        print(browser)


    def test_love(self,Love_To):
        print(Love_To[1])      # Dhaduti guledagudda to
