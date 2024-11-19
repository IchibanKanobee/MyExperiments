from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Subject, Question, get_all_descendant_subject_ids
from .serializers import QuestionSerializer, SubjectSerializer
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'This is the message from django!'})


@api_view(['POST'])
def add_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def add_subject(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def subject_list(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)



class QuestionPagination(PageNumberPagination):
    page_size = 1  # Number of questions per page
    page_size_query_param = 'page_size'
    max_page_size = 100


'''
@api_view(['GET'])
def question_list(request):
    subject_id = request.GET.get('subject_id')

    # Get the selected subject
    subject = Subject.objects.filter(id=subject_id).first()

    if not subject:
        return Response({'detail': 'Subject not found'}, status=404)
    
    questions = Question.objects.filter(subject_id=subject_id)
    paginator = QuestionPagination()
    result_page = paginator.paginate_queryset(questions, request)
    serializer = QuestionSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
'''

from django.http import JsonResponse
from django.core.paginator import Paginator

@api_view(['GET'])
def question_list(request):
    subject_id = request.GET.get('subject_id')
    page = request.GET.get('page', 1)

    if not subject_id:
        return JsonResponse({'error': 'subject_id is required'}, status=400)

    try:
        # Get all subject IDs including the selected subject and its children
        subject_ids = [subject_id] + list(get_all_descendant_subject_ids(subject_id))

        questions = Question.objects.filter(subject_id__in=subject_ids).order_by('question_id')
        
        paginator = Paginator(questions, 1)  # Paginate with 1 items per page
        paginated_questions = paginator.page(page)
        
        data = {
            'questions': list(paginated_questions.object_list.values()),
            'page': paginated_questions.number,
            'total_pages': paginator.num_pages,
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        question.delete()
        return JsonResponse({"message": "Question deleted successfully."}, status=200)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Question not found."}, status=404)
