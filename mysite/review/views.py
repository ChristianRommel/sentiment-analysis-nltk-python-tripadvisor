from django.shortcuts import render

from django.http import HttpResponse
from models import Reviews

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
# ################################################################################
def index(request):
    context = Reviews.objects.all()
    # Syntax rquest + Link to Template + optional context
    return render(request, 'review/index.html', {'reviews':context})
