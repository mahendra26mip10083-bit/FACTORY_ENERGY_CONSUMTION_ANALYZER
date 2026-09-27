# Facotry Energy Consumtion Analyzer 

## Problem Statement 
This the a python that can be used to chech the energy comsumtiom of machines in a factory from the terminal.

In the factory, different machines can consume differernt amount of electricity.If the energy used by each machine is calculate manually, it can take more time and it may be difficult to keep track of the total consumtion. This project provides a simple way to add machine details , calculate energy consumtion , find total energy used and calculate the electricity cost.

The project also gives a simple suggestion according to the energy consumed by each machine.

## Scoope of the project 
This project is mainly focused on basic factory machine energy management using python.

The user can do these things:
~ Add a new machine 
~ View machine details
~ Calculate energy comsumtion of machines
~ Calculate total Factory enrgy comsumtion 
~ Calculate electricity cost
~ Get suggestion according to energy comsumtion 

## Feachers

1. Add machine 
The user can add a machine by entering:
~ Machine name 
~ Power comsumtion 
~ Daily running hours
~ Working Days 

2. Display Machine Data 
This option displays the information of the machines stored in the program 

it showss:
~ Machine name 
~ Power consumtion 
~ Running hours
~ Working dyas 
~ Energy consumtion 

3. Total Energy consumtion 
This option calculate the total energy consumed by all the machines added to the program .

The formula is used :

Energy = power * running hours * Working days 

4. Calculate Elecrticity Cost 
The user can enter the electricity cost per kWh. The program then user the total energy consumtion to calculate the electricity cost.

Electricity Cost = Total Energy * Rate per kWh 

5. Energy Comsumtion suggestion 
The program checks the energy consumtion of every machine .

~ if comsumtion is above 1000kWh, It show a high energy comsumtiopn alert.
~ if consumtion is above 500kWh , It shows a medium energy comsumtion . 
~ Otherwise ,it shows low energy comsumtion . 


## Project modules 
The project is divided into different Python files so that each has its own work.

### main.py 
Contains function for adding machines and displaying machine details .

### machine.py 
Contains functions for adding machines and displaying machine details.

### energy.py
Contains funtions for calculating energy consumtion , total energy and eletricity cost.

### suggestion.py 
Contains the funtion for checking energy consumption and giving suggestion 

### README.md 
Contains information about the project and how it works.


## Technologies Used 
~ Python
~ Python lists 
~ Function 
~ Loops 
~ If-else Conditions 
~ Python modules 

## Future Scope 
In the future , the project can be improved by adding a data base , graphical user interface , monthly energy reports, data saving , and more detailed energy analysis 