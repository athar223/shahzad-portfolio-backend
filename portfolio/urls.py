from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('videos/', views.VideoListView.as_view(), name='video-list'),
    path('skills/', views.SkillListView.as_view(), name='skill-list'),
    path('contact/', views.ContactCreateView.as_view(), name='contact-create'),
    path('reviews/', views.ClientReviewListView.as_view(), name='review-list'),
    path('organizations/', views.OrganizationListView.as_view(), name='organization-list'),
    path('expertise/', views.ExpertiseListView.as_view(), name='expertise-list'),
    path('settings/', views.SiteSettingsView.as_view(), name='site-settings'),
]
