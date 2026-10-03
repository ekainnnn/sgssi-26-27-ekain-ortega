from collections import Counter

# Texto largo cifrado
texto_cifrado = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

def mostrar_frecuencias(texto):
    # Filtramos solo las letras mayúsculas para contar
    letras = [c for c in texto if c.isalpha() and c.isupper()]
    total = len(letras)
    frecuencias = Counter(letras)
    
    print("\n--- Letras más repetidas en el texto ---")
    for letra, cuenta in frecuencias.most_common(10): # Mostramos el top 10
        porcentaje = (cuenta / total) * 100
        print(f"Letra {letra}: {porcentaje:.2f}% ({cuenta} veces)")

# Diccionario para guardar tus sustituciones
reemplazos = {}

while True:
    # Generar el texto con los cambios que vayas haciendo
    texto_actual = ""
    for char in texto_cifrado:
        if char in reemplazos:
            # Ponemos la letra descifrada en minúscula para diferenciarla del texto cifrado (en mayúscula)
            texto_actual += reemplazos[char].lower()
        else:
            texto_actual += char

    print("\n" + "="*60)
    print("TEXTO ACTUAL:\n")
    print(texto_actual)
    print("="*60)
    
    mostrar_frecuencias(texto_cifrado)
    
    print("\nOpciones: [1] Cambiar letra  [2] Deshacer  [3] Salir")
    opcion = input("Elige (1/2/3): ")
    
    if opcion == '1':
        cifrada = input("Letra CIFRADA que quieres cambiar (ej. X): ").upper()
        clara = input(f"¿Por qué letra REAL quieres cambiar '{cifrada}'?: ").upper()
        reemplazos[cifrada] = clara
    elif opcion == '2':
        cifrada = input("Letra cifrada que quieres restaurar: ").upper()
        if cifrada in reemplazos:
            del reemplazos[cifrada]
    elif opcion == '3':
        break