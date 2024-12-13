import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

      

class TestAbs(unittest.TestCase):
	    
    def test_abs1(self):
        link1 = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys("qqq@qq.com")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text1 = browser.find_element(By.TAG_NAME, "h1").text  
        self.assertEqual(welcome_text1, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
    def test_abs2(self):
        link2 = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys("qqq@qq.com")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text2 = browser.find_element(By.TAG_NAME, "h1").text  
        self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!", "Should be absolute value of a number")           
        
if __name__ == "__main__":
    unittest.main()
