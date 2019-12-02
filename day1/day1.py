from Input import Input

calc_fuel = lambda mass: max((mass // 3) - 2, 0)

def day1():
    input = [int(string) for string in Input(dayNr = 1).lines()]

    erg1, erg2 = 0, 0
    for mass in input:
        fuel = calc_fuel(mass)
        erg1 += fuel
        erg2 += fuel
        while fuel > 0:
            fuel = calc_fuel(fuel)
            erg2 += fuel

    print(f'Part1: {erg1}')
    print(f'Part2: {erg2}')


if __name__ == '__main__':
    day1()