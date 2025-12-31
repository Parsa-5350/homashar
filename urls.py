from django.urls import path
from . import views 

app_name = 'homashahr'

urlpatterns = [
    path('', views.home , name='home'), # صفحه اصلی 
    path('manager/', views.home2, name='manager'), # صفحه ادمین شهردار 
    path('martyr_page/', views.martyr_page, name='martyr_page'), # صفحه شهیدها 
    path('shahrdar/', views.shahrdar, name='shahrdar'), #صفحه شهردار 
    path('shora/', views.shora, name='shora'), #صفحه شورا 
    path('form_martyrs/', views.martyrs, name='form_martyrs'), #فرم شهیدها 
    path('form_mayor/', views.mayor, name='form_mayor'), # فرم شهردار 
    path('form_municipality/', views.municipality, name='form_municipality'), #فرم مشخصات هماشهر 
    path('form_news/', views.news, name='form_news'), # فرم اخبار 
    path('form_personnel/', views.personnel, name='form_personnel'), # فرم پرسنل 
    path('form_projects/', views.project, name='form_projects'), # فرم پروژه ها 
    path('form_councils/', views.councils, name='form_councils'), # فرم شورا 
    path('form_history/', views.history, name='form_history'), #فرم تاریخچه 
    path('form_celebrities/', views.celebrities, name='form_celebrities'), # فرم مشاهیر 
    path('list_celebrities/', views.list_celebrities, name='list_celebrities'), # لیست مشاهیر 
    path('list_history/', views.list_history, name='list_history'), # لیست تاریخچه 
    path('list_mayor/', views.list_mayor, name='list_mayor'), # لیست شهردار 
    path('list_municipality/', views.list_municipality, name='list_municipality'), # لیست مشخصات هماشهر 
    path('list_personnel/', views.list_personnel, name='list_personnel'), # لیست پرسنل 
    path('list_project/', views.list_project, name='list_project'), #لیست پروژه ها 
    path('list_councils/', views.list_councils, name='list_councils'), # لیست شورا ها 
    path('list_news/', views.list_news, name='list_news'), # لیست اخبار 
    path('list_martyrs/', views.list_martyrs, name='list_martyrs'), # لیست شهیدها 
    #path('history_delete/<int:id',views.histiry_delete,name='history'),
    #path('news_delete/<int:id',views.news_delete,name='news'),
    #path('project_delete/<int:id',views.project_delete,name='project'),
    #path('councils_delete/<int:id',views.councils_delete,name='councils'),
    #path('mayor_delete/<int:id',views.mayor_delete,name='mayor'),
    #path('celebrities_delete/<int:id',views.celebrities_delete,name='celebrities'),
    #path('martyrs_delete/<int:id',views.martyrs_delete,name='martyrs'),
    #path('personnel_delete/<int:id',views.personnel_delete,name='personnel'),
    #path('municipality_delete/<int:id',views.municipality_delete,name='municipality'),
    #path('history_form/<int:id',views.history_form,name='history'),
    #path('news_form/<int:id',views.news_form,name='news'),
    #path('project_form/<int:id',views.project_form,name='project'),
    #path('councils_form/<int:id',views.councils_form,name='councils'),
    #path('mayor_form/<int:id',views.mayor_form,name='mayor'),
    #path('celebrities_form/<int:id',views.celebrities_form,name='celebrities'),
    #path('martyrs_form/<int:id',views.martyrs_form,name='martyrs'),
    #path('personnel_form/<int:id',views.personnel_form,name='personnel'),
    #path('municipality_form/<int:id',views.municipality_form,name='municipality'),
]