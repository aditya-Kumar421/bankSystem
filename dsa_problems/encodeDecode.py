
def caesar_cipher(msg, shift, encode=True):
    shift %= 26
    if not encode:
        shift = -shift
    
    result = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift + 26) % 26 + base)
        else:
            result += char
    
    if encode:
        print("Encoded message:", result)
    else:
        print("Decoded message:", result)

msg = input("Enter message: ")
shift = int(input("Enter the shift value: "))
choice = input("Encode (E) or Decode (D)? ").strip().lower()

encode = (choice == 'e')
caesar_cipher(msg, shift, encode)