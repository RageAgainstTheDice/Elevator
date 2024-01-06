# This program will involve a hypothetical building which, for the sake of simplicity, will hypothetically only
# consist of elevator rooms on each floor. The user will start at the lobby, i.e. "floor 0." At the start of the
# program (when it runs), the user will be prompted to decide how many floors and elevators there are in the
# building. Upon doing so, the program will then initiate a loop that creates the desired number of elevator objects.
# The main class will start with that; along with said main class will be an object class titled "Elevator",
# which will be used to define the elevator object within the main class. The only attribute of this class will be
# "current_floor", which will be randomized at the start of every program run. Meanwhile, in the main class,
# the user will then be prompted to call an elevator depending on whether they wish to go up or down. (If the user is
# already on the lowest or highest floor, the program will prevent them from choosing an option that would have them
# end up outside the building's bounds.) Afterwards, the program will determine which elevator--based on the
# randomly-generated floor positions--is closest to the user, and will "send that elevator down," i.e. change its
# "current_floor" variable to that of the user's. The program will make use of the "Time" package to simulate the
# time it takes for the elevator to arrive; in other words, the farther away the closest elevator is, the more time
# passes until the arrival prompt pops up. Then, the program will prompt the user to select a floor; if they
# initially chose "going up", then they can only choose a floor higher than their "current floor". Conversely,
# if they initially chose "going down", then they can only choose one lower. The elevator will then "arrive" to that
# floor by changing its "current_floor" variable to that of the user's input. The "Time" package will then be used
# here in the same manner as previously mentioned. After "arriving" at the desired floor, the user will be prompted
# to either call another elevator or end the program there; the former option continues the loop while the latter one
# breaks it. 

# Checklist:
#   "Elevator" object class -
#       Object initializer DONE
#       Getter(s) DONE
#       Setter(s) DONE
#   "Main" class -
#       "floors" and "elevators" amount prompts DONE
#       Loop that initializes desired number of elevator objects DONE
#       While loop that initiates the sequence DONE
#       "going up or down" prompt (and failsafe that prevents impossible actions) DONE
#       "which floor?" prompt (and failsafe that prevents impossible actions) DONE
#       Determining the closest elevator DONE
#       Bringing the closest elevator to the user and then sending the user to his/her desired floor DONE
#       Simulating time delay for previous step DONE
#       "go again?" prompt (along with corresponding usages of "continue" and "break" DONE
