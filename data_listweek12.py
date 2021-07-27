data_list = []
entity =[]
code =[]
year = []
years = []
minOverallYear = "-1"
maxOverallYear = "-1"
total_average = '-1'
userYearAges = []
maxOverallAge =0
minOverallAge =1000
minOverallCountry =" "
maxOverallCountry =" "
minUserYearAge=1000
maxUserYearAge=0
minUserYearCountry=" "
maxUserYearCountry=" "

year_user_interest = int(input("Enter the year of interest : "))

with open (r"C:\Users\Diogo Rangel\Programação\Python Learning\CSEPC -110\life-expectancy.csv") as data_file:
    next(data_file)
    for line in data_file:
        data_file_split = line.split(",")

        entity.append(data_file_split[0])
        code.append(data_file_split[1])
        year.append(data_file_split[2])
        years.append(data_file_split[3])

        userYearAges.append(years)
        maxOverallYear = max(years)
        minOverallYear = min(years)
        max_life_expectancy = max(years)
        min_life_expectancy = min(years)

    for peace in years:    
        if peace < minOverallYear:
            minOverallYear = peace
            minIndex = years.index(minOverallYear)    
            minOverallCountry = entity[minIndex]

        if peace > maxOverallYear:
            maxOverallYear = peace

        if year == year_user_interest:
            
            if peace < minUserYearAge:
                minUserYearAge == peace
                minUserIndex = years.index(minUserYearAge)    
                minOverallCountry = entity[minUserIndex]

            # if peace > maxUserYearAge:
            #     maxUserYearAge == peace

#average = sum(userYearAges) / len(userYearAges)
# print(f"The overall max life experience is: {maxOverallYear} from {maxOverallCountry} in {year}")
# print(f"The overall min life expectancy is: {minOverallYear} from {minOverallCountry } in {year}")

print(f"For the year: {year_user_interest}")
#print(f"The average life expectancy across all countries was: {average}")
# print(f"The max life expectancy was in {maxUserYearCountry} with {max_life_expectancy}")
print(f"The min life expectancy was in {minUserYearCountry} with {minUserYearAge}")    