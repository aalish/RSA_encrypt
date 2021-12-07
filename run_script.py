from core import decrypt_file as d
from core import encrypt_file as e
from core import generate_keys as g

print("This script will help you to use RSA encryption.")
print("Lets get started.")
print("If you have generated keys and used it please don't try to generate keys again.")

while 1:
    user_input = input("Select options:\n1. Generate keys\n2. Encrypt file.\n3. Decrypt file\nq for quit.\n>>>")

    if user_input == "1":
        g.main()

    elif user_input == "2":
        e.main()

    elif user_input == "3":
        d.main()

    elif user_input == "q":
        print("Thank you for using this script.")
        print("Bye Bye")

        quit()

    else:
        print("Print enter valid option.\n")
