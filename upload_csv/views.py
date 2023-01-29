from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import pandas as pd
import csv

from .models import CsvTable

def Home (request) :
    return HttpResponse("""<h4>bonjour, bienvenu sur cette page pour tester notre API python
                         qui a comme fonction de charger les données depuis un csv, définit le bon modèle
                         de base de données sqlite (table) et à la fin procéder aux insertions des données ligne par ligne dans la table. <br>
                         Merci de taper /api à la barre de recherche pour y accéder. </h4>""")




class ApiTest(View):

    def get(self, request):
        data = pd.read_csv("/home/roumna/projects/Test/data.csv", sep="|")
        
        data.to_csv("/home/roumna/projects/Test/upload_csv/data_new.csv", index= False)

        with open('/home/roumna/projects/Test/upload_csv/data_new.csv') as file:
            reader = csv.reader(file)
            next(reader)

            CsvTable.objects.all().delete()
            i=100
            for row in reader:
                if i > 0 :
                    print(row)
                    CsvTable.objects.get_or_create(NUMDOS = row[0], NUMDOSVERLING= row[1], ANCART=row[2], 
                                            FILIERE=row[3], ETAPE= float(row[4]), VERLING= row[5], FORMAT= row[6])
                    i=i-1
                    continue                  
                break

    
        rows_list = list(CsvTable.objects.values())
        return JsonResponse(rows_list, safe=False) 

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ApiTest, self).dispatch(request, *args, **kwargs)
