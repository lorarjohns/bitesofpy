def fuelCounter(stars): 
    total = 0
    for star in stars:
        total += star//3 - 2
    return total



def fuel(mass):
    return max(mass//3 - 2, 0)


def total_fuel_amount(starMass):
    if fuel(starMass) == 0:
        return 0
    
    return fuel(starMass) + total_fuel_amount(fuel(starMass))
    


with open('input.txt', 'r') as f:
    input = f.readlines()
ints = [int(i) for i in input]

if __name__ == "__main__":
    #santaNeeds = fuelCounter(ints)
    simple = sum([fuel(star) for star in ints])
    recurse = sum   ([total_fuel_amount(star) for star in ints])
    print(f"Santa needs {simple} fuel.")
    print(f"Santa needs {recurse} fuel.")

    