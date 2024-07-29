import random
import string

def generate_password(length):
     
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

   
    all_characters = lower + upper + digits + symbols

     
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

def main():
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

     
    password = generate_password(length)

     
    print("Generated password:", password)

if __name__ == "__main__":
    main()
