from django.urls import path

from .views import IndexView, GenericIndex
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/',GenericIndex.as_view(), name='contato')
    
    #path('404/', NotFoundView.as_view(), name='404'),
    #path('500/', ProcessErrorView.as_view(), name='500')
]