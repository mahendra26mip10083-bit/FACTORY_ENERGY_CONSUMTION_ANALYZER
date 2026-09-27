def calculate_energy(power , hourse, days):
    energy = power*hourse*days

    return energy

def total_energy(machines):
    if len(machines) ==0:
        print("No machine is available")
        return
    total = 0 

    for machine in machines :

        power = machine[1]
        hours = machine[2]
        days = machine[3]

        energy = calculate_energy(power, hours ,days)

        total = total + energy 

    print("Total Facory Energy consumtion:", total)

def calculate_totalcost(machines):
    if len(machines)==0:
        print("No machine are available.")

    total = 0 

    for machine in machines :
         
         power = machine[1]
         hours = machine[2]
         days = machine[3]

         energy = calculate_energy(power , hours ,days)

         total = total + energy

         rate_perKWh = float(input("enter electricity coast per KWh"))

         cost = total*rate_perKWh

         print("Total energy:" ,total ,"KWh")
         print("electricity cost:", cost )
