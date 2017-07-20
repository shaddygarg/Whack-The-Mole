from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import UserStat
# Create your views here.
@login_required
def profile(request):
    return render(request,'game/index.html')
@login_required
def game(request):
    return render(request,'game/game.html')
@login_required
def save(request):
    print 'executed1'
    score=request.POST['score']
    print score
    users=request.user.username
    data=UserStat.objects.create(username=users,score=score)
    data.save()
    return HttpResponse('Saved')
def leaderboard(request):
    highScores=UserStat.objects.all().order_by('score').reverse()
    return render(request,'game/leaderboard.html',{'highscores':highScores})
def logout(request):
    auth_logout(request)
    return render(request, 'registration/login.html')

