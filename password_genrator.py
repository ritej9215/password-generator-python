import secrets
import string 

def password1(length):
    if length < 2:
        return "Error: Password must be at least two characters long."
    
    char = string.ascii_letters + string.punctuation + string.digits
    return ''.join(secrets.choice(char) for _ in range(length))

# --- LOOPED INPUT SECTION ---
print("--- Secure Password Generator ---")

while True:
    try:
        user_input = input("\nEnter password length (or type 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break  # Exits the loop
            
        user_length = int(user_input)
        password = password1(user_length)
        print(f"Generated password: {password}")
        
    except ValueError:
        print("Invalid input! Please enter a whole number.")
