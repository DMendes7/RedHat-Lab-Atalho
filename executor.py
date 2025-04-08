import pyautogui
import time
import os

# Caminho do comandos.txt
caminho_comandos = os.path.join(os.path.dirname(__file__), 'comandos.txt')

# Função para limpar a linha
def limpar_linha(linha):
    return ''.join(c for c in linha if c.isprintable()).strip()

# Função para detectar e executar comandos especiais
def executar_comando(comando):
    comando = comando.strip()

    # Mapeamento de atalhos especiais
    atalhos = {
        '[i]': lambda: pyautogui.press('i'),
        '[esc]': lambda: pyautogui.press('esc'),
        '[ctrl+z]': lambda: pyautogui.hotkey('ctrl', 'z'),
        '[ctrl+c]': lambda: pyautogui.hotkey('ctrl', 'c'),
        '[ctrl+d]': lambda: pyautogui.hotkey('ctrl', 'd'),
        '[enter]': lambda: pyautogui.press('enter'),
        '[tab]': lambda: pyautogui.press('tab'),
        '[sleep-5]': lambda: time.sleep(5),
        '[sleep-10]': lambda: time.sleep(10),
    }

    if comando.lower() in atalhos:
        print(f"🔧 Executando atalho: {comando}")
        atalhos[comando.lower()]()
    else:
        print(f"⌨️ Enviando comando: {comando}")
        pyautogui.write(comando)
        pyautogui.press('enter')

        # Tratativas específicas para comandos sensíveis
        if comando.startswith("vim "):
            print("📝 Entrando no modo edição do vim, aguardando...")
            time.sleep(2)
        elif "chmod" in comando or "monitor" in comando:
            print("⏳ Aguardando para garantir que a interface do terminal seja limpa...")
            time.sleep(2)

# Lê os comandos do arquivo
with open(caminho_comandos, 'r', encoding='utf-8') as arquivo:
    comandos = [limpar_linha(linha) for linha in arquivo if limpar_linha(linha)]

# Instruções iniciais
print("=" * 50)
print(" Red Hat Lab Executor - Suporte a Comandos Especiais e Tratativas ")
print("=" * 50)
print("Você tem 5 segundos para clicar no terminal web ou bloco de notas...")

# Contagem regressiva
for i in range(5, 0, -1):
    print(f"⏳ Começando em {i} segundos...", end="\r")
    time.sleep(1)
print(" " * 50, end="\r")

# Executa os comandos
for i, comando in enumerate(comandos):
    executar_comando(comando)
    time.sleep(1.5)  # Delay padrão entre comandos
