import base64

def custom_substitution_encrypt(text):
    # Create a substitution mapping (simple example)
    substitution_map = {
        'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
        'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
        'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
        'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
        'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k',
        'z': 'l', ' ': '_'
    }
    return ''.join(substitution_map.get(char, char) for char in text)

def caesar_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def obfuscate_flag():
    # Original flag
    flag = "capstone{ehe_another_reverse_engineering}"
    
    # Step 1: Custom substitution encryption
    substituted_flag = custom_substitution_encrypt(flag)
    
    # Step 2: Caesar cipher encryption
    caesar_encrypted_flag = caesar_cipher(substituted_flag, 5)  # Shift by 5
    
    # Step 3: Base64 encode the result
    obfuscated_flag = base64.b64encode(caesar_encrypted_flag.encode()).decode()
    
    return obfuscated_flag

def reveal_flag(encoded_flag):
    # Step 1: Base64 decode
    decoded_flag = base64.b64decode(encoded_flag).decode()
    
    # Step 2: Reverse Caesar cipher
    caesar_decrypted_flag = caesar_cipher(decoded_flag, -5)  # Shift back by 5
    
    # Step 3: Reverse custom substitution
    substitution_map = {v: k for k, v in {
        'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q',
        'f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v',
        'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
        'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f',
        'u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k',
        'z': 'l', ' ': '_'
    }.items()}
    
    return ''.join(substitution_map.get(char, char) for char in caesar_decrypted_flag)

if __name__ == "__main__":
    encoded_flag = obfuscate_flag()
    print("Obfuscated Flag:", encoded_flag)
    # Uncomment the next line to reveal the flag to the user
    # print("Revealed Flag:", reveal_flag(encoded_flag))
