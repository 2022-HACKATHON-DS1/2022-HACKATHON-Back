from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostModelForm



from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
from frameapp.models import Text, Image
from frameapp.forms import TextModelForm,ImageModelForm

def text(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = TextModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('background')
    else:
        form = TextModelForm()
    
    
    return render(request, 'text.html', {'form' :form, 'post':post})


def background(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    text_content = Text.objects.last()

    if request.method == 'POST' or request.method == 'FILES':
        pic = ImageModelForm(request.POST, request.FILES)
        if pic.is_valid():
            pic.save()
            return redirect('detail')
        else:
            pic = ImageModelForm()
    return render(request, 'background.html', {'pic' :pic,'text_content':text_content, 'post':post})

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
