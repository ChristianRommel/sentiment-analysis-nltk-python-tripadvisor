# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from el_pagination.decorators import page_templates
from django.shortcuts import render
from django.http import HttpResponse
from models import Reviews, Evaluation
################################################################################
# Examples
###############################################################################

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
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
    context = {

    }
    return render(request, 'review/index.html', context)



################################################################################
# Pagination Templates for Reviews
################################################################################
@page_templates({
    'review/positiv_page.html': 'positiv_page',
    'review/neutral_page.html': 'neutral_page',
    'review/negativ_page.html': 'negativ_page'
})
################################################################################
#     #### Filter: Future work --> Positiv | Neutral | Negativ ####
################################################################################
def reviews(request, template='review/reviews.html', extra_context=None):
    review_positiv = Reviews.objects(review_eval = 'positiv').order_by('+hotel_name')
    review_neutral = Reviews.objects(review_eval = 'neutral').order_by('+hotel_name')
    review_negativ = Reviews.objects(review_eval = 'negativ').order_by('+hotel_name')
    best_hotels = Reviews.objects.aggregate(
        {
            "$match": {"review_eval": "positiv"}
        },
        {
    	    "$group" : {"_id" : "$hotel_name", "sum" : { "$sum" : 1 } }
        },
        {
            "$sort" : {"sum" : -1}
        },
        {
            "$limit": 10
        }
    )

    context = {
    # 'reviews':review_list,
    #Future work
    'reviews_positiv':review_positiv,
    'reviews_neutral':review_neutral,
    'reviews_negativ':review_negativ,
    'best_hotels' : best_hotels
    }
    if extra_context is not None:
        context.update(extra_context)

    return render(request, 'review/reviews.html', context )
################################################################################
# Pagination Templates for Evaluation
################################################################################
@page_templates({
    'review/false_positiv_page.html': 'false_positiv_page',
    'review/false_neutral_page.html': 'false_neutral_page',
    'review/false_negativ_page.html': 'false_negativ_page'
})
def evaluation(request, template='review/evaluation.html', extra_context=None):
    evaluation = Evaluation.objects.all()
    for eval in evaluation:
        positiv_false = eval.positiv_false
        neutral_false = eval.neutral_false
        negativ_false = eval.negativ_false

    context = {
    'evaluation': evaluation,
    'positiv_false' : positiv_false,
    'neutral_false' : neutral_false,
    'negativ_false' : negativ_false
    }
    if extra_context is not None:
        context.update(extra_context)
    # Syntax rquest + Link to Template + optional context
    return render(request, 'review/evaluation.html', context)
