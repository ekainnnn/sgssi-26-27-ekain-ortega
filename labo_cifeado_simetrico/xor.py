# Función para aplicar XOR byte a byte entre dos secuencias
def cifrado_xor(texto_bytes, clave_bytes):
    # zip junta el byte 1 del texto con el byte 1 de la clave, etc.
    # El operador ^ realiza la operación XOR a nivel de bits
    return bytes([b_texto ^ b_clave for b_texto, b_clave in zip(texto_bytes, clave_bytes)])

# 1. Leer mensaje y clave representados como cadenas de bytes
mensaje = b"ATAQUE AL AMANECER"
clave = b"CLAVE12345678901"

# 2. Aplicar la operación XOR para obtener el criptograma
criptograma = cifrado_xor(mensaje, clave)

# 3. Usar la misma operación XOR para recuperar el mensaje original
descifrado = cifrado_xor(criptograma, clave)

# 4. Mostrar el mensaje original, la clave y el criptograma en hexadecimal
print("--- Resultados en Hexadecimal ---")
print(f"Mensaje original : {mensaje.hex()}")
print(f"Clave            : {clave.hex()}")
print(f"Criptograma      : {criptograma.hex()}")

# 5. Comprobar que el descifrado produce exactamente el mensaje original
print("\n--- Comprobación Final ---")
print(f"Texto descifrado : {descifrado.decode('utf-8')}")

if mensaje == descifrado:
    print("[*] ÉXITO: El descifrado coincide exactamente con el mensaje original.")
else:
    print("[!] ERROR: El descifrado no coincide.")