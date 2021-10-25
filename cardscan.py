import nfc
from nfc.clf import RemoteTarget
from time import sleep
import pusher
import ndef

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

def Exit():
    print("device shutting down")
    exit()

def Write(tag):
    record = ndef.TextRecord("0140331-69")
    tag.ndef.records = [record]

def Scan():

    try:
        clf = nfc.ContactlessFrontend('usb')
    except:
        print("nfc device not connected")
        Exit()


    scanedUid = ""

    while scanedUid == "" or scanedUid == None:
        target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))

        
        
        if target is None:
            scanedUid = target
            sleep(0.25)
            continue

        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        Write(tag)
        record = tag.ndef
        print(record)
        
        scanedUid = target.sdd_res.hex()

        sleep(0.25)

    return scanedUid


def main():
    print("scanning...")

    studentID = Scan()

    Send(studentID)
    print("sending: " + studentID)

    sleep(1)
    main()


Send("scanner starting up!!!")
main()