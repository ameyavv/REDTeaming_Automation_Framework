import subprocess
import time
import os
"""def install_bettercap():
    try:
        # Execute shell script to install Bettercap
        subprocess.run(["bash", "Bettercap.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing Bettercap:", e)"""
       


def new_terminal(commands):
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


"""def run_bettercap():
    try:
        # Execute Bettercap command using subprocess
        subprocess.run(["Bettercap"], check=True)
    except FileNotFoundError:
        print("Bettercap is not installed. Installing...")
        install_bettercap()
        print("Bettercap installed successfully. Running...")
        run_bettercap()
        new_terminal(commands)
    except Exception as e:
        # Handle any other errors
        print("Error running Bettercap:", e)"""


def install_sherlock():
    try:
        # Execute shell script to install Sherlock
        subprocess.run(["bash", "Sherlock.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing Sherlock:", e)

def run_sherlock():
    try:
        # Execute Sherlock command using subprocess
        subprocess.run(["python3", "sherlock/sherlock.py"], check=True)
    except FileNotFoundError:
        print("Sherlock is not installed. Installing...")
        install_sherlock()
        print("Sherlock installed successfully. Running...")
        run_sherlock()
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running Sherlock:", e)

"""def install_theharvester():
    try:
        # Execute shell script to install TheHarvester
        subprocess.run(["bash", "theHarvester.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing TheHarvester:", e)"""

"""def run_theharvester():
    try:
        # Execute TheHarvester command using subprocess
        subprocess.run(["theharvester", "-d", "example.com", "-l", "100", "-b", "google"], check=True)
    except FileNotFoundError:
        print("TheHarvester is not installed. Installing...")
        subprocess.run(["bash", "theHarvester.sh"], check=True)
        print("TheHarvester installed successfully. Running...")
        subprocess.run(["theharvester", "-d", "example.com", "-l", "100", "-b", "google"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running TheHarvester:", e)"""


def install_theharvester():
    try:
        # Execute shell script to install TheHarvester
        subprocess.run(["bash", "theHarvester.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing TheHarvester:", e)

def find_theharvester_executable(installation_dir):
    # Search for TheHarvester executable within the installation directory
    for root, dirs, files in os.walk(installation_dir):
        for file in files:
            if file == "theharvester":
                return os.path.join(root, file)
    return None

def run_theharvester():
    try:
        # Check if TheHarvester is installed
        result = subprocess.run(["which", "theHarvester"], stdout=subprocess.PIPE)
        if result.returncode != 0:
            print("TheHarvester is not installed. Installing...")
            install_theharvester()
            print("TheHarvester installed successfully.")

        # Find TheHarvester executable
        theharvester_executable = find_theharvester_executable("/path/to/theharvester/installation/dir")
        if theharvester_executable:
            # Execute TheHarvester command using subprocess
            subprocess.run([theharvester_executable, "-d", "example.com", "-l", "100", "-b", "google"], check=True)
        else:
            print("Error: TheHarvester executable not found.")
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running TheHarvester:", e)


def install_linuxexploitsuggester():
    try:
        # Execute shell script to install Linux Exploit Suggester
        subprocess.run(["bash", "exploitsuggester.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing exploiting suggester:", e)
def run_linuxexploitsuggester():
    try:
        # Execute Linux Exploit Suggester command using subprocess
        subprocess.run(["Linux exploit suggester"], check=True)
    except FileNotFoundError:
        print("Linux Exploit Suggester is not installed. Installing...")
        install_()
        print("Linux Exploit suggester installed successfully. Running...")
        run_bettercap()
    except Exception as e:
        # Handle any other errors
        print("Error running exploit suggester :", e)


def is_nmap_installed():
    try:
        # Execute Nmap command using subprocess to check if it's installed
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def install_nmap():
    try:
        # Execute shell script to install Nmap
        subprocess.run(["bash", "install_nmap.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing Nmap:", e)

def run_nmap():
    if is_nmap_installed():
        try:
            # Execute Nmap command using subprocess
            subprocess.run(["nmap", "--version"], check=True)
        except subprocess.CalledProcessError as e:
            # Handle any errors
            print("Error running Nmap:", e)
    else:
        print("Nmap is not installed. Installing...")
        install_nmap()
        if is_nmap_installed():
            print("Nmap installed successfully. Running...")
            try:
                # Attempt to run Nmap again
                subprocess.run(["nmap", "--version"], check=True)
            except subprocess.CalledProcessError as e:
                # Handle any errors
                print("Error running Nmap:", e)
        else:
            print("Nmap installation failed.")


import subprocess

def install_sqlmap():
    try:
        # Execute shell script to install SQLMap
        subprocess.run(["bash", "sql.sh"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error installing SQLMap:", e)

def run_sqlmap(sqlmap_options):
    try:
        # Execute SQLMap command using subprocess
        subprocess.run(["sqlmap"] + sqlmap_options, check=True)
    except FileNotFoundError:
        print("SQLMap is not installed. Installing...")
        install_sqlmap()
        print("SQLMap installed successfully. Running...")
        run_sqlmap(sqlmap_options)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running SQLMap:", e)


while(True):
      print("1. SQL Injection\n2. OSINT\n3. Web Vulnerability Scanning\n4. Network Sniffing\n5. network protocol manipulation\n6. Web Directory Sniffer\n7. online account finder\n8. System Scanning\n9. System Scanning2\n10. Web Scanning\n11. Enumerating Device\n12. Vulnerable Exploits\n13. Unix\n14. PrivescCheck\n15. Remote Access a Device\n16. Hping\n17. Nmap\n18. NetCat\n19. Exit")
      print("Please enter the number of the activity that you wish to do from the above: ")
      choice = int(input())
      if choice == 1:
              print("Running SQL Map")
              run_sqlmap(sqlmap_options)
             
      elif choice == 2:
            print("Choose from the following tools:\n1. Spiderfoot(default)\n2. theHarvester")
            Tool = int(input())
            if Tool == 1:
                      print("Running Spiderfoot")
                      command = "x-terminal-emulator"
                      subprocess.Popen(command)
            elif Tool == 2:
                      print("Running theHarvester")
                      run_theharvester()

      elif choice == 3:
            print("Running Accutenix")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 4:
            print("Running Bettercap")
            new_terminal(commands)
      elif choice == 5:
            print("Running impacket temporary not available")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 6:
            print("Running Dirb")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 7:
            print("Running Sherlock")
            subprocess.run(["python3", "sherlock/sherlock.py"], check=True)
            run_sherlock()
      elif choice == 8:
            print("Running LinPEAS")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 9:
            print("Running LinEnum")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 10:
            print("Running Nikto")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 11:
            print("Running Linux Smart Enumeration")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 12:
            print("Running Linux Exploit Suggester")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 13:
            print("Running Unix Privesc Check")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 14:
            print("Running Privesc Check")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 15:
            print("Running Metasploit")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 16:
            print("Running Hping")
            command = "x-terminal-emulator"
            subprocess.Popen(command)
      elif choice == 17:
            print("Running Nmap")
            run_nmap()
      elif choice == 18:
            print("Running NetCat")
            command = "x-terminal-emulator"
            subprocess.Popen(command)

      elif choice == 19 :
            print("Thank you for using our program!!")
            break
      else:
          print("Invalid input")