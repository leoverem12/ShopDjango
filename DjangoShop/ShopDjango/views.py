from django.shortcuts import render
from .models import Cart, Item
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    item = Item.objects.all().order_by('id')
    paginator = Paginator(item, 2)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    
    page = paginator.get_page(page_num) 
    context = {'items': item, 'page': page, 'Items': page.object_list}
    
    return render(request=request, template_name="index.html", context=context)