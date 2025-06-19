from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)       
        f.write(ct_bytes)
    
    print(f"Encrypted image saved as {output_file}")

def decrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)         
        ct = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ct), AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(data)
    
    print(f"Decrypted image saved as {output_file}")

if __name__ == "__main__":
    key = b'This_is_a_16byte'  

    input_image = r"C:\Users\ghrib\Desktop\ProdigyInfoTech Tasks\Prodigy_cs_02\dog.jpg"
    encrypted_image = 'dog_encrypted.aes'
    decrypted_image = 'dog_decrypted.jpg'

    # Encrypt
    encrypt_image(input_image, encrypted_image, key)

    # Decrypt
    decrypt_image(encrypted_image, decrypted_image, key)
