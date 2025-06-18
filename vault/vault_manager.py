from os.path import join
import json

from crypto.utils import load_key, encrypt, decrypt

class Vault:
    def __init__(self, tp):
        # Init Key
        self.key = load_key()

        # Init Typewriter
        self.tp = tp

        # Data FP
        self.data_fp = join('data', 'data.json')
        self.data = None
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_fp, 'r') as data:
                self.data = json.load(data)
        
        except FileNotFoundError:
            self.tp.typewriter(f"File {self.data_fp} is not a valid filepath.")

    def view_passwords(self):
        names = []
        passwords = []

        for obj in self.data:
            names.append(obj['name'])
            passwords.append(obj['password'])

        data = {}

        for key, val in zip(names, passwords):
            data[key] = val

        self.tp.typewriter(data)

    def main(self):
        print(self.key)