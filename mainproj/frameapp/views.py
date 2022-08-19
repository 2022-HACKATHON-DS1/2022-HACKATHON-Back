from django.shortcuts import render, redirect, get_object_or_404
from .models import Text,Image
from .forms import TextModelForm,ImageModelForm

def text(request):
    if request.method == 'POST':
        form = TextModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('background')
    else:
        form = TextModelForm()
    return render(request, 'text.html', {'form' :form})


def background(request):
	text_content = Text.objects.last()

	if request.method == 'POST' or request.method == 'FILES':
		pic = ImageModelForm(request.POST, request.FILES)

		if pic.is_valid():
			pic.save()
			return redirect('mypage')
	else:
		pic = ImageModelForm()
	
	return render(request, 'background.html', {'pic' :pic,'text_content':text_content})
