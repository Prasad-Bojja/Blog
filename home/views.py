# Create your views here.
from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import logout
from django.http import*
from .models import*

def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'blog/home.html', context)


def login_view(request):
    return render(request, 'blog/login.html')

def register_view(request):
    return render(request, 'blog/register.html')



def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog/blog_details.html', context)


def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    print(context)
    return render(request, 'blog/see_blog.html', context)


def add_blog(request):
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        user = request.user  # Assuming you have authentication middleware enabled

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            # Create a new blog object
            BlogModel.objects.create(user=user, title=title, content=content, image=image)
            return redirect('see_blog')  # Redirect to a page displaying all blogs or a success page
    else:
        form = BlogForm()
    context['form'] = form
    return render(request, 'blog/add_blog.html', context)



def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        form = BlogForm(request.POST or None, request.FILES or None, instance=blog_obj)

        if request.method == 'POST' and form.is_valid():
            content = form.cleaned_data['content']
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']

            # Update the existing blog object
            blog_obj.content = content
            blog_obj.title = title
            blog_obj.image = image
            blog_obj.save()

            return redirect('blog_detail', slug=blog_obj.slug)

        context['blog_obj'] = blog_obj
        context['form'] = form
    except BlogModel.DoesNotExist:
        raise Http404("Blog does not exist")
    except Exception as e:
        print(e)

    return render(request, 'blog/blog_update.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')



def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')

'''def email_verification(request, token):
    try:
        profile = Profile.objects.get(token=token, is_verified=False)
        user = get_user_model().objects.get(id=profile.user.id)
        profile.is_verified = True
        profile.save()
        user.is_active = True  # You can set any additional activation logic here
        user.save()
        return render(request, 'verification_success.html')
    except Profile.DoesNotExist:
        return render(request, 'verification_failure.html')'''