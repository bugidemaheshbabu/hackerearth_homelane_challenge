from django.db import models
from datetime import datetime
# Create your models here.


# class State(models.Model):
#     name = models.CharField(max_length=250)
#

class StateWiseCovidDetails(models.Model):
    date = models.DateTimeField()
    state = models.CharField(max_length=250)
    confirmed_indian_national = models.CharField(max_length=100)
    confirmed_foreign_national = models.CharField(max_length=100)
    cured = models.IntegerField()
    deaths = models.IntegerField()
    confirmed = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.state}"


class StateWiseTesting(models.Model):
    date = models.DateTimeField()
    state = models.CharField(max_length=250)
    total_samples = models.IntegerField()
    negatives = models.IntegerField()
    positives = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.state}"


class StateWiseTestingDetails(models.Model):
    date = models.DateTimeField()
    # state = models.ForeignKey(State,
    #                           on_delete=models.CASCADE,
    #                           related_name='state'
    # )
    state = models.CharField(max_length=250)
    total_doses_administrated = models.IntegerField()
    total_sessions_conducted = models.IntegerField()
    total_sites = models.IntegerField()
    first_dose_administrated = models.IntegerField()
    second_dose_administrated = models.IntegerField()
    males = models.IntegerField()
    females = models.IntegerField()
    transgender = models.IntegerField()
    total_covaxin_administrated = models.IntegerField()
    total_covisheild_administrated = models.IntegerField()
    total_sputnik_administrated = models.IntegerField()
    aefi = models.IntegerField()
    age_range_18_45 = models.IntegerField()
    age_range_45_60 = models.IntegerField()
    age_range_gt_60 = models.IntegerField()
    total_individuals_vaccinated = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.state}"
