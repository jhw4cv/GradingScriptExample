from shutil import copyfile
import os
import subprocess

"""
   This file is what is used to actually compile and run each students program against
   my tests.  The script renames each students file as the class name, then runs my
   tester on that file.  Its easy to set back up for a new assignment because I only need
   to change the stuff at the top of this file.
"""

# Change these each script
assignment_path = "/Users/jackworkman/Documents/APCSFiles/NumberCruncher/"
class_name = "NumberCruncher.java"
tester_path = "/Users/jackworkman/Documents/APCSFiles/NumberCruncher/NumberCruncherTest.java"
tester_name = "NumberCruncherTest"

compile_command = "javac " + tester_path # Change this to test file name

divider_top = "+ ---------------------------------------------------------------------- +\n"
divider_bottom = "+ ---------------------------------------------------------------------- +\n \n \n"
#subprocess.call(compile_command, shell=True)
# Setting up results string
results = ""

# Open the directory where the files are stored
directory = os.fsencode(assignment_path)

first = True

for file in os.listdir(directory):
    file_name = str(os.path.basename(file))
    if class_name in file_name and ".swp" not in file_name:
        student_name = file_name[2 : file_name.find("-")] # Parses student name

        # After first run goes, the file that is named Assignment.java
        # can be part of this loop so this avoids the program trying
        # to test against itself
        if class_name in student_name:
            continue


        # Going to use this to copy file to class name
        copy_command = "cp " + assignment_path+file_name[2:-1] + " " + assignment_path+class_name
        subprocess.call(copy_command, shell=True)

        results += divider_top # Add separator before new section of output

        results += "Student name:\t" + student_name + "\tAssignment Name: " + class_name + "\n\n"

        compile_command = "javac " + class_name + " " + tester_name + ".java"

        subprocess.call(compile_command, shell=True)

        run_command = "java " + tester_name
        # subprocess.call(run_command, shell=True)
        results += subprocess.getoutput(run_command) + "\n"

        results += divider_bottom

        if not first:
            results += "\n"
            first = False


f = open(assignment_path+"results.txt", "w")
f.write(results)
