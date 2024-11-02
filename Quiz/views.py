from django.shortcuts import render, get_object_or_404, redirect
import json
from django.http import JsonResponse as j
# Create your views here.
from .models import *
from django.views.generic import ListView
from .forms import *
from django.contrib.auth.decorators import login_required
from Results.models import *
from Quiz.models import *
from MedApp.forms import *
def cours(request):
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_category')
    if categorie ==None and sub_categories==None :
        cours = cour.objects.all()
    elif categorie is not None:
        cours = cour.objects.filter(categorie__category = categorie)
    elif sub_categories is not None:
        cours = cour.objects.filter(sub_categorie__sub_category=sub_categories)
    categories = Category.objects.all()
    context = {'cours':cours,'categories':categories}
    return render(request,'dashboard/courses.html',context)



    
@login_required
def home(request):
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_category')
    user_semesters = request.user.profile.semestre.all()

    if categorie ==None and sub_categories==None :
        object_list = Quiz.objects.filter(semestre__in= user_semesters)
    elif categorie is not None:
        object_list = Quiz.objects.filter(categorie__module= categorie,semestre__in= user_semesters)
    elif sub_categories is not None:
        object_list = Quiz.objects.filter(sub_categorie__sous_module=sub_categories,semestre__in= user_semesters)
    categories  = Category.objects.filter(semestre__in= user_semesters)

    context ={'d':categories,'object_list':object_list}
    template_name='dashboard/home.html' 
    return render(request,template_name,context)

@login_required
def quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)
    questions = quiz.questions.all()
    user = request.user
    categorie = request.GET.get('categorie')
    sub_categories = request.GET.get('sub_category')
    user_semesters = request.user.profile.semestre.all()

    categories  = Category.objects.filter(semestre__in= user_semesters)


    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        
        if form.is_valid():
            user_semesters = request.user.profile.semestre.all()

            categories  = Category.objects.filter(semestre__in= user_semesters)
            score = 0
            total_questions = questions.count()
            result = Result.objects.create(quiz=quiz, user=user, score=0,resultat=0)
            results = []
            for question in questions:
                selected_answers = form.cleaned_data.get(f'question_{question.id}', [])
                correct_answers = list(question.answers.filter(is_correct=True))
                question_result = QuestionResult.objects.create(
                    result=result,
                    question=question,
                    is_correct=set(selected_answers) == set(correct_answers),
                    explication = question.explication,
                )
                
                question_result.selected_answers.set(selected_answers)
                question_result.correct_answers.set(correct_answers)
                question_result.explication = question.explication
                if question_result.is_correct:
                    score += 1
                results.append({
                    'question': question.text, 
                    'explication':question.explication, # Assuming 'text' is the field for question text
                    'selected_answers': selected_answers,
                    'correct_answers': correct_answers,
                    'd':categories,
                })
            result.score = score 
            

            if (score * 100) / total_questions > 0 :
                resultat = (score * 100) / total_questions
            else :
                resultat = 0
            result.resultat = resultat
        

            result.save()
                # Store the results

                

                # Create and save the result instance
            if request.method=='POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()
            else:
                form = ContactForm()
        
            # Calculate percentage
            
            return render(request, 'dashboard/result.html', {'d':categories,'score': score, 'total': total_questions, 'resultat': resultat, 'results': results,'form':form})

    else:
        form = QuizForm(questions=questions)
    categories  = Category.objects.filter(semestre__in= user_semesters)

    return render(request, 'dashboard/home_detail.html', {'d':categories,'quiz': quiz, 'form': form})
@login_required
def quiz_history_view(request):
    quiz_results = Result.objects.filter(user=request.user)
    return render(request, 'dashboard/quiz_history.html', {'results': quiz_results})
@login_required
def result_id(request,pk):
    result = Result.objects.get(id=pk)
    context = {'result':result}
    return render(request,'dashboard/result_id.html',context  )
