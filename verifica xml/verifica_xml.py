import os
import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET

def verificar_faltando_pasta(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.xml')]
    
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
        if nome_arquivo.endswith('.xml'):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            try:
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()
                conteudo = ET.tostring(root, encoding='unicode')
                
                if palavra_chave not in conteudo:
                    num_nota = nome_arquivo.split('.')[0]
                    não_autorizados.append(f"Nota {num_nota}: {palavra_chave} não encontrada")
            except ET.ParseError as e:
                arquivos_problematicos.append(f"Erro ao abrir {nome_arquivo}: {str(e)}")
            except Exception as e:
                arquivos_problematicos.append(f"Erro ao processar {nome_arquivo}: {str(e)}")

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
            messagebox.showwarning("Problemas Encontrados", "\n".join(arquivos_problematicos))
    else:
        messagebox.showerror("Erro", "O caminho especificado não existe.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Verificar Numerações e Autorização em XML")
janela.geometry("350x200")

# Botão para selecionar a pasta
botao_selecionar = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=20)

# Executa a interface gráfica
janela.mainloop()
