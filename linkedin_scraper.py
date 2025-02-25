from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/")

vagas_botao = driver.find_element(By.XPATH, "/html/body/nav/ul/li[4]/a")
vagas_botao.click()

try:
    pop_up = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/button'))
    )
    pop_up.click()
except Exception as e:
    print("Pop-up não encontrado ou erro ao fechar:", e)

vaga_titulo = driver.find_element(By.XPATH, '//*[@id="job-search-bar-keywords"]')
vaga_titulo.click()

vaga_titulo.send_keys("Analista de Dados")

vaga_localizacao = driver.find_element(By.XPATH, '//*[@id="job-search-bar-location"]')
vaga_localizacao.click()
vaga_localizacao.clear()

vaga_localizacao.send_keys("Brasil")
vaga_localizacao.send_keys(Keys.ARROW_DOWN)
vaga_localizacao.send_keys(Keys.RETURN)

vaga_card = driver.find_elements(By.CLASS_NAME, 'base-card__full-link')
len(vaga_card)
vaga_card[1].click()

vaga_textos = [top-card-layout__title for job in vaga_card]
vaga_textos