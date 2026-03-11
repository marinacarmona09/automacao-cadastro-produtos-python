import pyautogui 
import time
import pandas as pd

pyautogui.PAUSE = 0.5
link_produtos = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
arquivo_dados = "produtos.csv"

# Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link_produtos)
pyautogui.press("enter")

# pausa maior
time.sleep(3)

# Fazer login
pyautogui.click(x=516, y=404)
pyautogui.write("email@exemplo.com")
pyautogui.press("tab") # proximo campo
pyautogui.write("senha_exemplo")
pyautogui.press("tab") # botão enter
pyautogui.press("enter")

# pausa para site carregar
time.sleep(4)

# Abrir a base de dados (importar dados)
tabela = pd.read_csv(arquivo_dados)
print(tabela)

for linha in tabela.index: 
    # Cadastrar produtos
    pyautogui.click(x=464, y=295) # clica no campo "codigo do produto"
    codigo = str(tabela.loc[linha, "codigo"]) # str -> formatar como texto ; [linha,"coluna"]
    pyautogui.write(codigo)
    pyautogui.press("tab") # passa para proximo campo 
    # marca 
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo) 
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preço
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan": 
        pyautogui.write(obs)
    pyautogui.press("tab") # botão do enter
    pyautogui.press("enter") # clica enviar

    # voltar para inicio da pagina
    pyautogui.scroll(5000)

# Repetir o passo 4 até acabar a lista de produtos