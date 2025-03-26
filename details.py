def get_person_details():
    name=input("Enter your name:")
    address=input("Enter your address:")
    email=input("Enter your email:")
    phone=input("Enter your phone number:")
    return name,address,email,phone
def print_person_details(name,address,email,phone):

    print("\n-- Personal details --")
    print(f"Name:{name}")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"Phonenumber:{phone}")

name,address,email,phone= get_person_details()

print_person_details(name,address,email,phone)
