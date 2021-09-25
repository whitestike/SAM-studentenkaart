import nfc
from nfc.clf import RemoteTarget
from time import sleep

def Scan():
    clf = nfc.ContactlessFrontend('usb')

    scanedUid = ""

    while scanedUid == "" or scanedUid == None:
        target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
        
        if target is None:
            scanedUid = target
            sleep(0.25)
            continue

        serial = target.sdd_res.hex()

        scanedUid = serial

        sleep(0.25)

    return scanedUid

def main():

    print("scanning...")

    studentID = Scan()

    print(studentID)

    if studentID == "e95a8ef7":
        print("welkome Rickert Goyvaerts")
    else:
        print("studentID not recognised")
    
    sleep(1)
    main()

main()

