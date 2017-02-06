from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from models import Reviews, Evaluation

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     # employee = Employee.objects.create(
#     #     email="pedro.kong@company.com",
#     #     first_name="Pedro",
#     #     last_name="Kong"
#     # )
#     # employee.save()
#     context = Employee.objects.all()
#     #
#     # # Syntax rquest + Link to Template + optional context
#     return render(request, 'review/index.html', {'employees':context})
################################################################################
def index(request):
    return render(request, 'review/index.html', {})

def reviews(request):
    # review_list = Reviews.objects.all()
    review_list = Reviews.objects.all().order_by('+hotel_name')
    paginator = Paginator(review_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        review_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        review_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        review_list = paginator.page(paginator.num_pages)
#     #### Filter: Future work ####
#     review_positiv = Reviews.objects(review_eval = 'positiv').order_by('+hotel_name')
#     paginator = Paginator(review_positiv, 10) # Show 10 contacts per page
#     page = request.GET.get('page1')
#     try:
#         review_positiv = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         review_positiv = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         review_positiv = paginator.page(paginator.num_pages)
# ################################################################################
#     review_neutral = Reviews.objects(review_eval = 'neutral').order_by('+hotel_name')
#     paginator = Paginator(review_neutral, 10) # Show 10 contacts per page
#     page = request.GET.get('page2')
#     try:
#         review_neutral = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         review_neutral = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         review_neutral = paginator.page(paginator.num_pages)
# ################################################################################
#     review_negativ = Reviews.objects(review_eval = 'negativ').order_by('+hotel_name')
#     paginator = Paginator(review_negativ, 10) # Show 10 contacts per page
#     page = request.GET.get('page3')
#     try:
#         review_negativ = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         review_negativ = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         review_negativ = paginator.page(paginator.num_pages)
    context = {
    'reviews':review_list,
    #Future work
    # 'reviews_positiv':review_positiv,
    # 'reviews_neutral':review_neutral,
    # 'reviews_negativ':review_negativ
    }

    return render(request, 'review/reviews.html', context )

def evaluation(request):
    context = Evaluation.objects.all()
    # Syntax rquest + Link to Template + optional context
    return render(request, 'review/evaluation.html', {'evaluation':context})
