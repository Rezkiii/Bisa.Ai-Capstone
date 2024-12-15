def rot13(text):
  """Mendekripsi teks menggunakan algoritma ROT13."""
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  tr = str.maketrans(alphabet, alphabet[13:] + alphabet[:13])
  return text.translate(tr)

# Teks yang akan didekripsi
ciphertext = "pncfgbar{p0zova4gv0a_x3l}"

# Dekripsi teks
plaintext = rot13(ciphertext)

print("Teks asli:", plaintext)
