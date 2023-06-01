import pytest
from selenium import webdriver
from utilities.ReadConfigurations import read_configuration


@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()

    #def pytest_configure(conf):
      #  conf._metadata['Project Name'] = 'Qafox'
       # conf._metadata['Module Name'] = 'Search'
        #conf._metadata['Tester'] = 'Surya'

    #@pytest.mark.optionalhook
    #def pytest_metadata(metadata):
     #   metadata.pop(' Java_Home', None)
      #  metadata.pop(' Plugins', None)









    # if browser == 'chrome':
        #driver = webdriver.Chrome()
  #  elif browser == 'firefox':
        #driver = webdriver.Chrome()
  #  else:
        #driver = webdriver.Ie()
#    return driver


#def pytest_addoption(parser):
    #parser.addoption('--browser')


#@pytest.fixture()
#def browser(request):
    #return request.config.getoption("--browser")

