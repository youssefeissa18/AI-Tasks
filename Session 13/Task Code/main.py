import re
def createfile():
    counter = 0
    name = r"[A-Za-z]\w+\s\w+"
    phone = r"01[0125]\d\d\d\d\d\d\d\d"
    email = r"[A-Za-z0-9_]\w+@[A-Za-z]\.(com | net | eg | org)"
    Data = r"[1-9]|[12][0-9]|3[01]/[1-9]|1[0-2]/\d{4}"
    with open("File1.txt", "r") as file:
        strings = file.readlines()

    for line in strings:
        name_match = re.search(name, line)
        phone_match = re.search(phone, line)
        email_match = re.search(email, line)
        date_match = re.search(Data, line)
        counter += 1
        print(f"{counter} - {line}",end="\n")

        if not any([name_match, phone_match, email_match, date_match]):
            print("No information found in this line.")

createfile()