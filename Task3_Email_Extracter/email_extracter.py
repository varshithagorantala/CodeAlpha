import re

with open("input.txt", "r") as file:
    content = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Total emails found:", len(emails))