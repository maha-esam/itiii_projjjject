
from multiprocessing import context
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import get_user_model

from blog.models import BadWord, Category, Post
from django.contrib import messages

# Create your views here.

def replaceBadWord(words, text):
    string_words_list = text.split()

    result =''
    index = 0
    for word in words:

        stars = "*" * len(word.word) 
        for i in string_words_list:
            ind = string_words_list.index(i)
            if i == word.word:
                string_words_list[ind] = stars
        index += 1
    result = ' '.join(string_words_list)
    return result

def panel(request):
    User = get_user_model()
    users = User.objects.all().count()
    categories = Category.objects.all().count()
    posts = Post.objects.all().count()

    context = {
        'users':users,
        'categories':categories,
        'posts': posts,
    }
    return render(request,'adminpanel.html',context)

def users(request):
    User = get_user_model()
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request,'users.html',context)

def addUser(request):
    return HttpResponseRedirect('/register')

def makeAdmin(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)

    user.is_superuser = True

    user.save()

    return HttpResponseRedirect('/manage/users')

def removeAdmin(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)

    user.is_superuser = False

    user.save()

    return HttpResponseRedirect('/manage/users')

def deleteUser(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)

    user.delete()

    return HttpResponseRedirect('/manage/users')

def blockUser(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)

    user.is_active = False
    user.save()

    return HttpResponseRedirect('/manage/users')

def showEditForm(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)
    context={
        'user':user
    }

    return render(request,'edit_user.html',context)

def editUser(request,id):
    User = get_user_model()
    user = User.objects.get(pk=id)

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirm = request.POST.get('password_confirmation')
    if password == password_confirm:
        user.username= username
        user.email = email
        user.password= password
        user.save()

    return HttpResponseRedirect('/manage/users')

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'categories.html',context)

def addCategoryForm(request):
    return render(request,'add_category.html')

def addCategory(request):
    categroy = Category.objects.create(name=request.POST.get('name'))

    return HttpResponseRedirect('/manage/categories')

def editCategoryForm(request,id):
    category = Category.objects.get(pk=id)
    context={
        'category':category
    }
    return render(request,'edit_category.html',context)

def editCategroy(request,id):
    category = Category.objects.get(pk=id)

    category.name = request.POST.get('name')
    category.save()
    return HttpResponseRedirect('/manage/categories')

def deleteCategroy(request,id):
    category = Category.objects.get(pk=id)

    category.delete()

    return HttpResponseRedirect('/manage/categories')

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request,'manage_posts.html',context)

def addPostForm(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'add_post.html',context)

def addPost(request):
    category_id = request.POST.get('category_id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    category = Category.objects.get(pk=category_id)
    words = BadWord.objects.all()


    clean_title = replaceBadWord(words,title)
    clean_content = replaceBadWord(words,content)

    
    if(len(request.FILES) != 0):
        image = request.FILES['image']
    post = Post.objects.create(
        category = category,
        title = clean_title,
        image = image,
        content = clean_content,
        user = request.user
    )

    return HttpResponseRedirect('/manage/posts')
    
def editPostForm(request,id):
    categories = Category.objects.all()
    post = Post.objects.get(pk=id)
    context = {'categories':categories,'post':post}

    return render(request,'edit_post.html',context)

def editPost(request,id):
    category_id = request.POST.get('category_id')
    post = Post.objects.get(pk=id)

    title = request.POST.get('title')

    content = request.POST.get('content')
    category = Category.objects.get(pk=category_id)
    if(len(request.FILES) != 0):
        image = request.FILES['image']
    else:
        image = post.image

    post = Post.objects.update(
        category = category,
        title = title,
        image = image,
        content = content,
        user = request.user
    )

    return HttpResponseRedirect('/manage/posts')

def deletePost(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return HttpResponseRedirect('/manage/posts')

def words(request):
    words = BadWord.objects.all()
    context={
        'words':words
    }
    return render(request,'words.html',context)

def addwordForm(request):
    return render(request,'add_word.html')

def addword(request):
    word = BadWord.objects.create(
        word=request.POST.get('word')
    )
    return HttpResponseRedirect('/manage/words')

def editwordForm(request,id):
    word = BadWord.objects.get(pk=id)
    context={
        'word':word
    }
    return render(request,'edit_word.html',context)
    
def editword(request,id):
    word = BadWord.objects.get(pk=id)
    word.word = request.POST.get('word')
    word.save()
    return HttpResponseRedirect('/manage/words')

def deleteword(request,id):
    word = BadWord.objects.get(pk=id)
    word.delete()
    return HttpResponseRedirect('/manage/words')






















