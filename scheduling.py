#! /usr/bin/env python3
from datetime import datetime
from calendar import monthrange

list_of_RA = ['Biplab', 'Vibhu', 'Atsushi', 'Gaelle', 'Jenski', 'Emi']
duty_schedule_dictionary = {}

#listing weekend and weekdays
def separate_weekdays_and_weekends(start_day, end_day, month, year):
    list_of_weekends = []
    list_of_weekdays = []


def assign_RAs(list_od_days, list_of_RA):
    pass



if __name__ == "__main__":

    # will ask the beginning_date and end_date via cmd parameters

    beginning_date = '02-01-2022'
    end_date = '05-20-2022'


    def find_total_days(beginning_date, end_date):

        # only one year because the idea is that the months will fall
        # in the same year

        start_month = beginning_date.split("-")[0]
        start_day = beginning_date.split("-")[1]
        year = beginning_date.split("-")[2]

        end_month = end_date.split("-")[0]
        end_day = end_date.split("-")[1]

        for month in range(start_month, end_month+1):

            days_in_month_dict = {'Weekends': [], 'Weekdays': []}
            number_of_days_in_month = monthrange(year, month)[1]
            if month == start_month:
                start_day = start_day
            else:
                start_day = 1
            if month == end_month:
                end_date = end_day
            else:
                end_day = number_of_days_in_month

            for d in range(start_day, end_day+1):
                day = datetime(year, month, d)
                if day > 4:
                    days_in_month_dict['Weekend'].append(day)
                else:
                    days_in_month_dict['Weekdays'].append(day)
            
