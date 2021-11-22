from django.db import models


class MovieRating(models.IntegerChoices):
    ROTTEN = 0
    REALLY_POOR = 1
    POOR = 2
    BAD = 3
    BELOW_AVERAGE = 4
    AVERAGE = 5
    OKAY = 6
    GOOD = 7
    AVERAGELY_GOOD = 8
    GREAT = 9
    EXCELLENT = 10
