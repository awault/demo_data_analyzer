import pandas as pd

# Read data from file
data = pd.read_csv('adult.data.csv')

# How many of each race are represented in this dataset?
r_c = data.value_counts('race')

# What is the average age of men?
avg_age_m = round(data[data['sex']=='Male']['age'].mean(),1)

# What is the percentage of people who have a Bachelor's degree?
ed_percent = round(data['education'].value_counts(normalize=True) * 100,1)
bachelors = ed_percent['Bachelors']

# What percentage of people with advanced education
adv_degree = ['Bachelors','Masters','Doctorate']
perc_adv_degree = round(ed_percent[adv_degree], 1)

# What percentage of people without advanced education
perc_no_adv_degree = 100 - perc_adv_degree

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
data['higher_ed'] = data['education'].isin(adv_degree)
salary_ed_table = pd.crosstab(data['higher_ed'],data['salary'],normalize='index')*100
adv_deg_rich = round(salary_ed_table.loc[True,'>50K'], 1)

# What percentage of people without advanced education make more than 50K?
no_adv_degree_rich = round(salary_ed_table.loc[False,'>50K'], 1)

# What is the minimum number of hours a person works per week
min_weekly_hours = min(data['hours-per-week'])

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
hr_per_week = data['hours-per-week'].value_counts().sort_index()
min_hr_count = hr_per_week.iloc[0]

data['min_hr_worked'] = data['hours-per-week']==1
min_hrs_salary_table = pd.crosstab(data['min_hr_worked'],data['salary'],normalize='index') * 100
min_hrs_wealthy = min_hrs_salary_table.loc[True,'>50K']

# What country has the highest percentage of people that earn >50K?
inc_by_country = pd.crosstab(data['native-country'],data['salary'])
inc_by_country['perc_over_50k'] = inc_by_country['>50K'] / (inc_by_country['>50K'] + inc_by_country['<=50K'])
sorted_inc_by_country = inc_by_country.sort_values(by='perc_over_50k',ascending=False)
top_country = sorted_inc_by_country.index[0]
top_country_percent = round(sorted_inc_by_country['perc_over_50k'][0]*100, 1)


# Identify the most popular occupation for those who earn >50K in India.
india_50k = (data['native-country'] == 'India') & (data['salary']=='>50K')
india_50k = data[india_50k]
occ_rank = india_50k['occupation'].value_counts(ascending=False)
top_occ = occ_rank.index[0]

###################################################################

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = data

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = r_c

    # What is the average age of men?
    average_age_men = avg_age_m

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = bachelors

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = perc_adv_degree
    lower_education = perc_no_adv_degree

    # percentage with salary >50K
    higher_education_rich = adv_deg_rich
    lower_education_rich = no_adv_degree_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min_weekly_hours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_hr_count
    rich_percentage = min_hrs_wealthy

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = top_country
    highest_earning_country_percentage = top_country_percent

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = top_occ

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
