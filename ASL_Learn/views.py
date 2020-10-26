from django.shortcuts import render
import base64
import numpy as np
import cv2
import requests
p=False
def home(request):
    return render(request, 'ASL_Learn/home.html', {})
def imagedetection(request):
    print("works")
    b64_arr=request.POST['myData']
    text=request.POST['test']
    data=b64_arr[22:]
    PARAMS = {'data': data}
    print(text)

    response = requests.post(url='http://localhost:5000/predict?',data=PARAMS)
    predict=response.text[1]
    print(predict)
    global p
    p=False
    if text==predict:
        p=True
def result(request):
    global p
    print(p)
    return render(request , 'ASL_Learn/result.html' , {'p':p})
# Create your views here.
