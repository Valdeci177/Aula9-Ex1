import tkinter as tk

def converter():
    try:
        centimetros = float(entrada_cm.get())
        metros = centimetros / 100
        label_resultado.config(text=f"{centimetros} cm = {metros} m")
    except ValueError:
        label_resultado.config(text="Digite um número válido")

# Criar a janela
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

# Criar os widgets
label_cm = tk.Label(janela, text="Centímetros:")
label_cm.grid(row=0, column=0, padx=5, pady=5)

entrada_cm = tk.Entry(janela)
entrada_cm.grid(row=0, column=1, padx=5, pady=5)

botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.grid(row=1, columnspan=2, padx=5, pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=2, columnspan=2, padx=5, pady=5)

# Executar a janela
janela.mainloop()