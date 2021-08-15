import csv
from datetime import datetime
from .models import StateWiseCovidDetails, StateWiseTesting, StateWiseTestingDetails

covid_19_india_file_path = "/datasets/covid_19_india.csv"


def convert_to_datetime_obj(date, time="00:00 PM"):
    if time[-2] == "PM":
        if time[1].isdigit():
            time = str(int(time[:2]) + 12)
        else:
            time = str(int(time[:1]) + 12)
    else:
        if time[1].isdigit():
            time = str(int(time[:2]))
        else:
            time = str(int(time[:1]))

    date_time_str = date + " " + time
    # print(date_time_str)
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H')
    return date_time_obj


def populate_databse_all():
    with open(covid_19_india_file_path) as csv_file:
        reader = csv.reader(csv_file)
        state_wise_details_objs = []
        for row in reader[1:]:
            date_time_obj = convert_to_datetime_obj(row[1], row[2])
            state_wise_details_objs.append(
                StateWiseCovidDetails(
                    date=date_time_obj,
                    state=row[3],
                    confirmed_indian_national=row[4],
                    confirmed_foreign_national=row[5],
                    cured=row[6],
                    deaths=row[7],
                    confirmed=row[8]
                )
            )
        StateWiseCovidDetails.objects.bulk_create(state_wise_details_objs)


    covid_vaccine_statewise_filepath = "/datasets/covid_vaccine_statewise.csv"

    with open(covid_vaccine_statewise_filepath) as csv_file:
        reader = csv.reader(csv_file)
        vaccine_statewise_objects = []
        for row in reader[1:]:
            date_time_obj = convert_to_datetime_obj(row[0])
            vaccine_statewise_objects.append(
                StateWiseTestingDetails(
                    date=date_time_obj,
                    state=row[1],
                    total_doses_administrated=row[2],
                    total_sessions_conducted=row[3],
                    total_sites=row[4],
                    first_dose_administrated=row[5],
                    second_dose_administrated =row[6],
                    males =row[7],
                    females = row[8],
                    transgender =row[9],
                    total_covaxin_administrated=row[10],
                    total_covisheild_administrated=row[11],
                    total_sputnik_administrated=row[12],
                    aefi=row[13],
                    age_range_18_45=row[14],
                    age_range_45_60=row[15],
                    age_range_gt_60=row[16],
                    total_individuals_vaccinated=row[17],
                )
            )
        StateWiseTestingDetails.objects.bulk_create(state_wise_details_objs)


    state_wise_testing_file_path = "/datasets/StatewiseTestingDetails.csv"

    with open(state_wise_testing_file_path) as csv_file:
        reader = csv.reader(csv_file)
        state_wise_details_objs = []
        for row in reader[1:]:
            date_time_obj = convert_to_datetime_obj(row[0])
            state_wise_details_objs.append(
                StateWiseCovidDetails(
                    date=date_time_obj,
                    state=row[1],
                    total_samples=row[2],
                    negatives=row[3],
                    positives=row[4]
                )
            )
        StateWiseTesting.objects.bulk_create(state_wise_details_objs)
