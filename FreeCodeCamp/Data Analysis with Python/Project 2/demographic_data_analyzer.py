import pandas as pd
def calculate_demographic_data(print_data=True):
     # Read data from file
    df = pd.read_csv("adult.data.csv")
    # print(df.head())
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    number_of_bachelors = df['education'].value_counts().Bachelors
    number_of_records = df.shape[0]

    percentage_bachelors = round(number_of_bachelors/number_of_records*100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Experiments
    number_of_higher_education = df['education'].value_counts()['Doctorate'] + df['education'].value_counts()['Bachelors'] + df['education'].value_counts()['Masters']
    number_of_lower_education = number_of_records - number_of_higher_education


    high_ed_and_high_earners = df[(df['salary'] == '>50K') & ((df['education'] == 'Doctorate') | (df['education'] == 'Masters') | (df['education'] == 'Bachelors'))]


    low_ed_and_high_earners = df[(df['salary'] == '>50K') & ((df['education'] != 'Doctorate') & (df['education'] != 'Masters') & (df['education'] != 'Bachelors'))]

    # percentage with salary >50K
    higher_education_rich = round((high_ed_and_high_earners.shape[0]/number_of_higher_education)*100,1)
    lower_education_rich = round((low_ed_and_high_earners.shape[0]/number_of_lower_education)*100,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    ### Tests
    # print("--------minworkhours--------")
    # print(min_work_hours)
    # print("----------------------------")
    #
    #
    # print("***********")
    # number_of_min_hours_workers = df['hours-per-week'].value_counts()[1]
    # print('Number of min hours workers')
    # print(number_of_min_hours_workers)
    # number_of_min_hours_workers_rich = df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")].shape[0]
    # print("###########")
    # print(number_of_min_hours_workers_rich)
    # # print(df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")])
    # print("***********")
    # ### End Tests

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    number_of_min_hours_workers = df['hours-per-week'].value_counts()[1]
    number_of_min_hours_workers_rich = df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")].shape[0]
    num_min_workers = df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")].shape[0]

    rich_percentage = round((number_of_min_hours_workers_rich/number_of_min_hours_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    ### Tests
    num_high_earners = df.value_counts('salary')

    # print("####### High Earners #######")
    # print(df.value_counts('native-country'))
    # print(num_high_earners)
    # # print()
    # # print(df[(df["native-country"]) & (df["salary"] == ">50K")])
    # # print(df['native-country'&'salary'])


    # print(df.groupby("native-country")['salary'].apply(lambda x: x == (df['salary'] == ">50K").count()))
    high_earners_by_country = df.groupby('native-country')['salary'].apply(lambda x: (x=='>50K').sum()).reset_index(name='number-high-earners')
    high_earners_by_country = high_earners_by_country.set_index('native-country')
    country_occurs = df['native-country'].value_counts()
    country_occurs = country_occurs.sort_index()

    high_earners_by_country['total-pop'] = country_occurs
    high_earners_by_country['percentage-of-high-earners'] = round((high_earners_by_country['number-high-earners']/high_earners_by_country['total-pop'])*100,1)


    # print(high_earners_by_country['percentage-of-high-earners'].idxmax())
    # # print(high_earners_by_country)

    # print('###############')


    highest_earning_country = high_earners_by_country['percentage-of-high-earners'].idxmax()
    highest_earning_country_percentage = high_earners_by_country['percentage-of-high-earners'].max()

    # Identify the most popular occupation for those who earn >50K in India.
    # print("######## Occupation for High Earners India #######")
    # Print value_counts of occupations where native-country = India
    all_occupation = df.value_counts('occupation')
    india_occupation_high_earn = df[df['native-country'] == 'India'].value_counts('occupation')
    # print(all_occupation)
    # print(india_occupation_high_earn.idxmax())
    #
    #
    # print("######## End Tests #######")


    top_IN_occupation = india_occupation_high_earn.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
