import pyautogui
import time
import os
import sys

# Caminho do comandos.txt
caminho_comandos = os.path.join(os.path.dirname(__file__), 'comandos.txt')

# Lê os comandos ignorando linhas vazias
with open(caminho_comandos, 'r', encoding='utf-8') as arquivo:
    comandos = [linha.strip() for linha in arquivo if linha.strip()]

print("=" * 50)
print(" Red Hat Lab Executor - Automático com Delay ")
print("=" * 50)
print("Você tem 5 segundos para clicar no terminal web ou bloco de notas...")

# Contagem regressiva bonita
for i in range(5, 0, -1):
    print(f"⏳ Começando em {i} segundos...", end="\r")
    time.sleep(1)
print(" " * 50, end="\r")  # Limpa a linha final depois da contagem

# Enviando os comandos
for i, comando in enumerate(comandos):
    print(f"Enviando comando {i+1}/{len(comandos)}: {comando}")
    pyautogui.write(comando)
    pyautogui.press("enter")
    time.sleep(3)  # Tempo entre comandos (ajustável)
