from .models import *
from datetime import datetime, timedelta


def get_state_wise_testings(state_wise_testings_qs):
    state_wise = []
    for q in state_wise_testings_qs:
        state_wise.append(
            {
                "date": q.date,
                "state": q.state,
                "total_samples": q.total_samples,
                "negatives": q.negatives,
                "positives": q.positives
            }
        )
    return state_wise


def get_state_wise_covid_details(state_wise_covid_details_qs):
    state_wise_covid = []
    for q in state_wise_covid_details_qs:
        state_wise_covid.append(
            {
                "date": q.date,
                "state": q.state,
                "confirmed_indian_national": q.confirmed_indian_national,
                "confirmed_foreign_national": q.confirmed_foreign_national,
                "cured": q.cured,
                "deaths": q.deaths,
                "confirmed": q.confirmed
            }
        )
    return state_wise_covid


def get_state_wise_vaccine_details(state_wise_vaccine_details_qs):
    state_wise_vaccine = []
    for q in state_wise_vaccine_details_qs:
        state_wise_vaccine.append(
            {
                "date": q.date,
                "state": q.state,
                "total_doses_administrated": q.total_doses_administrated,
                "total_sessions_conducted": q.total_sessions_conducted,
                "total_sites": q.total_sites,
                "males": q.males,
                "females": q.females,
                "transgender": q.transgender,
                "total_covaxin_administrated": q.total_covaxin_administrated,
                "total_covisheild_administrated": q.total_covisheild_administrated,
                "total_sputnik_administrated": q.total_sputnik_administrated,
                "age_range_18_45": q.age_range_18_45,
                "age_range_45_60": q.age_range_45_60,
                "age_range_gt_60": q.age_range_gt_60,
                "total_individuals_vaccinated": q.total_individuals_vaccinated
            }
        )
    return state_wise_vaccine


def get_date_information(date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d')
    next_day_obj = date_time_obj + timedelta(days=1)
    date_info = {
        "state_wise_testings": [],
        "state_wise_covid_details": [],
        "state_wise_vaccine_details": []
    }
    state_wise_testings_qs = StateWiseTesting.objects.filter(date__range=[date_time_obj, next_day_obj])
    state_wise_covid_details_qs = StateWiseCovidDetails.objects.filter(date__range=[date_time_obj, next_day_obj])
    state_wise_vaccine_details_qs = StateWiseTestingDetails.objects.filter(date__range=[date_time_obj, next_day_obj])
    date_info["state_wise_testings"] = get_state_wise_testings(state_wise_testings_qs)
    date_info["state_wise_covid_details"] = get_state_wise_covid_details(state_wise_covid_details_qs)
    date_info["state_wise_vaccine_details"] = get_state_wise_vaccine_details(state_wise_vaccine_details_qs)
    return date_info


def get_state_information(state_name):
    state_info = {
        "state_wise_testings": [],
        "state_wise_covid_details": [],
        "state_wise_vaccine_details": []
    }
    state_wise_testings_qs = StateWiseTesting.objects.filter(state=state_name)
    state_wise_covid_details_qs = StateWiseCovidDetails.objects.filter(state=state_name)
    state_wise_vaccine_details_qs = StateWiseTestingDetails.objects.filter(state=state_name)
    state_info["state_wise_testings"] = get_state_wise_testings(state_wise_testings_qs)
    state_info["state_wise_covid_details"] = get_state_wise_covid_details(state_wise_covid_details_qs)
    state_info["state_wise_vaccine_details"] = get_state_wise_vaccine_details(state_wise_vaccine_details_qs)
    return state_info


def get_pinpoint_state_information(state_name, date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d')
    next_day_obj = date_time_obj + timedelta(days=1)
    state_info = {
        "state_wise_testings": [],
        "state_wise_covid_details": [],
        "state_wise_vaccine_details": []
    }
    state_wise_testings_qs = StateWiseTesting.objects.filter(state=state_name, date__range=[date_time_obj, next_day_obj])
    state_wise_covid_details_qs = StateWiseCovidDetails.objects.filter(state=state_name, date__range=[date_time_obj, next_day_obj])
    state_wise_vaccine_details_qs = StateWiseTestingDetails.objects.filter(state=state_name, date__range=[date_time_obj, next_day_obj])
    state_info["state_wise_testings"] = get_state_wise_testings(state_wise_testings_qs)
    state_info["state_wise_covid_details"] = get_state_wise_covid_details(state_wise_covid_details_qs)
    state_info["state_wise_vaccine_details"] = get_state_wise_vaccine_details(state_wise_vaccine_details_qs)
    return state_info
