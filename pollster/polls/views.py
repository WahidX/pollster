from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, Choice

def index(request):
	context = {
		'message': 'Noice',
		'data': {
			'value': 1,
			'offset': 2,
		}
	}
	return render(request, 'polls/index.html', context)

def api(request):
    # data = [{'name': 'Peter', 'email': 'peter@example.org'},
    #         {'name': 'Julia', 'email': 'julia@example.org'}]
	data = {
		'status': 'ok'
	}
	return JsonResponse(data)
