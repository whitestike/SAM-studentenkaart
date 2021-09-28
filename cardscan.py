import nfc
from nfc.clf import RemoteTarget
from time import sleep
import secrets
import pymysql

studentList = []

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

def ConnectToDB():
    db = pymysql.connect(host = secrets.HOST, user = secrets.USER, password = secrets.PASSWORD, database = secrets.DB)
    return db.cursor()


def GetData(UID):
    DB = ConnectToDB()

    sql = "SELECT * FROM `students` WHERE serial_number = '" + UID + "'"

    DB.execute(sql);
    return DB.fetchone()

def PrintPStudents(studentList):
    for student in studentList:
        print(student)


def main():

    print("scanning...")

    studentID = Scan()

    #if studentID == "e95a8ef7":
    #    print("debug mode")
    #    command = input("command: ")

    #    if command == "printlist":
    #        for student in studentList:
    #            print(student)
    #    elif command.startswith("lookup"):

    #        command = command.split()

    #        if command[1] + " " + command[2] in studentList:
    #            print(command[1] + " " + command[2] + " has scanned card")

    #    main()

    if studentID in studentList:
        print("card already scanned")
        main()
    
    student = GetData(studentID)

    studentList.append(student[2] + " " + student[3])
    print("welcome " + student[2] + " " + student[3])

    
    sleep(1)
    main()



main()