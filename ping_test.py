## @Author Max Friedland
## @Date 2/4/2022
import string
import subprocess

def guiPrompt() -> int:
    ##subprocess.call(["clear"])
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
    print("Please enter a number (1-4) or q/Q to quit: ")
    return input()

def gatewayConnectivity():
    print("\nTesting gateway connectivity...")
    process = subprocess.Popen("ip route", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    data: str = output[0].decode()
    line: str = data.splitlines()
    word: str = line[0].split(" ")
    print("Pinging default gateway @" + word[2])

    process = subprocess.Popen("ping -c 1 " + word[2], shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    line: str = output[0].decode()
    expected = "1 received"
    if line.find(expected) != -1:
        print("Test passed")
    else:
        print("Test failed")

def remoteConnectivity():
    print("\nTesting remote connection, trying 8.8.8.8")
    process = subprocess.Popen("ping 8.8.8.8 -c 1", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    line: str = output[0].decode()
    expected = "1 received"
    if line.find(expected) != -1:
        print("Test passed")
    else:
        print("Test failed")

def resolutionDNS():
    print("\nResolving DNS, trying google.com... ")
    process = subprocess.Popen("ping google.com -c 1", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    line:str = output[0].decode()
    expected = "1 received"
    if line.find(expected) != -1:
        print("Test passed")
    else:
        print("Test failed")

    print("\nResolving DNS, trying rit DNS @ 129.21.3.17 ")
    process = subprocess.Popen("ping 129.21.3.17 -c 1", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    line: str = output[0].decode()
    expected = "1 received"
    if line.find(expected) != -1:
        print("Test passed")
    else:
        print("Test failed")

def displayGateway():
    print("\nFinding default gateway, through \"ip route\"")
    process = subprocess.Popen("ip route", shell=True, stdout=subprocess.PIPE)
    output = process.communicate()
    data: str = output[0].decode()
    line: str = data.splitlines()
    word: str = line[0].split(" ")

    print("Your default gateway is: " + word[2])

def mainLoop():
    while(True):
        selection: str = guiPrompt()
        if selection == "1":
            gatewayConnectivity()
        elif selection == "2":
            remoteConnectivity()
        elif selection == "3":
            resolutionDNS()
        elif selection == "4":
            displayGateway()
        elif (selection == "q") or (selection == "Q"):
            print("Exiting...")
            break
        else:
            print("Invalid input, restarting...")
        input("*** Enter any key to continue ***")

def main():
    mainLoop()

main()