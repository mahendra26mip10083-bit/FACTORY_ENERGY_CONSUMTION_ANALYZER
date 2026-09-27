from machine import add_machines , show_data 
from energy import total_energy ,  calculate_totalcost
from suggestion import energy_suggestion


def main():

    machines = []

    while True:

        print("=====================================")

        print("FACORY CONSUMTION ANALYZER")

        print("=====================================")


        print("1. Add machine")
        print("2. display machine data")
        print("3. total energy consumtion")
        print("4. caclulate elecricity coast ")
        print("5. Energy comsumyion suggetion")
        print("6. Exite")

        choice = input("Enter the your choice")

        if choice == "1":
            add_machines(machines)

        elif choice == "2":
            show_data(machines)

        elif choice == "3":
            total_energy(machines)

        elif choice == "4":
            calculate_totalcost(machines)

        elif choice == "5":
            energy_suggestion(machines)

        elif choice == "6":
            print("Exite")

            break

        else:
            print("invalid choice")
            print("Program edded")

main()