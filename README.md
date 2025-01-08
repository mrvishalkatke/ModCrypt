# Modular Arithmetic-Based Cipher

This project demonstrates the encryption and decryption process of the plain text "Vishal" using a modular arithmetic-based cipher.

## Overview

The cipher utilizes modular arithmetic for secure message encryption and decryption. While the example uses small prime numbers for simplicity, real-world applications would involve much larger primes for enhanced security.

---

## Step-by-Step Explanation

### 1. Convert Characters to ASCII Values

Each character in "Vishal" is converted into its corresponding ASCII value:

| Character | ASCII Value |
|-----------|-------------|
| V         | 86          |
| i         | 105         |
| s         | 115         |
| h         | 104         |
| a         | 97          |
| l         | 108         |

So, the plain text "Vishal" is represented as:

{86, 105, 115, 104, 97, 108}


---

### 2. Key Setup

- Let’s take two small prime numbers  p = 17  and  q = 19 .
- Compute  N = p * q = 17 * 19 = 323 .
- Let’s choose an encryption key  K = 5 , which is coprime with  (p-1) * (q-1) = 16 * 18 = 288 .

---

### 3. Encryption Process

Each ASCII value \( P \) is encrypted using the formula:

\[
C = (P * K) mod N
\]

Where:
-  P  is the ASCII value of the character.
-  K = 5  is the encryption key.
-  N = 323 .

#### Encrypted Values:

- V (86) →  C = (86 * 5) mod 323 = 430 mod 323 = 107 
- i (105) →  C = (105 * 5) mod 323 = 525 mod 323 = 202 
- s (115) →  C = (115 * 5) mod 323 = 575 mod 323 = 252 
- h (104) →  C = (104 * 5) mod 323 = 520 mod 323 = 197 
- a (97) →  C = (97 * 5) mod 323 = 485 mod 323 = 162 
- l (108) →  C = (108 * 5) mod 323 = 540 mod 323 = 217 

| Character | ASCII Value | Encrypted Value (\( C \)) |
|-----------|-------------|---------------------------|
| V         | 86          | 107                       |
| i         | 105         | 202                       |
| s         | 115         | 252                       |
| h         | 104         | 197                       |
| a         | 97          | 162                       |
| l         | 108         | 217                       |

The encrypted message is:

{107, 202, 252, 197, 162, 217}


---

### 4. Decryption Process

To decrypt, we calculate the modular inverse \( K^{-1} \) of \( K \mod (p-1)(q-1) \) using the Extended Euclidean Algorithm. For \( K = 5 \) and \( (p-1)(q-1) = 288 \), the modular inverse is:

\[
K^{-1} = 173
\]

Each ciphertext value \( C \) is decrypted using the formula:

\[
P = (C * K-1) mod N
\]

Where:
-  C  is the ciphertext.
-  K-1 = 173  is the decryption key.
-  N = 323 .

#### Decrypted Values:

- 107 →  P = (107 * 173) mod 323 = 18511 mod 323 = 86  → V
- 202 →  P = (202 * 173) mod 323 = 34946 mod 323 = 105  → i
- 252 →  P = (252 * 173) mod 323 = 43644 mod 323 = 115  → s
- 197 →  P = (197 * 173) mod 323 = 34081 mod 323 = 104  → h
- 162 →  P = (162 * 173) mod 323 = 28026 mod 323 = 97  → a
- 217 →  P = (217 * 173) mod 323 = 37541 mod 323 = 108  → l

| Encrypted Value (\( C \)) | Decrypted ASCII Value (\( P \)) | Character |
|---------------------------|---------------------------------|-----------|
| 107                       | 86                              | V         |
| 202                       | 105                             | i         |
| 252                       | 115                             | s         |
| 197                       | 104                             | h         |
| 162                       | 97                              | a         |
| 217                       | 108                             | l         |

The decrypted message is:

{86, 105, 115, 104, 97, 108} = "Vishal"


---

## Conclusion

- **Original Text**: "Vishal"
- **Encrypted Message**: `{107, 202, 252, 197, 162, 217}`
- **Decrypted Message**: "Vishal"

This example illustrates the process of encryption and decryption using a modular arithmetic-based cipher. For real-world applications, larger prime numbers \( p \) and \( q \) should be used for better security.

---

## Note

This project demonstrates the concept of modular arithmetic in cryptography. It is intended for educational purposes, and real-world implementation should follow advanced cryptographic standards.
