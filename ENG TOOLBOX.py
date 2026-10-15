import math
import tkinter as tk

window = tk.Tk()
window.title("Engineering Toolbox")
window.geometry("500x450")
window.configure(bg="#A3A7F2")

title = tk.Label(
    window,
    text="Engineering Toolbox",
    font=("Arial", 22, "bold"),
    bg="#A3A7F2",
    fg="#030A15"
)
title.pack(pady=30)

subtitle = tk.Label(
    window,
    text="Useful calculators for engineering students",
    font=("Arial", 10),
    bg="#A3A7F2",
    fg="#030A15"
)
subtitle.pack(pady=5)

button_frame = tk.Frame(window, bg="#7D67D0")
button_frame.pack(pady=20)




def open_length_converter():
    converter = tk.Toplevel(window)
    converter.title("Length Converter")
    converter.geometry("350x300")
    converter.configure(bg="#F1F5F9")

    tk.Label(converter, text="Enter length:",bg="#F1F5F9",
        fg="#14243A",font=("Arial", 10)).pack(pady=5)

    length_entry = tk.Entry(converter , font=("Arial", 11),bg="white", fg="#14243A" , width=20 , bd=1,
relief="solid")
    length_entry.pack(pady=5)

    units = ["mm", "cm", "m", "km"]

    from_unit = tk.StringVar(value="cm")
    to_unit = tk.StringVar(value="m")

    tk.Label(converter, text="Convert from:",bg="#F1F5F9",
            fg="#14243A",font=("Arial", 10)).pack()
    from_menu = tk.OptionMenu(converter, from_unit, *units)
    from_menu.config(
    bg="#1769AA",
    fg="white",
    font=("Arial", 10)
    )
    from_menu.pack(pady=5)

    tk.Label(converter, text="Convert to:",bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack()
    to_menu = tk.OptionMenu(converter , to_unit , *units)
    to_menu.config(
    bg="#1769AA",
    fg="white",
    font=("Arial", 10)
    )
    to_menu.pack(pady=5)


    result_label = tk.Label(converter, text="Result will appear here", bg="#F1F5F9",
                            fg="#14243A",font=("Arial", 10))
    result_label.pack(pady=10)
    
    def convert_length():
        try:
            length = float(length_entry.get())
        except ValueError:
            result_label.config(text="Please enter a valid number!")
            return

        if length <= 0:
            result_label.config(text="Enter a positive length!")
            return

        measurements = {
            "mm": 0.001,
            "cm": 0.01,
            "m": 1,
            "km": 1000
        }

        unit_from = from_unit.get()
        unit_to = to_unit.get()

        length_in_meters = length * measurements[unit_from]
        converted_length = length_in_meters / measurements[unit_to]

        result_label.config(
            text=f"Result: {converted_length:g} {unit_to}"
        )

    tk.Button(
        converter,
        text="Convert",
        command=convert_length,
        bg="#1769AA",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).pack(pady=5)

def open_rectangle_calculator():
    converter = tk.Toplevel(window)
    converter.title("Rectangle Calculater")
    converter.geometry("350x300")
    converter.configure(bg="#F1F5F9")

    tk.Label(converter, text="Enter length:",bg="#F1F5F9",
                    fg="#14243A",font=("Arial", 10)).pack(pady=5)
    length_entry = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    length_entry.pack(pady=5)

    tk.Label(converter, text="Enter width:",bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    width_entry = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    width_entry.pack(pady=5)

    
    result_label_Area = tk.Label(converter, text="Area will appear here",bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    result_label_Area.pack(pady=10)

    result_label_Perimeter = tk.Label(converter, text="Perimeter will appear here",bg="#F1F5F9",
                    fg="#14243A",font=("Arial", 10))
    result_label_Perimeter.pack(pady=10)

    def calculate_rectangle():
        try:
            lenghth = float(length_entry.get())
            width = float(width_entry.get())
        except ValueError :
            result_label_Area.config(text="Invalid input. Please enter numbers")
            result_label_Perimeter.config(text="")
            return
        if lenghth <= 0 or width <= 0:
            result_label_Area.config(text="Please enter a positive number for lenghth and width")
            result_label_Perimeter.config(text="")
            return
        area = lenghth * width
        perimeter = 2 * (lenghth + width)
        result_label_Area.config(text=f"Area {area:.2f} ")
        result_label_Perimeter.config(text=f"Perimeter {perimeter:.2f}")
        
        
    tk.Button(
        converter,
        text="Calculate",
        command=calculate_rectangle,
        bg="#1769AA",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).pack(pady=5)

def open_triangle_calculator():
    converter = tk.Toplevel(window)
    converter.title("Triangle Calculator")
    converter.geometry("500x500")
    converter.configure(bg="#F1F5F9")

    tk.Label(converter, text="Enter height:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    height_entry = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    height_entry.pack(pady=5)

    tk.Label(converter, text="Enter base:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    base_entry = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    base_entry.pack(pady=5)

    tk.Label(converter, text="Enter length of the first side:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    length_entry_0 = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    length_entry_0.pack(pady=5)

    tk.Label(converter, text="Enter length of the second side:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    length_entry_1 = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    length_entry_1.pack(pady=5)

    tk.Label(converter, text="Enter length of the third side:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    length_entry_2 = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    length_entry_2.pack(pady=5)

    result_label_Area = tk.Label(converter, text="Area will appear here", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    result_label_Area.pack(pady=10)

    result_label_Perimeter = tk.Label(converter, text="perimeter will appear here", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    result_label_Perimeter.pack(pady=10)

    def calculate_triangle() :

        try:
            hight = float(height_entry.get())
            base = float(base_entry.get())
        except ValueError :
            result_label_Area.config(text="Invalid input. Please enter numbers")
            return
        if hight <= 0 or base <= 0:
            result_label_Area.config(text="Please enter a positive number for lenghth and width")
            return
        area = 1/2 * hight * base
        total = 0 
        lengths = [length_entry_0 , length_entry_1 , length_entry_2]
        side_lengths = []
        for item in lengths:
            try:
                length = float(item.get())
            except ValueError :
                result_label_Area.config(text="Invalid input. Please enter numbers")
                return
            if length <= 0:
                result_label_Area.config(text="Enter a positive number for the lenght")
                return
            side_lengths.append(length)
            total += length
        if (side_lengths[0] + side_lengths[1] <= side_lengths[2]
            or side_lengths[1] + side_lengths[2] <= side_lengths[0]
            or side_lengths[0] + side_lengths[2] <= side_lengths[1]):

            result_label_Area.config(text="These lengths cannot form a triangle.")
            return
            
            



        perimeter = total
        result_label_Perimeter.config(text=f"Perimeter: {perimeter:.2f}")
        result_label_Area.config(text=f"Area: {area:.2f}")
                
    tk.Button(
        converter,
        text="Calculate",
        command=calculate_triangle,
        bg="#1769AA",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).pack(pady=5)

def open_circle_calculator():
    converter = tk.Toplevel(window)
    converter.title("Circle Calculater")
    converter.geometry("350x350")
    converter.configure(bg="#F1F5F9")

    tk.Label(converter, text="Enter radius:", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10)).pack(pady=5)
    radius_entry = tk.Entry(converter , bd=1,relief="solid" , bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    radius_entry.pack(pady=5)

    result_label_Area = tk.Label(converter, text="Area will appear here",bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    result_label_Area.pack(pady=10)

    result_label_circumference = tk.Label(converter, text="circumference will appear here", bg="#F1F5F9",
                fg="#14243A",font=("Arial", 10))
    result_label_circumference.pack(pady=10)

    def calculate_circle():
        try:
            r = float(radius_entry.get())
        except ValueError :
            result_label_Area.config(text="Invalid input. Please enter numbers")
            return
        if r <= 0:
            result_label_Area.config(text="Radius must be a positive number")
            return
        p = math.pi
        area = p * r**2
        c = 2 * p * r
        result_label_Area.config(text=f"Area = {area:.2f} ")
        result_label_circumference.config(text=f"circumference = {c:.2f}")

    tk.Button(
        converter,
        text="Calculate",
        command=calculate_circle,
        bg="#1769AA",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).pack(pady=5)
        

    
button1 = tk.Button(
    button_frame,
    text="Length Converter",
    command=open_length_converter,
    bg="#1769AA",
    fg="white",
    font=("Arial", 11, "bold")
)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(
    button_frame,
    text="Rectangle Calculator",
    command=open_rectangle_calculator,
    bg="#1769AA",
    fg="white",
    font=("Arial", 11, "bold")
)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(
    button_frame,
    text="Triangle Calculator",
    command=open_triangle_calculator,
    bg="#1769AA",
    fg="white",
    font=("Arial", 11, "bold")
)
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = tk.Button(
    button_frame,
    text="Circle Calculator",
    command=open_circle_calculator,
    bg="#1769AA",
    fg="white",
    font=("Arial", 11, "bold")
)
button4.grid(row=1, column=1, padx=10, pady=10)

footer = tk.Label(
    window,
    text="Engineering Toolbox | Version 1.0",
    font=("Arial", 9),
    bg="#7D67D0",
    fg="white"
)
footer.pack(side="bottom", pady=15)



window.mainloop()



