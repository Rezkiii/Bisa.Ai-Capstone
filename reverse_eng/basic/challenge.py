def obfuscate_flag(flag):
    key = 42  # Simple XOR key
    obfuscated = ''.join(chr(ord(c) ^ key) for c in flag)
    return obfuscated

def main():
    flag = "capstone{reverse_engineering_basic}"
    obfuscated_flag = obfuscate_flag(flag)
    print("Obfuscated Flag:", obfuscated_flag)

if __name__ == "__main__":
    main()
