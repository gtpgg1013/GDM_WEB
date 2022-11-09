from django.urls import path

from . import views

app_name = 'gan_dm'

urlpatterns = [
    path('', views.index, name='index'),
    path('train', views.train, name='train'),
    path('inference/<int:gen_model_id>', views.inference, name='inference'),
    path('download/<int:rds_id>', views.download, name='download'),
    path('finish_rds/<int:rds_id>/', views.finish_rds, name='finish_rds')
]