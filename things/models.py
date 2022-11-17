from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Make a validator for the quantity field
def validate_quantity(q):
        if q<0  or q>100:
            #from django official documentation
            raise ValidationError(
            _('%(q)s is not in the required range of 0-100 (inclusive)'),
            params={'value': q},
        )

# Create your models here.
class Thing(models.Model): #extends django.db.models.Model
    name = models.CharField(max_length=30, unique=True,blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(unique=False,blank=False,validators=[validate_quantity])

    

    