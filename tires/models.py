from django.db import models

from django.utils.translation import gettext_lazy as _


class Tire(models.Model):
    TIN_Number = models.CharField(_("TIN_Number"), max_length=25)
    tire_number = models.IntegerField(_("tire_number"),)
    tire_type = models.CharField(_("tire_type"), max_length=25, default='Old')
    activity_id = models.ForeignKey(
        'Activity', on_delete=models.CASCADE, default=None
    )

    location_id = models.ForeignKey(
        'Location', on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.TIN_Number + ' ' + self.tire_number


class Activity(models.Model):
    activity_date = models.DateField(_("activity_date"),)
    tire_id = models.ForeignKey(
        'Tire', on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.activity_date


class Location(models.Model):
    location = models.CharField(_("location"), max_length=25)
    
    def __str__(self):
        return self.location

# class Tin(models.Model):
#     TIN_Number = models.CharField(max_length=25)
#     tire_number = models.IntegerField()

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['TIN_Number', 'tire_number'], name='unique_tire')]

#     def __str__(self):
#         return self.TIN_Number + ' ' + self.tire_number
