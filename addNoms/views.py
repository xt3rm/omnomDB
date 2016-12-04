from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import JournalEntry, UserGoal

def index(request):
        foodList = JournalEntry.objects.order_by('-tm')[:5]
        userGoal = UserGoal.objects.get(userID=1)
        print userGoal.kcal
        context = {'foodList' : foodList, 'userGoal' : userGoal }
        return render(request, 'addNoms/index.html', context)
