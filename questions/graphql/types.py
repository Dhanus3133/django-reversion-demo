from strawberry_django_plus import gql
from typing import Optional, Type, cast
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from questions.models import Question
from reversion.models import Revision, Version


@gql.django.type(Version)
class ReversionVersionType:
    revision: "ReversionRevisionType"
    object_id: gql.ID
    serialized_data: gql.auto


@gql.django.type(Question)
class QuestionType(gql.relay.Node):
    id: gql.auto
    question: gql.auto
    answer: gql.auto
    priority: gql.auto


@gql.django.type(Revision)
class ReversionRevisionType:
    date_created: gql.auto
    user: Optional["UserType"]
    comment: gql.auto


UserModel = cast(Type[AbstractUser], get_user_model())


@gql.django.type(UserModel)
class UserType(gql.relay.Node):
    username: gql.auto
    email: gql.auto
    is_active: gql.auto
    is_superuser: gql.auto
    is_staff: gql.auto

    id_attr = "username"

    @gql.django.field(only=["first_name", "last_name"])
    def full_name(self, root: AbstractUser) -> str:
        return f"{root.first_name or ''} {root.last_name or ''}".strip()
