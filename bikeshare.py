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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("\nWhich city would you like to explore? New York City, Chicago City or Washington City?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Please enter a valid city. Try again.")
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
      month = input("\nWhich month would you like to explore? January, February, March, April, May, June? If you would like to explore all months, input 'all'\n").title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Please enter a valid month. Try again.")
        continue
      else:
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
      day = input("\nWhich day would you like to explore? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday? If you would like to explore all days, input 'all'\n").title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Please enter a valid day. Try again.")
        continue
      else:
        break


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
    
    # Load data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Derive month and day from Start Time and make them a new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filter by month
    if month != 'All':
        #Use index to derive the month number
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        
        # Add month to the dataframe if it exist 
        df = df[df['month'] == month]
        
        # Add day of week to df if it exist
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination_ctation = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost frequent combination of start station and end station trip:', start_station, " & ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")
    


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)


    # TO DO: Display counts of gender
    try:
      gender_category = df['Gender'].value_counts()
      print('\nGender Category:\n', gender_category)
    except KeyError:
      print("\nGender Types:\nThere is no data available for this month")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nThere is no data available for this month.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', most_recent_year)
    except KeyError:
      print("\nMost Recent Year:\nThere is no data available for this month.")

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', most_common_year)
    except KeyError:
      print("\nMost Common Year:\nThere is no data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        start_loc = start_loc + 5
        print(df.iloc[start_loc:start_loc+5])
        print("You have just viewed a sample of the data requested")
        #display data function can be added to the function below


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
