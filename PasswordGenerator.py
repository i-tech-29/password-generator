import hashlib

def generate_password(master_key, device_ip):
    # Concatenate master key and device ip
    combined_info = master_key + device_ip
    
    # Hash the combined information using SHA-256
    hashed_info = hashlib.sha256(combined_info.encode()).hexdigest()
    
    # Return the first 12 characters of the hashed value as the password
    return hashed_info[:12]

def main():
    # Get master key and user information from the user
    master_key = input("Enter your master key: ")
    device_ip = input("Enter your device's/server's IP: ")
    
    # Generate and print the password
    password = generate_password(master_key, device_ip)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
