import os
import sys

def check_python_version():
    # Check if Python version is 3 or higher
    if sys.version_info < (3, 0):
        print("Python 3 or higher is required.")
        sys.exit(1)

def check_git_installed():
    # Check if Git is installed
    git_installed = os.system("which git >/dev/null 2>&1")
    if git_installed != 0:
        print("Git is not installed.")
        sys.exit(1)

def check_private_key_exists(private_key_path):
    # Check if the private key file exists
    if not os.path.isfile(private_key_path):
        print("Private key file not found.")
        sys.exit(1)

def login_and_clone(repository_url, private_key_path):
    # Set up SSH key authentication
    os.system(f"ssh-agent bash -c 'ssh-add {private_key_path}; git clone {repository_url}'")

# Replace the repository_url variable with the desired SSH link
repository_url = "git@github.com:datlaxbro/pi-nginx-html-and-php.git"
private_key_path = "/path/to/your/ssh/private/key"  # Replace with your SSH key path

check_python_version()
check_git_installed()
check_private_key_exists(private_key_path)

if len(sys.argv) > 1 and sys.argv[1] == "clone":
    login_and_clone(repository_url, private_key_path)
else:
    print("Please provide a valid command.")
    sys.exit(1)