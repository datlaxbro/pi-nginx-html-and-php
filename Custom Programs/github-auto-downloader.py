import os
import sys

def login_and_clone(repository_url):
    # Set up SSH key authentication
    ssh_key_path = "/path/to/your/ssh/private/key"  # Replace with your SSH key path
    os.system(f"ssh-agent bash -c 'ssh-add {ssh_key_path}; git clone {repository_url}'")

def check_for_updates(repository_url):
    # Set up SSH key authentication
    ssh_key_path = "/path/to/your/ssh/private/key"  # Replace with your SSH key path
    os.system(f"ssh-agent bash -c 'ssh-add {ssh_key_path}; git pull'")

# Replace the repository_url variable with the desired SSH link
repository_url = "git@github.com:datlaxbro/pi-nginx-html-and-php.git"

if len(sys.argv) > 1 and sys.argv[1] == "clone":
    login_and_clone(repository_url)
else:
    check_for_updates(repository_url)