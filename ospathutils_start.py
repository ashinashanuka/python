#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
 # print(os.name)


  # Check for item existence and type
#  print("item exists " + str(path.exists("textile.txt")))
#  print("item is a file " + str(path.isfile("textile.txt")))
 # print("item is a directory " + str(path.isdir("textile.txt")))

  # Work with file paths
#  print("item path " + str(path.realpath("textile.txt")))
#  print("item path and name  " + str(path.split(path.realpath("textile.txt"))))


  
  # Get the modification time
 # t = time.ctime(path.getatime("textile.txt"))
 # print(t)
 # print(datetime.datetime.fromtimestamp(path.getmtime("textile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textile.txt"))
  print("it has been " + str(td) + " since the file was modified")
  print("Or, " + str(td.total_seconds()) + "seconds")

  
if __name__ == "__main__":
  main()
