from django.shortcuts import render

def index(request):
    '''Meal planner main page.'''
    return render(request, 'meal_plan/index.html')