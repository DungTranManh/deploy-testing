from django.db import models

# Create your models here.
class Data(models.Model):
    ent_seq = models.IntegerField()
    keb = models.TextField()
    reb = models.TextField()
    name_type = models.TextField()
    trans_det = models.TextField()

    class Meta:
        ordering = ('ent_seq','keb','reb','trans_det')
    
