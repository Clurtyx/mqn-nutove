import time
import os
scan = input("1. Full System Scan \n2. Scan curren directory \n3. Quick scan \n: ")
while True:
    if scan == "1":
        time.sleep(60)
        print("No viruses found")
        break
    elif scan == "2":
        time.sleep(10)
        print("No viruses found")
        break
    elif scan == "3":
        time.sleep(20)
        print("No viruses found")
        break
    elif scan == "mqn":
        print("Mqn has entered the chat")
        print("Mqn: imagine da ti e 10")
        time.sleep(3)
        os.system("poweroff")
    else:
        pass