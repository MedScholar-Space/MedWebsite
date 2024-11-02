from django.shortcuts import render
from .forms import *
from .models import *
def cours(request):
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_category')
    user_semesters = request.user.profile.semestre.all()
    if categorie ==None and sub_categories==None :
        cours = cour.objects.filter(semestre__in=user_semesters)
    elif categorie is not None:
        cours = cour.objects.filter(categorie__module = categorie,semestre__in=user_semesters )
    elif sub_categories is not None:
        cours = cour.objects.filter(sub_categorie__sous_module=sub_categories,semestre__in=user_semesters )
    categories = Category.objects.filter(semestre__in=user_semesters)

    context = {'cours':cours,'d':categories}
    return render(request,'dashboard/courses.html',context)
def course(request,pk):
    course = cour.objects.get(id=pk)
    context={'course':course}
    return render(request,'dashboard/course_id.html',context)
def resume(request):
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_categorie')
    if categorie == None and sub_categories==None :
        resumes = Resume.objects.all()
    elif categorie is not None:
        resumes = Resume.objects.filter(categorie__category = categorie)
    elif sub_categories is not None:
        resumes = Resume.objects.filter(sub_categorie__sub_category=sub_categories)
    categories = Category.objects.all()
    context = {'resumes':resumes,'categories':categories}
    return render(request,'dashboard/resumes.html',context)

def support_du_cours(request):
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_categorie')
    if categorie == None and sub_categories==None :
        support = support_cour.objects.all()
    elif categorie is not None:
        support = support_cour.objects.filter(categorie__category = categorie)
    elif sub_categories is not None:
        support = support_cour.objects.filter(sub_categorie__sub_category=sub_categories)
    categories = Category.objects.all()
    context = {'support':support,'categories':categories}
    return render(request,'dashboard/support.html',context)
    '''  '''

def home(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm
        
    context ={'form':form}
    return render(request,'index.html',context)
def test(request):
    modules = request.GET.get("modules")
    user_semesters = request.user.profile.semestre.all()
    categories = Category.objects.filter(semestre__semestre= modules,semestre__in=user_semesters  )
    modules =  Category.objects.filter(semestre__in=user_semesters  )

    context={'d':modules,'categories':categories}
    return render(request,'dashboard/modules.html',context)
def semestre_categories(request):
    user_semesters = request.user.profile.semestre.all()

    categories = Category.objects.filter(semestre__in=user_semesters)
    return render(request,'dashboard/index.html',context={'d':categories})