from django.db import models

from django.utils.translation import gettext_lazy as _


class Tire(models.Model):
    tin_id = models.ForeignKey(
        'Tin', on_delete=models.CASCADE
    )


class Tin(models.Model):
    TIN_Number = models.CharField()
    tire_number = models.IntegerField

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['TIN_Number', 'tire_number'], name='unique_tire')]
    
    def __str__(self):
        return self.TIN_Number + ' ' + self.tire_number
