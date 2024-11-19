from django.urls import path
from .views import hello_world, add_question, add_subject, subject_list, question_list, delete_question

urlpatterns = [
    path('hello-world/', hello_world, name='hello-world'),
    path('add-question/', add_question, name='add-question'),
    path('add-subject/', add_subject, name='add-subject'),
    path('subjects/', subject_list, name='subject-list'),
    path('questions/', question_list, name='question-list'),
    path('questions/<int:question_id>/delete/', delete_question, name='delete-question'),

]
