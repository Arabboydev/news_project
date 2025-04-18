from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import News, Category
from .forms import ContactForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context=context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context=context)


# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:15]
#     local_one = News.published.filter(category__name="Mahalliy").order_by("-publish_time")[:1]
#     local_news = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_news': local_news,
#         'local_one': local_one,
#     }
#     return render(request, 'news/home.html', context=context)
class HomaPageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]
        context['xorij_xabarlar'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]
        context['sport_xabarlar'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:5]
        context['texnalogiya_xabarlar'] = News.published.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:5]
        context['ommabop_xabarlar'] = News.published.all().filter(category__name="Ommabop").order_by("-publish_time")[:5]

        return context


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'news/contact.html',context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun rahmat</h2>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.htnl', context=context)

# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur!")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context=context)


def page_404_View(request):
    context = {

    }
    return render(request,'news/404.html', context=context)


def about_pageView(request):
    context = {

    }
    return render(request, 'news/about.html', context=context)


class LocalNewsView(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = "mahalliy_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Mahalliy")
        return news


class XorijNewsView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = "xorij_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorij")
        return news


class TechnologyNewsView(ListView):
    model = News
    template_name = "news/texnalogiya.html"
    context_object_name = "texnalogiya_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnalogiya")
        return news


class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news


class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')


class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')



