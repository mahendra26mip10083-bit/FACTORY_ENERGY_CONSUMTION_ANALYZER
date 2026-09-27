from energy import calculate_energy

def add_machines(machines):
    machine_name = input("enter machine name:")

    power = float(input("Enter power comsumtion"))

    hours = float(input("Enter the daily running hours :"))

    days = int(input("Enter the working days;"))

    machine = [machine_name , power , hours , days]

    machines.append(machine)

    print("machine added successfully:")


def show_data(machines):

    if len(machines) == 0 :

        print("no machine is available now")
        return

    print("\n==============MACHINE DETAILS=============== ")

    for machine in machines : 
        machine_name = machine[0]
        power = machine[1]
        hours = machine[2]
        days = machine[3]

        energy = calculate_energy(power, hours ,days )


        print("machine:",machine_name)
        print("power:",power) 
        print("hourse", hours)
        print("days" , days)
        print("energy consumtion;" ,energy , "kWh")
