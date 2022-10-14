import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        driver = webdriver.Chrome()
        driver.get("http://qaboy.com/")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))


if __name__ == '__main__':
    unittest.main()