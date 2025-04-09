from django.urls import path
from .views import news_list, news_detail, HomaPageView, ContactPageView,page_404_View, about_pageView, \
    LocalNewsView, TechnologyNewsView, SportNewsView, XorijNewsView, \
    NewsDeleteView, NewsUpdateView, NewsCreateView

urlpatterns = [
    path('', HomaPageView.as_view(), name='home_page'),
    path('news/', news_list, name="all_news_list"),

    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),

    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404-page/', page_404_View, name='404_page'),
    path('about_page/', about_pageView, name='about_page'),

    path('local', LocalNewsView.as_view(), name="local_news_app"),
    path('xorij', XorijNewsView.as_view(), name="xorij_news_app"),
    path('technolgy', TechnologyNewsView.as_view(), name="texnalogiya_news_app"),
    path('sport', SportNewsView.as_view(), name="sport_news_app"),
]