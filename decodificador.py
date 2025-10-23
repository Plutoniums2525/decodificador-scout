import unicodedata
import os


CLAVES = {
    "MURCIELAGO": {
        'M': '1', 'U': '2', 'R': '3', 'C': '4', 'I': '5',
        'E': '6', 'L': '7', 'A': '8', 'G': '9', 'O': '0'
    },
    "ABUELITO": {
        'A': '1', 'B': '2', 'U': '3', 'E': '4',
        'L': '5', 'I': '6', 'T': '7', 'O': '8'
    },
    "ALFABETO_INVERSO": {
        **{chr(a): chr(ord('Z') - (a - ord('A'))) for a in range(ord('A'), ord('Z') + 1)},
        'Ñ': 'Ñ'
    },
    "CENIT_POLAR": {
        'C': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R',
        'P': 'C', 'O': 'E', 'L': 'N', 'A': 'I', 'R': 'T'
    }
}



def _strip_accents(s: str) -> str:
    """Elimina acentos (á→a, é→e, etc.)."""
    return ''.join(ch for ch in unicodedata.normalize('NFD', s)
                   if unicodedata.category(ch) != 'Mn')

def encode_text(text: str, clave: str = "MURCIELAGO") -> str:
    """Codifica texto según la clave elegida."""
    mapa = CLAVES.get(clave.upper())
    if not mapa:
        raise ValueError(f"Clave '{clave}' no está definida.")

    result = []
    for ch in text:
        base = _strip_accents(ch).upper()
        result.append(mapa.get(base, ch))
    return ''.join(result)

def decode_text(cipher: str, clave: str = "MURCIELAGO") -> str:
    """Decodifica texto según la clave elegida."""
    mapa = CLAVES.get(clave.upper())
    if not mapa:
        raise ValueError(f"Clave '{clave}' no está definida.")

    inverso = {v: k for k, v in mapa.items()}
    result = []
    for ch in cipher:
        result.append(inverso.get(ch, ch))
    return ''.join(result)

# --- Menú interactivo ---
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clave_actual = "MURCIELAGO"

    while True:
        print("====================================")
        print("🔐  Cifrador por sustitución simple")
        print("====================================")
        print(f"🔑 Clave actual: {clave_actual}")
        print("------------------------------------")
        print("1. Codificar texto")
        print("2. Decodificar texto")
        print("3. Cambiar clave")
        print("4. Salir")
        print("------------------------------------")
        opcion = input("Elige una opción (1/2/3/4): ").strip()

        if opcion == '1':
            texto = input("\nEscribe el texto a codificar: ")
            print("\n🔒 Resultado:")
            print(encode_text(texto, clave_actual))
        elif opcion == '2':
            texto = input("\nEscribe el texto a decodificar: ")
            print("\n🔓 Resultado:")
            print(decode_text(texto, clave_actual))
        elif opcion == '3':
            print("\nClaves disponibles:", ', '.join(CLAVES.keys()))
            nueva = input("Escribe el nombre de la clave: ").strip().upper()
            if nueva in CLAVES:
                clave_actual = nueva
                print(f"✅ Clave cambiada a {nueva}")
            else:
                print("❌ Esa clave no existe.")
        elif opcion == '4':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

        input("\nPresiona Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()
