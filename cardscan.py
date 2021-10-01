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


def GetData(UID , table):
    DB = ConnectToDB()

    sql = "SELECT * FROM `"+ table +"` WHERE serial_number = '" + UID + "'"

    DB.execute(sql);
    return DB.fetchone()

def PrintPStudents(studentList):
    for student in studentList:
        print(student)

def Debug(ID):
    if ID == "e95a8ef7":
            print("debug mode")
            command = input("command: ")

            if command == "printlist":
                for student in studentList:
                    print(student)
            elif command.startswith("lookup"):

                command = command.split()

                if command[1] + " " + command[2] in studentList:
                    print(command[1] + " " + command[2] + " has scanned card")

            main()


def main():

    print("scanning...")

    studentID = Scan()

    if False:
        Debug(studentID)

    
    student = GetData(studentID, "students")

    if student == None:
        student = GetData(studentID, "teachers")

<<<<<<< HEAD
=======
    if student[2] + " " + student[3] in studentList:
        print("card already scanned")
        main()
>>>>>>> a297745263a5959220c00fdcc945123f347ac451
        print("welcome " + student[2] + " " + student[3])
    else:
        studentList.append(student[2] + " " + student[3])
        print("welcome " + student[2] + " " + student[3])

    
    sleep(1)
    main()



main()