def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Pembagian dengan nol."
    else:
        return "Operasi tidak dikenal."


def main():
    print("Kalkulator sederhana. Masukkan dua angka dan pilih operasi.")

    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Error: Masukkan angka yang valid.")
        return
    
        operation = input("Pilih operasi (+, -, *, /): ").strip()
        result = calculate(num1, num2, operation)

        print(f"Hasil: {result}")
    
    # Rapikan tampilan jika hasilnya berupa angka bulat
    if isinstance(result, float) and result.is_integer():
        result = int(result)
        
    print(f"Hasil: {result}")

if __name__ == "__main__":
    main()
