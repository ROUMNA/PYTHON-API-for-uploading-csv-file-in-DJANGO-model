from django.db import models

class DataTable(models.Model) :
    NUMDOS = models.CharField('NUMDOS' , max_length=255)   
    NUMDOSVERLING = models.CharField('NUMDOSVERLING' , max_length=255) 
    ANCART = models.CharField('ANCART' , max_length=255)
    FILIERE = models.CharField('FILIERE' , max_length=255)
    ETAPE = models.IntegerField('ETAPE')
    VERLING = models.CharField('VERLING' , max_length=255) 
    FORMAT = models.CharField('FORMAT' , max_length=255) 

class CsvTable(models.Model) :  
    NUMDOSVERLING = models.CharField('NUMDOSVERLING' , max_length=255) 
    ANCART = models.CharField('ANCART' , max_length=255)
    FILIERE = models.CharField('FILIERE' , max_length=255)
    ETAPE = models.IntegerField('ETAPE')
    VERLING = models.CharField('VERLING' , max_length=255)
    NUMDOS = models.CharField('NUMDOS' , max_length=255) 
    FORMAT = models.CharField('FORMAT' , max_length=255)    
