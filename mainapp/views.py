import json

from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.core import serializers
from .decorators import unauthenticated_user, allowed_users
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PostmanForm, PublishForm


@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin','postmans']) # 'postmans' to allow guests view home page
def home(request):
    posts = Post.objects.all()
    all_posts = Post.objects.all()
    posts_size = all_posts.count()
    categories_count = Category.objects.all().annotate(posts_count=Count('post'))
    context = {'posts':posts, 'posts_size':posts_size,'categories_count':categories_count}
    return render(request, "mainapp/home.html", context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def viewPost(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'mainapp/post.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def addPhoto(request):
    categories_count = Category.objects.all().annotate(posts_count=Count('post'))
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        # print('data',data)
        # print('image',image)
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        post = Post.objects.create(
            postman = request.user.postman,
            category = category,
            title = data['title'],
            description = data['description'],
            image = image
        )
        return redirect('/')

    context = {'categories': categories, 'categories_count':categories_count}
    return render(request, 'mainapp/addPhoto.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin','postmans'])
def load_post_data_view(request, **kwargs):
    category = request.build_absolute_uri()
    print(category) #http://127.0.0.1:8000/data/3/ this is why the category with query is not working
    print(request.POST['page'])
    page = request.POST['page']
    # num_posts = kwargs.get('num_posts')
    visible = 3
    # upper = num_posts
    # lower = upper - visible
    size = Post.objects.all()[(int(page) - 1) * 6:int(page) * 6].count()
    qs = Post.objects.all()[(int(page) - 1) * 6:int(page) * 6]
    print(qs)
    print(size)
    data = []
    for obj in qs:
        item = {
            'category':obj.category.name,
            'created': obj.created,
            'id': obj.id,
            'title': obj.title,
            'description': obj.description[0:200],
            'image': obj.image.url,
        }
        data.append(item)
    return JsonResponse({'data':data, 'size': size})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def view_category(request,**kwargs):
    categories_count = Category.objects.all().annotate(posts_count=Count('post'))
    all_posts = Post.objects.all()
    posts_size = all_posts.count()
    print(kwargs['category'])
    category = kwargs['category']
    file = open("dzen.txt", "r")
    content = file.readlines()
    print(content[0])
    file.close()
    background_text = content[0] if category == "culture" \
        else content[4] if category == "movies" \
        else content[2] if category == "sports" \
        else content[3] if category == "history" \
        else content[1]
    posts = Post.objects.filter(category__name = category)
    posts_filter = Post.objects.exclude(category__name = category)
    context={'posts':posts, 'category':category, 'posts_filter': posts_filter, 'background_text':background_text, 'categories_count':categories_count, 'posts_size':posts_size}
    return render(request, 'mainapp/category.html', context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def rate_post(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Post.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score':val}, safe=False)
    return JsonResponse({'success':'false'})

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='postmans')
            user.groups.add(group)
            Postman.objects.create(
                user=user,
                name=user.username,
            )
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            return redirect('/login')
    context = {'form':form}
    return render(request, 'register/register.html', context)

@unauthenticated_user # if we are logged in and go to /login, will be redirected to home page
def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('/') else
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,  "Username or Password is incorrect")
    context={}
    return render(request, 'register/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin','postmans'])
def userPage(request):
    postman = request.user.postman
    form = PostmanForm(instance=postman)
    if request.method == 'POST':
        form = PostmanForm(request.POST, request.FILES, instance=postman)
        if form.is_valid():
            form.save()
    user_name = request.user.username
    print(user_name)
    posts = request.user.postman.post_set.all() # all posts of that postman
    context = {'posts':posts, 'user_name':user_name, 'form':form}
    return render(request, 'register/user.html', context)

def userAddPublications(request):
    post_title=request.POST.get('titleValue')
    post_descr=request.POST.get('descrValue')
    post_author = request.POST.get('authorValue')
    post_category = request.POST.get('categoryValue')
    user = request.user.username
    category = Category.objects.get(name=post_category)
    postman=Postman.objects.get(name=user)
    publisher = Publisher.objects.create(
        publisher_name=post_author,
        category=category,
        publisher_title=post_title,
        country=post_descr,
        postman=postman
    )
    response = JsonResponse({'title':post_title, 'description': post_descr, 'author':post_author, 'category':post_category, 'user':user})
    return response
@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin','postmans'])
def userViewPublications(request):
    categories_count = Category.objects.all().annotate(posts_count=Count('post'))
    user = request.user.username
    all_posts = Post.objects.all()
    posts_size = all_posts.count()
    cat = Category.objects.all()
    publisher = Publisher.objects.all()
    postman = Postman.objects.order_by('-date_created')[0:3]
    filter_posts = Post.objects.order_by('-created')[0:3]

    context = {'user':user,'category_count':categories_count, 'all_posts':all_posts,'filter_posts':filter_posts, 'posts_size':posts_size, 'category':cat, 'publisher':publisher, 'postman':postman}
    return render(request, 'mainapp/viewPublication.html', context)
def userDeletePublications(request):
    id=request.POST.get('id')
    publisher = Publisher.objects.get(id=id)
    publisher.delete()
    response=JsonResponse({'error': False, 'errorMessage':'Deleted Successfully'})
    return response
def userEditPublications(request):
    update_id = request.POST.get('id')
    update_pub=Publisher.objects.get(id=update_id)
    print(update_pub)
    data = {
        'author': update_pub.publisher_name,
        'title': update_pub.publisher_title,
        'country': update_pub.country,
        'category':update_pub.category.name,
        'user': update_pub.postman.name
    }

    response=JsonResponse({'update_pub': data, 'error':False, 'errorMessage':'Updated Successfully' })
    return response
def userUpdatePublications(request):
    modalTitle = request.POST.get('modalTitle')
    update_publisher = Publisher.objects.get(publisher_name=modalTitle)
    edit_author=request.POST.get('editAuthor')
    edit_title=request.POST.get('editTitle')
    edit_country=request.POST.get('editCountry')
    edit_category=request.POST.get('editCategory')
    update_publisher.publisher_name = edit_author,
    update_publisher.publisher_title = edit_title,
    update_publisher.country=edit_country,
    update_publisher.category=Category.objects.get(name=edit_category)
    update_publisher.save()
    data = {
        'upd_author': update_publisher.publisher_name,
        'upd_title': update_publisher.publisher_title,
        'upd_country': update_publisher.country,
        'upd_cat': update_publisher.category.name
    }
    response=JsonResponse({'data': data, 'error':False})
    return response
def search_publication(request):
    game = request.POST.get('data')
    print(game)
    qs = Publisher.objects.filter(publisher_name__icontains=game)
    if len(qs) > 0 and len(game) > 0:
        data = []
        for pos in qs:
            item= {
                'publisher_name':pos.publisher_name,
                'publisher_title':pos.publisher_title,
                'country': pos.country,
                'cat': pos.category.name
            }
            data.append(item)
        results = data
    else:
        results = 'No Posts Found...'
    return JsonResponse({'dt':results})
