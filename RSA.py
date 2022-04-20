# IU1941230093 Saurav Panchal
# To implement RSA Algorithm

# Import required modules
import math

# Convenience Functions
def calculate_gcd(e, phi):
    return math.gcd(e, phi)

def check_prime(n):
    if n > 1:
        for _ in range(2, n//2 + 1):
            if n % _ == 0:
                return False
        else:
            return True
    else:
        return False


# Driver Functions
def get_prime():
    while True:
        inp = input("Enter prime numbers ? ").split()
        p, q = int(inp[0]), int(inp[1])
        if check_prime(p) and check_prime(q):
            print("p, q (Accepted)")
            break
        else:
            print("Try Again ...")
    return p, q

def calculate_n(p, q):
    return p * q

def calculate_phi_of_n(n):
    phi = (p - 1) * (q - 1)
    print("phi_of_n (Calculated) =>", phi)
    return phi

def get_e(phi_of_n):
    e = int(input("Enter e ? "))
    if e > 1 and e < phi_of_n:
        gcd = calculate_gcd(e, phi_of_n)
        if gcd == 1:
            print("e (Accepted)")
            return e
        else:
            print("e (Rejected) => gcd != 1")
    else:
        print("e (Rejected) => e < 1 or e > phi_of_n")

def get_d(e, phi_of_n):
    d = None
    for i in range(50):
        d = round(((((phi_of_n) * i) + 1) / e), 2)
        if d > 1 and d / int(d) == 1.0:
            print("d (Calculated) =>", d)
            return int(d)

def get_keys(e, d, n):
    public_key, private_key = (e, n), (d, n)
    print("Public key =>", public_key)
    print("Private key =>", private_key)

def get_cipher(P, e, n, p, q):
    if P < n:
        C = ((P ** e) % (n))
    C = modify_rsa(C, p, q)
    print("After modification (Cipher) :", C)
    return C

def get_plain_text(C, d, n, p, q):
    P = modify_rsa(C, p, q, flag = 1, y = C)
    P = ((P ** d) % (n))
    print("After modification (Plain) :", P)
    return P


# Modification over standard RSA.
def modify_rsa(C, p, q, flag = 0, y = None):
    base = (p + q) // 2
    if flag == 1:
        x = math.pow(base, y)
        return int(x)
    else:
        y = math.log(C, base)
        return y

p, q = get_prime()
n = calculate_n(p, q)
phi_of_n = calculate_phi_of_n(n)
e = get_e(phi_of_n = phi_of_n)
d = get_d(e, phi_of_n = phi_of_n)
get_keys(e, d, n)

flag = int(input("Enter to use RSA as in Key-Exchange-Mode (0) or Cipher-Text-Mode (1) ? "))
if not flag:
    C = get_cipher(P = p, e = e, n = n, p = p, q = q)
    P = get_plain_text(C, d = d, n = n, p = p, q = q)
else:
    m = int(input("Enter m ? "))
    C = get_cipher(m, e = e, n = n, p = p, q = q)
    P = get_plain_text(C, d = d, n = n, p = p, q = q)