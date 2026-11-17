
def decimal_para_binario(num):

    if num < 2:
        return str(num)

    return decimal_para_binario(num // 2) + str(num % 2)


num = 13

resultado = decimal_para_binario(num)

print(f"Decimal: {num}")
print(f"Binário: {resultado}")
