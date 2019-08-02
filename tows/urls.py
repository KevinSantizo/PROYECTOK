from django.urls import path
from tows import views

app_name = 'tows'
urlpatterns = [
    path('page/', views.show, name='page'),
    path('show-assignments/', views.AssignmentListView.as_view(), name='show-assignments'),
    path('new-crane/', views.create_crane_form, name='new-crane'),
    path('add-crane/', views.confirm_create_crane, name='add-crane'),
    path('new-pilot/', views.create_pilot_form, name='new-pilot'),
    path('add-pilot/', views.confirm_create_pilot, name='add-pilot'),
    path('new-assignment/', views.create_assignment_form, name='new-assignment'),
    path('add-assignment/', views.confirm_create_assignment, name='add-assignment'),
    path('delete/<int:assignment_id>/', views.delete_assignment, name='delete'),
    path('show-available/', views.show_available, name='show-available'),
    path('delete-available/<int:available_id>/', views.delete_available_assignment, name='delete-available'),

]

