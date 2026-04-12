# --------------------------------
# Autora: García Herrera Valeria
# Fecha: 08 - marzo - 2026
# --------------------------------

def gcd(a, b):
    """Calcula el Máximo Común Divisor."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Algoritmo Extendido de Euclides para hallar el inverso modular."""
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    """Calcula d tal que (e * d) % phi == 1."""
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None  # Indica que no existe inverso
    else:
        return x % phi

# --- 1. GENERACIÓN DE LLAVES ---
p = 353
q = 503
n = p * q
phi = (p - 1) * (q - 1)

# Elegimos un 'e' que sea coprimo con phi.
# 997 es una excelente opción para este caso.
e = 997

d = mod_inverse(e, phi)

if d is None:
    print(f"Error: e={e} no es coprimo con phi={phi}. Elige otro 'e'.")
else:
    print(f"--------- LLAVES RSA GENERADAS ---------")
    print(f"Módulo (n): {n}")
    print(f"Llave Pública (e): {e}")
    print(f"Llave Privada (d): {d}")
    print("-" * 40)

    # --- 2. CIFRADO ---
    # El mensaje M debe ser menor que n (123 < 177559)
    mensaje_original = 123

    # C = M^e mod n
    cifrado = pow(mensaje_original, e, n)

    print(f"Mensaje original: {mensaje_original}")
    print(f"Mensaje cifrado (enviado por la red): {cifrado}")
    print("-" * 40)

    # --- 3. DESCIFRADO ---
    # M = C^d mod n
    descifrado = pow(cifrado, d, n)

    print(f"Mensaje descifrado (con llave privada): {descifrado}")

    # Verificación final
    if mensaje_original == descifrado:
        print("\nEl mensaje fue recuperado correctamente.")
