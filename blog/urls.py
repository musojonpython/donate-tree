from django.urls import path
from blog.views import (
    home,
    companyPlantedTree,
    treeList,
    faqList,
    plantedTree,
    register,
    login,
    donate,
    donateProject,
    toshkentVil,
    treeDetail
)

urlpatterns = [
    path("", home, name="home"),
    path('tree-list', treeList, name="tree-list"),
    path('tree-detail/<int:id>', treeDetail, name="tree-detail"),
    path('company-planted-tree', companyPlantedTree, name="company-planted"),
    path('faq-list', faqList, name="faq-list"),
    path('planted-tree', plantedTree, name="planted-trees"),
    path('register', register, name='register'),
    # path('login', login, name="login"),
    path('donate', donate, name="donate"),
    path('donate-projects', donateProject, name="donate-projects"),
    path('toshkentVil', toshkentVil, name="toshkentVil")
    ]