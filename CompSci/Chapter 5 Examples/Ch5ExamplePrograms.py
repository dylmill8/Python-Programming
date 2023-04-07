#
# Name:
#
# This module contains practice programs for Ch5
#

# ADD HEADER COMMENT HERE
def nickname():
    # get user's name and grade number
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    grade = int(input("Enter your grade: "))

    nick = fname[0]+lname[:]
    gradeList = ["Freshman", "Sophmore", "Junior", "Senior"]
    gradeName = gradeList[grade-9]
    print(nick,"the",gradeName)

nickname()
