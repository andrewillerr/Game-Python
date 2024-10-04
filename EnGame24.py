import tkinter as tk
from tkinter import messagebox
import itertools

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return None

def find_24(numbers):
    operators = ['+', '-', '*', '/']
    results = []
    for num_perm in itertools.permutations(numbers):
        for ops in itertools.product(operators, repeat=3):
            # การจัดกลุ่มตัวเลขแบบต่างๆ
            expressions = [
                f"(({num_perm[0]} {ops[0]} {num_perm[1]}) {ops[1]} {num_perm[2]}) {ops[2]} {num_perm[3]}",
                f"({num_perm[0]} {ops[0]} ({num_perm[1]} {ops[1]} {num_perm[2]})) {ops[2]} {num_perm[3]}",
                f"({num_perm[0]} {ops[0]} {num_perm[1]}) {ops[1]} ({num_perm[2]} {ops[2]} {num_perm[3]})",
                f"{num_perm[0]} {ops[0]} (({num_perm[1]} {ops[1]} {num_perm[2]}) {ops[2]} {num_perm[3]})",
                f"{num_perm[0]} {ops[0]} ({num_perm[1]} {ops[1]} ({num_perm[2]} {ops[2]} {num_perm[3]}))"
            ]
            for expr in expressions:
                try:
                    if abs(eval(expr) - 24) < 1e-6:  # ตรวจสอบให้แน่ใจว่าใกล้เคียงกับ 24
                        results.append(expr)
                except ZeroDivisionError:
                    continue
    return results

def on_submit():
    try:
        numbers = list(map(int, entry.get().split()))
        if len(numbers) != 4:
            messagebox.showerror("Error", "กรุณาใส่ตัวเลข 4 ตัวเท่านั้น")
            return
        
        results = find_24(numbers)
        if results:
            messagebox.showinfo("ผลลัพธ์", "\n".join(results))
        else:
            messagebox.showinfo("ผลลัพธ์", "ไม่พบวิธีการที่ได้ 24")
    except ValueError:
        messagebox.showerror("Error", "กรุณาใส่ตัวเลขที่ถูกต้อง")

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Game 24")

label = tk.Label(root, text="กรุณาใส่ตัวเลข 4 ตัว (คั่นด้วยเว้นวรรค):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

submit_button = tk.Button(root, text="ยืนยัน", command=on_submit)
submit_button.pack(pady=20)

root.mainloop()
