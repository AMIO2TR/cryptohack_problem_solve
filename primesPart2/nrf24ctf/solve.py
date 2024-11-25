from Crypto.Util.number import long_to_bytes
import sympy

# Given values
n = 2185117275407329493704409643426031750335664972502908228262569687853653253551641974999282770639297709207236515859043038670980072205112304661053691511338842726627494610440140259408325780945409058103256016533574664390745346605574976173834922404667585562002578669413889647210969834492555462230987942573557380522922238633429860211518953531550631797422965614944467280372149634100051335857185289141709891849112908988640903449692041845495169810184856466411086118945896740639276885520058078076157709163178813579385884534836496965087352623083616039623887918665045348095257961014902148530541607448714905048573465680784601333555074241869411687
c = 581709100817811444920095357195895023478596451568720098152765957738707547829576237509544181919071255363689905724280375610887977312507761513211172227645388299103836870890147385219082978395082680729159127040376442084884930631174614809647228529428302972753538050532437310768824758424363981358581910130829599990356824263654014749049422701767054305023571186976620569665182213765143548768316585552344481478610858991409358753209494898686158928183472709413923383461689667289210692956228953095011987153532366537268324357515516119882013754515432309251346060422842792751839294125415140428250398469331333831712594655104413985532550929508100211
e = 65537  # Given public exponent

# Step 1: Factor n
factors = sympy.factorint(n)
p = list(factors.keys())[0]
q = list(factors.values())[0]

# Step 2: Compute φ(n) and d
phi_n = (p - 1) * (q - 1)

# Compute the modular inverse of e
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

gcd, d, _ = extended_gcd(e, phi_n)
d = d % phi_n  # Ensure d is positive

# Step 3: Decrypt the ciphertext
m = pow(c, d, n)

# Convert long integer to bytes to retrieve the flag
flag_bytes = long_to_bytes(m)
print(flag_bytes)