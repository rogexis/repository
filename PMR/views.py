from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class tiempo(object):
	def __init__(self, right_now):

		self.right_now = right_now

def welcome(request):

	pestañas = ['News', 'Dashboard', 'Diagrams', 'Trends', 'Warnings', 'Reports']
	now = datetime.now()

	ahora = tiempo(now)
	temp = 'template.html'
	#ruta = 'C:\\Users\\rogex\\Desktop\\PMR\\PMR\\PMR'
	#temp_wlc = open(f'{ruta}\\Templates\\{temp}')
	#tmp = Template(temp_wlc.read())
	#temp_wlc.close()

	#temp_wlc=loader.get_template(temp)

	#ctx = Context({'ahora':ahora.right_now, 'pestanias':pestañas})
	ctx = {'ahora':ahora.right_now, 'pestanias':pestañas}
	#contain = temp_wlc.render(ctx)

	return render(request, temp, ctx) 	#HttpResponse(contain)

def logout(request):
	return HttpResponse('Are you sure that you want to logout?')































