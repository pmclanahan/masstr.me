from django.conf import settings
from django.db import models
from django.utils import timezone


LB_CONVERSION = 2.2046
LBS = 1
KGS = 2


class Mass(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    kilos = models.FloatField()
    recorded = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    @property
    def lbs(self):
        return self.kilos * LB_CONVERSION

    @lbs.setter
    def lbs(self, value):
        self.kilos = value / LB_CONVERSION

    def mass_value(self, unit=LBS):
        value = self.lbs if unit == LBS else self.kilos
        return round(value, 2)

    def __unicode__(self):
        return '{} {}'.format(self.user.get_short_name(), self.mass_value())
