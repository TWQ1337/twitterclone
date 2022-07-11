from random import choice
from django.contrib.auth.models import User
from tweets.models import TweetModel
from faker import Faker


def generate_fake_tweets(count: int) -> bool:
    users = User.objects.all()
    print(f' users found: {users.count()}')
    faker = Faker()
    models_to_create: list[TweetModel] = []
    for _ in range(count):
        models_to_create.append(TweetModel(
            created_by=choice(users),
            body=faker.paragraph()
        ))
    TweetModel.objects.bulk_create(models_to_create)
    return True