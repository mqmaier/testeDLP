from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

def testar_credenciais(url, credenciais):
    resultados = {}
    
    chrome_driver_path = 'path'
    service = Service(chrome_driver_path)
    service.start()
    driver = webdriver.Chrome(service=service)
    
    for i, credencial in enumerate(credenciais, 1):
        try:
            
            driver.get(url)
            
            
            campo_usuário = driver.find_element(By.ID, "user_email")
            campo_usuário.clear()
            campo_usuário.send_keys(credencial["usuario"])
            
            campo_senha = driver.find_element(By.ID, "user_password")
            campo_senha.clear()
            campo_senha.send_keys(credencial["senha"])
            campo_senha.send_keys(Keys.RETURN)
            
            time.sleep(2)
            
            if "Dashboard" in driver.title:
                print(f"Login bem sucedido com usuário: {credencial['usuario']} e senha: {credencial['senha']}")
                resultados[i] = {"usuario": credencial['usuario'], "senha": credencial['senha'], "sucesso": True}
            else:
                print(f"Login falou para o usuário: {credencial['usuario']} e senha: {credencial['senha']}")
                resultados[i] = {"usuario": credencial['usuario'], "senha": credencial['senha'], "sucesso": False}
                
        
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
    
    driver.quit()
    
    return resultados
    
def mostrar_resultados(resultados):
    print("\Resultados dos testes de credenciais:")
    for i, resultado in resultados.items():
        status = "Sucesso" if resultado["sucesso"] else "Falha"
        print(f"{i}. Usuário: {resultado['usuario']}, Senha: {resultado['senha']}, Status: {status}")
url = "https://dashboard.ebanx.com/users/sign_in"

credenciais = [
    {"usuario": "USER/EMAIL", "senha": "SENHA"},
    {"usuario": "USER/EMAIL", "senha": "SENHA"},
    {"usuario": "USER/EMAIL", "senha": "SENHA"},
    {"usuario": "USER/EMAIL", "senha": "SENHA"},
    

]

resultados  testar_credenciais(url, credenciais)

mostrar = input("Deseja ver os resultados dos testes? (s/n): ")
if mostrar.lower()=="s":
    mostrar_resultados(resultados)
else:
    print("Encerrado.")