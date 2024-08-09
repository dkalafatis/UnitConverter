import tkinter as tk
from tkinter import ttk


# Conversion Functions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value + 459.67) * 5 / 9
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value * 9 / 5) - 459.67


def convert_volume(value, from_unit, to_unit):
    liters_to_gallons = 0.264172
    liters_to_cups = 4.22675
    if from_unit == to_unit:
        return value
    elif from_unit == "Liters":
        if to_unit == "Gallons":
            return value * liters_to_gallons
        elif to_unit == "Cups":
            return value * liters_to_cups
    elif from_unit == "Gallons":
        if to_unit == "Liters":
            return value / liters_to_gallons
        elif to_unit == "Cups":
            return value * (liters_to_cups / liters_to_gallons)
    elif from_unit == "Cups":
        if to_unit == "Liters":
            return value / liters_to_cups
        elif to_unit == "Gallons":
            return value / (liters_to_cups / liters_to_gallons)


def convert_mass(value, from_unit, to_unit):
    kilograms_to_pounds = 2.20462
    kilograms_to_ounces = 35.274
    if from_unit == to_unit:
        return value
    elif from_unit == "Kilograms":
        if to_unit == "Pounds":
            return value * kilograms_to_pounds
        elif to_unit == "Ounces":
            return value * kilograms_to_ounces
    elif from_unit == "Pounds":
        if to_unit == "Kilograms":
            return value / kilograms_to_pounds
        elif to_unit == "Ounces":
            return value * 16
    elif from_unit == "Ounces":
        if to_unit == "Kilograms":
            return value / kilograms_to_ounces
        elif to_unit == "Pounds":
            return value / 16


# GUI
class UnitConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        # Unit Category
        self.category_var = tk.StringVar()
        self.category_options = ["Temperature", "Volume", "Mass"]
        self.category_var.set(self.category_options[0])
        tk.Label(root, text="Select Category:").grid(row=0, column=0)
        self.category_menu = tk.OptionMenu(root, self.category_var, *self.category_options, command=self.update_units)
        self.category_menu.grid(row=0, column=1)

        # From Unit
        self.from_unit_var = tk.StringVar()
        self.from_unit_menu = tk.OptionMenu(root, self.from_unit_var, "")
        self.from_unit_menu.grid(row=1, column=0)

        # To Unit
        self.to_unit_var = tk.StringVar()
        self.to_unit_menu = tk.OptionMenu(root, self.to_unit_var, "")
        self.to_unit_menu.grid(row=1, column=2)

        # Value Entry
        tk.Label(root, text="Value:").grid(row=2, column=0)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=2, column=1)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=1)

        # Result Label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=4, column=1)

        self.update_units("Temperature")

    def update_units(self, category):
        units = {
            "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "Volume": ["Liters", "Gallons", "Cups"],
            "Mass": ["Kilograms", "Pounds", "Ounces"]
        }

        self.from_unit_menu["menu"].delete(0, "end")
        self.to_unit_menu["menu"].delete(0, "end")

        for unit in units[category]:
            self.from_unit_menu["menu"].add_command(label=unit, command=tk._setit(self.from_unit_var, unit))
            self.to_unit_menu["menu"].add_command(label=unit, command=tk._setit(self.to_unit_var, unit))

        self.from_unit_var.set(units[category][0])
        self.to_unit_var.set(units[category][0])

    def convert(self):
        value = float(self.value_entry.get())
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        category = self.category_var.get()

        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        else:  # Mass
            result = convert_mass(value, from_unit, to_unit)

        self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()
