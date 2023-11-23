import random
from datetime import date
from django.utils import timezone
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SalasCuna.settings")

# Initialize Django
django.setup()

import random
from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from SalasCuna_api.models import (
    Child,
    ChildAnswer,
    Answer,
    Question,
    Poll,
)

fake = Faker()

main_poll_name = 'Encuesta Socio Ambiental'
def create_poll():
    # for _ in range(num_polls):
    Poll.objects.create(name=main_poll_name)

poll_mock_questions = {
    'Single Choice':{
        'Question':{
            'type': 'Single Choice',
            'description':'Composicion familiar',
        },
        'Answer':{
            'type':'Boolean', #0 Boolean
            'descriptions': [
                'Nuclear',
                'Extensa',
                'Mono Femenina',
                'Mono Masculina',
                'Homoparental',
                'Familia de acogimiento',
                'Mono Femenina extensa',
                'Monoparental Masculino',
            ]
        },
    },
    'Multiple Choice':{
        'Question':{
            'type': 'Multiple Choice',
            'description': 'Ingresos generales del grupo familiar conviviente',
        },
        'Answer':{
            'type':'Float', #2 Float
            'descriptions': [
                'Por trabajo en relacion de dependencia formal',
                'Por trabajo en relacion de dependencia informal',
                'Por cuenta propia formal',
                'Por cuenta propia informal',
                'Cuota alimentaria formal',
                'Cuota alimentaria informal'
                'Por transferencia estatal',
                'Otro',
            ]
        },
    },
    'Parent Question':{
        'Parent':{
            'Question':{
                'type': 'Single Choice',
                'description':'Posee Obra Social?',
            },
            'Answer':{
                'type':'Boolean', #0 boolean
                'descriptions': ['Si', 'No']
            },  
        },
        'Child':{
            'Question':{
                'type': 'Single Option',
                'description':'Cual?',
            },
            'Answer':{
                'type':'String', #3 string
                'descriptions': ['Ingrese su obra social']
            },  
        },
    },
}

def create_answer(questionObject, answer_dict):
    answerObjects = []
    
    print(f'questionObject {questionObject}')
    print(f'answer_dict {answer_dict}')
    
    for element in answer_dict['descriptions']:
        answerObject = Answer.objects.create(
            question = questionObject,
            description = element,
            answerType = answer_dict['type'],
        )
        answerObjects.append(answerObject)
        
    return answerObjects

def create_question(parentObject, question_dict, pollObject):
    
    print(f'parentObject {parentObject}')
    print(f'question_dict {question_dict}')
    print(f'pollObject {pollObject}')
    
    questionObject = Question.objects.create(
        parentQuestion = parentObject,
        description = question_dict['description'],
        questionType = question_dict['type'],
        poll = pollObject
    )
    
    return questionObject


def create_questions_and_answers():
    main_poll = Poll.objects.all().filter(name=main_poll_name)[0]
    
    for key in poll_mock_questions:
        if key == 'Parent Question':
            parentQuestionObject = create_question(None, poll_mock_questions[key]['Parent']['Question'], main_poll)
            print(parentQuestionObject)

            parentQuestionAnswer = create_answer(parentQuestionObject, poll_mock_questions[key]['Parent']['Answer'])
            print(parentQuestionAnswer)

            childQuestionObject = create_question(parentQuestionObject, poll_mock_questions[key]['Child']['Question'], main_poll)
            print(childQuestionObject)
            
            childAnswer = create_answer(childQuestionObject, poll_mock_questions[key]['Child']['Answer'])
            print(childAnswer)
        else:
            questionObject = create_question(None, poll_mock_questions[key]['Question'], main_poll)
           
            questionAnswer = create_answer(questionObject, poll_mock_questions[key]['Answer'])
            print(questionAnswer)

# Call the functions to create the mock data
create_poll()
create_questions_and_answers()
# create_childAnswer(30)

print("Mock data has been successfully created.")

# manage.py makemigrations
# manage.py migrate
# mock_data.py
# mock_data_poll.py
# manage.py runserver

# def create_polls(num_polls):
#     for _ in range(num_polls):
#         Poll.objects.create(name=fake.word())
    

# def create_questions(num_questions):
#     polls = Poll.objects.all()
#     types = (
#         ('Single Option', 'Single Option'),
#         ('Single Choice', 'Single Choice'),
#         ('Multiple Choice', 'Multiple Choice'))
#     for _ in range(num_questions):
#         Question.objects.create(
#             description = f"Pregunta N°{fake.random_int(min=1, max=500)}",
#             questionType = random.choice(types),
#             poll = random.choice(polls)
#         )


# def create_answer(num_answer):
#     questions = Question.objects.all()
#     types = (
#         ('Boolean', 'Boolean'),
#         ('Integer', 'Integer'),
#         ('Float', 'Float'),
#         ('String', 'String'))
#     for _ in range(num_answer):
#         Answer.objects.create(
#             description=f"Respuesta N°{fake.random_int(min=1, max=500)}",
#             question=random.choice(questions),
#             answerType=random.choice(types)
#         )


# def create_childAnswer(num_childAnswer):
#     childs = Child.objects.all()
#     answers = Answer.objects.all()
#     for _ in range(num_childAnswer):
#         ChildAnswer.objects.create(
#             child=random.choice(childs),
#             answer=random.choice(answers),
#             value=fake.word()
#         )
