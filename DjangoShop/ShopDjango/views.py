from django.shortcuts import render
from .models import Cart, Item
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    item = Item.objects.all().order_by('id')
    paginator = Paginator(item, 2)
    print("1")
    if 'page' in request.GET:
        print("2")
        page_num = request.GET['page']
    else:
        print("3")
        page_num = 1
    print("4")
    page = paginator.get_page(page_num) 
    context = {'items': item, 'page': page, 'Items': page.object_list}
    print("5")
    return render(request=request, template_name="indexa.html", context=context)