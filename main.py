import secrets
import string
import re
import hashlib
import requests

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def analyze_password(password):
    score = sum([
        len(password) >= 8,
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))
    ])
    return ["Weak", "Weak", "Weak", "Moderate", "Moderate", "Strong"][score]

def is_password_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("⚠️ Error contacting HIBP API.")
            return -1
        
        for line in response.text.splitlines():
            h, count = line.split(":")
            if h == suffix:
                return int(count)
        return 0
    except requests.RequestException:
        print("⚠️ Network error checking password leak.")
        return -1

def main():
    # Generate and analyze a new password
    new_password = generate_password(16)
    print(f"\nGenerated Password: {new_password}")
    print(f"Strength: {analyze_password(new_password)}")

    # User input
    user_password = input("\nEnter a password to analyze: ").strip()
    strength = analyze_password(user_password)
    print(f"Strength: {strength}")
    
    pwned_count = is_password_pwned(user_password)
    if pwned_count > 0:
        print(f"⚠️ Found in breaches {pwned_count} times!")
    elif pwned_count == 0:
        print("✅ This password was not found in known breaches.")
    # No message if pwned_count == -1 due to error

if __name__ == "__main__":
    main()
