'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

hub_url = "http://localhost:4444"

options = Options()

driver = webdriver.Remote(
    command_executor=hub_url,
    options=options
)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/muhammad.buddha17/")
time.sleep(5)

driver.maximize_window()
time.sleep(5)
print(driver.title)

driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Linux ke liye important
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

