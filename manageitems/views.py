from urllib import request
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Computer, Monitor, Mouse, KeyBoard
from .serializer import ComputerSerializer, MouseSerializer, MonitorSerializer, KeyBoardSerializer


@api_view(["GET"])
def computer_view(request):
    computer = Computer.objects.all()
    serializer = ComputerSerializer(computer, many=True)
    return Response(serializer.data)
    
    #here i was using the orignal way without rest
    
#     comp_list = list(computer.values())
#     return JsonResponse({
#         'computer': comp_list
# })

@api_view(["POST"])
def computer_create(request):
    serializer = ComputerSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(["GET", "PUT", "DELETE"])    
def computer(request, pk):
    computer = Computer.objects.get(pk=pk)
    if request.method == "GET":
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = ComputerSerializer(computer, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error())
    
    if request.method == "DELETE":
        computer.delete()
        return Response({
            "delete":True
        })
        
        
@api_view(["GET"])       
def mouse_view(request):
    mouse = Mouse.objects.all()
    serializer = MouseSerializer(mouse, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def mouse_create(request):
    serializer = MouseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def mouse(request, pk):
    mouse = Mouse.objects.get(pk = pk)
    if request.method == "GET":
        serializer = MouseSerializer(mouse)
        return Response(serializer.data) 
    
    if request.method == "PUT":
        serializer = MouseSerializer(mouse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        mouse.delete()
        return Response({
            "delete":True
        })
        

@api_view(["GET"])
def monitor_view(request):
    monitor = Monitor.objects.all()
    serializer = MonitorSerializer(monitor, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def monitor_create(request):
    serializer = MonitorSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])
def monitor(request, pk):
    monitor = Monitor.objects.get(pk=pk)
    if request.method == "PUT":
        serializer = MonitorSerializer(monitor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "GET":
        serializer = MonitorSerializer(monitor)
        return Response(serializer.data)
    
    if request.method == "DELETE":
        monitor.delete()
        return Response({"delete":True})
    
    

@api_view(["GET"])
def keyboard_view(request):
    keyboard = KeyBoard.objects.all()
    serializer = KeyBoardSerializer(keyboard, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def keyboard_create(request):
    serializer = KeyBoardSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET","PUT", "DELETE"])
def keyboard(request, pk):
    keyboard = KeyBoard.objects.get(pk=pk)
    
    if request.method == "GET":
        serializer = KeyBoardSerializer(keyboard)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = KeyBoardSerializer(keyboard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == "DELETE":
        keyboard.delete()
        return Response({"delete":True})
        
        
          