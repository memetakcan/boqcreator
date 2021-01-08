from django.db import models

# Create your models here.
Categories = [('B', 'Wall'),('F', 'Floor'),('G', 'Ceiling'),('T', 'Panel')]
Materials = [('01', 'Ceramic'),('02', 'Plaster'),('03', 'Stone'),('04', 'Wood')]
objecttpye = [("F","Family"),("M","Material")]



class getboq(models.Model):
    #objtype = models.CharField(max_length=20,choices=objecttpye,default=None)
    category = models.CharField(max_length=20,choices=Categories,default=None)
    material = models.CharField(max_length=20,choices=Materials,default=None)
    schedule = models.BooleanField(verbose_name="Metraja Girsin mi?",default=False)
    #boqdescription = models.TextField(verbose_name="BoQ Description")
    #boqcodes = models.CharField(max_length=20,default=None)

