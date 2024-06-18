def measurement_converter():
    conversions = {
        "1": ("mm to cm", lambda x: x / 10),
        "2": ("cm to m", lambda x: x / 100),
        "3": ("m to km", lambda x: x / 1000),
        "4": ("ft to m", lambda x: x * 0.3048),
        "5": ("in to cm", lambda x: x * 2.54)
    }

 
    choice = input("Choose a conversion (1-5): ")
    value = float(input("Enter the value to convert: "))

    if choice in conversions:
        _, func = conversions[choice]
        result = func(value)
        print(f"Converted value: {result}")

measurement_converter()