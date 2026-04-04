import os
import dados
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

navegador = webdriver.Chrome()
navegador.maximize_window()
espera = WebDriverWait(navegador, 15)

navegador.get(dados.sislob)

espera.until(EC.presence_of_element_located((By.NAME, 'id'))).send_keys(dados.usuario)
navegador.find_element(By.NAME, 'senha').send_keys(dados.senha)
botaoConfirmar = navegador.find_element(By.NAME, 'enviar').click()

menu = navegador.current_window_handle
abas_antes = navegador.window_handles

espera.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Adicionar itens nos processos de compra"))
).click()

espera.until(EC.new_window_is_opened(abas_antes))

abas_depois = navegador.window_handles
nova_aba = next(aba for aba in abas_depois if aba not in abas_antes)

navegador.switch_to.window(nova_aba)

try:
    navegador.find_element(By.CLASS_NAME, "zebra2")
    existe = True
except NoSuchElementException:
    existe = False 
if existe:
    navegador.close()
    espera.until(EC.number_of_windows_to_be(1))
    navegador.switch_to.window(menu)
else:
    pyautogui.alert("NENHUMA RMS ENCONTRADA")
    navegador.close()
    espera.until(EC.number_of_windows_to_be(1))
    navegador.switch_to.window(menu)

espera.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Entrada de Processos"))
).click()

espera.until(EC.new_window_is_opened(abas_antes))
abas_depois = navegador.window_handles
nova_aba = next(aba for aba in abas_depois if aba not in abas_antes)
navegador.switch_to.window(nova_aba)

espera.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Adicionar']"))
).click()


sleep(10)