print("=========== VOLUME CONVERTER SYSTEM ===========")
print("-----------------------------------------------")
print(">> 1 - Convert liters -> milliliters.")
print(">> 2 - Convert milliliters -> liters.")
print(">> 3 - Convert liters -> cubic meters.")
print(">> 4 - Convert cubic meters -> liters.")
print(">> 0 - EXIT.")
print("-----------------------------------------------")


choice = input(">> Choose an option (0-4): ").strip()

       
print(">> ERR . . . Value must be positive and non-zero.")
print(">> ERR . . . Please enter only a number.")
print(">> ERR . . . Invalid option. Try again.")


print("-----------------------------------------------")
print(f">> {value} liters = {liters_to_milliliters(value):.2f} milliliters.")
print("-----------------------------------------------")
print(f">> {value} milliliters = {milliliters_to_liters(value):.3f} liters.")
print("-----------------------------------------------")
print(f">> {value} liters = {liters_to_cubic_meters(value):.3f} cubic meters.")
print("-----------------------------------------------")
print(f">> {value} cubic meters = {cubic_meters_to_liters(value):.1f} liters.")
print("-----------------------------------------------")

     
print(">> Bye-bye . . .")
print("-----------------------------------------------")
print("===============================================")
