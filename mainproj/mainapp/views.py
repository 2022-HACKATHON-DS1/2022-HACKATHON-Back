from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostModelForm
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from selenium import webdriver
import time



# brower = webdriver.Chrome('./chromedriver.exe')
# url = 'https://www.instagram.com/explore/tags/%EC%9D%B8%EC%83%9D%EB%84%A4%EC%BB%B7%ED%8F%AC%EC%A6%88/'
# brower.get(url)
# 
# html = brower.page_source
# 
# soup = BeautifulSoup(html, 'html.parser')
# img1 = soup.select('div._aagv > img')[0]['src']
# print(img1)

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created')[:6]
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def mypage(request):
    # /?year=2022
    year = request.GET.get('year', None) # 쿼리스트링 X
    
    # 전체보기 선택시 최근 날짜(date) 순으로 정렬
    if year is None:
        posts = Post.objects.all().order_by('-date')
    # 해당 연도에 맞는 게시글만 보여주기
    else:
        posts = Post.objects.filter(date__year=year)

    queryset1 = Post.objects.all()
    count = queryset1.count()

    return render(request, 'mypage.html', {'posts':posts, 'count':count})

def postformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostModelForm()
    return render(request, 'newpost.html', {'form' :form})

def event(request):
    return render(request, 'event.html')

def reward(request):
    return render(request, 'reward.html')

def detail_img(request):
    return render(request, 'detail_img.html', {'img1':img1})

