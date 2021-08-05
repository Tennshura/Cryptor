from tkinter import *
import Encryptor as Enc
import Decryptor as Dec

root = Tk()
root.title("Seeded Encryptor/Decryptor")
root.geometry("650x500")


def encrypt_data():
    output_text.delete(1.0, END)
    enc_seed = ent_seed.get()
    enc_data = text_enc.get("1.0", "end-1c")
    encrypt = Enc.SeededEncryptor(enc_seed, enc_data)
    enc_output = encrypt.run_encryption()
    output_text.insert(1.0, enc_output)


def decrypt_data():
    output_text.delete(1.0, END)
    dec_seed = ent_seed.get()
    dec_data = text_dec.get("1.0", "end-1c")
    decrypt = Dec.SeededDecryptor(dec_seed, dec_data)
    dec_output = decrypt.run_decryption()
    output_text.insert(1.0, dec_output)


# creating widgets

frame_titlebar = Frame(root, bg="#003249")
frame_encrypt = Frame(root, bg="#007ea7")
frame_decrypt = Frame(root, bg="#80ced7")
frame_output = Frame(root, bg="#003249")
label_title = Label(
    frame_titlebar,
    text="Seeded Encryptor/Decryptor",
    bg="#003249",
    fg="#ffffff",
    font=("Times", "18", "bold italic"),
)
label_enc_text = Label(
    frame_encrypt, text="Data to encrypt:", bg="#007ea7", font=("Times", "14")
)
label_dec_text = Label(
    frame_decrypt, text="Data to decrypt:", bg="#80ced7", font=("Times", "14")
)
ent_seed = Entry(frame_titlebar, width=50, borderwidth=3, justify="center")
text_enc = Text(frame_encrypt, width=20, height=5)
text_dec = Text(frame_decrypt, width=20, height=5)
button_enc = Button(
    frame_encrypt, text="Encrypt!", padx=20, pady=10, command=encrypt_data
)
button_dec = Button(
    frame_decrypt, text="Decrypt!", padx=20, pady=10, command=decrypt_data
)
label_output = Label(
    frame_output,
    text="Output Data:",
    bg="#003249",
    fg="white",
    font=("Times", "18", "bold italic"),
)
output_text = Text(frame_output, width=70, height=20)


# putting them onto the screen

frame_titlebar.place(relwidth=1, relheight=0.15)
frame_encrypt.place(relwidth=0.5, relheight=0.55, rely=0.15)
frame_decrypt.place(relwidth=0.5, relheight=0.55, rely=0.15, relx=0.5)
frame_output.place(relwidth=1, relheight=0.30, rely=0.70)
label_title.pack(anchor="n", pady=3)
ent_seed.pack(anchor="n", pady=3)
ent_seed.insert(0, "Type seed here")
label_enc_text.pack(anchor="n", pady=10)
text_enc.pack(anchor="n", fill="both", pady=10, padx=10, expand="yes")
button_enc.pack(anchor="n", side="bottom", pady=10)
label_dec_text.pack(anchor="n", pady=10)
text_dec.pack(anchor="n", fill="both", pady=10, padx=10, expand="yes")
button_dec.pack(anchor="n", side="bottom", pady=10)
label_output.pack(anchor="n", pady=5)
output_text.pack(anchor="s", fill="both", padx=10, pady=10)


# creating an event loop

if __name__ == "__main__":
    root.mainloop()
