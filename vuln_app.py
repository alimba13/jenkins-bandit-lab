# vuln_app.py
import subprocess

def dangerous_function(user_input):
    # Vuln: injection de commande possible
    subprocess.call("ls " + user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Enter directory to list: ")
    dangerous_function(user_input)
