from django.shortcuts import render
from .models import *
from django.db.models import Count

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
        print(category_job_counts)
        
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

def about_us(request):
    return render(request , 'about-us.html')

def category(request):
    return render(request , 'category.html')

def price(request):
    return render(request , 'price.html')

def blog_home(request):
    return render(request , 'blog-home.html')

def contact(request):
    return render(request , 'contact.html')

def single(request):
    return render(request , 'single.html')

def search(request):
    return render(request , 'search.html')

def elements(request):
    return render(request , 'elements.html')


