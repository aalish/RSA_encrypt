from os import path
from os import makedirs
from rsa import decrypt
import rsa

from Crypto.PublicKey import RSA
def main():
    print("Enter path for private key.\nPress ENTER to use default.")
    user_input = input("Default= keys/private_key.txt\n>>>")

    if user_input == "":
        private_path = "keys/private_key.txt"
        privateKey=extract_keys()
    else:
        if not path.exists(user_input):
            print("Invalid path")
            quit()
        private_path = user_input
        privateKey=extract_keys(private_path)
    print("\nEnter located of encrypted text.\nPress ENTER for default.")
    user_input = input("Default = datas/encrypted.txt\n>>>")


    if user_input == "":
        decrypt_msg(privateKey=privateKey)
    else:

        if not path.exists(user_input):
            print("\n Path doesn't exists.")
            quit()
        decrypt_msg(file_name=user_input, privateKey=privateKey)


def extract_keys(file_name=None):
    if file_name == None:
        if not path.exists("keys"):
            makedirs("keys")
            print("\nNo folder named keys and keys named as private_key.txt found")
            error_handle()
        file_name="keys/private_key.txt"

    read_privatekey = open(file_name,"r")
    privateKey = read_privatekey.read()
    # privateKey = RSA.importKey(read_privatekey.read())
    privateKey = rsa.PrivateKey.load_pkcs1(privateKey)
    # print(type(privateKey))
    # # privateKey = pkcs1_oaep.new(privateKey)
    # print(type(privateKey))
    read_privatekey.close()
    return privateKey

def decrypt_msg(privateKey,file_name = None):
    if file_name == None:
        if not path.exists("datas"):
            makedirs("datas")
        if not path.exists("datas/encrypted.txt"):
            print("There is no encrypted data")
            quit()
        file_name="datas/encrypted.txt"
    encry = open(file_name,"rb")
    enc_data = encry.read()
    # print(type(enc_data))
    decrypted_msg = decrypt(enc_data, privateKey).decode()
    print("Decrypted Message is: \n")
    print(decrypted_msg)

    print("\nDo you want to save the file?\n ")
    user_input = input("Press 1 to save the file.")
    if user_input == "1":
        make_output_folder(msg=decrypted_msg)

def make_output_folder(msg):
    write_decrpted_data = open("datas/decrypted.txt","w+")
    write_decrpted_data.write(msg)
    write_decrpted_data.close()
    print("Sucessfully written into the file datas/decrypted.txt\n")
    print("Please verify the txt document.")
    #
    # read_decrypted_data = open("datas/decrypted.txt","r")
    # data=read_decrypted_data.read()
    # decrypted_strings = decrypt("data is this".encode(), publicKey)
    # write_encrypted_data.write(str(encrypted_strings))
    # write_encrypted_data.close()

def error_handle():
    print("For your convinence, We have created folder named keys \nPlease place private key inside the file named as private_key.txt\n ")

    quit()
