from energy import calculate_energy

def energy_suggestion(machines):
    if len(machines) == 0:
        print("NO machine are available.")
        return

    for machine in machines :
         machine_name = machine[0]
         power = machine[1]
         hours = machine[2]
         days = machine[3]

         energy = calculate_energy(power ,hours , days)

         print("\n Machine:",machine_name)
         print("Energy consumtion:", energy,"KWh")

         if energy > 1000:
             print("ALERT : High energy comsumtion.")
             print("SUGGESTION : Reduce machine ruuning hours and maintain machine efficiency")

         elif energy > 500 :
             print("Medium energy comsumtion")
             print("SUGGESTION : Used monitor machine ")

         else :
             print("Low energy consution.")
             print("SUGGESTION : Energy consution ia under control")
