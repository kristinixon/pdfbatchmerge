import os

files = os.listdir(r"C:\Users\knixon\Desktop\mapmaker\test")
files.sort
files #view files

command_prefix = "pdftk "
command_args = ""
command_end = "cat output output1.pdf"
counter = 0

for file in files:
  if ".py" not in file:
    if "Microsoft Outlook" in file:
      if files.index(file) != 0:
        os.system(command_prefix + command_args + command_end)
      counter = counter + 1
      command_args = '"' + file + '"' + " "
      command_end = "cat output output" + str(counter) + ".pdf"
    else:
      command_args = command_args + '"' + file + '"' + " "

os.system(command_prefix + command_args + command_end)
