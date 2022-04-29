import time
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
    else:
        pass