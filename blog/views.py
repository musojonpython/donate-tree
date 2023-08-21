from django.shortcuts import render, get_object_or_404
from .models import PlantedTrees, MainPageStatic, AboutTrees, AllTreesCount
from datetime import datetime, timezone

def home(request):
    allTreesNumber = AllTreesCount.objects.all()[0]
    mainStatics = MainPageStatic.objects.all()

    treesToday = PlantedTrees.objects.filter(time=PlantedTrees.Time.Today)
    treesMonth = PlantedTrees.objects.filter(time=PlantedTrees.Time.Month)
    treesYear = PlantedTrees.objects.filter(time=PlantedTrees.Time.Year)

    time  = treesToday[0].deadline - datetime.now(timezone.utc)
    differToday = {
        "days": time.days,
        "hours": time.seconds//3600,
        "minutes": time.seconds // 60 % 60
    }

    time = treesMonth[0].deadline - datetime.now(timezone.utc)
    differMonth = {
        "days": time.days,
        "hours": time.seconds // 3600,
        "minutes": time.seconds // 60 % 60
    }

    time = treesYear[0].deadline - datetime.now(timezone.utc)
    differYear = {
        "days": time.days,
        "hours": time.seconds // 3600,
        "minutes": time.seconds // 60 % 60
    }

    context = {
        "treesToday": treesToday,
        "treesMonth": treesMonth,
        "treesYear": treesYear,
        "differToday": differToday,
        "differMonth": differMonth,
        "differYear": differYear,
        "mainStatics": mainStatics,
        "allTreesNumber": allTreesNumber
    }

    return render(request, 'index.html', context=context)

def donateProject(request):
    return render(request, 'donateProjects.html', context={})

def treeList(request):

    treesList = AboutTrees.objects.all()

    context = {
        "treesList": treesList
    }
    return render(request, 'treeList.html', context)

def faqList(request):
    return render(request, 'faqlist.html', context={})

def treeDetail(request, id):
    singleTree = get_object_or_404(AboutTrees, id=id)

    context = {
        "tree": singleTree
    }
    return render(request, 'treeDetail.html', context=context)

def donate(request):
    return render(request, 'donation.html', context={})

def register(request):
    return render(request, 'register.html', context={})

def login(request):
    return render(request, 'account/login.html', context={})


def companyPlantedTree(request):
    return render(request, 'companyTreeList.html', context={})

def plantedTree(request):
    return render(request, 'daraxtpage.html', context={})

def toshkentVil(request):
    return render(request, 'regions/toshkentVil.html', context={})
