import sqlite3  # banco de dados
import tkinter as tk  # interface básica
from tkinter import messagebox  # caixas de mensagens
from tkinter import ttk  # interface gráfica

def conectar():
    return sqlite3.connect('teste.db')

# Criar a tabela com o id como AUTOINCREMENT e PRIMARY KEY
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        imc REAL
        )
    ''')
    conn.commit()
    conn.close()

# Resetar o contador do ID para 1
def resetar_contador():
    conn = conectar()
    c = conn.cursor()
    c.execute("DELETE FROM sqlite_sequence WHERE name='usuarios';")  # Reseta o contador de id
    conn.commit()
    conn.close()

# Calcular o IMC e atualizar no banco
def calcular_imc():
    try:
        altura_cm = float(entry_altura.get())
        peso = float(entry_peso.get())
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)

        messagebox.showinfo(f'IMC Calculado', f'O seu IMC é: {round(imc, 2)}')  # Exibe o IMC

        # Exibir a mensagem de classificação
        if imc < 16:
            messagebox.showinfo(f'IMC Muito Baixo', 'Seu IMC está muito baixo! Risco de doença.')
        elif 16 <= imc < 18.5:
            messagebox.showinfo(f'IMC Baixo', 'Seu IMC está baixo. Você está abaixo do peso normal.')
        elif 18.5 <= imc <= 24.9:
            messagebox.showinfo(f'IMC Normal', 'Seu IMC está normal. Parabéns, você tem um peso saudável!')
        elif 25 <= imc <= 29.9:
            messagebox.showinfo(f'IMC Sobrepeso', 'Seu IMC está alto. Você está com sobrepeso.')
        else:
            messagebox.showinfo(f'IMC Obesidade', 'Seu IMC está muito alto. Você está com obesidade.')

        # Pega o nome e email dos campos
        nome = entry_nome.get()
        email = entry_email.get()

        if nome and email:
            conn = conectar()
            c = conn.cursor()

            # Verifica se o usuário já existe com base no nome e email
            c.execute('SELECT id FROM usuarios WHERE nome = ? AND email = ?', (nome, email))
            user = c.fetchone()

            if user:
                # Se já existir, atualiza o IMC
                user_id = user[0]
                c.execute('UPDATE usuarios SET imc = ? WHERE id = ?', (round(imc, 2), user_id))
                conn.commit()
                messagebox.showinfo('Sucesso', f'IMC de {nome} atualizado com sucesso!')
            else:
                # Caso não exista, cria um novo usuário
                c.execute('INSERT INTO usuarios (nome, email, imc) VALUES (?, ?, ?)', (nome, email, round(imc, 2)))
                conn.commit()
                messagebox.showinfo('Sucesso', f'Novo usuário {nome} inserido com IMC calculado!')
            
            conn.close()
            mostrar_usuario()  # Atualiza a tabela

        else:
            messagebox.showerror('Erro', 'Por favor, insira nome e e-mail do usuário.')

    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira valores válidos para altura e peso.')

# Mostrar usuários cadastrados
def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3]))  # ID, nome, email e IMC
    conn.close()

# Deletar usuário
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()
    else:
       messagebox.showerror('', 'OCORREU UM ERRO')

# Atualizar dados do usuário
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ? ',(novo_nome,novo_email,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')

# Configuração da interface gráfica
janela = tk.Tk()
janela.title('CRUD')

# Labels e entradas de texto
label_nome = tk.Label(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail:')
label_email.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text='ALTURA (cm):')
label_altura.grid(row=2, column=0, padx=10, pady=10, sticky='w')
entry_altura = tk.Entry(janela)
entry_altura.grid(row=2, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text='PESO (Kg):')
label_peso.grid(row=3, column=0, padx=10, pady=10, sticky='w')
entry_peso = tk.Entry(janela)
entry_peso.grid(row=3, column=1, padx=10, pady=10)

# Arvore (Tabela)
columns = ('ID', 'NOME', 'EMAIL', 'IMC')

tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

# Botões na coluna 2
btn_deletar = tk.Button(janela, text='DELETAR',command=delete_usuario)
btn_deletar.grid(row=4, column=1, padx=10, pady=10, sticky='w')

btn_atualizar = tk.Button(janela, text='ATUALIZAR',command=editar)
btn_atualizar.grid(row=5, column=1, padx=10, pady=10, sticky='w')

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=6, column=1, padx=10, pady=10, sticky='w')

criar_tabela()
resetar_contador()  # Resetar o contador do ID
mostrar_usuario()

janela.mainloop()
