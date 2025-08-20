# Python script to collect user data

def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    user_data['email'] = input("Enter your email: ")
    return user_data

def main():
    data = collect_user_data()
    print("Collected Data:", data)

    # To anonymize or protect this data:
    # - Do not store raw data in plain text files.
    # - Hash or encrypt sensitive fields (e.g., use hashlib or cryptography libraries).
    # - Remove or mask direct identifiers (e.g., replace name/email with pseudonyms or hashes).
    # - Store data in secure, access-controlled locations.
    # - Only collect and retain data that is strictly necessary.

if __name__ == "__main__":
    main()
