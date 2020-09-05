from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.utils import timezone
# Create your views here.

def home(request):
	posts = Posts.objects
	return render(request ,'Posts/home.html', {'posts': posts})



@login_required(login_url="/accounts/signup")
def create(request):
	if request.method == 'POST':

		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['images']:

			post = Posts()
			post.title = request.POST['title']
			post.body = request.POST['body']
			post.url = request.POST['url']
			post.icon = request.FILES['icon']
			post.image = request.FILES['images']
			post.pub_date = timezone.datetime.now()
			post.explored_by = request.user
			post.save()
			return redirect('/Posts/'+ str(post.id))

		else:
			return render(request ,'Posts/create.html', {'error':'All fields must be filled.'})

	else:
		return render(request ,'Posts/create.html')



def details(request, post_id):
	post = get_object_or_404(Posts, pk=post_id)
	return render(request, 'Posts/details.html', {'post':post})



@login_required(login_url="/accounts/signup")
def upvote(request, post_id):
	if request.method =='POST':
		post = get_object_or_404(Posts, pk=post_id)
		post.vote_total += 1
		post.save()
		return redirect('/Posts/'+ str(post_id))