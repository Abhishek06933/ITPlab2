def get_input():
    while True:
        try:
            organisms = int(input("Starting number of organisms: "))
            percentage_increase = float(input("average daily percentage increase: "))
            days = int(input("Enter how many days' worth of data should be printed: "))
            if organisms > 0 and percentage_increase > 0 and days > 0:
                return organisms, percentage_increase, days
            else:
                print("Error: Please enter positive values only.")
        except ValueError:
            print("Error: Please enter numeric values only.")
        
def print_data(start_organisms, percentage_increase, days):
    current_organisms = start_organisms
    print("Day Approximate                         Population")
    for day in range(1, days+1):
       
        print(f"{day:2d}                                        {current_organisms}")
        current_organisms += current_organisms * percentage_increase / 100

def main():
    organisms, percentage_increase, days = get_input()
    print_data(organisms, percentage_increase, days)

if __name__ == '__main__':
    main()
