import xmlrpc.client

# Conectar al servidor XML-RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

# Operaciones de prueba
print("Operaciones remotas en el servidor de calculadora:")

try:
    resultado = proxy.sumar(10, 5)
    print("Resultado de 10 + 5:", resultado)

    resultado = proxy.restar(10, 5)
    print("Resultado de 10 - 5:", resultado)

    resultado = proxy.multiplicar(10, 5)
    print("Resultado de 10 * 5:", resultado)

    resultado = proxy.dividir(10, 5)
    print("Resultado de 10 / 5:", resultado)

    resultado = proxy.potencia(2, 3)
    print("Resultado de 2 ^ 3:", resultado)

    resultado = proxy.raiz_cuadrada(16)
    print("Resultado de √16:", resultado)

    resultado = proxy.dividir(10, 0)
    print("Resultado de 10 / 0:", resultado)

    resultado = proxy.raiz_cuadrada(-9)
    print("Resultado de √-9:", resultado)

except Exception as e:
    print(f"Error durante la operación: {e}")
