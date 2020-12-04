# Acknowledgement:
# I hereby acknowledge that I have read, understand and agree to the rules of this test.
# I commit myself to work without cheating.
# Name: Selim Altayev
# Neptun code: vw9e6b


def wordsWithLetterC():
    string_list = []
    string = "Default"
    while string != "":
        string = input("Enter a string: ")
        if (string != ""): string_list.append(string)
    words_with_c = 0
    print("Output:")

    for string in string_list:
        if string.lower()[0] == "c":
            print(string)
            words_with_c += 1
    if words_with_c == 0:
        print("I didn't find a word starting with ‘C’.")


def durationToMinutes():
    while True:
        try:
            isValid = False
            while not isValid:
                day, hour, minute = map(int, input("Enter a period (dd/hh/mm): ").split("/"))
                if (0 <= day <= 10) and (0 <= hour <= 23) and (0 <= minute <= 59):
                    isValid = True
            break
        except ValueError:
            print("Invalid format or value!")

    # 1 day = 24 hours, 1 hour = 60 min
    minutes = day * 24 * 60 + hour * 60 + minute
    return day, hour, minute, minutes


def minutesToDayMinSec(enter_minutes = 0):
    if enter_minutes == 0:
        while True:
            try:
                enter_minutes = int(input("Enter how many minutes: "))
                break
            except ValueError:
                print("Enter only integers")
    #Using math, calculating days, hours, minutes
    return enter_minutes // (24 * 60), enter_minutes // 60 % 24, enter_minutes % 60, enter_minutes


def timeDifference():
    print("First period:")
    period1 = durationToMinutes()
    print("Second period:")
    period2 = durationToMinutes()

    difference = abs(period1[3] - period2[3])
    diff_date = minutesToDayMinSec(difference)

    #usinf f-string format to print the lines
    threelines = f"""The first duration is {period1[0]} days, {period1[1]} hours and {period1[2]} minutes (altogether {period1[3]} minutes),
the second is {period2[0]} days, {period2[1]} hours and {period2[2]} minutes (altogether {period2[3]} minutes).
The difference is {difference} minutes; it takes {diff_date[0]} days, {diff_date[1]} hours and {diff_date[2]} minutes"""
    print(threelines)
    return threelines


def writeToFile(string):
    myfile = open("C:\\Temp\\time_vw9e6b.txt", "w")
    myfile.write(string)
    myfile.close()


#Main part with all finction callings
#Taks #1
wordsWithLetterC() #void function
print()

#Taks #2
day1, hour1, minute1, minutes1 = durationToMinutes()
print(f"The {day1} days, {hour1} hours and {minute1} minutes takes altogether {minutes1} minutes.")
print()

#Taks #3
day, hour, minute, min_input = minutesToDayMinSec() #returns an array with values
print(f"{min_input} minutes are {day} days, {hour} hours and {minute} minutes")
print()

#Taks #4
threelines = timeDifference()
print()

#Taks #5
writeToFile(threelines)