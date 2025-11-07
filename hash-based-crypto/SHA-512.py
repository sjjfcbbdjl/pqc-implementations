def my_sha512(message):
    binary = ''.join(format(ord(char), '08b') for char in message)
    l = len(binary)
    print("Binary Representation:", binary)
    print(f"Lenght of the message in binary is: {l} bits")

    binary1 = binary + '1'

    print("Binary before:", binary)
    print("Binary after appending 1:", binary1)

    k = (896 - (l + 1)) % 1024

# Now append k 0's at the end of binary1
    binary2 = binary1 + '0' * k

    print(f"Original lenght (bits): {l}")
    print(f"Number of 0's appended: {k}")
    print(f"Total lenght after padding (bits): {len(binary2)}")


    l_bin = format(l, '0128b')

# Now, append this 128-bit representation of l to binary2
    binary_f = binary2 + l_bin

    print(f"Final length after appending: {len(binary_f)} bits")
    print(f"Message after padding: {binary_f}")


# SHA-512 initialization. 

# SHA-512 maintains 8 32-bit variables as state variables.

    H = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1, 0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179 ]

    print(f"Initial SHA-512 state variables = {H[0]:016x} {H[1]:016x} {H[2]:016x} {H[3]:016x} {H[4]:016x} {H[5]:016x} {H[6]:016x} {H[7]:016x}")


# Now the padded message is divided into 1024-bit blocks for further processing in SHA-512.

    block_size = 1024

    blocks = [binary_f[i:i + block_size] for i in range(0, len(binary_f), block_size)] 

    m = len(blocks)

    print(f"Total number of 1024-bit blocks: m = {m}")

    for i, block in enumerate(blocks):
        print(f"Block {i+1} (B^{i+1}):")
        print(block)
        print("-" * 70) 


    
    
    def ROTL(x, n): 
        """calculate shift of x by n bit positions to the left"""
        return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

    def ROTR(x, n):
        """ Calculate shift of x by n bit positions to the right"""
        return ((x >> n) | (x << (64 - n))) & 0xFFFFFFFFFFFFFFFF

    def SHR(x, n):
        """Calculate logical right shift of x by n bit positions"""
        return x >> n

# The SHA-512 uses a sequence of 80 constant 64-bit words:

    K = [
    0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
    0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
    0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
    0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
    0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
    0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
    0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
    0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
    0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
    0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
    0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
    0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
    0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
    0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
    0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
    0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
    0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
    0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
    0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
    0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
] 
                  

# The SHA-512 uses 6 logical functions where each function takes 64-bit words as input and produces a 64-bit word as output.


    def f1(x, y, z):
        return (x & y) ^ ((~x & 0xFFFFFFFFFFFFFFFF) & z)

    def f2(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def f3(x):
        return ROTR(x, 28) ^ ROTR(x, 34) ^ ROTR(x, 39)

    def f4(x):
        return ROTR(x, 14) ^ ROTR(x, 18) ^ ROTR(x, 41)

    def f5(x):
        return ROTR(x,1) ^ ROTR(x, 8) ^ SHR(x, 7)

    def f6(x):
        return ROTR(x, 19) ^ ROTR(x, 61) ^ SHR(x, 6)

    def add_mod64(*args):
        """Add multiple 64-bit integers with wrap-around (mod 2^64)."""
        return sum(args) & 0xFFFFFFFFFFFFFFFF

    def compute_intermediate_hash(H_prev, a, b, c, d, e, f, g, h):
        """ Compute the updated hash value after processing a block. """

        H0 = add_mod64(H_prev[0], a) & 0xffffffffffffffff
        H1 = add_mod64(H_prev[1], b) & 0xffffffffffffffff
        H2 = add_mod64(H_prev[2], c) & 0xffffffffffffffff
        H3 = add_mod64(H_prev[3], d) & 0xffffffffffffffff
        H4 = add_mod64(H_prev[4], e) & 0xffffffffffffffff
        H5 = add_mod64(H_prev[5], f) & 0xffffffffffffffff
        H6 = add_mod64(H_prev[6], g) & 0xffffffffffffffff
        H7 = add_mod64(H_prev[7], h) & 0xffffffffffffffff



        H_i = [H0, H1, H2, H3, H4, H5, H6, H7]
        return H_i



# the main loop of SHA-512 algo


# We now loop over each block B^i for i = 1 to m

    for i, block_binary in enumerate(blocks):
        print(f"\n--- Processing Block {i+1} ---")

    # Now we prepare W[0],..., W[79] 

        W = [int(block_binary[j:j+64], 2) for j in range(0, 1024, 64)]
    
        for t in range(16, 80):
            s0 = f5(W[t-15])
            s1 = f6(W[t-2])

            val = add_mod64(s1, W[t-7], s0, W[t-16])

            W.append(val)

        

        print("Generated W array for this block (W[0]...W[79]):")
        for t in range(80):
            print(f" W[{t:2d}] = {W[t]:016x}")

        a, b, c, d, e, f, g, h = H 

        print(f"Input Hash:  {a:016x} {b:016x} {c:016x} {d:016x} {e:016x} {f:016x} {g:016x} {h:016x}")

# Now, the 80 rounds.

        print(f" len(W) = {len(W)}, len(K) = {len(K)}")

        for t in range(80):
            TMP1 = add_mod64(h, f4(e), f1(e, f, g), K[t], W[t])
            TMP2 = add_mod64(f3(a), f2(a, b, c))
            h = g
            g = f
            f = e
            e = add_mod64(d, TMP1)
            d = c
            c = b
            b = a
            a = add_mod64(TMP1, TMP2)
        
            print(f" t={t:2d}: {a:016x} {b:016x} {c:016x} {d:016x} {e:016x} {f:016x} {g:016x} {h:016x}")


        H = compute_intermediate_hash(H, a, b, c, d, e, f, g, h)

        block_hash = ''.join(f'{s:016x}' for s in H)
        print(f"OutputHash: {block_hash}")

   

    final_hash = ''.join(f'{s:016x}' for s in H)
    print(f"\nFinal SHA-512 Hash: {final_hash}")
    return final_hash

message = input("Please Enter your Message: ")

final_hash = my_sha512(message)

import hashlib

lib_hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
print(f"SHA-512 Hash using hashlib: {lib_hash}")
print(f"Match: {final_hash == lib_hash}")