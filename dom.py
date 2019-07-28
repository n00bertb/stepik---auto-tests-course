import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#функция вычисления задачи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#открываем нужную страничку
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#ждём на страничке момента пока цена дома не упадет до 10000 RUR
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
#находим кнопку забронировать и нажимаем ее
browser.find_element(By.ID,"book").click()
#считываем значения x и передаем его в функцию
x = browser.find_element(By.ID,"input_value").text
y = calc(x)
#полученное из функции значение передаём в поле ответа
browser.find_element(By.ID,"answer").send_keys(y)
#находим кнопку отправить и нажимаем ее
browser.find_element(By.ID,"solve").click()

