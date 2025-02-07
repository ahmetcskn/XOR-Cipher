import base64
import colorama
from colorama import Fore

class XORCipher:
    def __init__(self):
        colorama.init(autoreset=True)

    def xor_cipher(self, text, key):
        new_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
        return ''.join(chr(ord(k) ^ ord(m)) for k, m in zip(text, new_key))

    def encrypt(self, text, key):
        encrypted_text = self.xor_cipher(text, key)
        return base64.b64encode(encrypted_text.encode()).decode()

    def decrypt(self, encoded_text, key):
        try:
            decoded_text = base64.b64decode(encoded_text).decode()
            return self.xor_cipher(decoded_text, key)
        except Exception:
            return "Error: Invalid decryption input!"

    def run(self):
        while True:
            print(f"{Fore.GREEN}------ XOR Cipher ------")
            print(f"{Fore.CYAN}(1) Encrypt text.")
            print(f"{Fore.CYAN}(2) Decrypt text.")
            print(f"{Fore.RED}Type 'q' to exit.")

            choice = input(f"{Fore.CYAN}Select option: ").strip()

            if choice.lower() == 'q':
                print("Exiting...")
                break

            if choice not in ["1", "2"]:
                print("Error: Invalid Option!")
                continue

            text = input(f"{Fore.YELLOW}Text: ")
            key = input(f"{Fore.YELLOW}Key: ")

            if choice == "1":
                print(f"Encrypted text (Base64): {self.encrypt(text, key)}")

            elif choice == "2":
                print(f"Decrypted text: {self.decrypt(text, key)}")

if __name__ == "__main__":
    cipher = XORCipher()
    cipher.run()