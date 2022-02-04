## @Author Max Friedland
## @Date 2/4/2022

import subprocess

def guiPrompt() -> int:
    subprocess.call(["clear"])
    print("**********************************")
    print("*****  ping troubleshooter   *****")
    print("**********************************")
    print()
    print("Make a selection: ")
    print("    1 - Test connectivity to your gateway.")
    print("    2 - Test for remote connectivity.")
    print("    3 - Test for DNS resolution.")
    print("    4 - Display gateway IP Address.")
    print()
    print("Please enter a number (1-4): ")
    return input()

def gatewayConnectivity():
    pass

def remoteConnectivity():
    pass

def resolutionDNS():
    print("\nResolving DNS, trying google.com... ")

def displayGateway():
    pass

def mainLoop():
    while(True):
        selection = guiPrompt()
        if selection == "1":
            gatewayConnectivity()
        elif selection == "2":
            remoteConnectivity()
        elif selection == "3":
            resolutionDNS()
        elif selection == "4":
            displayGateway()
        else:
            print("Invalid input, restarting...")
        input("*** Enter any key to continue ***")

def main():
    mainLoop()

main()