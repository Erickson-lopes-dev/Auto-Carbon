from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller

# Verifique se a versão atual do chromedriver existe e se não existir,
# baixe-o automaticamente, em seguida, adicione chromedriver ao caminho
from selenium.webdriver.common.keys import Keys

chromedriver_autoinstaller.install()

# instancia o webdriver do chrome
driver = webdriver.Chrome()

languge = 'Python'

# Abre a página
driver.get("https://carbon.now.sh")

try:
    drop_language_xpath = '//*[@id="downshift-input-Auto"]'

    dropdown_language = driver.find_element_by_xpath(drop_language_xpath)

    sleep(0.30)
    dropdown_language.click()

    python = driver.find_element_by_xpath('//*[@id="downshift-1-item-50"]')

    sleep(0.30)

    python.click()
except Exception as error:
    print(f'Erro ao selecionar a linguagem: {error}')

else:
    campo = driver.find_element_by_xpath('//*[@id="export-container"]/div/div[2]/div/div[4]/div[1]')
    campo.click()

    campo = driver.find_element_by_xpath('//*[@id="export-container"]/div/div[2]/div/div[1]/textarea')
    campo.sendKeys('ola')
sleep(10)

input()
# Fecha a janela
driver.close()