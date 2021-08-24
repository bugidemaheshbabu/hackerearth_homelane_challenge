from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from core import utils
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def get_date_info(request, date):
    date_info_dict = utils.get_date_information(date)
    return JsonResponse(date_info_dict)


def get_state_info(request, state_name):
    state_info_dict = utils.get_state_information(state_name)
    return JsonResponse(state_info_dict)


def get_pinpoint_state_info(request, state_name, date):
    state_info_dict = utils.get_pinpoint_state_information(state_name, date)
    return JsonResponse(state_info_dict)


@csrf_exempt
def get_given_states_info(request):
    states_list = request.POST.get('STATES')
    states_list = json.loads(states_list)
    all_states_info = utils.get_all_states_information(states_list)
    return JsonResponse(all_states_info)

"""
import requests
states_list = ['Bihar', 'Panjab']
url = 'http://localhost:9000/core/get-given-states-info/'
my_obj = {'STATES':json.dumps(states_list)}
re = requests.post(url, my_obj)
re.content
"""