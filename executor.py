import pyautogui
import time
import os

# Caminho do comandos.txt
caminho_comandos = os.path.join(os.path.dirname(__file__), 'comandos.txt')

# Função para limpar a linha
def limpar_linha(linha):
    return ''.join(c for c in linha if c.isprintable()).strip()

# Função para pausar para mensagens humanas
def instrucoes_usuario(mensagem):
    print(f"\n🔔 INSTRUÇÃO PARA VOCÊ: {mensagem}")
    input("👉 Pressione Enter quando tiver concluído...")
    print("⏳ Retomando em 5 segundos...")
    for i in range(5, 0, -1):
        print(f"⏳ {i}...", end="\r")
        time.sleep(1)
    print(" " * 30, end="\r")

# Função para comandos especiais
def executar_comando(comando):
    comando = comando.strip()

    # Instruções personalizadas (ex: <digite Yes>)
    if comando.startswith('<') and comando.endswith('>'):
        mensagem = comando[1:-1].strip()
        instrucoes_usuario(mensagem)
        return

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
        '[aguarde-interacao]': aguardar_interacao
    }

    if comando.lower() in atalhos:
        print(f"🔧 Executando atalho: {comando}")
        atalhos[comando.lower()]()
    else:
        print(f"⌨️ Enviando comando: {comando}")
        pyautogui.write(comando)
        pyautogui.press('enter')

        if comando.startswith("vim "):
            print("📝 Entrando no modo edição do vim, aguardando...")
            time.sleep(2)
        elif "chmod" in comando or "monitor" in comando:
            print("⏳ Garantindo tempo de resposta para terminal...")
            time.sleep(2)

# Aguarda confirmação manual
def aguardar_interacao():
    print("🛑 Ação manual necessária: digite senha, aceite 'yes', etc.")
    input("👉 Pressione Enter quando concluir a ação...")
    print("⏳ Aguardando mais 5 segundos...")
    time.sleep(5)

# Lê comandos
with open(caminho_comandos, 'r', encoding='utf-8') as arquivo:
    comandos = [limpar_linha(linha) for linha in arquivo if limpar_linha(linha)]

# Mensagem inicial
print("=" * 50)
print(" Red Hat Lab Executor - Suporte a Atalhos e Instruções Manuais ")
print("=" * 50)
print("Você tem 5 segundos para focar no terminal alvo...")

for i in range(5, 0, -1):
    print(f"⏳ Começando em {i} segundos...", end="\r")
    time.sleep(1)
print(" " * 50, end="\r")

# Execução dos comandos
for i, comando in enumerate(comandos):
    executar_comando(comando)
    time.sleep(1.5)
