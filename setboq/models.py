from django.db import models
from django.urls import reverse
from .dbmodel import *


Categories = get_category()
Materials = get_material()
Objecttpyes = [("Family","Family"),("Material","Material")]
Schtypes = [('C', 'Piece'),('L', 'length'),('V', 'Volume'),('A', 'Area'),("W","Weight")]
Projects = [('IUA', 'IUA')]
Scheduleins = [("1","Yes"),("0","No")]

class setboq(models.Model):
    user = models.ForeignKey("auth.User",verbose_name="author",on_delete=models.CASCADE,related_name="boqs")
    category = models.CharField(max_length=20,choices=Categories,default=None)
    material = models.CharField(max_length=20,choices=Materials,verbose_name="Material or Type",default=None)
    schedulein = models.CharField(max_length=20,choices=Scheduleins,verbose_name="will It Count?",default=None,null=True)
    schtype = models.CharField(max_length=20,choices=Schtypes,default=None,null=True)
    boqdescription = models.TextField(verbose_name="BoQ Description")
    boqcodes = models.CharField(max_length=20,default=None)
    objecttype = models.CharField(max_length=20,choices=Objecttpyes,default=None)
    image = models.FileField(null=True, blank=True)
    project = models.CharField(max_length=20,choices=Projects,default=None)


    def get_absolute_url(self):
        #return "/setboq/{}/detail".format(self.id)
        return reverse("setboq:detail",args=[self.id])

    def get_create_url(self):
        #return "/setboq/{}/detail".format(self.id)
        return reverse("setboq:set")

    def get_update_url(self):
        #return "/setboq/{}/detail".format(self.id)
        return reverse("setboq:update",args=[self.id])

    def get_delete_url(self):
        #return "/setboq/{}/detail".format(self.id)
        return reverse("setboq:delete",args=[self.id])
    def get_boq_url(self):
        return reverse("setboq:getboq")



    class Meta:
        ordering=["-id"]

