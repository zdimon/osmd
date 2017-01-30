from django.shortcuts import render
from django.shortcuts import render_to_response
from page.models import *
from django.shortcuts import render_to_response, get_object_or_404
# Create your views here.

def index(req):
    page = Page.objects.get(slug='index')
    subjects = Subject.objects.all()
    return render_to_response('index.html',{'page': page, 'subjects': subjects})


def subject(request,id):
    subject = get_object_or_404(Subject, id=id)
    context = {'subject': subject }
    return render_to_response('subject.html', context)

def n():
    pass
