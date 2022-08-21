# Author Name: Deziallia Morris
# Purpose: Create Airport Codes with Dictionary

# include airport, city and state with key as the code

AIRPORTS = {'ATL': 'Hartsfield-Jackson International Airport (Atlanta, GA)',
            'DFW': 'Dallas/Fort Worth International Airport (Dallas & Fort Worth, TX',
            'DEN': 'Denver International Airport (Denver, CO',
            'ORD': 'O\'Hare International Airport (Chicago, IL',
            'LAX': 'Los Angeles International Airport (Los Angeles, CA',
            'CLT': 'Charlotte Douglas International Airport (Charlotte, NC',
            'LAS': 'McCarran International Airport (Las Vegas, NV',
            'PHX': 'Phoenix Sky Harbor International Airport (Phoenix, AZ',
            'MCO': 'Orlando International Airport (Orlando, FL)',
            'SEA': 'Seattle-Tacoma International Airport (Seattle, WA)',
            'MIA': 'Miami International Airport (Miami, FL)',
            'IAH': 'George Bush Intercontinental Airport (Houston, TX)',
            'JFK': 'John F. Kennedy International Airport (New York City, NY)',
            'FLL': 'Fort Lauderdale-Hollywood International Airport (Fort Lauderdale, FL)',
            'SFO': 'San Francisco International Airport (San Francisco, CA',
            'EWR': 'Newark Liberty International Airport (Newark & New York City, NJ)',
            'MSP': 'Minneapolis-Saint Paul International Airport (Minneapolis & Saint Paul, MN)',
            'DTW': 'Detroit Metropolitan Airport (Detroit, MI)',
            'BOS': 'Logan International Airport (Boston, MA)',
            'PHL': 'Philadelphia International Airport (Philadelphia, PA',
            'STL': 'St. Louis Lambert International Airport (St. Louis, MO)',
            'BWI': 'Baltimore/Washington International Airport (Baltimore, MD)',
            'TPA': 'Tampa International Airport (Tampa, FL)',
            'SAN': 'San Diego International Airport (San Diego, CA)',
            'SLC': 'Salt Lake City International Airport (Salt Lake City, UT)',
            'IAD': 'Washington Dulles International Airport (Washington D.C., VA)',
            'BNA': 'Nashville International Airport (Nashville, TN)',
            'LGA': 'LaGuardia Airport (New York, NY)',
            'DAL': 'Dallas Love Field (Dallas, TX)',
            'DCA': 'Ronald Reagan Washington National Airport (Washington D.C., VA)',
            'PDX': 'Portland International Airport (Portland, OR)'}

NOT_FOUND = "Airport code not found in dictionaries"


def main():
    print("Welcome to the Airport Lookup Program:\n")

    user_input = input("Enter an airport code: ")

    search_dict(user_input.upper())


def search_dict(user_input):
    if user_input in AIRPORTS:
        print(AIRPORTS[user_input])

    elif user_input not in AIRPORTS:
        print(NOT_FOUND)


main()
