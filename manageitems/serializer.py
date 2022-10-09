from venv import create
from rest_framework import serializers
from .models import Computer, Mouse, KeyBoard, Monitor

class ComputerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    brand = serializers.CharField(max_length=100)
    processor_speed = serializers.CharField(max_length=100)
    core_version = serializers.IntegerField()
    number_of_usbport = serializers.IntegerField()
    number_of_hdmiport = serializers.IntegerField()
    
    def create(self, data):
        return Computer.objects.create(**data)
    
    def update(self, instance, data):
        instance.brand = data.get('brand', instance.brand)
        instance.processor_speed = data.get('processor_speed', instance.processor_speed)
        instance.core_version = data.get('core_version', instance.core_version)
        instance.number_of_usbport = data.get('number_of_usbport', instance.number_of_usbport)
        instance.number_of_hdmiport = data.get('number_of_hdmiport', instance.number_of_hdmiport)
        instance.save()
        return instance
    
    
class MouseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    brand = serializers.CharField(max_length = 100)
    model = serializers.CharField(max_length = 100)
    type =  serializers.CharField(max_length = 100)
    colour = serializers.CharField(max_length = 100)
    
    def create(self,data):
        return Mouse.objects.create(**data)
    
    def update(self, instance, data):
        instance.brand = data.get('brand', instance.brand)
        instance.model = data.get('model', instance.model)
        instance.type = data.get('type', instance.type)
        instance.color = data.get('color', instance.color)
        instance.save()
        return instance
    
class KeyBoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True),
    brand = serializers.CharField(max_length=100), 
    model = serializers.CharField(max_length = 100),  
    type = serializers.CharField(max_length = 100), 
    colour = serializers.CharField(max_length=100),
    has_numeric_keypad = serializers.BooleanField(default = False), 
    has_back_light = serializers.BooleanField(default = False)
    
    
    def create(self, data):
        return KeyBoard.objects.create(**data)
    
    def update(self, instance, data):
        instance.brand = data.get("brand", instance.brand)
        instance.model = data.get("model", instance.model)
        instance.type = data.get("type", instance.type)
        instance.colour = data.get("colour", instance.colour)
        instance.has_numeric_keypad = data.get("has_numeric_keypad", instance.has_numeric_keypad)
        instance.has_back_light = data.get("has_back_light", instance.has_back_light)
        instance.save()
        return instance
    
    
class MonitorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    brand = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=100)
    screen_resolution = serializers.CharField(max_length=100) 
    list_of_ports = serializers.CharField(max_length= 100) 
    
    def create(self, data):
        return Monitor.objects.create(**data)
    
    def update(self, instance,data):
        instance.brand = data.get('brand', instance.brand),
        instance.version = data.get('version', instance.version),
        instance.screen_resolution = data.get('screen_resolution', instance.screen_resolution),
        instance.list_of_ports = data.get('list_of_ports', instance.list_of_ports)
        instance.save()
        return instance
    
        