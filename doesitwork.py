# from primeme import RandomRSAPrimeNumber
import primeme
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def CreateABadKey():
    #get 10 sequential prime numbers, starting with a random number
    sequential_primes = primeme.SequentialRSAPrimeNumbers(1024, 5)
    #so now that we have prime how to get a key pair from it?
    p = sequential_primes[0]["prime_number"]
    q = sequential_primes[1]["prime_number"]
    n = p * q
    e = 65537
    d = primeme.Private_d(e, p, q)

    something = RSA.construct((n,e,d,p,q))
    print("Private Key:")
    print(something.export_key('PEM').decode())
    with open("priv_key", 'w') as fh:
        fh.write(something.export_key('PEM').decode())

    print("Public Key")
    print(something.public_key().exportKey('PEM').decode())
    with open("pub_key", 'w') as fh:
        fh.write(something.public_key().exportKey('PEM').decode())

def EncryptAMessage():
    # encrypt a message with the public key
    with open("pub_key", "r") as fh:
        key = fh.read()

    rsakey = RSA.import_key(key)
    plaintext = "The quick brown fox jumped over the lazy dog".encode("UTF-8")
    encryptor = PKCS1_OAEP.new(rsakey.publickey())
    encrypted = encryptor.encrypt(plaintext)

    with open("cipher_text", "w") as fh:
        fh.write(binascii.hexlify(encrypted).decode())
    print(f"cipher text written to cipher_text:\n{binascii.hexlify(encrypted).decode()}")

def DecryptAMessage():
    # decrypt the message with the private key
    with open("priv_key", "r") as fh:
        private = fh.read()
    rsakey = RSA.import_key(private)
    decryptor = PKCS1_OAEP.new(rsakey)
    with open("cipher_text", "r") as fh:
        cipher_text = fh.read()
    cipher_binhex = binascii.unhexlify(cipher_text)

    decrypted = decryptor.decrypt(cipher_binhex)
    print(f"deciphered text:\n{decrypted.decode()}")

# get a single prime number (at random)
# results = primeme.RandomRSAPrimeNumber(1024)

# CreateABadKey()
# EncryptAMessage()
# DecryptAMessage()



print('hold up')

