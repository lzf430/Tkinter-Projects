import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def calculate():
    calculation = float(miles_entry.get())
    km = round(calculation * 1.609, 2)
    km_result.config(text=f"{km}")


# Create Entry
miles_entry = tkinter.Entry(width=7)
miles_entry.grid(column=1, row=0)

# Create Multiple Labels
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="KM")
km_label.grid(column=2, row=1)

km_result = tkinter.Label(text="0")
km_result.grid(column=1, row=1)

# Create Button
calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
































window.mainloop()