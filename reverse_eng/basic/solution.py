def deobfuscate_flag(obfuscated):
    key = 42  # Same XOR key
    deobfuscated = ''.join(chr(ord(c) ^ key) for c in obfuscated)
    return deobfuscated

if __name__ == "__main__":
    obfuscated_flag = "F#\x02\"IKZY^EDOQXO\OXYOuODMCDOOXCDMuHKYCIW"  # Example output from challenge.py
    original_flag = deobfuscate_flag(obfuscated_flag)
    print("Original Flag:", original_flag)
