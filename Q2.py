def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        print("Error: Invalid binary number.")
        return None

binary_number = input("Enter a binary number: ")

decimal_number = binary_to_decimal(binary_number)

if decimal_number is not None:
    print(f"The equivalent decimal number is: {decimal_number}")