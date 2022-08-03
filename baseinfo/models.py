from django.db import models

# Create your models here.
class Provinces(models.Model):
    provinceName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.provinceName)

    class Meta:
        verbose_name_plural = 'Provinces'

class ProvinceGeofence(models.Model):
    province = models.ForeignKey(Provinces,on_delete=models.CASCADE, null=False, blank=False)
    provinceLat = models.FloatField();
    provinceLong = models.FloatField();

    def __str__(self):
        return str(self.province) + '-' + str(self.provinceLat) + '-' + str(self.provinceLong)

    class Meta:
        verbose_name_plural = 'ProvinceGeofence'

class Regions(models.Model):
    regionName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.regionName)

    class Meta:
        verbose_name_plural = 'Regions'

class RegionsGeofence(models.Model):
    region = models.ForeignKey(Provinces,on_delete=models.CASCADE, null=False, blank=False)
    regionLat = models.FloatField();
    regionLong = models.FloatField();

    def __str__(self):
        return str(self.region) + '-' + str(self.regionLat) + '-' + str(self.regionLong)

    class Meta:
        verbose_name_plural = 'RegionsGeofence'