from selenium import webdriver

webdriver = webdriver.Chrome(

webdriver.get('https://aleo.tools/')

generate = webdriver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/div/div[1]/button/span')
generate.click()

Private_Key = webdriver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/form/div[2]/div[2]/div/div/span/span/input')

View_Key = webdriver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/form/div[3]/div[2]/div/div/span/span/input')

Address = webdriver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/form/div[4]/div[2]/div/div/span/span/input')

print(Private_Key, View_Key, Address)