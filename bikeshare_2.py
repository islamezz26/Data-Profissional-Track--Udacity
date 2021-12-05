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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("please choose a city from chicago, new york city, washington: ").lower()
        if city not in CITY_DATA:
            print("choose correct city,please")

        else:
            break    

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("please choose a month from  january, february, ... , june: ").lower()
        months=["january",'february','march','april','may','june']
        if month != "all" and month not in months:
            print("enter a full valid month,please")

        else:
            break    


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("please choose a day from  monday, tuesday, ... sunday: ").lower()
        days=['monday','tuesday','wenaseday','thursday','friday','saturday','sunday']
        if day != "all" and day not in days:
            print("enter a full valid day,please")

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
    #load the data and convo the 'Start Time'
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #extract data and make new column for month and day
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()

    #FILTER OF DATA
    if month != 'all':
         months= ['january', 'february','march' ,'april' , 'may', 'june']
         month= months.index(month) +1
         df=df[df['month'] == month]    


    if day != 'all':
         df=df[df['day']== day.title()]
         
    return df     
def display_raw_data(df):
    i=0
    answer=input('would you like to display 5 raw/ yas or no' ).lower()
    pd.set_option('display.max_colums',None) 
    while True:
        if answer=='no':
            break
        print(df[i:i+5])
        answer=input('would you like to display 5 raw/ yas or no' ).lower()
        i+=5    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    start_time=time.time()

    print("elipse time", (time.time()- start_time))
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df ['month'].mode()[0])

    # display the most common day of week
    print(df ['day'].mode()[0])

    # display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df ['Start Station'].mode()[0])

    # display most commonly used end station
    print(df[ 'End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    GroupFaild=df.groupby(['Start Station','End Station'])
    print(GroupFaild.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df ['Trip Duration'].sum())    

    # display mean travel time
    print(df ['Trip Duration'].mean())    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df ['User Type'].value_counts())
      


    # Display counts of gender
    if 'Gender' in df:
      print(df ['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        print(int(df['Birth Year'].mode()[0]))
        print(int(df['Birth Year'].max()))
        print(int(df['Birth Year'].min()))



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
