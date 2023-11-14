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

from SalasCuna_api.models import Poll, Question, Answer

fake = Faker()

# Función para crear preguntas y respuestas para una encuesta
def create_questions_and_answers(poll, num_questions):
    questions = []
    for _ in range(num_questions):
        question = Question.objects.create(
            description=fake.sentence(),
            questionType=random.choice(['Single Option', 'Single Choice', 'Multiple Choice']),
            poll=poll,
        )
        answer = Answer.objects.create(
            description=fake.word(),
            answerType=random.choice(['Boolean', 'Integer', 'Float', 'String']),
            question=question,
        )
        questions.append(question)
    return questions

# Función para crear una encuesta con preguntas y respuestas
def create_poll_with_questions(num_questions):
    with transaction.atomic():
        poll = Poll.objects.create(name=fake.word())
        questions = create_questions_and_answers(poll, num_questions)
    return poll, questions

# Crear encuestas con preguntas y respuestas de ejemplo
num_polls = 3
num_questions_per_poll = 5

for _ in range(num_polls):
    poll, _ = create_poll_with_questions(num_questions_per_poll)
    print(f"Created poll: {poll.name} with {num_questions_per_poll} questions.")

print("Data creation completed.")
