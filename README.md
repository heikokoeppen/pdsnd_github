
### Date created
This project was created on February 24, 2021

### Project Title
Explore US Bikeshare Data - an Udacity Project

### Description
This project is a part of the Udacity Nanodegree Program "Programming for Data Science with Python"  

The project uses data provided by Motivate, a bike share system provider for many major cities in the United States.

Python is used to explore data related to bike share systems for Chicago, New York City an Washington.  

User can filter by city, month and day of week to compute statistics.
Additionally user can display raw-data or transposed sets of data

**Note:** Only the first half of 2017 is considered


### Requirements
To run the code, the environment should be setup as follows:
- Python 3.8.5
- Pandas 1.1.3
- Numpy 1.19.2
- Tabulate 0.8.9

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year




### Statistics Computed
###### 1 Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day
- total rentals at most popular hour
- percentage of rentals at most popular hour

**note:** This statistic can be stored on your local computer

###### 2 Popular stations and trip

- most common start station
- total rentals at most popular start station
- most common end station
- total rentals at most popular end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**note:** This statistic can be stored on your local computer

###### 3 Trip duration

- total travel time
- total rentals
- average travel time
  - number of trips with less / more duration than average travel time

- longest and shortest trip duration

**note:** This statistic can be stored on your local computer


###### 4 User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)
  - number of user which are older / younger than most common birth year
  - year of birth from oldest / youngest User


### Files used
- chicago.csv
- new_york_city.csv
- washington.csv

### Open Topics
Implement the ability to store User Statistics

### Credits
Thanks to [Udacity](https://www.udacity.com/) for their well-structured Nanodegree program  

 Special thanks to [Juno Lee](https://github.com/junolee) and [Richard Kalehoff](https://github.com/richardkalehoff), mentors at Udacity.
 They helped me to improve my skills in Python and Git / Github
