from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get("http://200.201.27.34:81/sislob/login.jsp")

navegador.find_element("name", "id").send_keys("*********")
navegador.find_element("name", "senha").send_keys("********")
botaoConfirmar = navegador.find_element("name", "enviar")
botaoConfirmar.click()

sleep(1)
listaRMS = navegador.find_element("link text", "Adicionar itens nos processos de compra")
listaRMS.click()

abas = navegador.window_handles
navegador.switch_to.window(abas[-1])

sleep(10)