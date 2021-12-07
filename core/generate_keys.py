from rsa import newkeys
from os import path
from os import makedirs


def main():
    if not path.exists("keys"):
        makedirs("keys")

    if path.exists("keys/private_key.txt"):
        print("A private key already exists so please do check and run again.")
        quit()

    if path.exists("keys/public_key.txt"):
        print("A public key already exists please do check and run again.")
        quit()

    publicKey, privateKey = newkeys(512)
    Private_keys_path = open("keys/private_key.txt","w")
    Private_keys_path.write(privateKey.save_pkcs1().decode('utf-8'))
    Private_keys_path.close()

    Public_keys_path = open("keys/public_key.txt","w")
    Public_keys_path.write(publicKey.save_pkcs1().decode('utf-8'))
    Public_keys_path.close()

    print("Sucessfully saved the keys to keys/n")
    print("private_key.txt for private key: Don't Share")
    print("public_key.txt for public key: Do Share")
    # print(type(publicKey))
