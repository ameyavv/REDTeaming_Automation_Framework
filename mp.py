
import subprocess
import time
import os
import socket

def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't have to be reachable)
        s.connect(('8.8.8.8', 80))
        # Get the local IP address
        ip_address = s.getsockname()[0]
    except Exception as e:
        print("Error:", e)
        ip_address = "Unable to retrieve IP address"
    finally:
        # Close the socket
        s.close()

    return ip_address

# Get the IP address
ip_address = get_ip_address()
print("Your IP address is:", ip_address)

def pspy(commands7):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """

    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands7)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands7 = ["sudo pspy --debug"]

def netcat(commands5):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """

    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands5)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands5 = ["sudo nc -lvnp 87 -s " + ip_address]

def new_terminal(commands3):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """
    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands3)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands3 = ["sudo hping3"]

def bettercap(commands):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """
    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands = ["sudo bettercap"]


def install_sqlmap():
    try:
        # Execute shell commands to update and install SQLMap
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "sqlmap"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing SQLMap:", e)

def run_sqlmap(url):
    try:
        # Execute SQLMap command using subprocess
        subprocess.run(["sqlmap", "-u", url], check=True)
    except FileNotFoundError:
        print("SQLMap is not installed. Installing...")
        install_sqlmap()
        print("SQLMap installed successfully. Running...")
        run_sqlmap(url)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running SQLMap:", e)



def LinuxES(commands1):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """
    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands1)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands1 = ["./Linux-Exploit-Suggester.sh"]


def LSE(commands2):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """
    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands2)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands2 = ["./lse.sh"]





def install_dirb():
    try:
        # Execute shell script to install Dirb
        subprocess.run(["bash", "install_dirb.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing Dirb:", e)

def run_dirb():
    try:
        # Prompt the user for the URL
        url = input("Enter the URL to scan with Dirb: ")

        # Execute Dirb command using subprocess
        subprocess.run(["dirb", url], check=True)
    except FileNotFoundError:
        print("Dirb is not installed. Installing...")
        install_dirb()
        print("Dirb installed successfully. Running...")
        run_dirb()
    except Exception as e:
        # Handle any other errors
        print("Error running Dirb:", e)




while(True):
      print("1. SQL Injection\n2. OSINT\n3. Web Vulnerability Scanning\n4. Network Sniffing\n5. network protocol manipulation\n6. Web Directory Sniffer\n7. online account finder\n8. System Scanning\n9. System Scanning2\n10. Web Scanning\n11. Enumeration \n12. Detecting Vulnerable Exploits\n13. Unix\n14. Remote Access a Device\n15. Hping\n16. Nmap\n17. NetCat\n18. Dirsearch\n19. Exit")
      print("Please enter the number of the activity that you wish to do from the above: ")
      choice = int(input())
      if choice == 1:
              url = input("Enter the URL to be scanned with sqlmap: ")
              print("Running SQLMap...")
              run_sqlmap(url)

      elif choice == 2:
            #print("Choose from the following tools:\n1. Spiderfoot(default)\n2. theHarvester")
            '''Tool = int(input())
            if Tool == 1:
                      print("Running Spiderfoot")
                      command = "x-terminal-emulator"
                      subprocess.Popen(command)
            elif Tool == 2:'''
            print("Running theHarvester")
            cm01 = ["python3", "theHarvester.py"]
            command = str(input("Please enter the specifications you want: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))

            cm03 = cm01 + cm02

            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/theHarvester"))
            subprocess.call(cm03 , cwd=dpath)

      elif choice == 3:
            print("Running Accutenix")

      elif choice == 4:
            print("Running Bettercap")
            new_terminal(commands)

      elif choice == 5:
            print("Running impacket")
            cm01 = ["smbclient"]
            command = str(input("Please enter the specifications you want: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))
            cm03 = cm01 + cm02
            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/impacket"))
            subprocess.call(cm03 , cwd=dpath)

      elif choice == 6:
            print("Running Dirb")
            run_dirb()

      elif choice == 7:
            print("Running Sherlock")
            uname = str(input("Please enter the username you want to search: \n\n\n"))
            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/sherlock/sherlock"))
            subprocess.call(["python3", "sherlock.py", uname], cwd= dpath)

      elif choice == 8:
            print("Running LinPEAS")
            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/REDTeaming_Automation_Framework"))
            subprocess.call(["./linpeas.sh"], cwd= dpath)

      elif choice == 9:
            print("Running LinEnum")
            #command = "x-terminal-emulator"
            #subprocess.Popen(command)
            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/REDTeaming_Automation_Framework/LinEnum"))
            subprocess.call(["./LinEnum.sh"], cwd= dpath)

      elif choice == 10:
            print("Running Nikto")
            cm01 = ["nikto"]
            command = str(input("Please enter the specifications you want: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))
            cm03 = cm01 + cm02
            subprocess.call(cm03)

      elif choice == 11:
            print("Running Linux Smart Enumeration")
            LSE(commands2)

      elif choice == 12:
            print("Running Linux Exploit Suggester")
            LinuxES(commands1)

      elif choice == 13:
            print("Running Unix Privesc Check")
            cm01 = ["unix-privesc-check"]
            command = str(input("Please enter the specifications you want{ standard | detailed } with IP address: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))
            cm03 = cm01 + cm02
            subprocess.call(cm03)

      elif choice == 14:
            print("Running Metasploit")

      elif choice == 15:
            print("Running Hping")
            new_terminal(commands3)

      elif choice == 16:
            print("Running Nmap")
            cm01 = ["nmap"]
            command = str(input("Please enter the specifications you want: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))
            cm03 = cm01 + cm02
            subprocess.call(cm03)

      elif choice == 17:
            print("Running NetCat")
            netcat(commands5)

      elif choice == 18:
            print("Running Dirsearch")
            cm01 = ["python3", "dirsearch.py"]
            command = str(input("Please enter the specifications you want: "))
            print("\n\n\n")
            cm02 = list(command.split(" "))

            cm03 = cm01 + cm02

            dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/dirsearch"))
            subprocess.call(cm03 , cwd=dpath)
          
      elif choice ==19:
          print("Running Pspy")
          pspy(commands7)
          
      elif choice == 20 :
            print("Thank you for using our program!!")
            break
      else:
          print("Invalid input")


