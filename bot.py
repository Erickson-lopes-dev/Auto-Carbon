from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller

# Verifique se a versão atual do chromedriver existe e se não existir,
# baixe-o automaticamente, em seguida, adicione chromedriver ao caminho
chromedriver_autoinstaller.install()


driver = webdriver.Chrome()
driver.get("https://carbon.now.sh")

sleep(10)
driver.close()