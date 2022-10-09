
from django.contrib import admin
from django.urls import path
from .views import computer_view,computer_create,computer, mouse_view,mouse,mouse_create, monitor_view, monitor_create, monitor, keyboard_view, keyboard_create, keyboard

urlpatterns = [
    #Computer Routes
    path("", computer_create),
    path("computer/", computer_view),
    path("<int:pk>", computer),
    
    #Mouse Routes
    path("mouse/", mouse_view),
    path("mouse/<int:pk>", mouse),
    path("addmouse/", mouse_create),
    
    #Monitor
    path("monitor/", monitor_view),
    path("monitoradd/", monitor_create),
    path("monitor/<int:pk>", monitor),
    
    #Keyboard
    
    path("keyboard/", keyboard_view),
    path("keyboardadd/", keyboard_create),
    path("keyboard/<int:pk>", keyboard)
    
    
]
