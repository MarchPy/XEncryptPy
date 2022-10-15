import os
import shutil
import threading
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet


class Core:
    def __init__(self, open_dialog) -> None:
        if open_dialog is True:
            self.path = filedialog.askopenfilename()
        elif open_dialog is False:
            pass

    @staticmethod
    def encrypt_file(path_file):
        def start_encryption():
            # Usando chave
            # <--------------------------------------------------------------->
            fernet = Fernet(key_gen)
            with open(path_mod1, "rb") as file:
                data_origem = file.read()
            # <--------------------------------------------------------------->

            # Encriptar arquivo
            # <--------------------------------------------------------------->
            encrypted = fernet.encrypt(data_origem)
            with open(path_mod1, "wb") as file:
                file.write(encrypted)
            # <--------------------------------------------------------------->

        path_mod1 = path_file.replace(" ", "_")
        path_mod2 = path_mod1.replace("/", " ")
        os.rename(path_file, path_mod1)
        folder = "Keys"

        try:
            os.mkdir(folder)
        except FileExistsError:
            pass

        # Criando chave privada e salvando
        # <--------------------------------------------------------------->
        key_gen = Fernet.generate_key()
        name = f"KeyFile [{path_mod2.split()[-1]}].key"
        with open(name, "wb") as file_key:
            file_key.write(key_gen)
            messagebox.showinfo("Chave", f"Chave criada para o arquivo {path_file}")
        try:
            shutil.move(name, folder)
            messagebox.showwarning("Atenção", "Arquivo Key movido para pasta /Keys.")
        except Exception as e:
            if "already exists" in e.__str__():
                messagebox.showwarning("Erro", "Arquivo key existente na pasta Keys, o arquivo foi salvo na pasta raiz do programa.")
            else:
                messagebox.showerror("Erro", e.__str__())
        # <--------------------------------------------------------------->

        # Executando uma thread
        messagebox.showinfo("", "Começando a encriptar.")
        thrd = threading.Thread(target=start_encryption)
        thrd.start()

    @staticmethod
    def decrypt_file(path_file, private_key):
        try:
            # Abrindo o arquvo key
            # <---------------------------------->
            with open(private_key, "rb") as key_file:
                key = key_file.read()
            # <---------------------------------->

            # Lendo o arquivo encriptado
            # <---------------------------------->
            fernet = Fernet(key)
            with open(path_file, "rb") as file:
                file_encrypted = file.read()
            # <---------------------------------->

            # Descriptando
            # <---------------------------------->
            decrypted = fernet.decrypt(file_encrypted)
            with open(path_file, "wb") as file:
                file.write(decrypted)
                messagebox.showinfo("Sucesso", "Arquivo Desencriptado.")
            # <---------------------------------->

        except Exception:
            messagebox.showerror("Erro", "Private Key ou caminho invalido.")

    def return_path(self):
        return self.path
