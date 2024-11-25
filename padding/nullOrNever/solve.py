from Crypto.Util.number import bytes_to_long, long_to_bytes
from sympy import symbols, Poly, solve, ZZ

n = 95341235345618011251857577682324351171197688101180707030749869409235726634345899397258784261937590128088284421816891826202978052640992678267974129629670862991769812330793126662251062120518795878693122854189330426777286315442926939843468730196970939951374889986320771714519309125434348512571864406646232154103
e = 3
c = 63476139027102349822147098087901756023488558030079225358836870725611623045683759473454129221778690683914555720975250395929721681009556415292257804239149809875424000027362678341633901036035522299395660255954384685936351041718040558055860508481512479599089561391846007771856837130233678763953257086620228436828

# Create the symbol for the polynomial
x = symbols('x')

for i in range(9, 93):
    flag = b'crypto{'
    
    # Create the padded message and convert to long
    m = flag + (b'\x00' * i) + b'}' + (b'\x00' * (100 - len(flag) - i - 1))
    m = bytes_to_long(m)
    
    # Construct the polynomial (m + x)**e - c
    f = (m + x)**e - c
    
    # Convert to a SymPy polynomial
    poly_f = Poly(f, x, domain=ZZ)
    
    # Print the constructed polynomial
    print(f"Polynomial for i={i}:\n", poly_f)
    
    # Find the small roots of the polynomial modulo n (SymPy does not have small_roots, we approximate using solve_mod)
    # We will use `solve` with modular arithmetic in SymPy (since there's no small_roots in SymPy)
    try:
        # Find solutions modulo n
        solutions = solve(poly_f, x, domain=ZZ.nmod(n))
        if solutions:
            temp = solutions[0]
            # Convert the solution back to bytes and print the flag
            middle = long_to_bytes(temp)
            flag = (flag + middle + b'}').decode()
            print("Flag found:", flag)
            break
        else:
            print('Not yet!!!')
    except Exception as e:
        print(f"Error during solve: {e}")
