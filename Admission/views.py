from django.shortcuts import render
from django.http import HttpResponse
import pickle

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request, 'index.html')


def admission(request):
    marks = float(request.POST['marks'])
    grade = float(request.POST['grade'])
    model_path = str(BASE_DIR) + '\\final_model.sav'
    model = pickle.load(open(model_path, 'rb'))
    out = f'Yay you {model.predict([[marks, grade]])}'
    return HttpResponse(str(out))

