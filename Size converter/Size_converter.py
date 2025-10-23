def liters_to_milliliters(liters):
    return liters * 1000

def milliliters_to_liters(ml):
    return ml / 1000

def liters_to_cubic_meters(liters):
    return liters / 1000

def cubic_meters_to_liters(m3):
    return m3 * 1000

def main():
    print("=========== VOLUME CONVERTER SYSTEM ===========")
    print("-----------------------------------------------")
    print(">> 1 - Convert liters -> milliliters.")
    print(">> 2 - Convert milliliters -> liters.")
    print(">> 3 - Convert liters -> cubic meters.")
    print(">> 4 - Convert cubic meters -> liters.")
    print(">> 0 - EXIT.")
    print("-----------------------------------------------")

    while True:
        choice = input(">> Choose an option (0-4): ").strip()

        if not choice.isdigit() or int(choice) not in range(0, 5):
            print("-----------------------------------------------")
            print(">> ERR . . . Invalid option. Try again.")
            print("-----------------------------------------------")
            continue

        choice = int(choice)
        if choice == 0:
            print("-----------------------------------------------")
            print(">> Bye-bye . . .")
            print("-----------------------------------------------")
            print("===============================================")
            break
        try:
            value = float(input(">> Enter the value: ").replace(",", "."))
            if value <= 0:
                print("-----------------------------------------------")
                print(">> ERR . . . Value must be positive and non-zero.")
                print("-----------------------------------------------")
                continue
        except ValueError:
            print("-----------------------------------------------")
            print(">> ERR . . . Please enter only a number.")
            print("-----------------------------------------------")
            continue

        if choice == 1:
            print("-----------------------------------------------")
            print(f">> {value} liters = {liters_to_milliliters(value):.2f} milliliters.")
        elif choice == 2:
            print("-----------------------------------------------")
            print(f">> {value} milliliters = {milliliters_to_liters(value):.3f} liters.")
        elif choice == 3:
            print("-----------------------------------------------")
            print(f">> {value} liters = {liters_to_cubic_meters(value):.3f} cubic meters.")
        elif choice == 4:
            print("-----------------------------------------------")
            print(f">> {value} cubic meters = {cubic_meters_to_liters(value):.1f} liters.")
        print("-----------------------------------------------")

if __name__ == "__main__":
    main()