# XTS-AES-Cryptography
Basic Cryptography Cipher utilizing XTS-AES algorithms 

XTS builds on top of XEX designed by Phillip Rogaway and extends this by a tweak value and ciphertext stealing. The mode defined by IEEE uses an AES cipher, 
in fact AES is used twice. Simplified (without i and alpha), the tweak value is encrypted, then XORed with the plaintext block.
