from django.shortcuts import render, redirect
from .models import TweetModel

# Create your views here.

def home(request):
    user = request.user.is_authenticated # 로그인이 되어 있는지 확인하는 기능
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user  # 사용자의 전체 정보를 불러옴
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content', '')
        my_tweet.save()
        return redirect('/tweet')