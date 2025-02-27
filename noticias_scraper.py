from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.infomoney.com.br/mercados/wirecard-como-o-sumico-de-us-2-bilhoes-levou-uma-gigante-alema-a-falencia/")
driver.maximize_window()

sleep(5)

try:
    pop_up = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="fechar"]'))
    )
    pop_up.click()
except Exception as e:
    print("Pop-up não encontrado ou erro ao fechar:", e)

noticiaTitulo = driver.find_element(By.CLASS_NAME, 'text-3xl').text
noticiaSubTitulo = driver.find_element(By.CLASS_NAME, 'text-lg').text

noticiaTexto = driver.find_elements(By.TAG_NAME, 'p')
noticiaCompleta = "\n".join([p.text for p in noticiaTexto if p.text.strip()])

tabela = pd.DataFrame(columns=["Título", "Subtítulo", "Texto"])

tabela.loc[len(tabela)] = [noticiaTitulo, noticiaSubTitulo, noticiaCompleta]

tabela.to_csv("noticia.csv", index=False, encoding="utf-8")

print(tabela)