from django.shortcuts import render
import base64
import numpy as np
import cv2

def home(request):
    return render(request, 'ASL_Learn/home.html', {})
def imagedetection(request):
    b64_arr=request.POST['myData']
    print(b64_arr[22:])
    im_bytes = base64.b64decode(b64_arr[22:])
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    print(img)
# Create your views here.
