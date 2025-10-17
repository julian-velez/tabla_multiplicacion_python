# Pedimos al usuario que escriba el número para la tabla de multiplicar
multiplicacion = int(input("¿Qué tabla de multiplicar quieres ver? "))

# Pedimos hasta qué número quiere que llegue la tabla
limite = int(input("¿Hasta qué número quieres multiplicar? "))

# Usamos un bucle 'for' que va desde 0 hasta el número indicado por el usuario
for numero in range(limite + 1):
    # Imprimimos la operación con formato limpio usando una f-string
    print(f"{multiplicacion} x {numero} = {multiplicacion * numero}")
