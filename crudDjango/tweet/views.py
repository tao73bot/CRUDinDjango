from django.shortcuts import get_object_or_404, redirect, render,get_list_or_404
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})


def tweet_create(request):
    form = TweetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect('tweet_list')
    return render(request,'tweet_form.html',{'form':form})

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