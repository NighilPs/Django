from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('book',views.book,name='book'),
    path('comment', views.comment, name='comment'),
    path('sign',views.sign,name='sign'),
    path('sub',views.sub,name='sub'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('old',views.old,name='old'),
    path('oldsubmit',views.oldsubmit,name='oldsubmit'),
    path('old_bookings',views.old_bookings,name='old_bookings'),
    path('submit',views.submit,name='submit'),
    path('doc',views.doc,name='doc'),
    path('doclogin',views.doclogin,name='doclogin'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('appoinment',views.appoinment,name='appoinment'),
    path('edit',views.edit,name='edit'),
    path('save',views.save,name='save'),
    path('today',views.today_booking,name='today'),
    path('all',views.all,name='all'),
    path('date',views.date,name='date')

    #
]
