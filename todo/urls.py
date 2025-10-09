from django.urls import path
from . import views

urlpatterns = [
    #Add task feature
    path('addTask/', views.addTask, name= 'addTask'),

    #Mark as Done feature
    path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),

    #Undo feature
    path('undoTask/<int:pk>/', views.undoTask, name='undoTask'),

    #Edit feature
    path('editTask/<int:pk>/', views.editTask, name='editTask'),

    #Delete feature
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    
]



