from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.core.paginator import Paginator

from blog.models import Category, Post, Comment

# Create your views here.
def landingPage(request,page=None):
    if page == None:
        page = 1
    categories = Category.objects.all()
    userCategories = Category.objects.filter(user = request.user.id )

    posts = Post.objects.filter(category_id__in=userCategories).order_by('created_at')
    paginator = Paginator(posts, per_page=5)
    page_number = paginator.get_page(page)

    context={
        'categories':categories,
        'posts':page_number,
        'page':page
    }
    return render(request,'landing_page.html',context)

def new_post(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'new_post.html',context)


def store_post(request):
    category_id = request.POST.get('category_id')
    title = request.POST.get('title')
    title = request.POST.get('title')

    content = request.POST.get('content')
    category = Category.objects.get(pk=category_id)
    if(len(request.FILES) != 0):
        image = request.FILES['image']
    post = Post.objects.create(
        category = category,
        title = title,
        image = image,
        content = content,
        user = request.user
    )

    return redirect('/1')

def categoryPosts(request,id):

    category = Category.objects.get(pk=id)

    posts = Post.objects.filter(category=category)

    context={
        'category':category,
        'posts':posts
    }
    return render(request,'category_posts.html',context)

def post(request,id):
    post = Post.objects.get(pk=id)
    context={
        'post':post
    }

    return render(request,'post.html',context)

def storeComment(request):
    post = Post.objects.get(pk=request.POST.get('post_id'))
    comment = request.POST.get('comment')

    save = Comment.objects.create(content=comment,post=post,user=request.user)

    return HttpResponseRedirect('/post/'+str(post.id))


def like(request,id):
    post = Post.objects.get(pk=id)
    if post.likes == None:
        post.likes = 1
    else:
        post.likes = post.likes + 1
        
    post.save()

    return HttpResponseRedirect('/post/'+str(post.id))


def dislike(request,id):
    post = Post.objects.get(pk=id)

    if post.dislikes == None:
        post.dislikes = 1
    else:
        post.dislikes = post.dislikes + 1
        
    post.save()

    return HttpResponseRedirect('/post/'+str(post.id))


def searchResult(request,page=None):
    search = request.GET.get('search')
    if page == None:
        page = 1
    categories = Category.objects.all()
    userCategories = Category.objects.filter(user = request.user )

    posts = Post.objects.filter(category_id__in=userCategories).filter(title__contains=search).order_by('created_at')
    paginator = Paginator(posts, per_page=5)
    page_number = paginator.get_page(page)
    # result = Post.objects.filter(title__contains=search)
    context={
        'categories':categories,
        'posts':page_number,
        'page':page
    }

    return render(request,'search.html',context)  




