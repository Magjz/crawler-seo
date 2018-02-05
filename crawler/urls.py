from django.urls import path
from . import views 


urlpatterns = [
    path('projet/', views.Project.as_view(), name="projet"), 
    path('projet/<int:id>', views.ProjectDetail.as_view(), name="projetDetail"), 
    path('crawler/', views.Crawler.as_view(), name="crawler"),
    # path('crawler/<int:id>', views.CrawlerDetail.as_view(), name="crawl-detail"),

]