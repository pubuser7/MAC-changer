#!/usr/bin/env python

import subprocess
import optparse
import os
import sys

def check_root():
    uid = os.getuid()
    if str(uid) != '0':
        print("[*] Run az root")
        sys.exit()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="manualy_mac", help="Change MAC manualy")
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        sys.exit()
    return parser.parse_args()

def change_mac(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[*] Completed!")

def main():
    check_root()
    (options, argument) = get_arguments()
    change_mac(str(options.interface), str(options.mac))

if __name__ == "__main__":
    main()

