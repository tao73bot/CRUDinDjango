from django.shortcuts import get_object_or_404, redirect, render,get_list_or_404
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, "index.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    form = TweetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)
    form = TweetForm(request.POST or None, request.FILES or None, instance=tweet)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
    return render(request,'tweet_form.html',{'form':form})

def tweet_delete(request,pk):
    tweet = get_object_or_404(Tweet, pk=pk, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(request,user)
        return redirect('tweet_list')
        # return redirect('login')
    return render(request, 'registration/register.html', {'form': form})