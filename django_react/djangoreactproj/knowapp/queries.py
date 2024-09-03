from django_cte import With
from django.db.models import OuterRef, Subquery
from .models import Subject, Question

def get_recursive_subjects(subject_name):
    subject_cte = With.recursive(Subject.objects.filter(name=subject_name)).union(
        Subject.objects.filter(parent=OuterRef('subject_id'))
    )
    all_subjects = subject_cte.queryset()
    
    questions = Question.objects.filter(subject__in=Subquery(all_subjects.values('subject_id')))
    return questions

# Example usage
#questions = get_recursive_subjects('biology')
#for question in questions:
#    print(f"Question: {question.text}")
#    print(f"Answer: {question.correct_answer.text}")
