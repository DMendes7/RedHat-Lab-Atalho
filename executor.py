import pyautogui
import time
import os

# Caminho do comandos.txt
caminho_comandos = os.path.join(os.path.dirname(__file__), 'comandos.txt')

# Limpa linhas do txt
def limpar_comando(texto):
    return ''.join(c for c in texto if c.isprintable()).strip()

# Lê os comandos
with open(caminho_comandos, 'r', encoding='utf-8') as arquivo:
    comandos = [limpar_comando(linha) for linha in arquivo if limpar_comando(linha)]

# Digita caractere por caractere de forma confiável
def digitar_comando(comando):
    for char in comando:
        if char == '/':
            pyautogui.write('/', interval=0.01)  # ✅ Aqui funciona pra ABNT
        elif char == '-':
            pyautogui.write('-', interval=0.01)
        elif char == '_':
            pyautogui.write('_', interval=0.01)
        elif char == ' ':
            pyautogui.press('space')
        else:
            pyautogui.write(char, interval=0.01)
    pyautogui.press("enter")

# Instruções
print("=" * 50)
print(" Red Hat Lab Executor - 100% Compatível com Teclado ABNT ")
print("=" * 50)
for i in range(5, 0, -1):
    print(f"⏳ Começando em {i} segundos...", end="\r")
    time.sleep(1)
time.sleep(5)

# Executa
for i, comando in enumerate(comandos):
    print(f"⌨️ Enviando comando {i+1}/{len(comandos)}: {comando}")
    digitar_comando(comando)
    time.sleep(3)
