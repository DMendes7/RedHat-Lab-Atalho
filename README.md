# 🚀 RedHat Lab Executor

Automatize a digitação dos comandos nos laboratórios da Red Hat com estilo, praticidade e zero sofrimento mental.  
Este script foi criado para **universitários que não aguentam mais digitar `ssh student@servera` pela milésima vez**. 🙃

---

## ✨ O que é isso?

Um script Python que simula seu teclado e **digita automaticamente os comandos do laboratório** por você.  
Funciona em terminais via navegador, como as VMs utilizadas nos labs da **Red Hat Academy**, **Cisco Netacad**, etc.

> Ele usa a biblioteca `pyautogui` para simular as teclas. Você só precisa preparar o terreno, clicar no terminal e deixar o script fazer o resto. 😉

---

## 📁 Estrutura do Projeto

```
RedHat-Lab-Atalho/
├── comandos.txt       # Lista dos comandos a serem executados
└── executor.py        # Script Python que envia os comandos simulando teclado
```

---

## 🛠️ Como usar

### 1. ✅ Instale as dependências
```bash
pip install pyautogui
```

### 2. ✍️ Edite o `comandos.txt`

Antes de iniciar **qualquer laboratório**, **copie e cole os comandos EXATOS** (e na ordem correta!) que você terá que digitar durante o lab.

Exemplo:
```
lab start users-user
ssh student@servera
sudo -i
student
```

> ⚠️ **A ordem importa!** Se os comandos estiverem fora de sequência, o lab pode não funcionar corretamente. Você foi avisado. 😅

---

### 3. ▶️ Execute o script

No terminal local (VS Code, PowerShell, cmd, etc), digite:

```bash
python executor.py
```

Ele vai mostrar algo assim:

```
==================================================
 Red Hat Lab Executor - Automático com Delay 
==================================================
Você tem 5 segundos para clicar no terminal web ou bloco de notas...
```

---

### 4. 🖱️ Clique no terminal web!

Enquanto o script faz a contagem regressiva (5 segundos), **clique dentro do terminal do navegador** onde você executa os comandos do laboratório.

> Após isso, o script vai digitar automaticamente cada comando com uma pausa de 3 segundos entre eles.

---

### 📽️ Demonstração

![Demo GIF](img/exemplo.gif)

---

## 📌 Dicas úteis

- Quer testar antes de usar no lab?  
  Use um site tipo [aNotepad](https://pt.anotepad.com/) pra simular um terminal.

- O tempo entre os comandos é de **3 segundos**, mas pode ser ajustado no `executor.py`:
  ```python
  time.sleep(3)
  ```

---

## 🧠 Por que isso existe?

Porque digitar os mesmos comandos 30 vezes por semana é um teste de paciência.  
Feito por e para universitários que só querem **sobreviver aos labs** com o mínimo de sofrimento. 🧃

---

## 👾 Requisitos

- Python 3.8+
- `pyautogui`
- Um pouco de juízo (ou pelo menos copiar os comandos direito 😅)

---

## 🙋‍♂️ Feito com raiva de digitar por:  
**Davi Mendes**  
💻 Engenharia de Software - PUC Minas

---
