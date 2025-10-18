from tkinter import *
import random
import time

root = Tk()
root.geometry("1000x600")
root.title("Hotel Net-Tech")

order_number = StringVar()
cost_var = StringVar()
service_charge_var = StringVar()
tax_var = StringVar()
subtotal_var = StringVar()
total_var = StringVar()

items = ["drink", "burger", "cherry", "fries", "pizza", "biscuit", "roll", "tea"]
prices = {
    "drink": 20,
    "burger": 50,
    "cherry": 30,
    "fries": 25,
    "pizza": 80,
    "biscuit": 15,
    "roll": 40,
    "tea": 10
}
entries = {}

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_display.config(text=current_time)
    time_display.after(1000, update_time)

def calculate_total():
    order_number.set(str(random.randint(1000, 9999)))
    total_cost = 0
    for item in items:
        qty = int(entries[item].get() or 0)
        total_cost += prices[item] * qty

    service = round(total_cost * 0.05, 2)
    tax = round(total_cost * 0.10, 2)
    total = total_cost + service + tax

    cost_var.set(f"{total_cost}")
    service_charge_var.set(f"{service}")
    tax_var.set(f"{tax}")
    subtotal_var.set(f"{total_cost}")
    total_var.set(f"{total}")

def reset_all():
    for entry in entries.values():
        entry.delete(0, END)
    order_number.set("")
    cost_var.set("")
    service_charge_var.set("")
    tax_var.set("")
    subtotal_var.set("")
    total_var.set("")
    calculator_display.delete(0, END)


def exit_app():
    root.destroy()

menu_frame = Frame(root, bd=10, relief=RIDGE, bg='skyblue')
menu_frame.pack(side=LEFT)

bill_frame = Frame(root, bd=10, relief=RIDGE, bg='magenta')
bill_frame.pack(side=LEFT)

calc_frame = Frame(root, bd=10, relief=RIDGE, bg='white')
calc_frame.pack(side=RIGHT)

Label(menu_frame, text="Drink").grid(row=0, column=0)
entries["drink"] = Entry(menu_frame)
entries["drink"].grid(row=0, column=1)

Label(menu_frame, text="Burger King").grid(row=1, column=0)
entries["burger"] = Entry(menu_frame)
entries["burger"].grid(row=1, column=1)

Label(menu_frame, text="Cherry").grid(row=2, column=0)
entries["cherry"] = Entry(menu_frame)
entries["cherry"].grid(row=2, column=1)

Label(menu_frame, text="Nacho Fries").grid(row=3, column=0)
entries["fries"] = Entry(menu_frame)
entries["fries"].grid(row=3, column=1)

Label(menu_frame, text="Pizza").grid(row=4, column=0)
entries["pizza"] = Entry(menu_frame)
entries["pizza"].grid(row=4, column=1)

Label(menu_frame, text="Biscuits").grid(row=5, column=0)
entries["biscuit"] = Entry(menu_frame)
entries["biscuit"].grid(row=5, column=1)

Label(menu_frame, text="Roll").grid(row=6, column=0)
entries["roll"] = Entry(menu_frame)
entries["roll"].grid(row=6, column=1)

Label(menu_frame, text="Tea").grid(row=7, column=0)
entries["tea"] = Entry(menu_frame)
entries["tea"].grid(row=7, column=1)

Label(bill_frame, text="Order Number:").grid(row=0, column=0)
Label(bill_frame, textvariable=order_number).grid(row=0, column=1)

Label(bill_frame, text="Cost:").grid(row=1, column=0)
Label(bill_frame, textvariable=cost_var).grid(row=1, column=1)

Label(bill_frame, text="Service Cost:").grid(row=2, column=0)
Label(bill_frame, textvariable=service_charge_var).grid(row=2, column=1)

Label(bill_frame, text="Tax:").grid(row=3, column=0)
Label(bill_frame, textvariable=tax_var).grid(row=3, column=1)

Label(bill_frame, text="Sub Total:").grid(row=4, column=0)
Label(bill_frame, textvariable=subtotal_var).grid(row=4, column=1)

Label(bill_frame, text="Total:").grid(row=5, column=0)
Label(bill_frame, textvariable=total_var).grid(row=5, column=1)

time_display = Label(calc_frame, font=('Arial', 16), fg='red', bg='black')
time_display.grid(row=0, columnspan=4)
update_time()

calculator_display = Entry(calc_frame, font=('Arial', 16), bd=5, justify='right')
calculator_display.grid(row=1, column=0, columnspan=4)

def calculator_click(char):
    if char == '=':
        try:
            result = eval(calculator_display.get())
            calculator_display.delete(0, END)
            calculator_display.insert(END, str(result))
        except:
            calculator_display.delete(0, END)
            calculator_display.insert(END, "Error")
    elif char == 'C':
        calculator_display.delete(0, END)
    else:
        calculator_display.insert(END, char)

buttons = [
    ['1','2','3','+'],
    ['4','5','6','-'],
    ['7','8','9','*'],
    ['C','0','=','/']
]

for r, row in enumerate(buttons, start=2):
    for c, char in enumerate(row):
        Button(calc_frame, text=char, width=5, height=2, command=lambda ch=char: calculator_click(ch)).grid(row=r, column=c)

Button(menu_frame, text="Total", command=calculate_total, bg='red', fg='white', width=10).grid(row=8, column=0)
Button(menu_frame, text="Reset", command=reset_all, bg='red', fg='white', width=10).grid(row=8, column=1)
Button(menu_frame, text="Quit", command=exit_app, bg='red', fg='white', width=10).grid(row=9, columnspan=2)

root.mainloop()