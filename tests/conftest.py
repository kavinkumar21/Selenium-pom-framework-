import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
opts.add_argument('--log-level=3')
driver = webdriver.Chrome(options=opts)

@pytest.fixture(scope="session")
def conf():
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()