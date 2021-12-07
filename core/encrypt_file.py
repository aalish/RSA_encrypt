from os import path
from os import makedirs
from rsa import encrypt
import rsa
#from Crypto.PublicKey.RSA import importKey

def main():
    print("\nEnter full path for public key. Press Enter key if you want to use default\n")
    user_input=input("\nDefault = keys/public_key.txt\n>>>")
    if user_input =="":
        publicKey=get_keys()
    else:
        publicKey=get_keys(user_input)

    print("\n\nDo you want to manually type the string or pass a file?")
    user_input = input("\nPress 1 for manual type. \nPress 2 for reading a file.\n>>>")
    if user_input == "1":
        strings = input("\nEnter strings:\n>>>")
        encrypt_file(strings=strings, keys=publicKey)

    elif user_input == "2":
        path = input("\nEnter path to the file\n>>>")
        if not path.exists(path):
            print("\nWrong Path")
            quit()
        strings = read_file(path)
        encrypt_file(strings=strings, keys=publicKey)
    else:
        print("\nWrong Option")
        quit()

def encrypt_file(strings,keys):
    # print(type(publicKey))


    encrypted_strings = encrypt(strings.encode(), keys)
    print("\nEncrypted form of the string is:")
    print(encrypted_strings)
    user_input = input("\nDo you want to save it as a file?\nPress y for yes\n>>>")
    if user_input == "y":
        write_file(encrypted_strings)


def write_file(encrypted_strings):
    if not path.exists("datas"):
        makedirs("datas")
    write_encrypted_data = open("datas/encrypted.txt","wb+")
    write_encrypted_data.write(encrypted_strings)
    write_encrypted_data.close()
    print("\nSucessfully writted into file datas/encrypted.txt\n")

def  get_keys(keys_path=None):
    if keys_path:
        if not path.exists(keys_path):
            print("Invalid key path.\n Please try again.")
            quit()
        key_path=keys_path
    else:
        if not path.exists("keys"):
            makedirs("keys")
            print("\nNo folder named keys and keys named as public_key.txt found")
            error_handle()
        key_path = "keys/public_key.txt"
    # try:
    read_publickey = open(key_path,"r")
#    publicKey = RSA.importKey(read_publickey.read())
    publicKey = read_publickey.read()
    publicKey = rsa.PublicKey.load_pkcs1(publicKey)
    read_publickey.close()
    return publicKey

def read_file(file_path):
    file_handle = open(file_path,"r")
    data = file_handle.read()
    return data

    # except:
    #     error_handle()

def error_handle():
    print("\nFor your convinence, We have created folder named keys \nPlease place pubic key inside the file named as public_key.txt\n ")
    quit()
