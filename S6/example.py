r"""
This script creates an empty file.
"""
import datetime
now = datetime.datetime.now()
filename=now.strftime('%y-%m-%d-%H-%M-%S')+'.txt'

#Create an empty file
def create_file():
  """This function creates an empty file"""
  with open(filename, "w") as file:
    file.write("") #writing an empty string

create_file()