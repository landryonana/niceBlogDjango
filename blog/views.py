from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import (Paginator,
                                   PageNotAnInteger,
                                   EmptyPage)
from django.core.mail import send_mail
from django.db.models import Count

from .models import Category, Post, Link
from .forms import SearchForm, ContactEmailForm


# recents posts
recent_posts = Post.published.all()[:3]

# all link
links = Link.objects.all()[:3]


def post_about(request):
    about = 'about'
    return render(request, 'blog/about.html', {
        'about': about,
    })


def post_contact(request):
    contact = 'contact'
    sent = False
    if request.method == 'POST':
        form_contact = ContactEmailForm(request.POST)
        if form_contact.is_valid():
            data = form_contact.cleaned_data
            subject = f"{data['name']} contact you for {data['subject']}"
            message = f"He/She says that : {data['message']}"
            send_mail(subject, message,
                      data['email'], ['lndronana@gmail.com'])
            sent = True
            return redirect('blog:post_contact_share_email')
    else:
        form_contact = ContactEmailForm()

    return render(request, 'blog/contact.html', {
        'contact': contact,
        'sent': sent,
        'form_contact': form_contact,
    })


def post_search(request):
    form_search = SearchForm()
    query = None
    categories = Category.objects.all()
    results = []
    if 'query' in request.GET:
        form_search = SearchForm(request.GET)
        if form_search.is_valid():
            query = form_search.cleaned_data['query']
            results = Post.published.filter(title__contains=query)

    return render(request, 'blog/post_search.html', {
        'results': results,
        'form_search': form_search,
        'categories': categories,
    })


def contactSuccessEmail(request):
    return render(request, 'blog/contact_sucsess.html')


def post_list(request):
    categories = Category.objects.all()
    posts = Post.published.all()
    form_search = SearchForm()

    return render(request, 'blog/post_list.html', {
        'categories': categories,
        'recent_posts': recent_posts,
        'posts': posts,
        'form_search': form_search,
        'links': links,
    })


def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    print(category)
    posts_of_category = Post.objects.filter(
        category=category)
    print(posts_of_category)
    categories = Category.objects.all()
    form_search = SearchForm()

    return render(request, 'blog/post_list.html', {
        'category': category,
        'posts_of_category': posts_of_category,
        'form_search': form_search,
        'categories': categories,
        'recent_posts': recent_posts,
        'links': links,
    })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,)
    categories = Category.objects.all()
    form_search = SearchForm()
    # get all posts that have the same tag
    posts_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=posts_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-publish')[:4]

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form_search': form_search,
        'recent_posts': recent_posts,
        'categories': categories,
        'links': links,
        'similar_posts': similar_posts,
    })
