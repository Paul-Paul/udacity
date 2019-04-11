import time
import pandas as pd


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
    city = ''
    cities = ['chicago', 'new york city', 'washington']
    while city not in cities:
        city = input(' Would you like to see data for \'Chicago\', \'New \
York City\', or \'Washington?\'').lower()
        if city not in cities:
            print('There\'s no this city')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month = input('Which month? all, january, february, march, april, may, \
june?')
        if month not in months:
            print('wrong')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Which day? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?')
        if day in days:
            break
        else:
            print('wrong')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month # 1月 = 1
    df['week_day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]

    if day != 'all':
        #days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        df = df[df['week_day']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is: {}\n'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the most common day of week is: {}\n'.format(df['week_day'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour is: {}\n'.format(df['hour'].mode()[0]))

    print("\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is {}\n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most commonly used end station is {}\n'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    most_trip = df['Start Station'] + ' ' + '-' +  ' ' + df['End Station']
    print('the most frequent combination of start station and end station trip is {}'.format(most_trip.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is: {:.4f} minutes\n'.format((df['Trip Duration'].sum())/60))

    # TO DO: display mean travel time
    print('mean travel time is: {:.4f} minutes\n'.format((df['Trip Duration'].mean())/60))

    print("\nThis took {} seconds." .format(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types:\n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\ncounts of gender:\n')
        print(df['Gender'].value_counts())
    except KeyError:
        print('There\'s no Gender info\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        print('\nearliest year of birth: {}'.format(df['Birth Year'].min()))
        print('\nmost recent your of birth: {}'.format(df['Birth Year'].max()))
        print('\nmost common year of birth: {}'.format(df['Birth Year'].mode()[0]))
    except KeyError:
        print('There\'s no birth info\n')

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
