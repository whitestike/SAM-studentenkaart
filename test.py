import nfc
from nfc.clf import RemoteTarget
from time import sleep

clf = nfc.ContactlessFrontend('usb')

scanedUid = ""

while True:
    target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))
    
    if target is None:
        scanedUid = target
        print(scanedUid)
        continue

    serial = target.sdd_res.hex()

    scanedUid = serial

    print(scanedUid)
    sleep(0.2)  # don't burn the CPU