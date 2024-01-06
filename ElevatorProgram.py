import Elevator, time, random


def closest_elevator(floor, elevator_array):
    func_count = 0
    range_list = []
    for j in range(len(elevator_array)):
        range_list.append(abs(elevator_array[func_count] - floor))
        func_count += 1
    index = 0
    for k in range(len(range_list)):
        if range_list[index] == min(range_list):
            break
        else:
            index += 1
            continue
    return index


def time_lag(floor):
    for a in range(floor):
        print('. ', end='')
        time.sleep(1)
    print()


if __name__ == '__main__':
    print('Welcome to this basic elevator simulator. You are currently in the lobby, i.e. "floor 0."\n')
    current_floor = 0
    plus_floors = int(input('How many floors are there above the lobby? '))
    while plus_floors < 1:
        print('Please enter a positive integer: ', end='')
        plus_floors = int(input())
    print()
    minus_floors = int(input('How many floors are there below the lobby? '))
    while minus_floors < 1:
        print('Please enter a positive integer: ', end='')
        minus_floors = int(input())
    total_floors = plus_floors + minus_floors + 1
    print()
    elevators = int(input('How many elevators does this building have? '))
    while elevators < 1:
        print('Please enter a positive integer: ', end='')
        elevators = int(input())
    print()
    while True:
        count = 1
        elevator_list = []
        floor_list = []
        for i in range(elevators):
            elevator_list.append(
                Elevator.Elevator(f'Elevator {count}', count, int(random.randrange(-minus_floors, plus_floors))))
            floor_list.append(elevator_list[count - 1].get_current_floor())
            count += 1
        response = int(input('Choose a call button:\n1. up\n0. down\n'))
        # print(response)
        while response > 1 or response < 0:
            print('Remember, "1" for up and "0" for down!', end=' ')
            response = int(input())
            # print(response)
        print()
        closest = closest_elevator(current_floor, floor_list)
        # print(floor_list)
        # print(closest)
        print(f'{elevator_list[closest].get_name()} is the closest elevator. It will arrive shortly.')
        time_lag(abs(elevator_list[closest].get_current_floor() - current_floor))
        elevator_list[closest].set_current_floor(current_floor)
        # print(elevator_list[closest].get_current_floor())
        floor_choice = int(input(f'{elevator_list[closest].get_name()} has arrived. Now, please choose a floor: '))
        while floor_choice < -minus_floors or floor_choice > plus_floors or floor_choice == current_floor or \
                (response == 1 and floor_choice < current_floor) or (response == 0 and floor_choice > current_floor):
            if floor_choice < -minus_floors or floor_choice > plus_floors:
                print(
                    f'That floor does not exist. Please enter a value from {-minus_floors} to {plus_floors}: ', end='')
            elif floor_choice == current_floor:
                print('You are already on that floor. Please select a different floor: ', end='')
            elif response == 1 and floor_choice < current_floor:
                print('You cannot go to a floor below you if you previously indicated that you\'re going up. Please '
                      'enter a floor above you: ', end='')
            elif response == 0 and floor_choice > current_floor:
                print('You cannot go to a floor above you if you previously indicated that you\'re going down. Please '
                      'enter a floor below you: ', end='')
            floor_choice = int(input())
        print(f'You selected {floor_choice}. Your elevator will arrive at its destination shortly.')
        time_lag(abs(floor_choice - current_floor))
        elevator_list[closest].set_current_floor(floor_choice)
        # print(elevator_list[closest].get_current_floor())
        current_floor = floor_choice
        choice = int(input(f'You have now arrived on floor {current_floor}. Would you like to use the call button '
                           f'again?\n1. yes\n0. no\n'))
        while choice > 1 or choice < 0:
            print('Remember, "1" for yes and "0" for no!', end=' ')
            choice = int(input())
        if choice == 1:
            continue
        else:
            break
    print(end='')
print(end='')
