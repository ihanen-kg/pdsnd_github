import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # 1)(Adding comment) get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Would you like to see data for Chicago, New york, or Washington?  ")).lower()
        cities = ['chicago','new york' , 'washington']

        if city in cities :
            break
        else:
            print("Sorry, your response was not right.")
            continue


    # get user input for month (all, january, february, ... , june)

    while True:
            try:
                month = str(input("which month? january, february, march, april, may, , june or all. ")).lower()

            except ValueError:
                print("That\' not a valid response!")
            except KeyboardInterrupt:
                prtint()
                continue
            months = ['all','january','february','march','april','may','june' , 'all']
            if month.lower() in months:
                break
            else:
                print("Sorry, your response was not right.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            try:
                day = str(input("which day? Please type weekday or all days. ")).lower()
            except ValueError:
                print()
            except KeyboardInterrupt:
                print()

            days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            if day.lower() in days:
                break
            else:
                print("Please inter  weekday name")


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month: ", most_common_month )
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day: ", most_common_day )
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour: " ,most_common_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_st = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station is ', most_common_st )

    # display most commonly used end station
    most_common_en = df['End Station'].value_counts().idxmax()
    print("most commonly used end station is ", most_common_en )


    # display most frequent combination of start station and end station trip
    common_st_en = df[['Start Station', 'End Station']].mode().loc[0]
    print("most commonly used start station and end station : {}, {}".format(common_st_en[0], common_st_en[1]))

    print("\nThis took %sno seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    if city != 'washington':
    # Display counts of gender

        count_gender = df['Gender'].value_counts()

    # Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        most_common_year = birth_year.value_counts().idxmax()
        print("the most common birth year is ", most_common_year)
        most_recent = birth_year.max()
        print("the most recent birth year is ", most_recent)
        earliest_year = birth_year.min()
        print("the earliest birth year is ", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def more_raw_data(df):
    st = 0
    raw_data = input(" would you like to see 5 lines of raw data? Enter yes or no?\n")
    while raw_data.lower() == 'yes':
        df_data = df.iloc[st: st+5]
        print(df_data)
        st += 5
        raw_data = input("would you like to see more 5 lines of raw data? Enter yes or no?\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        more_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
