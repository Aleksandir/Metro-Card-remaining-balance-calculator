# ENTER YOUR VALUES HERE
CURRENT_METROCARD_BALANCE = 15.4
FAIR = 4.20
REMAINING_BALANCE = 0.4

# below is the working code, do not change unless you know what you're doing
highBalance = False

runningBalance = CURRENT_METROCARD_BALANCE
runCount = 0
while not runningBalance % FAIR < REMAINING_BALANCE:
    runCount += 1

    runningBalance += 15

    if runningBalance > 500:
        print(
            "The balance required is over $500, which is not realistic, please increase the remaining balance allowed"
        )
        highBalance = True
        break

if highBalance != True:
    print(
        f"$ {str(runningBalance)} is the required balance as of now, this will give you {round(runningBalance / FAIR)} trips"
    )
