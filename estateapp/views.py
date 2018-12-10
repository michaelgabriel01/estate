from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .models import Property
from .forms import SearchForm, PropertyForm
from .utils import paginate, search_by


class PropertyView(TemplateView):
    template_name = 'house.html'
    limit = 10
    search_fields = ['description', 'city', 'price', 'photo']

    def get(self, request):
        queryset = Property.objects.all().order_by('description')
        search_form = SearchForm(request.GET)
        has_house = queryset.exists()
        search_found = has_house

        if search_form.is_valid():
            queryset = search_by(request, queryset, self.search_fields)
            search_found = queryset.exists()
        
        house = paginate(request, queryset, self.limit)

            # return render(request, self.template_name, {'search_form': search_form})# 'search_form': search_form,
        return render(request, self.template_name, {'house': house, 'search_form': search_form,
            'search_found': search_found, 'has_house': has_house})


def home(request):
    photo = Property.objects.all()
    return render(request, 'home.html', { 'photo': photo })

def success(request):
    return render(request, 'success.html')

def photo_upload(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PropertyForm()
    return render(request, 'photo_upload.html', {
        'form': form
    })

def service(request):
    return render(request, 'service.html')
