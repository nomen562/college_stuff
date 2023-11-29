import tkinter as tk
from tkinter import ttk

# Function to process user input and recommend cars
def process_input():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    budget = int(budget_entry.get())
    car_type = car_type_var.get()
    car_noseat = car_noseat_var.get()

    welcome_label.grid_forget()  # Hide the welcome message

    # Sample car names and features (you can replace this with data from Google)
    car_names =  [
        {"name": "Hyundai i20 ", "type": "HATCHBACK", "seats": 5, "price": 700000, "features": "Advanced safety features"},
        {"name": "TATA TIAGO XE", "type": "SEDAN", "seats": 5, "price": 600000, "features": "Leather seats"},
        {"name": "MARUTI SUZUKI SWIFT", "type": "HATCHBACK", "seats": 2, "price": 770000, "features": "Turbocharged engine"},
        {"name": "MARUTI SUZUKI BALENO DELTA AGS", "type": "SEDAN", "seats": 5, "price": 800000, "features": "Panoramic sunroof"},
        {"name": "HONDA AMAZE", "type": "SUV", "seats": 7, "price": 950000, "features": "Advanced safety features"},
        {"name": "TATA NEXON CRATIVE", "type": "HATCHBACK", "seats": 5, "price": 1100000, "features": "Leather seats"},
        {"name": "KIA SONET HTX", "type": "SUV", "seats": 5, "price": 1200000, "features": " 998 CC PETROL ENGINE"},
        {"name": "MARUTI SUZUKI CIAZ (DELTA 1.5)", "type": "SEDAN", "seats": 5, "price": 1110000, "features": "AVERAGE = 20.65 KmPL"},
        {"name": "MARUTI SUZUKI ERTIGA ZXI AT", "type": "SUV", "seats": 7, "price": 1250000, "features": "1462 CC PETROL ENGINE , AVERAGE = 20.3 KmPL"},
        {"name": "MAHINDRA BOLER0 NEO", "type": "SUV", "seats": 7, "price": 1215000, "features": "1493 DIESEL ENGINE"},
        {"name": "MAHINDRA THAR LX", "type": "", "seats": 5, "price": 1380000, "features": "1997 CC PETROL ENGINE"},
        {"name": "KIA CARENS PRESTIGE PLUS", "type": "HATCHBACK", "seats": 5, "price": 1490000, "features": "1482 CC PETROL ENGINE"},
        {"name": "HYUNDAI CREATA S ", "type": "HATCHBACK", "seats": 5, "price": 1450000, "features": "1493 CC DIESEL ENGINE"},
        {"name": "TATA HARRIER PURE(O)", "type": "SUV", "seats": 5, "price": 1750000, "features": "1956 DIESEL ENGINE"},
        {"name": "TOYOTA INNVOA HICROSS", "type": "SUV", "seats": 7, "price": 1970000, "features": "1987 CC PETROL ENGINE"},
        {"name": "MG HECTOR PLUS", "type": " =SUV", "seats": 5,"price": 1970000, "features": "TURBO DIESEL ENGINE"},
        {"name": "HYUNDAI VERNA SX", "type": "SEDAN", "seats": 5, "price": 1490000, "features": "1482 CC PETROL ENGINE , AVERAGE = 20 KmPL"},
        {"name": "HONDA CITY HYBRID eHV", "type": "Sedan", "seats": 5, "price": 1890000, "features": "HYBRID ELECTRIC + PETROL ENGINE"},
        {"name": "JEEP COMPASS NIGHT EAGLE", "type": "SUV", "seats": 5, "price": 2400000, "features": "1956 CC DIESEL ENGINE"},
        {"name": "MG GLOSTER", "type": "SUV", "seats": 7, "price": 3879000, "features": "1996 CC DIESEL ENIGINE + AUTOMATIC"},
        {"name": "TOYOTA FORTUNER", "type": "SUV", "seats": 7, "price": 3500000, "features": "AUTOMATIC , 2694 CC ENIGINE"},
        {"name": "SKODA KODIAQ", "type": "Sedan", "seats": 5, "price": 3850000, "features": "AUTOMATIC"},
        {"name": "XUV700 ", "type": "SUV", "seats": 7, "price": 2330000, "features": "AUTOMATIC 2184 CC DIESEL ENGINE"},
        {"name": "KIA SELTOS", "type": "Sedan", "seats": 5, "price": 2029000, "features": "AUTOMATIC"},
        {"name": "TATA SAFARI DUAL TONE", "type": "SUV", "seats": 7, "price": 2550000, "features": "1956 CC DIESEL ENGINE"},
        {"name": "BMW X1 M SPORT", "type": "Sedan", "seats": 5, "price":5160000, "features": "AUTOMATIC , 1995 CC DIESEL ENIGINE"},
        {"name": "TOYOTA FORTUNER LEGENDER", "type": "SUV", "seats": 7, "price": 4360000, "features": "AUTOMATIC 2755 CC DIESEL ENGINE"},
        {"name": "TOYOTA CAMRY", "type": "SEDAN", "seats": 5, "price": 4616000, "features": "2487 CC HYBRID ENGINE"},
        {"name": "AUDI A4 SERIES PREMIUM", "type": "SEDAN", "seats": 5, "price": 4800000, "features": " AUTOMATIC , 1984 CC ENIGINE"},
        {"name": "MERCEDES BENZ GLA", "type": "SUV", "seats": 5, "price": 5000000, "features": "ATUMATIC DIESEL ENGINE"},
        {"name": "VOLVO XC4O RECHARGE ", "type": "SUV", "seats": 5, "price": 5690000, "features": "AUTOMATIC , ELECTRIC"},
        {"name": "MERCEDES BENZ C CLASS", "type": "SEDAN", "seats": 5, "price": 6000000, "features": "AUTOMATIC 1496 CC PETROL ENGINE"},
        {"name": "MINI COOPER", "type": "HATCHBACK", "seats": 5, "price": 4250000, "features": "AUTOMATIC , 1998 CC PETROL ENGINE"},
        {"name": "AUDI Q3 SPORTBACK", "type": "Sedan", "seats": 5, "price": 5297000, "features": "1984 CC PETROL ENGINE"},
        {"name": "HONDA CITY", "type": "SEDAN", "seats": 5, "price": 1490000, "features": "5 STAR SAFETY"},
        {"name": "LAND ROVER RANGE ROVER EVOQUE", "type": "SUV", "seats": 5, "price": 7100000, "features": "1997 CC PETROL ENGINE"},
        {"name": "VOLVO XC40 RECHARGE", "type": "SUV", "seats": 5, "price": 6400000, "features": "Advanced safety features, ELECTRIC"},
        {"name": "JEEP WRANGELR", "type": "SUV", "seats": 5, "price": 6500000, "features": "Leather seats"},
        {"name": "BMW X5", "type": "SUV", "seats": 5, "price": 9500000, "features": "Turbocharged 2995 CC ENGINE"},
        {"name": "JAGUAR F TYPE", "type": "SPORTS", "seats": 2, "price": 9990000, "features": "SPORTS CAR"},
        {"name": "LAND ROVER DEFENDER 110", "type": "SUV", "seats": 5, "price": 9350000, "features": "Advanced safety features "},
        {"name": "MERCEDES BENZ AMG COUPE", "type": "SEDAN", "seats": 5, "price": 8720000, "features": "2996 CC TURBO ENGINE"},
        {"name": "BMW Z4 ", "type": "SPORTS", "seats": 2, "price": 9000000, "features": "Turbocharged engine"},
        {"name": "BMW X3", "type": "SUV", "seats": 5, "price": 8890000, "features": "Panoramic sunroof"},
        
    ]


    for car in car_names:
        if car["type"].lower() == car_type.lower() and car["seats"] == int(car_noseat) and car["price"] <= budget:
            result_text.config(text=f"Car Name: {car['name']}\nPrice: ₹{car['price']}\nFeatures: {car['features']}")
            return

    result_text.config(text="Oops! Sorry, we couldn't find a car that matches your criteria.")

# Create a tkinter window
window = tk.Tk()
window.title("Car Kharido")
window.geometry("500x500")

# Create and arrange UI elements with styles
style = ttk.Style()
style.configure("TLabel", background="#FFD700", foreground="blue", font=("Arial", 14))
style.configure("TButton", background="green", foreground="white", font=("Arial", 12))

welcome_label = ttk.Label(window, text="Welcome to Car Kharido!", font=("Arial", 16, "bold"), foreground="blue")
welcome_label.pack(pady=10)

personal_info_frame = ttk.Frame(window)
personal_info_frame.pack(pady=10)

name_label = ttk.Label(personal_info_frame, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(personal_info_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label = ttk.Label(personal_info_frame, text="Enter your email:")
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry = ttk.Entry(personal_info_frame)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = ttk.Label(personal_info_frame, text="Enter your password:")
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = ttk.Entry(personal_info_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

welcome_label = ttk.Label(window, text="How can I help you!", font=("Arial", 16, "bold"), foreground="blue")
welcome_label.pack(pady=10)

budget_label = ttk.Label(window, text="Enter your budget:")
budget_label.pack(pady=5)
budget_entry = ttk.Entry(window)
budget_entry.pack(pady=5)

car_type_label = ttk.Label(window, text="Enter your car type (SUV/SEDAN/HATCHBACK/SPORTS):")
car_type_label.pack(pady=5)
car_type_var = tk.StringVar(window)
car_type_var.set("suv")
car_type_entry = ttk.Entry(window, textvariable=car_type_var)
car_type_entry.pack(pady=5)

car_noseat_label = ttk.Label(window, text="Enter number of seats you want in your car:")
car_noseat_label.pack(pady=5)
car_noseat_var = tk.StringVar(window)
car_noseat_var.set("5")
car_noseat_entry = ttk.Entry(window, textvariable=car_noseat_var)
car_noseat_entry.pack(pady=5)

welcome_label = ttk.Label(window, text="OK Lets proceed your requirements further", font=("Arial", 16, "bold"), foreground="blue")
welcome_label.pack(pady=10)

process_button = ttk.Button(window, text="Process", command=process_input)
process_button.pack(pady=10)

result_text = ttk.Label(window, text="", wraplength=350)
result_text.pack(pady=10)

# Start the tkinter main loop
window.mainloop()