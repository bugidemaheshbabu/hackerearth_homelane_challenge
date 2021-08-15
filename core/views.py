from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .utils import get_date_information, get_state_information, get_pinpoint_state_information
# Create your views here.


def get_date_info(request, date):
    date_info_dict = get_date_information(date)
    return JsonResponse(date_info_dict)


def get_state_info(request, state_name):
    state_info_dict = get_state_information(state_name)
    return JsonResponse(state_info_dict)


def get_pinpoint_state_info(request, state_name, date):
    state_info_dict = get_pinpoint_state_information(state_name, date)
    return JsonResponse(state_info_dict)
