
def calculate_rainfall():
    num_years = int(input("Enter the number of years: "))
    total_rainfall = 0
    num_months = 0
   
    for year in range(1, num_years+1):
        year_rainfall = 0
        for month in range(1, 13):
           
            rainfall_cm = float(input(f"Enter rainfall for Year {year}, Month {month} (in centimetres): "))
           
            year_rainfall += rainfall_cm
            total_rainfall += rainfall_cm
            num_months += 1
        avg_monthly_rainfall = year_rainfall / 12
       
        print(f"Total rainfall for Year {year}: {year_rainfall} centimetres")
        print(f"Average monthly rainfall for Year {year}: {avg_monthly_rainfall:.2f} centimetres")
   
    overall_avg_monthly_rainfall = total_rainfall / num_months

    print(f"Total rainfall for all {num_years} years: {total_rainfall} centimetres")
    print(f"Overall average monthly rainfall for all {num_years} years: {overall_avg_monthly_rainfall:.2f} centimetres")


calculate_rainfall()
