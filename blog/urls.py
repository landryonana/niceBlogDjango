from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.post_list, name='post_list'),

    path('about/', views.post_about, name='post_about'),

    path('contact/', views.post_contact, name='post_contact'),

    path('contact/share/success/', views.contactSuccessEmail,
         name='post_contact_share_email'),

    path('search/', views.post_search, name='post_search'),

    path('<slug:category_slug>/', views.post_by_category,
         name='post_by_category'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),


]
