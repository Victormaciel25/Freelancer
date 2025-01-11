from tkinter import Tk, Label, Entry, Button, Text, END
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

def buscar_precos():
    produto = entry_produto.get()  # Obtém o nome do produto da interface
    if not produto:
        exibir_resultados("Por favor, insira um produto.")
        return

    # Configuração do WebDriver
    driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado
    driver.get("https://www.mercadolivre.com.br")  # Substitua pelo site desejado
    
    try:
        # Localizar o campo de busca e pesquisar o produto
        search_box = driver.find_element(By.NAME, "as_word")
        search_box.send_keys(produto)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Espera carregar a página
        driver.maximize_window()  # Maximiza a janela do navegador
        time.sleep(2)
        # Coletar os preços dos produtos
        precos = []
        cont = 1
        elementos_precos = driver.find_elements(By.XPATH, f"//*[@id='root-app']/div/div[3]/section/ol/li[{cont}]/div/div/div[2]/div[2]/div[1]/div[1]/div/span[1]/span[2]/text()")
        time.sleep(1)
        for elemento in elementos_precos:
            # texto_preco = elemento.text
            # Remover caracteres não numéricos e converter para float
            # preco = float(re.sub(r"[^\d]", "", texto_preco))
            preco = float(elemento)
            cont += 1
            precos.append(preco)

        driver.quit()

        if not precos:
            exibir_resultados("Nenhum preço encontrado para o produto informado.")
            return

        # Processar os preços
        maior_preco = max(precos)
        menor_preco = min(precos)
        media_precos = sum(precos) / len(precos)

        # Exibir os resultados na interface
        resultado = (
            f"Produto: {produto}\n"
            f"Maior preço: R$ {maior_preco:.2f}\n"
            f"Menor preço: R$ {menor_preco:.2f}\n"
            f"Média de preços: R$ {media_precos:.2f}\n"
        )
        exibir_resultados(resultado)

    except Exception as e:
        exibir_resultados(f"Erro durante a execução: {e}")
        driver.quit()

def exibir_resultados(mensagem):
    """Exibe a mensagem na área de texto."""
    text_resultados.delete(1.0, END)
    text_resultados.insert(END, mensagem)

# Criação da interface gráfica
root = Tk()
root.title("Buscador de Preços")

# Rótulos e campo de entrada
Label(root, text="Produto:").grid(row=0, column=0, padx=10, pady=10)
entry_produto = Entry(root, width=40)
entry_produto.grid(row=0, column=1, padx=10, pady=10)

# Botão para buscar preços
botao_buscar = Button(root, text="Buscar Preços", command=buscar_precos)
botao_buscar.grid(row=1, column=0, columnspan=2, pady=10)

# Área de texto para exibir os resultados
text_resultados = Text(root, width=60, height=15)
text_resultados.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Inicia a interface
root.mainloop()
