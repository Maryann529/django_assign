from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

CONNECTION_TYPE = (
    ("1","Wireless"),
    ("2","Wired")
    
)

KEYBOARD_TYPE = (
    ("1","Wireless"),
    ("2","Wired")
    
)

PORT_TYPE = (
    ("1","VGA"),
    ("2","HDMI"),
    ("3","Optional"),
    
)

PORT_CHOICES = [
    
    ('Serial', (
        
            ('vga', 'VGA'),
            ('hdmi', 'HDMI'),
            ('hdmi', 'HDMI')
        )
    ),
    
    ('Parrallel', (
        
            ('vga', 'VGA'),
            ('hdmi', 'HDMI'),
            ('hdmi', 'HDMI')
        )
    ),

]


class Computer(models.Model):
     brand = models.CharField(max_length = 100) 
     processor_speed = models.CharField(max_length=100)
     core_version = models.IntegerField() 
     number_of_usbport = models.IntegerField() 
     number_of_hdmiport = models.IntegerField()

# def __str__(self):
#     return self.brand




class Mouse(models.Model):
    brand = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    type =  models.CharField(
        choices = CONNECTION_TYPE,
        default = "1",
        max_length = 100
    )
    colour = models.CharField(max_length= 100)
    
    
class KeyBoard(models.Model):
    
    brand = models.CharField(max_length=100), 
    model = models.CharField(max_length = 100),  
    type = models.CharField(
        
            choices = CONNECTION_TYPE,        
            default = "1",
            max_length = 100
        ), 
    colour = models.CharField(max_length=100),
    has_numeric_keypad = models.BooleanField(default = False), 
    has_back_light = models.BooleanField(default = False)
    
    
    
class Monitor(models.Model):
    brand = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    screen_resolution = models.CharField(max_length=100) 
    list_of_ports = models.CharField(
        choices = PORT_CHOICES,
        default = "1",
        max_length= 100
    ) 
    