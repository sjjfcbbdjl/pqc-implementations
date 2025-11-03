# Post Quantum Cryptography (PQC) Implementation

Welcome to this repository where various **PQC** algorithms are implemented. This mainly focuses on exploring and experimenting with crypto schemes that are thought to be secure against future quantum computers.

# Overview

As quantum computing advances, the existing implemented classical crypto schemes face threats due to their vulnerability to quantum algorithms like Shor's. In this repo, we give detailed implementation of various **pqc algos** under different categories, including:

- **Lattice based Cryptography:**

  It's security is based on the hardness of mathematical problems on high dimensional lattices. There are mainly two classes:

  1. Learning with errors (LWE): goal is to find a secret key vector s from a series of noisy linear equations.
  2. Short integer solution (SIS): goal is to find a set of small integers that solve a particular matrix equation.

  There are two standards published by NIST which are based on the lattice based cryptography:

  1. Key encapsulation mechanism (KEM): It is a way to establish a shared secret between two parties, which can then be used for symmetric encryption. There are two schemes:
    
     (i).   CRYSTALS-Kyber **(ML-KEM)**: To be used for general purpose public key encryption and key establishment. It is intended to replace ECDH. It is based on the Module                   learning with errors (MLWE) problem. Primary Standard.
     (ii).  NTRU: Also a KEM. Not selected as primary standard but have very high performance. It is based on the NTRU assumption, which is related to findind a specific type of                lattice.

  2. Digial signature algos: Used to verify the authencity and integrity of a message. It replaces RSA and ECDSA. There are two schemes:
 
     (i).    CRYSTALS-Dilithium **(ML-DSA)**: For digital signatures. Based on the MLWE and Module short integer solution (MSIS) problems.
     (ii).   Falcon: A secondary digital signature algorithm. It produces a very small signatur (much smalled than DSA). Useful where storage or bandwidth is highly constrained,                 such as IoT decies, blockchain. It is based on the SIS problem over NTRU lattices. But the process of generating keys and signing is more complex (than in ML-DSA).

- **Hash-Based Cryptography :**

  Secure hash algorithms (SHA) are based on hash functions. The hash of a message is easy to compute but it is almost impossible to find the original message given the hash. Its      security is based on cryptographic hash functions.
  There are mainly three families of SHA: SHA-1, SHA-2, and SHA-3. A collision was found in SHA-1, hence it is unsecure and broken, so no in use today.

  SHA-2 variants: SHA-256, SHA-512, SHA-224, SHA-384, SHA-512/224, SHA-512/256

  SHA-3 variants: SHA3-224, SHA3-256, SHA3-384, SHA3-512.

  SHA variants differ in terms of maximum message size, hash size, block size and number of rounds.

  Now, the SHA itself is not a post quantum cryptographic algo but is part of the hashing algo used in some post quantum signature schemes standardized or considered by NIST.
  The hash based cryptography is primarily used for digital signatures. 
  How does it work, the hash based cryptography? These are buuilt by combining two simpler concepts:

  (i).   One time signatures (OTS): A scheme where we can generate a private and a public key. The catch is we can use this key paor to sign one single message.
  (ii).  Merkle trees : It is a way to combine thousands or millions of public keys into one single master public key. We line up all our one time public keys as leaves of a tree            and then hash them in pairs. We take the resulting hash ans hash them in pairs and do it until one is left with one single hash value at top.

  Schemes : (a). Key generation: We generate, for example, one million OTS key pairs and their corresponding one million public keys, then use Merkle tree to create a master public                  key and share it with the world.
            (b). Signing: To sign the first message, use the first OTS private key. The sign consists of the one time signature itself and the authentication path.
            (c). Verification: Verifier takes the OTS, the message and the authentication path. They use the path to recalculate the master public key. If it matches, the sign is                    valid. For second message, we use the second OTS private key and so on.

  There are two types of schemes, one is stateful in which we have to keep track of which OTS key we've used, in order to prevent attack.
  And the other is stateless, which cleverly uses the message being signed to clevery deterministically select which of the million OTS keys to use. Makes it bit slower and larger    but solves the stateful problem and makes it safe for everyday use.

  The NIST standard **SPHINCS+ (SLH-DSA)** is based on stateless hash based cryptography. SPHINCS+ is complement to the primary standard CRYSTALS-Dilithium. 
  

   
  

- **Code Based Cryptography:**



## Features

- Detailed implementations of leading PQC algorithms.


## Implemented Algorithms

| Category              | Algorithms                                | Description                              |
|-----------------------|-------------------------------------------|------------------------------------------|
| Hash-Based            | XMSS, SPHINCS+                            | Stateless and stateful hash-based signatures |
| Lattice-Based         | NTRUEncrypt, Kyber, Dilithium             | Encryption and signature schemes based on lattice hardness |




**Contributions are welcome!**


