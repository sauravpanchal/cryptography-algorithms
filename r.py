import math

from RSA import modify_rsa

def calculate_gcd(e, phi):
    return math.gcd(e, phi)

def check_prime(n):
    if n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def get_prime():
    while True:
        inp = input("Enter prime numbers ? ").split()
        p, q = int(inp[0]), int(inp[1])
        if check_prime(p) and check_prime(q):
            print("p, q (Accepted)")
            break
        else:
            print("Try again ...")
    return p, q
def calculate_n(p, q):
    return p * q

def calculate_phi_of_n(p, q):
    phi = (p - 1) * (q - 1)
    print("phi_of_n (Calculated) => ", phi)
    return phi

def get_e(phi_of_n):
    e = int(input("Enter e ? "))
    if e > 1 and e < phi_of_n:
        gcd = calculate_gcd(e, phi_of_n)
        if gcd == 1:
            print("e (acc)")
            return e
        else:
            print("e (rej)")
    else:
        print("e (rej)")
        
def get_d(e, phi_of_n):
    d = None
    for i in range(50):
        d = round(((((phi_of_n) * i) + 1) / e), 2)
        if d > 1 and d / int(d) == 1.0:
            print("d", d)
            return int(d)

def get_keys(e, d, n):
    public_key, private_key = (e, n), (d, n)
    print("Pub", public_key)
    print("Pri", private_key)

def get_cipher(P, e, n, p, q):
    if P < n:
        C = ((P ** e) % (n))
    C = modify_rsa(C, p, q)
    print("Cipher:", C)
    return C

def get_plain_text(C, d, n, p, q):
    P = modify_rsa(C, p, q, 1, C)
    P = ((P ** d) % n)
    print("PT ", P)
    return P

def modify_rsa(C, p, q, flag = 0, y = None):
    base = 10
    if flag == 1:
        x = math.pow(base, y)
        return int(x)
    else:
        y = math.log(C, base)
        return y

p, q = get_prime()
n = calculate_n(p, q)
phi_of_n = calculate_phi_of_n(p, q)
e = get_e(phi_of_n)
d = get_d(e, phi_of_n)
get_keys(e, d, n)

flag = int(input("Mode:"))
if not flag:
    C = get_cipher(p, e, n, p, q)
    P = get_plain_text(C, d, n, p, q)
else:
    m = int(input("m ? "))
    C = get_cipher(m, e, n, p, q)
    P = get_plain_text(C, d, n, p, q)