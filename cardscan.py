import nfc
from nfc.clf import RemoteTarget
from time import sleep
import pusher

studentList = []

def Send(msg):

    pusher_client = pusher.Pusher(
        app_id='1275452',
        key='92353ee8426715c5cc4f',
        secret='c5e4a1a431e5d39cdc8d',
        cluster='eu',
        ssl=True
    )

    pusher_client.trigger('my-channel', 'my-event', {'message': msg})

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

    Send(studentID)
    print("sending: " + studentID)

    sleep(1)
    main()



main()