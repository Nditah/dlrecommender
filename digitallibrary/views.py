from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student, Item, Rating


def index(request):
    return HttpResponse("You're at the Digital Library index.")

def search(request):
    return HttpResponse("You're at the Digital Library search.")

# student
def students(request):
    student_list = Student.objects.order_by('fullname')[:50]
    template = loader.get_template('digitallibrary/index.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))

def studentDetail(request, student_id):
    response = "You're looking at details of student %s."
    return HttpResponse(response % student_id)

def studentRatings(request, student_id):
    response = "You're looking at ratings by student %s."
    return HttpResponse(response % student_id)

def item(request, item_id):
    response = "You're looking at the item %s."
    return HttpResponse(response % item_id)

# item
def items(request):
    return HttpResponse("You're at the Digital Library items.")

def itemDetail(request, item_id):
    response = "You're looking at details of item %s."
    return HttpResponse(response % item_id)

def itemRatings(request, item_id):
    response = "You're looking at students' ratings of item %s."
    return HttpResponse(response % item_id)

# rating
def ratings(request):
    return HttpResponse("You're at the Digital Library ratings.")

def ratingDetail(request, rating_id):
    response = "You're looking at details of rating %s."
    return HttpResponse(response % rating_id)

def rate(request, student_id, item_id):
    response = "You're looking at student %s rating of item %s."
    return HttpResponse(response % (student_id, item_id))

 