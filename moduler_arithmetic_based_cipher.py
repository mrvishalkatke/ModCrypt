import math

# Function to compute the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find the modular inverse of K mod m
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to find modular inverse of K under mod m
def mod_inverse(K, m):
    gcd_value, x, y = extended_gcd(K, m)
    if gcd_value != 1:
        raise ValueError(f"Modular inverse does not exist for K={K} and m={m}.")
    else:
        # x might be negative, so we adjust it to be positive
        return x % m

# Encryption function with a shifted range for printable ASCII characters
def encrypt(plaintext, K, N):
    ciphertext = []
    for char in plaintext:
        P = ord(char)  # Convert character to ASCII
        # Shift ASCII values to ensure they fit within the printable ASCII range
        shifted_P = P - 32  # Shift to ensure it's in the range (0-94)
        C = (shifted_P ** K) % N  # Apply encryption formula (use exponentiation)
        ciphertext.append(C)
    return ciphertext

# Decryption function with shifted range back to original characters
def decrypt(ciphertext, K_inverse, N):
    decrypted_text = ""
    for C in ciphertext:
        P = (C ** K_inverse) % N  # Apply decryption formula (use exponentiation)
        shifted_P = P + 32  # Shift back to the printable ASCII range
        decrypted_text += chr(shifted_P)  # Convert ASCII back to character
    return decrypted_text

# Function to compute the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to find the modular inverse of K mod m
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to find modular inverse of K under mod m
def mod_inverse(K, m):
    gcd_value, x, y = extended_gcd(K, m)
    if gcd_value != 1:
        raise ValueError(f"Modular inverse does not exist for K={K} and m={m}.")
    else:
        # x might be negative, so we adjust it to be positive
        return x % m

def main():
    # Using larger primes for p and q
    p = 17
    q = 19
    N = p * q  # Calculate modulus N
    K = 5  # Encryption key, must be coprime with phi_N

    print(f"Public key (K, N): ({K}, {N})")

    # Modular inverse of K under (p-1)*(q-1)
    phi_N = (p - 1) * (q - 1)  # Euler's Totient (p-1)(q-1) = 3120
    K_inverse = mod_inverse(K, phi_N)

    print(f"Private key (K_inverse): {K_inverse}")

    # Plaintext input
    plaintext = "Vishal"
    print(f"Plaintext: {plaintext}")
    
    # Print the ASCII values of the plaintext
    ascii_values = [ord(char) for char in plaintext]
    print(f"ASCII values of plaintext: {ascii_values}")

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, K, N)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, K_inverse, N)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
