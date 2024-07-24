import main

import network
import vfs
import json

sta_if  = network.WLAN(network.STA_IF)
vfs.mount(bdev,"/")

def connectToNetwork(SSID,Key):
    print("connecting to network...")
    sta_if.active(True)
    if not sta_if.isconnected():
        sta_if.connect(SSID,Key)
        while not sta_if.isconnected():
            pass
    print("Connected")
    return True

def startUp():
    try:
        with open("/config.json","r") as configFile:
            config = json.load(configFile)
            try:
                connectToNetwork(config["SSID"],config["KEY"])
                print("Everything A-Ok")
            except:
                print("Network connection failed...")
                print("Perhaps recheck your network configuration:")
                config["SSID"] = input("    Enter SSID: ")
                config["KEY"] = input("    Enter Password: ")
                startUp()
                return
    except OSError:
        print("Error while starting up: Configuration not found")
        print("Creating new configuration file")

        config = {
            "SSID":"",
            "KEY":""
        }

        print("Setup your network:")
        config["SSID"] = input("    Enter SSID: ")
        config["KEY"] = input("    Enter Key: ")

        with open("/config.json","w") as configFile:
            configFile.write(str(config).replace("'",'"'))
        startUp()
        return

startUp()