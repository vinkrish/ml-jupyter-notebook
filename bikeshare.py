import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for chicago, new york city or washington?\n')
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('please select one of the listed city')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month? january, february, march, april, may, june or all.\n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('please select from month listed')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day? monday, tuesday, wednesday, thursday, friday, saturday, sunday or all.\n').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('please select from day listed')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv('C:/Users/Vinay/Tutorials/Udacity/Nanodegree/Machine Learning Foundation/1.Introduction to Programming/Project/' + CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all' and day == 'all':
        return df[df['Start Time'].dt.month == ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1]
    elif month != 'all' and day != 'all':
        return df[(df['Start Time'].dt.month == ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1) & (df['Start Time'].dt.dayofweek == ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day))]
    elif day != 'all':
        return df[df['Start Time'].dt.dayofweek == ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day)]
    else:
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # display the most common month
    common_month = df['month'].mode()[0]
    print('most common month: ', common_month)

    # extract day of week from the Start Time column to create an dayofweek column
    df['dayofweek'] = df['Start Time'].dt.dayofweek

    # display the most common day of week
    common_dayofweek = df['dayofweek'].mode()[0]
    print('most common day of week: ', common_dayofweek)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('most common start hour: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most common start station: ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most common end station: ', common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination_all = df.groupby(["Start Station", "End Station"]).size().reset_index(name="Count")
    # print(frequent_combination_all)
    frequent_combination = frequent_combination_all['Count'].idxmax()
    print('most frequent combination of start station and end station trip: \n', frequent_combination_all.loc[frequent_combination])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time: ', df['Trip Duration'].sum()/60, 'minutes')

    # display mean travel time
    print('mean travel time: ', df['Trip Duration'].mean()/60, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('user type count: \n', user_type_count)
    print()

    try:
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('gender count: \n', gender_count)
        print()

        # Display earliest, most recent, and most common year of birth
        common_birth_year = df['Birth Year'].mode()[0]
        print('most common birth year: ', common_birth_year)
    except:
        print('City has no record for Gender and Birth Year!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
