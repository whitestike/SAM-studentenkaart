import nfc
from nfc.clf import RemoteTarget
from time import sleep
import pymysql

studentsPresent = []

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
    db = pymysql.connect(host="localhost", user="root", password="root", database="nfcstudent_test" )
    return db.cursor()


def GetData(UID):
    DB = ConnectToDB()

    sql = "SELECT * FROM STUDENT WHERE UID = '" + UID + "'"

    DB.execute(sql);
    return DB.fetchone()

def PrintPStudents(studentList):
    for student in studentList:
        print(student)


def main():

    print("scanning...")

    studentID = Scan()

    #if studentID == "e95a8ef7":
    #    command = input("command: ")
    #    if input == "printlist":
    #        for student in list:
    #            print(student)
    #    main()

    if studentID in studentsPresent:
        print("card already scanned")
        main()
    
    student = GetData(studentID)
    print("card has been scanned: " + studentID)


    studentsPresent.append(studentID)
    print("welcome " + student[1] + " " + student[2])

    
    sleep(1)
    main()



main()