from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json


def index(request):
    return render(request,'mapa/mapa.html')

def get_manzanas(request):
	radio=request.GET.get('radio',"100")
	lat=request.GET.get('lat',"19.4")
	lng=request.GET.get('long',"-99.1")
	with connection.cursor() as cursor:
	 	cursor.execute("select manzanasporradio("+lng+","+lat+","+radio+")")
	 	results=cursor.fetchone()
	 	data= json.dumps(results[0])
	return HttpResponse(data, content_type='application/json')
	
