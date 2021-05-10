from django.shortcuts import render

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