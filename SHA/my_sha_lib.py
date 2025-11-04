def my_sha256(message):
    
    binary = ''.join(format(ord(char), '08b') for char in message)
    l = len(binary)

    binary1 = binary + '1'

    k = (448 - (l+1)) % 512

    binary2 = binary1 + '0' * k

    l_bin = format(l, '064b')

    binary_f = binary2 + l_bin

    H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

    block_size = 512
    blocks = [binary_f[i:i + block_size] for i in range(0, len(binary_f), block_size)]
    m = len(blocks)
    
    def ROTL(x, n):
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
    
    def ROTR(x, n):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
    
    def SHR(x, n):
        return x >> n
    
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    def f1(x, y, z):
        return (x & y) ^ ((~x & 0xFFFFFFFF) & z)
    
    def f2(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)
    
    def f3(x):
        return ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22)
    
    def f4(x):
        return ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25)
    
    def f5(x):
        return ROTR(x, 7) ^ ROTR(x, 18) ^ SHR(x, 3)
    
    def f6(x):
        return ROTR(x, 17) ^ ROTR(x, 19) ^ SHR(x, 10)
    
    def add_mod32(*args):
        return sum(args) & 0xFFFFFFFF
    
    def compute_intermediate_hash(H_prev, a, b, c, d, e, f, g, h):
        H0 = add_mod32(H_prev[0], a) & 0xFFFFFFFF
        H1 = add_mod32(H_prev[1], b) & 0xFFFFFFFF
        H2 = add_mod32(H_prev[2], c) & 0xFFFFFFFF
        H3 = add_mod32(H_prev[3], d) & 0xFFFFFFFF
        H4 = add_mod32(H_prev[4], e) & 0xFFFFFFFF
        H5 = add_mod32(H_prev[5], f) & 0xFFFFFFFF   
        H6 = add_mod32(H_prev[6], g) & 0xFFFFFFFF
        H7 = add_mod32(H_prev[7], h) & 0xFFFFFFFF

        H_i = [H0, H1, H2, H3, H4, H5, H6, H7]
        return H_i
    
    for i, block_binary in enumerate(blocks):
        W = [int(block_binary[j:j+32], 2) for j in range(0, 512, 32)]
        for t in range(16, 64):
            s0 = f5(W[t-15])
            s1 = f6(W[t-2])
            val = add_mod32(s1, W[t-7], s0, W[t-16])
            W.append(val)

        a, b, c, d, e, f, g, h = H

        for t in range(64):
            TMP1 = add_mod32(h, f4(e), f1(e, f, g), K[t], W[t])
            TMP2 = add_mod32(f3(a), f2(a, b, c))
            h = g
            g = f
            f = e
            e = add_mod32(d, TMP1)
            d = c
            c = b
            b = a
            a = add_mod32(TMP1, TMP2)

        H = compute_intermediate_hash(H, a, b, c, d, e, f, g, h)

        block_hash = ''.join(f'{s:08x}' for s in H)

    final_hash = ''.join(f'{s:08x}' for s in H)
    return final_hash


