import smtplib, time, imaplib, email, os.path, html, subprocess

EMAIL_ACCOUNT = #xxxxxxx
PASSWORD = #xxxxxxx

APCS_FOLDER_PATH = "/Users/jackworkman/Documents/APCSFiles/"

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

YEAR = "2018" # This will be important for formatting the date

# Keep assignments and their corresponding tests in same indices
assignments = ["NumberCruncher", "Test"]
testers = ["number_cruncher_test.py", "test.py"]

def pull_emails():
    """"
    This function will pull all email attatchments and turn them into .java files, placing them
    in the proper assignment folder.  Another function is used later on to actually compile
    and run each students .java files.
    """

    email_list = []
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')

    result, data = mail.uid('search', None, 'SUBJECT "Number Cruncher"') # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # result, email_data = conn.store(num,'-FLAGS','\\Seen')
        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # Header Details
        # Provides information needed to know which student and on what date the assignment was submitted
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
        date = str(email.header.make_header(email.header.decode_header(email_message['Date'])))

        # Don't need day of week or actual time so will clean date a bit
        # Date normally looks something like Fri, 11 Jan 2018 14:53:04 -0500
        # But personally only need 11_Jan_2018

        l = date.find(",") + 2 # gets rid of day of week
        r = date.find(YEAR) + 4 # gets rid of year
        date = date[l : r]
        date = date.replace(" ", "_")

        # Body details
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue

            # Attachment processing begins here
            class_name = part.get_filename()


            if bool(class_name) and class_name[0: class_name.find(".java")] in assignments:
                # Strip .java from class name
                # The file name will include .java later
                class_name = class_name[0: class_name.find(".java")]

                # Clean up the student name here since the students
                # email address is not needed, just their name.
                student_name = email_from

                # imaplib always includes <email address> after the name
                # so look for "<" to strip out email address
                student_name = student_name[0 : student_name.find("<")]
                student_name = student_name.rstrip()

                # Also want to replace white space with _ for better file names
                student_name = student_name.replace(" ","_")

                # file name will now have format jack_workman-11_Jan_2018-HelloWorld.java
                file_name = student_name + "-" + date + "-" + class_name + ".java"
                file_path = APCS_FOLDER_PATH + class_name + "/" + file_name
                fp = open(file_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()



"""
    Main part of program.  Here you select which program you want to grade
    and whether or not you want to redownload programs     
"""
for i in range(len(assignments)):
    print(i, assignments[i])

assignment = int(input("Enter assignment number to grade: "))

if assignment not in range(0, len(assignments)):
    while assignment not in range(0, len(assignments)):
        assignment = int(input("Input invalid, please try again: "))

download_mail = input("Do you want to re-download programs? (y/n) ")

if download_mail != "y" and download_mail != "n":
    while download_mail != "y" and download_mail != "n":
        download_mail = input("Input invalid, please try again: ")

if download_mail == "y":
    print("Downloading files...")
    messages = pull_emails()
    print("Download complete")


run_command = "cd " + assignments[assignment] +"\n" + "python3 " + testers[assignment] + "\n" + "cd ..\n"

print("Running programs...")

process = subprocess.call(run_command, shell=True)

print("Run complete. Outputted to: " + assignments[assignment] + "/results.txt:")

#print("cat " + APCS_FOLDER_PATH + assignments[assignment] + "/results.txt")
process = subprocess.call("cat " + APCS_FOLDER_PATH + assignments[assignment] + "/results.txt", shell=True)
