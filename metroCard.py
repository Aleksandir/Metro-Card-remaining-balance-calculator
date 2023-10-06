# ENTER YOUR VALUES HERE
# [ ] add feature so below variables can be assigned though user input
CURRENT_METROCARD_BALANCE = 15.4
FAIR = 4.20
REMAINING_BALANCE = 0.2

# below is the working code, do not change unless you know what you're doing
highBalance = False

runningBalance = CURRENT_METROCARD_BALANCE
runCount = 0
while not runningBalance % FAIR < REMAINING_BALANCE:
    runCount += 1

    runningBalance += 15

    print(runningBalance)
    if runningBalance > 9999999:
        break

    # if runningBalance > 500:
    #     print(
    #         "The balance required is over $500, which is not realistic, please increase the remaining balance allowed"
    #     )
    #     highBalance = True
    #     break

if highBalance != True:
    print(
        f"$ {str(runningBalance)} is the required balance as of now, this will give you {round(runningBalance / FAIR)} trips"
    )

# metroCard.py

# This script calculates the number of trips that can be taken with a given balance on a metro card.

# Usage:
#     - Set the values of CURRENT_METROCARD_BALANCE, FAIR, and REMAINING_BALANCE at the top of the script.
#     - Run the script to see the number of trips that can be taken with the given balance.

# Variables:
#     - CURRENT_METROCARD_BALANCE: The current balance on the metro card.
#     - FAIR: The cost of a single trip.
#     - REMAINING_BALANCE: The minimum remaining balance required on the card after a trip.

# Output:
#     - If the balance required is over $500, the script will print an error message.
#     - Otherwise, the script will print the required balance and the number of trips that can be taken with that balance.

# Example:
#     - CURRENT_METROCARD_BALANCE = 15.4
#     - FAIR = 4.20
#     - REMAINING_BALANCE = 0.4
#     - Output: "$ 60.4 is the required balance as of now, this will give you 14 trips"
