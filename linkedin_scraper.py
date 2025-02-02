from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/login")

time.sleep(30)

url_vagas = "https://www.linkedin.com/jobs/search/?keywords=Cientista%20de%20Dados"
driver.get(url_vagas)

time.sleep(10)

from selenium.webdriver.common.by import By

vagas = driver.find_elements(By.CLASS_NAME, "job-card-container")

for vaga in vagas:
    try:
        titulo = vaga.find_element(By.CSS_SELECTOR, ".job-card-list__title").text
        empresa = vaga.find_element(By.CSS_SELECTOR, ".job-card-container__company-name").text
        localizacao = vaga.find_element(By.CSS_SELECTOR, ".job-card-container__metadata-item").text

        print(f"Vaga: {titulo}\nEmpresa: {empresa}")
    except Exception as e:
        print(f"Erro ao extrair informações da vaga: {e}")
              
