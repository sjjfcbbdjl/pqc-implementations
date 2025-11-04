# Converting the message into binary

message = input("Please Enter your Message: ")
binary = ''.join(format(ord(char), '08b') for char in message)
l = len(binary)
print("Binary Representation:", binary)
print(f"Lenght of the message in binary is: {l} bits")

# Appending '1' to the binary representation

binary1 = binary + '1'

print("Binary before:", binary)
print("Binary after appending 1:", binary1)


# Now we want to append '0's until the length is congruent to 448 mod 512

#Calculating the number of '0's to append
k = (448 - (l + 1)) % 512

# Now append k 0's at the end of binary1
binary2 = binary1 + '0' * k

print(f"Original lenght (bits): {l}")
print(f"Number of 0's appended: {k}")
print(f"Total lenght after padding (bits): {len(binary2)}")


# Now for the remaining 64 bits,we need to append the binary representation of the original length l

l_bin = format(l, '064b')

# Now, append this 64-bit representation of l to binary2
binary_f = binary2 + l_bin

print(f"Final length after appending: {len(binary_f)} bits")
print(f"Message after padding: {binary_f}")



#Initialization of SHA-1

# SHA-1 maintains five 32-bit words as state variables

H = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

print(f"Initial SHA-1 State Variables: {H[0]:08x} {H[1]:08x} {H[2]:08x} {H[3]:08x} {H[4]:08x}")


# Now we divide the padded message into 512-bit blocks: B^1, B^2, ..., B^m

block_size = 512

blocks = [binary_f[i:i + block_size] for i in range(0, len(binary_f), block_size)]

m = len(blocks)

print(f"Total number of 512-bit blocks: m = {m}")

for i, block in enumerate(blocks):
    print(f"Block {i+1} (B^{i+1}):")
    print(block)
    print("-" * 70) 
    


# Now, we define all the functions and constants used in SHA-1.

def ROTL(x, n): 
    """calculate shift of x by n bit positions to the left"""
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


# Now, we define a sequence of eighty constant 32-bit words K[t] for t = 0 to 79 by:


K = []

for t in range(80):
    if 0 <= t <= 19:
        K_t = 0x5a827999
    elif 20 <= t <= 39:
        K_t = 0x6ed9eba1
    elif 40 <= t <= 59:
        K_t = 0x8f1bbcdc
    else:  # 60 <= t <= 79
        K_t = 0xca62c1d6
    K.append(K_t)


# Now, we define the sequence of functions f[t] where t from 0 to 79 where each function operates on three 32 bit words and produces a 32 bit word output.

def f(t, x, y, z,):
    """SHA-1 functions f[t] for t = 0 to 79"""
    if 0 <= t <= 19:
        return (x & y) ^ ((~x & 0xFFFFFFFF) & z)
    elif 20 <= t <= 39:
        return x ^ y ^ z
    elif 40 <= t <= 59:
        return (x & y) ^ (x & z) ^ (y & z)
    else:  # 60 <= t <= 79
        return x ^ y ^ z
    

def add_mod32(*args):
    """Add multiple 32-bit integers with wrap-around (mod 2^32)."""
    return sum(args) & 0xFFFFFFFF



def compute_intermediate_hash(H_prev, a, b, c, d, e):
    """ Compute the updated hash value after processing a block. """

    H0 = add_mod32(H_prev[0], a) & 0xffffffff
    H1 = add_mod32(H_prev[1], b) & 0xffffffff
    H2 = add_mod32(H_prev[2], c) & 0xffffffff
    H3 = add_mod32(H_prev[3], d) & 0xffffffff
    H4 = add_mod32(H_prev[4], e) & 0xffffffff

    H_i = [H0, H1, H2, H3, H4]
    return H_i




# Now our main hashing algorithm begins.

# We now loop over each block B^i for i = 1 to m

for i, block_binary in enumerate(blocks):
    print(f"\n--- Processing Block {i+1} ---")

    # Now we prepare W[0],..., W[79] 

    W = [int(block_binary[j:j+32], 2) for j in range(0, 512, 32)]
    
    for t in range(16, 80):
        val = W[t-3] ^ W[t-8] ^ W[t-14] ^ W[t-16]
        W.append(ROTL(val, 1))

    print("Generated W array for this block (W[0]...W[79]):")
    for t in range(80):
        print(f" W[{t:2d}] = {W[t]:08x}")

    # Now, we initialise the working variables.

    a, b, c, d, e = H 

    print(f"Input Hash:  {a:08x} {b:08x} {c:08x} {d:08x} {e:08x}")

# Now, the 80 rounds.

    for t in range(80):
        TMP = add_mod32(ROTL(a, 5), f(t, b, c, d), e, K[t], W[t])
        e = d
        d = c
        c = ROTL(b, 30)
        b = a
        a = TMP

        print(f" t={t:2d}: {a:08x} {b:08x} {c:08x} {d:08x} {e:08x}")

    
# Now, we compute the intermediate hash value H^i

    H = compute_intermediate_hash(H, a, b, c, d, e)

    block_hash = ''.join(f'{h:08x}' for h in H)
    print(f"OutputHash: {block_hash}")


# Final hash value after processing all blocks

final_hash = ''.join(f'{h:08x}' for h in H)
print(f"\nFinal SHA-1 Hash: {final_hash}")



# We can verify our implementation using Python's hashlib library

import hashlib

lib_hash = hashlib.sha1(message.encode('utf-8')).hexdigest()
print(f"SHA-1 Hash using hashlib: {lib_hash}")
print(f"Match: {final_hash == lib_hash}")

