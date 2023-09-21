from django.shortcuts import render
from .models import *
from django.db.models import Count
from django.db.models import Count
from datetime import datetime
# Create your views here.
def index(request):
    features = Features.objects.all()[0:4]
    categories = Category.objects.all()[0:20]
    popular_posts = Jobs.objects.filter(trend=True)[0:8]
    recent_job = Jobs.objects.order_by('create_at')[0:10]
    jobs_by_locarion = Jobs.objects.values('country', 'cite').annotate(count=Count('id'))[0:10]
    categories = Category.objects.all()
    category_job_counts = []
    for category in categories:
        job_count = Jobs.objects.filter(category=category).count()
        category_job_counts.append((category.title, job_count))
        # print(category_job_counts)
        
    best_rating_jobs = Jobs.objects.order_by('-rating')[0:5]
    
    # title, description, auther, category, country, cite, create_at, update_at, trend, approve, link, applyed, type, time, slary, location, tage
    return render(request , 'index.html', {
        "features":features, 
        "categories":categories, 
        "popular_posts":popular_posts, 
        "recent_job":recent_job, 
        "jobs_by_locarion":jobs_by_locarion, 
        "category_job_counts":category_job_counts, 
        "best_rating_jobs":best_rating_jobs, 
        })

def single(request , id):
    jop_details = Jobs.objects.get(id=id)
    jobs_by_locarion = Jobs.objects.values('country', 'cite').annotate(count=Count('id'))[0:10]
    categories = Category.objects.all()
    category_job_counts = []
    for category in categories:
        job_count = Jobs.objects.filter(category=category).count()
        category_job_counts.append((category.title, job_count))
        
    best_rating_jobs = Jobs.objects.order_by('-rating')[0:5]
    
    return render(request , 'single.html', {
        "jop_details":jop_details, 
        "jobs_by_locarion":jobs_by_locarion, 
        "category_job_counts":category_job_counts, 
        "best_rating_jobs":best_rating_jobs, 
    })


def blog_home(request):
    jobs = Jobs.objects.all()[0:8]
    recent_job = Jobs.objects.order_by('create_at')[0:10]    
    auther = Profile.objects.filter(id=1)
    # Get the current year and month
    
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    # Query to retrieve posts by archive date or month
    archive_posts = Jobs.objects.filter(create_at__year=current_year, create_at__month=current_month).values('create_at__year', 'create_at__month').annotate(post_count=Count('id'))
    
   
    return render(request , 'blog-home.html', {
        "jobs":jobs,
        "auther":auther,
        
        "recent_job":recent_job,
        "archive_posts":archive_posts,
    })

def about_us(request):
    return render(request , 'about-us.html')

def category(request):
    return render(request , 'category.html')

def price(request):
    return render(request , 'price.html')


def contact(request):
    return render(request , 'contact.html')


def search(request):
    return render(request , 'search.html')

def elements(request):
    return render(request , 'elements.html')


