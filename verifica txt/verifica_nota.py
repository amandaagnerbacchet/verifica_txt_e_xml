"""import os
import tkinter as tk
from tkinter import filedialog, messagebox

def verificar_faltando_pasta(pasta):
    arquivos = os.listdir(pasta)
    
    numerações = [int(nome.split('.')[0]) for nome in arquivos if nome.split('.')[0].isdigit()]
    
    if not numerações:
        return []

    numerações.sort()
    
    menor_numeração = numerações[0]
    maior_numeração = numerações[-1]
    
    numerações_esperadas = set(range(menor_numeração, maior_numeração + 1))
    
    faltando = sorted(numerações_esperadas - set(numerações))
    
    return faltando

def verificar_autorizacao_em_arquivos(pasta):
    palavra_chave = "Autorizado"
    não_autorizados = []

    for nome_arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_arquivo) and nome_arquivo.split('.')[0].isdigit():
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if palavra_chave not in conteudo:
                    num_nota = nome_arquivo.split('.')[0]
                    não_autorizados.append(f"Nota {num_nota}: {palavra_chave} não encontrada")
    
    return não_autorizados

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    
    if not pasta:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada.")
        return

    if os.path.exists(pasta):
        faltando = verificar_faltando_pasta(pasta)
        if faltando:
            messagebox.showinfo("Numerações Faltando", f"Numerações faltando: {faltando}")
        else:
            messagebox.showinfo("Numerações Faltando", "Nenhuma numeração faltando.")
        
        não_autorizados = verificar_autorizacao_em_arquivos(pasta)
        if não_autorizados:
            messagebox.showinfo("Resultados da Verificação", "\n".join(não_autorizados))
        else:
            messagebox.showinfo("Resultados da Verificação", "Todos os arquivos estão autorizados.")
    else:
        messagebox.showerror("Erro", "O caminho especificado não existe.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Verificar Numerações e Autorização")
janela.geometry("300x150")

# Botão para selecionar a pasta
botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=20)

# Executa a interface gráfica
janela.mainloop()
""" 

import os
import tkinter as tk
from tkinter import filedialog, messagebox

def verificar_faltando_pasta(pasta):
    arquivos = os.listdir(pasta)
    
    numerações = [int(nome.split('.')[0]) for nome in arquivos if nome.split('.')[0].isdigit()]
    
    if not numerações:
        return []

    numerações.sort()
    
    menor_numeração = numerações[0]
    maior_numeração = numerações[-1]
    
    numerações_esperadas = set(range(menor_numeração, maior_numeração + 1))
    
    faltando = sorted(numerações_esperadas - set(numerações))
    
    return faltando

def verificar_autorizacao_em_arquivos(pasta):
    palavra_chave = "Autorizado"
    não_autorizados = []
    arquivos_problematicos = []

    for nome_arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_arquivo) and nome_arquivo.split('.')[0].isdigit():
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
            except UnicodeDecodeError:
                # Tenta com outra codificação caso ocorra erro
                try:
                    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
                        conteudo = arquivo.read()
                except Exception as e:
                    arquivos_problematicos.append(f"Erro ao abrir {nome_arquivo}: {str(e)}")
                    continue

            if palavra_chave not in conteudo:
                num_nota = nome_arquivo.split('.')[0]
                não_autorizados.append(f"Nota {num_nota}: {palavra_chave} não encontrada")

    return não_autorizados, arquivos_problematicos

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    
    if not pasta:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada.")
        return

    if os.path.exists(pasta):
        faltando = verificar_faltando_pasta(pasta)
        if faltando:
            messagebox.showinfo("Numerações Faltando", f"Numerações faltando: {faltando}")
        else:
            messagebox.showinfo("Numerações Faltando", "Nenhuma numeração faltando.")
        
        não_autorizados, arquivos_problematicos = verificar_autorizacao_em_arquivos(pasta)
        if não_autorizados:
            messagebox.showinfo("Resultados da Verificação", "\n".join(não_autorizados))
        else:
            messagebox.showinfo("Resultados da Verificação", "Todos os arquivos estão autorizados.")
        
        if arquivos_problematicos:
            messagebox.showwarning("Problemas de Decodificação", "\n".join(arquivos_problematicos))
    else:
        messagebox.showerror("Erro", "O caminho especificado não existe.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Verificar Numerações e Autorização")
janela.geometry("300x150")

# Botão para selecionar a pasta
botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=20)

# Executa a interface gráfica
janela.mainloop()

