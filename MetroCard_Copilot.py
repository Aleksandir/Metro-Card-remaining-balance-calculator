balance = float(input("Enter your current metro card balance: "))
fair = float(input("Enter the fair: "))

remaining_balance = 0.2
running_balance = balance
trip_count = 0

while running_balance >= fair:
    trip_count += 1
    running_balance -= fair

    if running_balance < fair:
        break

    if running_balance >= 100 and running_balance % 100 == 0:
        remaining_balance += 0.2

transfer_amount = round(fair - running_balance + remaining_balance, 2)
transfer_amount = round(transfer_amount / 10) * 10

print(
    f"You need to transfer ${transfer_amount:.2f} to your balance to have the smallest remaining balance possible."
)
print(f"You can take {trip_count} trips with that amount of money.")
