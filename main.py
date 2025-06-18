from VividText import VividText as vt

from utils.helpers import cc
from vault.vault_manager import Vault

class Main:
    def __init__(self):
        # Init Main loop running
        self.running = True
    
        # Init vt
        self.tp = vt(bold=True, sleep=.03)

        # Menu options
        self.options = ["Vault", "Settings", "Exit"]

        # Password Vault
        self.vault = Vault(self.tp)

    def test(self):
        self.vault.view_passwords()

    # Main Loop
    def main(self):
        self.tp.typewriter("-------------------- Password Manager --------------------")
        while self.running:
            self.tp.menuTypewriter(" | ", self.options)
            option = self.tp.inputTypewriter("Select an option").strip().title()

            if option == '1' or option.startswith("Vau") or option == "Vault":
                pass

            elif option == '2' or option.startswith("Set") or option == "Settings":
                pass
        
            elif option == '3' or option.startswith("Ex") or option == "Exit":
                self.running = False
                cc()
                continue
            
            else:
                self.tp.typewriter(f"{option} is not a valid option.")
            
            self.tp.inputTypewriter("Press Enter To Continue.", end='')
            cc()
    
if __name__ == "__main__":
    main = Main()
    main.test()