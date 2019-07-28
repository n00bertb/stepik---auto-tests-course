#Тест валится т.к. неможет найти УНИКАЛЬНЫЙ placeholder(Введите фамилию)
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPage(unittest.TestCase):
	def test_page1(self):
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/registration1.html")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите имя"]')
		element.send_keys("Antuan")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите фамилию"]')
		element.send_keys("Gradu")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите Email"]')
		element.send_keys("jojo@mqil.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(2)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "текст должен совпадать") 

	def test_page2(self):
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/registration2.html")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите имя"]')
		element.send_keys("Antuan")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите фамилию"]')
		element.send_keys("Gradu")
		element = browser.find_element(By.XPATH, '//input[@placeholder="Введите Email"]')
		element.send_keys("jojo@mqil.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(2)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "текст должен совпадать")


if __name__ == "__main__":
	unittest.main()
