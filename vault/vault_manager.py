from os.path import join
import json

from crypto.utils import load_key, encrypt, decrypt

class Vault:
    def __init__(self, tp):
        # Init Key
        self.key = load_key()

        # Init Typewriter
        self.tp = tp

        # Master Password
        self.master_password = ''
        self.master_password_accepted = False

        # Data FP
        self.data_fp = join('data', 'data.json')
        self.data = None

        # Accounts FP
        self.account_fp = join('data', 'accounts.json')
        self.accounts = None

        # Load data
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_fp, 'r') as data:
                self.data = json.load(data)
        
        except FileNotFoundError:
            self.tp.typewriter(f"File {self.data_fp} is not a valid filepath.")
        
        try:
            with open(self.data_fp, 'r') as data:
                self.accounts = json.load(data)
        
        except FileNotFoundError:
            self.tp.typewriter(f"File {self.account_fp} is not a valid filepath.")

    def view_current_accounts(self):
        users = [entry['name'] for entry in self.accounts]

        if len(users) == 0:
            self.tp.typewriter("There are no accounts set. Go make one!")
            return
        
        for i, user in enumerate(users, 1):
            self.tp.typewriter(f"{i}. {user}")

    def add_new_accounts(self):
        pass

    def accept_master_password(self):
        max_tries = 5
        while max_tries != 0:
            max_tries -= 1
        
        self.master_password_accepted = True

    def view_passwords(self):
        self.accept_master_password()
        if self.master_password_accepted:
            data = {entry['name']: entry['password'] for entry in self.data}
            print(data)

    def main(self):
        self.accept_master_password()
        if self.master_password_accepted:
            running = True
            while running:
                pass