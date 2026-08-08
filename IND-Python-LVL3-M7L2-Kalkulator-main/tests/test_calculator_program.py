import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'tidak diketahui') == "Operasi tidak dikenal."

# 1. Tes Pengurangan
def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2

# 2. Tes Perkalian
def test_calculate_multiplication():
    assert calculate(4, 3, '*') == 12

# 3. Tes Tambahan (Keren): Pembagian dengan Nol
def test_calculate_division_by_zero():
    assert calculate(5, 0, '/') == "Error: Pembagian dengan nol."

# 4. Tes Tambahan (Keren): Bilangan Negatif
def test_calculate_negative_numbers():
    assert calculate(-2, -3, '*') == 6

'''
Tugas. Saat ini ada tiga unit-test yang sudah dibuat
Program mengecek apakah kalkulator berfungsi dengan benar untuk operasi penjumlahan, pembagian dan operasi yang tidak dikenal
Kamu perlu menambahkan minimal tes untuk operasi berikut:
1. Pengurangan
2. Perkalian
Akan lebih keren kalau kamu bisa membuat dan menambahkan tes-tes tambahan
'''
