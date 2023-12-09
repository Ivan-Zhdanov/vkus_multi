from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import secrets
# import undetected_chromedriver as uc
from selenium import webdriver
import time
import fake_useragent
import keyboard


# url = 'https://foodandhealth.ru/?s=%D0%B0'
# url = 'https://foodandhealth.ru/page/1/?s=%D0%B0'

service = Service(executable_path='./webdriver/chromedriver.exe')
options = webdriver.ChromeOptions()

# useragent = fake_useragent.UserAgent()
# options.add_argument(f'user-agent={useragent.Random}')
# proxy
# options.add_argument("--proxy-server=95.164.200.193:9241")
# proxy_username = 'UpuaEg'
# proxy_password = 'uZbywh'
# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{proxy_username}:{proxy_password}@95.164.111.156:9600',
#         # 'verify_ssl': False,
#     }
# }

driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:\\Users\\elero\\OneDrive\\Desktop\\Python\\ALPHA_AG\\webdriver\\chromedriver.exe', options=options)
# driver = uc.Chrome()

# ----------------------------------

# driver = webdriver.Chrome(options=options, executable_path=r"C:\\vk\\vkus\\chromedriver.exe")


# url = "https://bot.sannysoft.com/"
# driver.get(url)
# time.sleep(5)
# driver.quit()
#

#
# for n in range(117, 118):
#     url = f'https://foodandhealth.ru/page/{n}/?s=%D0%B0'
#     driver.get(url=url)
#     hrefs = driver.find_elements(By.XPATH, "//h2/a")
#     for href in hrefs:
#         print(href.get_attribute('href'))
#


# url ='https://platform.openai.com/login?launch'
# driver.get(url=url)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=service, options=options)

# url ='https://platform.openai.com/login?launch'
# driver.get(url=url)


driver.execute_script("window.open('https://platform.openai.com/login?launch', '_blank')")

a = input('------')
api_btn = driver.find_element(By.XPATH, "//h1[contains(text(), 'API')]").click()
time.sleep(35)
driver.switch_to.window(driver.window_handles[1])

driver.switch_to.frame(0)

driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()



driver.execute_script("window.open('https://nowsecure.nl/', '_blank')")



#
# email = driver.find_element(By.XPATH, "//input[@inputmode='email']").send_keys("william69henderlitewdq@outlook.com")
# button = driver.find_element(By.XPATH, "//div[@class='c3fc7dc62']").click()
#
# time.sleep(2)
# keyboard.write('128ZuR6mqgBZQBI5')
# time.sleep(2)
# keyboard.press_and_release('enter')



# email = driver.find_element(By.XPATH, "//div[@class='ccaa5e013']").send_keys("123")
# psw = driver.find_element(By.XPATH, "//input[@name ='password']']").send_keys("128ZuR6mqgBZQBI5")
# button2 = driver.find_element(By.XPATH, "//button[@name='action']").click()

# edit_field = driver.find_element(By.XPATH, "//textarea[@class='w-full mx-4 overflow-y-auto custom-scrollbar resize-y pr-8 text-md bg-base-100 border-primary-focus border rounded-md max-h-40 disabled:border-base-300 disabled:bg-base-300 disabled:cursor-not-allowed']")
# edit_field.send_keys("Напиши что такое мучнистая гниль")
# edit_field.send_keys(Keys.ENTER)
# keyboard.send("enter")
# time.sleep(1000)
# log_in = driver.find_element(By.PARTIAL_LINK_TEXT, r"Log").click()

x = input('введи число')
print(x)
# time.sleep(1000)
