from langdetect import detect

def descifrar_cesar(criptograma, desplazamiento):
    texto_claro = ""
    for c in criptograma:
        if c.isalpha():
            # Definir la base ASCII dependiendo de si es mayúscula o minúscula
            base = ord('A') if c.isupper() else ord('a')
            # Aplicar aritmética modular (módulo 26) para retroceder en el alfabeto
            texto_claro += chr((ord(c) - base - desplazamiento) % 26 + base)
        else:
            # Mantener espacios y signos de puntuación intactos
            texto_claro += c
    return texto_claro

mensaje_cifrado = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

print("Iniciando ataque de fuerza bruta...\n")

# Probar los 25 desplazamientos posibles del cifrado César
for clave in range(1, 26):
    intento = descifrar_cesar(mensaje_cifrado, clave)
    
    try:
        # Evaluar si el texto tiene sentido en español
        if detect(intento) == 'es':
            print(f"[*] ¡CLAVE ENCONTRADA! Desplazamiento: {clave}")
            print(f"[*] Mensaje original: {intento}")
            break
    except:
        # langdetect lanza error si el texto no tiene letras reconocibles; lo ignoramos
        pass