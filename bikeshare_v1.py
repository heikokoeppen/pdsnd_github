"""
created with:
    python 3.8.5
    pandas 1.1.3
    numpy 1.19.2
"""


import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def raw_preview(city):
   
    """
    Display the  first five rows from the selected csv-file 
    and ask the user in a loop if five more rows.
    The Function is called by the get_filters() function
    should be displayed
    
    Parameters
    ----------
    city : str
        name of the city to analyze.

    Returns
    -------
    None.

    """
   
    # variable used to specify the number of rows to be returned
    raw_count = 5
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # while user was asked if raw data should be displayed in the get_filters() function
    # the first five lines will be displayed, before starting the loop
    print(tabulate(df.iloc[np.arange(0,5)], headers ="keys"))
    
    # While-loop is true, as long as the the variable is less than the maximum number of rows
    while (raw_count < df.shape[0]):
        check = input('continue (y/n): ')
        
        # IF Statement check, if user want to continue
        if check.lower() in ('y', 'yes'):
            
            #increase variable to display 5 more rows
            raw_count += 5
            print(tabulate(df.iloc[np.arange(0+raw_count,5+raw_count)], headers ="keys"))
            
        # Elif Statement check, if user want to break
        elif check.lower() in ('n', 'no'):
            break
        
        # Else STatement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue



def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns
    -------
    city : str
        name of the city to analyze..
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.

    """
    
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city. 
    while True:
        
        # User Input for city
        city = input("Would you like to see data for "
                     "Chicago, New York City or Washington? : ")
        city = city.lower()
        
        # If Statement checks if the input doesn't match with given names
        if city not in ('new york city', 'chicago', 'washington'):
            print("\nCould not recognize your input, please repeat")
            continue
        
        # when input match with given name, Else-Statement ask, if user want to call 
        # Function raw_preview(city)
        else:
            while True:
                raw_data = input("Would you like to check the data first? (y/n) ")
                
                # When User input 'y' or 'yes
                if raw_data.lower() in ('yes', 'y'):
                    
                    # Call Function raw_preview(city)
                    raw_preview(city)
                    break
                
                # Elif Statement breaks the loop, if user input is 'n' or 'no'
                elif raw_data.lower() in ('no', 'n'):
                    break
                
                # Else Statement check if the input is not recognized
                else:
                    print("\nCould not recognize your input, please repeat")
                    continue
            break

    # get user input for month
    while True:
        month = input("Which month do you want to choose? "
                      "January, February, March, April, May, June or all: ")
        month = month.lower()
        
        # If Statement checks if the input doesn't match with given months
        if month not in ('january', 'february', 'march', 'april',
                         'may', 'june', 'all'):
            print("\nCould not recognize your input, please repeat")
            continue
        else:
            break

    # get user input for day of week  
    while True:
        day = input("Finally, what day do you want to analyze? "
                    "Monday, Tuesday, Wednesday, Thursday, Friday "
                    "Saturday, Sunday or all : ")
        day = day.lower()
        
        # If Statement checks if the input doesn't match with given days
        if day not in ('monday', 'tuesday', 'wednesday',
                       'thursday', 'friday', 'saturday',
                       'sunday', 'all'):
            print("\nCould not recognize your input, please repeat")
            continue
        else:
            break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Parameters
    ----------
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.

    Returns
    -------
    df : Pandas DataFrame 
        containing city data filtered by month and day

    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    
    # extract day of the week from the Start Time column to create an day_of_week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter month if applicable
    if month != 'all':
        
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_num]

    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df, city, month, day):
    
    """
    Displays statistics on the most frequent times of travel.
    
    Parameters
    ----------
    df : Pandas DataFrame 
        containing city data filtered by month and day
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.
        
    Returns
    -------
    None.
    
    """
    # get the month that appears most often
    popular_month = df['month'].mode()[0]
    
    # get the day of week that appears most often
    popular_day = df['day_of_week'].mode()[0]
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # get the hour that appears most often
    popular_hour = df['hour'].mode()[0]
    
    # get total rentals at most popular hour
    tot_rent_pop_hour = df['hour'].where(df['hour'] == popular_hour)
    tot_rent_pop_hour = tot_rent_pop_hour.value_counts().values[0]
    
    # calculate percentage of rentals at most popular
    perc = 100 * tot_rent_pop_hour / df['month'].count()
    
    # get user input to display time statistics
    while True:
        time_stat = input('\nDo you want to examine time statistics (y/n)?: ')
        
        # When User input 'y' or 'yes
        if time_stat.lower() in ('yes', 'y'):
            print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()

            # display the most common month when month wasn't filtered
            if month == 'all':
                print('Most popular month:', popular_month)

            # display the most common day of week when day of week wasn't filtered
            if day == 'all':
                print('Most popular day:', popular_day)

            # display the most common start hour
            print('Most popular start hour:', popular_hour)
            
            # display total rentals at most popular hour
            print('\nTotal rentals at most popular hour: ', tot_rent_pop_hour)
            
            # display percentage of rentals at most popular hour
            print('For the most popular hour, that are {} percent of all rentals considering '
                  'filter settings'.format(perc.round(2)))
            
            # display filter settings
            print('\nFilter: city: {}, month: {}, day of week: {}.'
                  .format(city.title(), month.title(), day.title()))

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        
        # Elif Statement breaks the loop, if user input is 'n' or 'no'
        elif time_stat.lower() in ('no', 'n'):
            break
        
        # Else Statement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue


def station_stats(df, city, month, day):

    """
    Displays statistics on the most popular stations and trip.
    
    Parameters
    ----------
    df : Pandas DataFrame 
        containing city data filtered by month and day
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.
        
    Returns
    -------
    None.
    
    """

    # get start station that appears most often
    popular_start_station = df['Start Station']. \
        mode()[0]
        
    # get total rentals at most popular start station 
    pop_start_station_count = df['Start Station']. \
        value_counts().head(1).values[0]
        
    # get end station that appears most often
    popular_end_station = df['End Station'].mode()[0]
    
    # get total rentals at most popular end station
    pop_end_station_count = df['End Station']. \
        value_counts().head(1).values[0]
        
    # get the combination of start station and end station
    # that appears most often
    pop_comb = df.groupby(['Start Station', 'End Station']). \
        size().sort_values(ascending=False).head(1)

    # get user input to display station statistics
    while True:
        station_stat = input('\nDo you want to examine '
                             'station statistics (y/n)?: ')
        
        # When User input 'y' or 'yes
        if station_stat.lower() in ('yes', 'y'):
            print('\nCalculating The Most Popular Stations and Trip...\n')
            start_time = time.time()

            # display most commonly used start station and total rentals at this station
            print('\nMost popular start station: ', popular_start_station)
            print('Total rentals at this station: ', pop_start_station_count)

            # display most commonly used end station and total rentals at this station
            print('\nMost popular end station: ', popular_end_station)
            print('Total number of rentals finished at this station: ',
                  pop_end_station_count)

            # display most frequent combination of start station and end station trip
            print('\nMost frequent combination of Start Station and End station:'
                  '\n{} used {} times.'
                  .format(pop_comb.index[0], pop_comb.values[0]))
            
            
            print('\nFilter: city: {}, month: {}, day of week: {}.'
                  .format(city.title(), month.title(), day.title()))
            
            # display filter settings
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        
        # Elif Statement breaks the loop, if user input is 'n' or 'no'
        elif station_stat.lower() in ('no', 'n'):
            break
        
        # Else Statement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue


def trip_duration_stats(df, city, month, day):

    """
    Displays statistics on the total and average trip duration.
    
    Parameters
    ----------
    df : Pandas DataFrame 
        containing city data filtered by month and day
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.
        
    Returns
    -------
    None.
    
    """

    # get the total duration of all trips
    total_duration = df['Trip Duration'].sum()
    
    # get total rentals
    total_rentals = df['Trip Duration'].count()
    
    # get the average trip duration
    trip_dur_mean = df['Trip Duration'].mean()
    
    # count trips with less duration than average trip duration
    trips_less_avg = (df['Trip Duration'][df['Trip Duration'] <
                      df['Trip Duration'].mean()]).count()
    
    # count trips with more or equal duration than average trip duration
    trips_more_avg = (df['Trip Duration'][df['Trip Duration'] >=
                      df['Trip Duration'].mean()]).count()
    
    # get longest trip duration
    max_dur = df['Trip Duration'].max()
    
    # get shortest trip duration
    min_dur = df['Trip Duration'].min()

    # get user input to display trip statistics
    while True:
        trip_stat = input('\nDo you want to examine '
                          'trip statistics (y/n)?: ')
        
        # When User input 'y' or 'yes
        if trip_stat.lower() in ('yes', 'y'):
            print('\nCalculating Trip Duration...\n')
            start_time = time.time()

            # display total travel time and total rentals
            print('\nTotal duration: ', total_duration)
            print('\nTotal rentals: ', total_rentals)

            # display mean travel time
            print('\nAvg Duration: ', trip_dur_mean)
            
            
            # display trips with less duration than average travel duration
            print('\nCount of rentals with less duration than '
                  'average trip duration: ', trips_less_avg)
            
            # display trips with more or equal duration than average travel duration
            print('Count of rentals with more or equal duration '
                  'than average trip duration: ', trips_more_avg)
            
            # display longest travel time and shortest travel time
            print('\nMax Duration: ', max_dur)
            print('Min Duration: ', min_dur)
            
             # display filter settings
            print('\nFilter: city: {}, month: {}, day of week: {}.'
                  .format(city.title(), month.title(), day.title()))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        
        # Elif Statement breaks the loop, if user input is 'n' or 'no'
        elif trip_stat.lower() in ('no', 'n'):
            break
        
        # Else Statement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue
        
def user_stats(df, city, month, day):
    
    """
    Displays statistics on bikeshare users.
    
    Parameters
    ----------
    df : Pandas DataFrame 
        containing city data filtered by month and day
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.
        
    Returns
    -------
    None.
    
    """

    # count values for each user type
    user_types = df['User Type'].value_counts(). \
        rename_axis('User Types').reset_index(name='Counts')
        
    # count NaN values in column user type    
    empty_user_types = df['User Type'].isnull().sum()
    
    # get user input to display user statistics
    while True:
        user_stat = input('\nDo you want to examine '
                          'user statistics (y/n)?: ')
        
        # When User input 'y' or 'yes
        if user_stat.lower() in ('yes', 'y'):
            print('\nCalculating User Stats...\n')
            start_time = time.time()

            # Display counts of user types
            print('\n', user_types.to_string(index=False))
            
            # display missing information about user type
            if empty_user_types > 0:
                print('For {} rentals are no user type information available'.
                      format(empty_user_types))

            # Display counts of gender
            # This information is not available in all files.
            # Therefore it will be handled in a try Statement.
            try:
                
                # count values for each gender
                gender = df['Gender'].value_counts().rename_axis('Gender'). \
                        reset_index(name='Counts')
                        
                # count NaN values in column gender
                empty_gender = df['Gender'].isna().sum()
                
                # display counts of gender
                print('\n', gender.to_string(index=False))
                
                # display missing information about gender
                if empty_gender > 0:
                    print('For {} rentals are no gender information available'.
                          format(empty_gender))
                    
            # missing columns will produce a KeyError.
            # User get information that data are not available
            except KeyError:
                print('\nFor {} are no information about Gender available'.
                      format(city.title()))

            # Display earliest, most recent, and most common birth year
            # This information is not available in all files.
            # Therefore it will be handled in a try Statement.
            try:
                
                # get the earliest birth year
                old_birth = df['Birth Year'].min()
                
                # get the most recent birth year
                young_birth = df['Birth Year'].max()
                
                # get the most common birth year
                most_common_year = df['Birth Year'].mode()[0]
                
                # count user which are older than most common birth year
                older_than_common = (df['Birth Year'][df['Birth Year'] <
                                     df['Birth Year'].mode()[0]]).count()
                
                 # count user which are younger than most common birth year
                younger_than_common = (df['Birth Year'][df['Birth Year'] >=
                                       df['Birth Year'].mode()[0]]).count()
                
                # count NaN values in column Birth Year
                empty_birth = df['Birth Year'].isna().sum()
                
                # display the year of birth from oldest user
                print('\nThe oldest user was born in', int(old_birth))
                
                # display the year of birth from youngest user
                print('The youngest user was born in', int(young_birth))
                
                # display missing information about year of birth
                if empty_birth > 0:
                    print('For {} rentals are no birth information available'.
                          format(empty_birth))
                    
                # display most common year of birth
                print('\nThe most common birth year is: ', int(most_common_year))
                
                # display how many user are older 
                # than the most common year of birth
                print('{} user are older than the most common birth year.'.
                      format(older_than_common))
                
                # display how many user are younger or have the same age
                # than the most common year of birth
                print('{} user are younger or have the same birth year '
                      'than the most common birth year.'.
                      format(younger_than_common))
                
            # missing columns will produce a KeyError.
            # User get information that data are not available    
            except KeyError:
                print('\nFor {} are no information about birth year '
                      'available'.format(city.title()))
                
            # display filter settings
            print('\nFilter: city: {}, month: {}, day of week: {}.'
                  .format(city.title(), month.title(), day.title()))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        
        # Elif Statement breaks the loop, if user input is 'n' or 'no'
        elif user_stat.lower() in ('no', 'n'):
            break
        
        # Else Statement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue


def individual_data(df, city, month, day):
    
    
    """
    Displays individual data.
    
    Parameters
    ----------
    df : Pandas DataFrame 
        containing city data filtered by month and day
    city : str
        name of the city to analyze.
    month : str
        name of the month to filter by, or "all" to apply no month filter.
    day : str
        name of the day of week to filter by, or "all" to apply no day filter.
        
    Returns
    -------
    None.
    
    """
    
    # option to make sure, all data are displayed
    pd.set_option('display.max_columns', None)
    
     # get user input to display individual data
    while True:
        submit = input('Would you like to see individual data (y/n): ')
        
        # When User input 'y' or 'yes
        if submit.lower() in ('yes', 'y'):
            x = 0
            
            # Transpose the Dataframe an display first 5 records 
            print(df[x:x+5].transpose())
            
             # display filter settings
            print('\nFilter: city: {}, month: {}, day of week: {}.'
                  .format(city.title(), month.title(), day.title()))
            
            # While-loop is true, as long as the the variable is less than the maximum number of rows
            while (x < df.shape[0]):
                
                # get user input to continue display individual data
                cont = input('continue (y/n): ')
                
                # When User input 'y' or 'yes
                if cont.lower() in ('y', 'yes'):
                    x += 5
                    
                    # Transpose the Dataframe an display next 5 records
                    print(df[x:x+5].transpose())
                    
                    # display filter settings
                    print('\nFilter: city: {}, month: {}, day of week: {}.'
                          .format(city.title(), month.title(), day.title()))
                # Elif Statement breaks the loop, if user input is 'n' or 'no'
                elif cont.lower() in ('n', 'no'):
                    break
                
                # Else Statement check if the input is not recognized
                else:
                    print("\nCould not recognize your input, please repeat")
                    continue
            break
        
        # Elif Statement breaks the loop, if user input is 'n' or 'no'
        elif submit.lower() in ('n', 'no'):
            break
        
        # Else Statement check if the input is not recognized
        else:
            print("\nCould not recognize your input, please repeat")
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        individual_data(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ('yes', 'y'):
            break


if __name__ == "__main__":
	main()
