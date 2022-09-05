from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def buy(request):
    return render(request, 'buy.html')

def client(request):
    return render(request, 'client.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    return render(request, 'feedback.html')

def doctors(request):
    return render(request, 'doctors.html')

def index(request):
    return render(request, 'index.html')

# =============================================================

def docIndex(request):
    return render(request, 'doc/doc-index.html')

def docAbout(request):
    return render(request,'doc/doc-about.html')

def docNews(request):
    return render(request, 'doc/doc-blog-details.html')

def docBlog(request):
    return render(request, 'doc/doc-blog.html')

def docContact(request):
    return render(request, 'doc/doc-contact.html')

def docFeedback(request):
    return render(request, 'doc/doc-feedback.html')