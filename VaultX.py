import os
import cmd
import sys
import shutil
from cryptography.fernet import Fernet

class VaultXShell(cmd.Cmd):
    """
    VaultX v3.0: High-Performance Secure File Manager.
    Includes Navigation, Encryption, and File Management.
    """
    
    intro = "="*60 + "\n  Welcome to VaultX - Enterprise Edition (v3.0)\n" + "="*60
    
    def __init__(self) -> None:
        super().__init__()
        self.key_file = "secret.key"
        self.load_or_create_key()
        self.update_prompt()

    def load_or_create_key(self) -> None:
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as kf:
                kf.write(key)
        with open(self.key_file, "rb") as kf:
            self.cipher = Fernet(kf.read())

    def update_prompt(self) -> None:
        self.prompt = f"\n[VaultX @ {os.getcwd()}] > "

    def precmd(self, line: str) -> str:
        self.update_prompt()
        return line

    # --- BASIC COMMANDS ---
    def do_ls(self, arg: str) -> None:
        """Folder ki saari files dikhayega."""
        items = os.listdir(os.getcwd())
        print(f"Items in current directory ({len(items)}):")
        for item in items:
            prefix = "DIR" if os.path.isdir(item) else "FILE"
            print(f"  [{prefix}] |-- {item}")

    def do_pwd(self, arg: str) -> None:
        """Current rasta dikhayega."""
        print(f"Current Path: {os.getcwd()}")

    def do_cd(self, path: str) -> None:
        """Folder change karein. Usage: cd folder_name ya cd .."""
        try:
            os.chdir(path)
            print(f"Directory changed to: {os.getcwd()}")
        except Exception as e:
            print(f"Error: {e}")

    # --- FILE MANAGEMENT ---
    def do_mkdir(self, name: str) -> None:
        """Naya folder banayein. Usage: mkdir my_folder"""
        try:
            os.mkdir(name)
            print(f"Success: Folder '{name}' ban gaya hai.")
        except FileExistsError:
            print(f"Error: Folder '{name}' pehle se maujood hai.")

    def do_rename(self, arg: str) -> None:
        """Naam badlein. Usage: rename purana.txt naya.txt"""
        try:
            old, new = arg.split()
            os.rename(old, new)
            print(f"Success: '{old}' ka naam badal kar '{new}' kar diya gaya.")
        except ValueError:
            print("Error: Usage 'rename <old_name> <new_name>'")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete(self, filename: str) -> None:
        """File delete karein. Usage: delete test.txt"""
        try:
            os.remove(filename)
            print(f"Success: File '{filename}' delete ho gayi.")
        except Exception as e:
            print(f"Error: {e}")

    # --- ENCRYPTION (VAULT FEATURES) ---
    def do_lock(self, filename: str) -> None:
        """File ko password-less encryption se secure karein."""
        if not os.path.exists(filename):
            print("Error: File nahi mili.")
            return
        with open(filename, "rb") as f:
            data = f.read()
        encrypted_data = self.cipher.encrypt(data)
        with open(filename, "wb") as f:
            f.write(encrypted_data)
        print(f"LOCKED: '{filename}' ab secure hai.")

    def do_unlock(self, filename: str) -> None:
        """Encrypted file ko wapas normal karein."""
        try:
            with open(filename, "rb") as f:
                data = f.read()
            decrypted_data = self.cipher.decrypt(data)
            with open(filename, "wb") as f:
                f.write(decrypted_data)
            print(f"UNLOCKED: '{filename}' normal ho gayi.")
        except Exception as e:
            print(f"Error: Unlock nahi ho paya. {e}")

    def do_exit(self, arg: str) -> bool:
        print("Exiting VaultX. Goodbye!")
        return True

if __name__ == '__main__':
    VaultXShell().cmdloop()