import pyautogui
import pandas as pd
import time

EstoqueDaEmpresa = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write("https://cadastramentodeestoque.com.br")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=685, y=451)


pyautogui.write("colaborador@empresa.com")
pyautogui.press("tab")
pyautogui.write("senhadoColaborador")
pyautogui.press("tab")
pyautogui.press("enter")



for linha in EstoqueDaEmpresa:
    pyautogui.click(x=653, y=294)
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "codigo"])) 
    pyautogui.press("tab")
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = EstoqueDaEmpresa.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(EstoqueDaEmpresa.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
