#!/usr/bin/python
import re
import os, sys

myList = []
ipList = []

def readLogFile(fileName):
    global myList   

    with open(fileName, "r") as MyFile:
        for i in MyFile:    
            myList.append(i)
        MyFile.close()

def findIpAdress():
    global ipList

    for i in myList:
        if re.search('[0-9]+(?:\.[0-9]+){3}', i):
            ipList += re.findall('[0-9]+(?:\.[0-9]+){3}', i)

def saveResult(fileName):
    path = "output"  
    os.mkdir(path, 0775);    
    count = 0
    count2 = 0

    with open(fileName, "w") as MyFile2:
    
        for x in ipList:
            count += 1

        MyFile2.write("{0} new connection to your server from ip address:\n".format(count))
        for z in ipList:
            count2 += 1
            MyFile2.write("{0}. {1}\n".format(count2, z))
        MyFile2.close()


def main():
    """Main function"""

    readLogFile("logs/logFile")
    findIpAdress()
    saveResult("output/ipaddress")

if __name__ == "__main__":
    main()
