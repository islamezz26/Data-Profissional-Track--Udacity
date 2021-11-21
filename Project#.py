import time
import pandas as pd



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def check_input(input_str,input_type):
    while True :
        input_read =input(input_str)
        try:
            if input_read in {'chicago','new york','washington'}.lower() and input_type==1:
                break
            elif   input_read in{'all', 'january', 'february','march' ,'april' , 'may', 'june'}.lower() and input_type==2:  
                break
            elif   input_read in  {'all', 'saturday', 'sunday','monday' ,'tuesday' , 'wednesday', 'thursday','friday'}.lower() and input_type==3 :
                break 
            else:
                if input_type==1:
                    print('wrong  your choosing should be chicago,new york,washington' )
                if input_type==2:
                    print('wrong  your choosing should be all, january,february,march ,april , may, june' )
                if input_type==3:
                    print('wrong  your choosing should be all, saturday, sunday,monday ,tuesday ,wednesday, thursday,friday' )
        
        except ValueError : 
            print('sorry error input') 

    return input_type 

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
    city= check_input('chicago,new york,washington',1)

    # get user input for month (all, january, february, ... , june)
    month= check_input('which month',2)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day= check_input('which day',3)

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_timedelta['Start Time']

    #extract data and make new column for month and day
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()

    #FILTER OF DATA
    if month != 'all':
         months= {'january', 'february','march' ,'april' , 'may', 'june'}
         month=months.index[month] +1
         df=df[df['month']== month]    


    if day != 'all':
         df=df[df['day']== day.title]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    start_time=time.time()

    print("elipse time", (time.time()- start_time))
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df ('month').mode()[0])

    # display the most common day of week
    print(df ('day_of_week').mode()[0])

    # display the most common start hour
    print(df ('hour').mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df ('Start Station').mode()[0])

    # display most commonly used end station
    print(df ('End Station').mode()[0])

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


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df ['User Type'].value_counts())
      


    # Display counts of gender
    if city != 'washington':
      print(df ['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].mode()[0])
    print(df['Birth Year'].max()[0])
    print(df['Birth Year'].min()[0])



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
        user_stats(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
