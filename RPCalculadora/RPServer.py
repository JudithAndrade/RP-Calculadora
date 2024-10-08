from xmlrpc.server import SimpleXMLRPCServer
import math

# Funciones de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)

# Crear el servidor
server = SimpleXMLRPCServer(('localhost', 9000))
print("Servidor de calculadora escuchando en el puerto 9000...")

# Registrar funciones para ser llamadas de manera remota
server.register_function(sumar, 'sumar')
server.register_function(restar, 'restar')
server.register_function(multiplicar, 'multiplicar')
server.register_function(dividir, 'dividir')
server.register_function(potencia, 'potencia')
server.register_function(raiz_cuadrada, 'raiz_cuadrada')

# Ejecutar el servidor indefinidamente
server.serve_forever()
