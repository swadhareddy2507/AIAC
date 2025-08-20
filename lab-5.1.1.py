def mask_email(email):
    """
    Masks the email address for privacy.
    Example: 'john.doe@gmail.com' -> 'j*****@gmail.com'
    """
    try:
        local, domain = email.split('@')
        if len(local) > 1:
            masked_local = local[0] + '*' * (len(local) - 1)
        else:
            masked_local = '*'  # If local part is only 1 character
        return masked_local + '@' + domain
    except Exception:
        return '*' * len(email)

def collect_user_data():
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['age'] = input("Enter your age: ")
    email = input("Enter your email: ")
    user_data['email'] = mask_email(email)  # Store masked email only
    return user_data

def main():
    data = collect_user_data()
    print("Collected Data (with protected email):", data)

    # How to further anonymize or protect personal data:
    # - Do not store raw data in plain text files.
    # - Remove or mask direct identifiers (e.g., replace name/email with pseudonyms or hashes).
    # - Encrypt sensitive fields using secure libraries (e.g., cryptography).
    # - Store data in secure, access-controlled locations.
    # - Only collect and retain data that is strictly necessary.

if __name__ == "__main__":
    main()
