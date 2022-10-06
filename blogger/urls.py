"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import *
from blog.views import *
from Admin.views import *

urlpatterns = [
    path('',landingPage),
    path(
        "<int:page>",
        landingPage,
        name="terms-by-page"
    ),
    path('admin/', admin.site.urls),
    path('login/',showLogin),
    path('log_in/',loginUser),
    path('logout/',logout),
    path('register/',showRegister),
    path('register/save/',register),
    path('post/create/',new_post),
    path('post/store/',store_post),

    path('subscribe/<int:id>',categorySubscribe),
    path('unsubscribe/<int:id>',categoryUnSubscribe),
    path('category/posts/<int:id>',categoryPosts),
    path('post/<int:id>',post),
    path('post/comment/store/',storeComment),
    path('post/like/<int:id>',like),
    path('post/dislike/<int:id>',dislike),

    path('manage/blogger/',panel),
    path('manage/users/',users),
    path('manage/user/add/',addUser),
    path('manage/makeadmin/<int:id>',makeAdmin),
    path('manage/removeadmin/<int:id>',removeAdmin),
    path('manage/user/delete/<int:id>',deleteUser),
    path('manage/user/block/<int:id>',blockUser),
    path('manage/user/edit/form/<int:id>',showEditForm),
    path('manage/user/edit/<int:id>',editUser),

    path('manage/categories/',categories),
    path('manage/category/add/form/',addCategoryForm),
    path('manage/category/add/',addCategory),
    path('manage/category/edit/form/<int:id>',editCategoryForm),
    path('manage/category/edit/<int:id>',editCategroy),
    path('manage/category/delete/<int:id>',deleteCategroy),
    
    path('manage/posts/',posts),
    path('manage/post/add/form/',addPostForm),
    path('manage/post/add/',addPost),
    path('manage/post/edit/form/<int:id>',editPostForm),
    path('manage/post/edit/<int:id>',editPost),
    path('manage/post/delete/<int:id>',deletePost),
    
    
    path('manage/words/',words),
    path('manage/word/add/form/',addwordForm),
    path('manage/word/add/',addword),
    path('manage/word/edit/form/<int:id>',editwordForm),
    path('manage/word/edit/<int:id>',editword),
    path('manage/word/delete/<int:id>',deleteword),

    # path('manage/word/delete/<int:id>',searchRequest),
    path('search/',searchResult),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

