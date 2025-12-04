import tkinter as tk
from tkinter import messagebox

def counter(a, b): # кол-во целых чисел в промежутке от a до b
    summ = 0
    for i in range(a, b, 1) if a < b else range(b, a, 1):
        summ += 1
    return summ

def calculate():
    try:
        a_val = int(entry_a.get())
        b_val = int(entry_b.get())
        result = counter(a_val, b_val)
        messagebox.showinfo("Результат", f"Количество целых чисел: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные целые числа!")

window = tk.Tk()
window.title("Счётчик чисел")

tk.Label(window, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

tk.Label(window, text="b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

btn = tk.Button(window, text="Посчитать", command=calculate)
btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
