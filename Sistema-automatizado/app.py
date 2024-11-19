import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(957,539, duration=0.5)
pyautogui.write('jhulya')
# 2 - Clicar e digitar minha senha
pyautogui.click(953,566, duration=0.5)
pyautogui.write('123')
# 3 - Clicar em "Entrar"
pyautogui.click(869,595, duration=0.5)
# 4 - Extrair cada produtovictor123456
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1 - Clicar e digitar produto
        pyautogui.click(673,527, duration=0.5)
        pyautogui.write(produto)
        # 2 - Clicar e digitar quantidade
        pyautogui.click(672,554, duration=0.5)
        pyautogui.write(quantidade)
        # 3 - Clicar e digitar preço
        pyautogui.click(670,581, duration=0.5)
        pyautogui.write(preco)
        # 4 - Clicar em registrar
        pyautogui.click(590,738, duration=0.5)
        sleep(1)