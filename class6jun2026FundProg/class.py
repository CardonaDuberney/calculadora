# Ingreso de bultos
categoria_liviana = 0
categoria_normal = 0

print("--- ⛴️ CATEGORIZACIÓN DE BULTOS ✈️ ---")

while True:
    try:
        cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))
        if cantidad_bultos > 0:
            break
        print("Error: Ingrese una cantidad mayor a 0.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

for bulto in range(cantidad_bultos):
    
    while True:
        try:
            peso = float(input(f"Ingrese el peso del bulto {bulto + 1} (1-10 kg): "))
            
            if 1 <= peso <= 10:
                break 
            else:
                print("Error: El peso debe ser un número entre 1 y 10.")
                
        except ValueError:
            print("Error: Ingrese un valor numérico válido para el peso.")
    
    if 1 <= peso <= 5:
        categoria_liviana += 1
    elif 6 <= peso <= 10:
        categoria_normal += 1

valor_categoria_liviana = categoria_liviana * 1000
valor_categoria_normal = categoria_normal * 2000

print("\n--- RESUMEN ---")
print(f"Cantidad de bultos livianos: {categoria_liviana}")
print(f"Cantidad de bultos normales: {categoria_normal}")
print(f"Total a pagar por bultos livianos: {valor_categoria_liviana}")
print(f"Total a pagar por bultos normales: {valor_categoria_normal}")
print(f"Total a pagar: {valor_categoria_liviana + valor_categoria_normal}")
print("---------------\n")