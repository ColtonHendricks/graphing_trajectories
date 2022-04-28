# import libraries and functions
import matplotlib.pyplot as plt
import numpy as np
from func import integrate_graph

# global variables
total_mass = 0
dry_mass = 0
burn_time = 0
total_impulse = 0
propellant_mass = 0
average_thrust = 0
mass_flow_rate = 0


def set_var_preset():
    global total_mass, dry_mass, burn_time, total_impulse, propellant_mass, average_thrust, mass_flow_rate
    # Set variables
    total_mass = 1
    dry_mass = 0.906
    burn_time = 3.5
    total_impulse = 49.6
    propellant_mass = 0.064
    average_thrust = total_impulse / burn_time
    mass_flow_rate = propellant_mass / burn_time
    # angle = float(input("What angle are you launching your rocket at?: "))


def set_var_input():
    global total_mass, dry_mass, burn_time, total_impulse, propellant_mass, average_thrust, mass_flow_rate
    # Set variables
    total_mass = float(input("Enter the total mass of the rocket in kg: "))
    dry_mass = float(input("Enter the dry mass of the rocket in kg: "))
    burn_time = float(input("Enter the time that the rocket will burn for in seconds: "))
    total_impulse = burn_time * float(input("Enter the average thrust of the rocket you are using in N: "))
    propellant_mass = float(input("Enter the propellant mass of your rocket in kg: "))
    average_thrust = total_impulse / burn_time
    mass_flow_rate = propellant_mass / burn_time
    # angle = float(input("What angle are you launching your rocket at?: "))


def main():

    answer = int(input("Would you like to graph based on a preset of variables (Press 1)"
                       "\n or graph based of your own inputs (Press 2): "))

    if answer == 1:
        set_var_preset()
    elif answer == 2:
        set_var_input()

    # set time as an array of evenly spaced numbers from 0 to 10
    time = np.linspace(0, 10, 100, False)

    # return values where time equals burn time
    index = int(np.where(time == burn_time)[0]+1)
    # kinematics of thrust where the average thrust is repeated for the amount of time that the engine burns for
    thrust = (np.append(np.repeat(average_thrust, index), np.repeat(0, len(time) - index)))
    # function for mass over time while it changes as fuel burns
    mass = np.append(np.repeat(total_mass, index) - time[0:index] * mass_flow_rate, np.repeat(dry_mass, len(time) - index))
    # acceleration
    acceleration = thrust/mass - 9.81
    # function of velocity depending on time and acceleration
    velocity = integrate_graph(time, acceleration)
    # function of displacement depending on time and velocity
    displacement = integrate_graph(time, velocity)

    # plot acceleration and velocity
    plt.style.use('dark_background')
    plt.plot(time, acceleration)
    plt.plot(time, velocity)
    plt.legend(["Acceleration (m/s^2)", "Velocity (m/s)"])
    plt.xlabel("Time (s)")
    plt.title("Flight of a model rocket")
    plt.show()

    plt.style.use('dark_background')
    plt.plot(time, displacement)
    plt.legend("Displacement (m)")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.title("Flight of a model rocket")
    plt.figtext(.075, 0.005, "When the graph crosses the y-axis the rocket has reached ground level")
    plt.show()


if __name__ == "__main__":
    main()
