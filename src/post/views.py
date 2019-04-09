from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_view(request, id=None):
    print(id)
    try:
        instance = Post.objects.get(id=id)
        if request.user.is_authenticated():
            context = {'title': 'IamWorkingFine', 'instance':instance}
    except Exception as e:
        context = {'title': 'NotWorkingFine', 'id':id}
    return render(request, 'index.html', context)
    #return HttpResponse('<p>HELLO</p>')
def post_list_view(request):

    instance = Post.objects.all()
    context = {'title': 'IamWorkingFine', 'instance':instance}
    return render(request, 'list.html', context)

def post_detail_view(request):
    return HttpResponse('<p>HELLO DETAIL VIEW</p>')
