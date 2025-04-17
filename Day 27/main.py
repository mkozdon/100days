import tkinter as tk

window = tk.Tk()
window.title("Miles Converter")
window.minsize(250, 150)
window.config(padx=20, pady=20)


def convert():
    output_label["text"] = round(float(miles_input.get()) * 1.60934, 2)


miles_label = tk.Label(text="Miles")
km_label = tk.Label(text="Km")
equal_label = tk.Label(text="is equal to")
output_label = tk.Label(text="0")
calculate = tk.Button(text="Calculate", command=convert)
miles_input = tk.Entry(width=10)

miles_input.grid(column=1, row=0)
output_label.grid(column=1, row=1)
calculate.grid(column=1, row=2)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equal_label.grid(column=0, row=1)


window.mainloop()
