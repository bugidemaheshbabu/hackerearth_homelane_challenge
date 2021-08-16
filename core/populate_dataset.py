import csv
from datetime import datetime
from .models import StateWiseCovidDetails, StateWiseTesting, StateWiseTestingDetails

covid_19_india_file_path = "core/datasets/covid_19_india.csv"


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


def vaccine_date_time_obj(date):
    return datetime.strptime(date, '%d/%m/%Y')


def populate_database_all():
    with open(covid_19_india_file_path) as csv_file:
        reader = list(csv.reader(csv_file))
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

    # populate StateWiseTestingDetails
    covid_vaccine_statewise_filepath = "core/datasets/covid_vaccine_statewise.csv"

    with open(covid_vaccine_statewise_filepath) as csv_file:
        reader = list(csv.reader(csv_file))
        vaccine_statewise_objects = []
        for row in reader[1:]:
            date_time_obj = vaccine_date_time_obj(row[0])
            vaccine_statewise_objects.append(
                StateWiseTestingDetails(
                    date=date_time_obj,
                    state=row[1],
                    total_doses_administrated=int(float(row[2])) if row[2] else 0,
                    total_sessions_conducted=int(float(row[3])) if row[3] else 0,
                    total_sites=int(float(row[4])) if row[4] else 0,
                    first_dose_administrated=int(float(row[5])) if row[5] else 0,
                    second_dose_administrated=int(float(row[6])) if row[6] else 0,
                    males=int(float(row[7])) if row[7] else 0,
                    females=int(float(row[8])) if row[8] else 0,
                    transgender=int(float(row[9])) if row[9] else 0,
                    total_covaxin_administrated=int(float(row[10])) if row[10] else 0,
                    total_covisheild_administrated=int(float(row[11])) if row[11] else 0,
                    total_sputnik_administrated=int(float(row[12])) if row[12] else 0,
                    aefi=int(float(row[13])) if row[13] else 0,
                    age_range_18_45=int(float(row[14])) if row[14] else 0,
                    age_range_45_60=int(float(row[15])) if row[15] else 0,
                    age_range_gt_60=int(float(row[16])) if row[16] else 0,
                    total_individuals_vaccinated=int(float(row[17])) if row[17] else 0
                )
            )
        StateWiseTestingDetails.objects.bulk_create(vaccine_statewise_objects)

    # populate StateWiseCovidDetails
    state_wise_testing_file_path = "core/datasets/StatewiseTestingDetails.csv"

    with open(state_wise_testing_file_path) as csv_file:
        reader = list(csv.reader(csv_file))
        state_wise_details_objs = []
        for row in reader[1:]:
            print(row)
            date_time_obj = convert_to_datetime_obj(row[0])
            state_wise_details_objs.append(
                StateWiseTesting(
                    date=date_time_obj,
                    state=row[1],
                    total_samples=int(float(row[2])) if row[2] else 0,
                    negatives=int(float(row[3])) if row[3] and row[3] != " " else 0,
                    positives=int(float(row[4])) if row[4] else 0
                )
            )
        StateWiseTesting.objects.bulk_create(state_wise_details_objs)
