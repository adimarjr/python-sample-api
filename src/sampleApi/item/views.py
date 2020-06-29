from django.shortcuts import render
from .forms import ItemModelForm
from .models import Item

def item_list_view(request):
    qs = Item.objects.all()
    template_name = 'item/list.html'
    context = {'item_list': qs}
    return render(request, template_name, context)


def item_create_view(request):
    form = ItemModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = ItemModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)  