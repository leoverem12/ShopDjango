from django.shortcuts import render
from .models import Cart, Item
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    context = {
        "items": [
            {
                "name": "Бажаю потужного здоров’я собі. Вам бажаю перемоги. Сьогодні хочу вам презентувати свій план перемоги, впевнений, вам сподобається. По-Перше, жорстко хочеться вже в НАТО. Прямо зараз, требую від західних колег прийняти рішення. Друге, много грошей нам давайте негайно, а то вже дихати неможливо. Третє, це, авжеж, те що раїся вороги, Україна найдемократичніша. І останнє, але не по важливості, це авжеж перемога. Нам потрібна перемога, тож це основний пункт. Може здатися, що ми не сильно парились на цим планом, і будете, праві. Ми для вас навіть презентацію в Паверпоінті не підготували.",
                "count": 2019
            },
            {
                "name": "Бетон",
                "count": 500
            },
            {
                "name": "Крюківський Вагонобудівний Завод",
                "count": 1
            }
        ]
    }
    item = Item.objects.all()
    paginator = Paginator(item, 2)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    
    page = paginator.get_page(page_num) 
    context = {'items': item, 'page': page, 'Items': page.object_list}
    
    return render(request=request, template_name="index.html", context=context)