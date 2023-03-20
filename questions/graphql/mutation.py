import reversion
from reversion.models import Version
from strawberry.types import Info
from strawberry_django_plus import gql
from questions.graphql.query import QuestionType
from questions.models import Question
from djangorev.utils import decode_id_from_gql_id


@gql.type
class Mutation:
    @gql.django.input_mutation
    def create_question(self, info: Info, question: str) -> QuestionType:
        with reversion.create_revision():
            q = Question.objects.create(question=question)
            reversion.set_user(info.context.request.user)
            reversion.set_comment("Version 1")
            return q

    @gql.django.input_mutation
    def update_question(self, info: Info, id: gql.ID, question: str) -> QuestionType:
        with reversion.create_revision():
            q = Question.objects.get(id=decode_id_from_gql_id(id))
            q.question = question
            reversion.set_user(info.context.request.user)
            reversion.set_comment(
                f"Version {Version.objects.filter(object_id=decode_id_from_gql_id(id)).count()+1}"
            )
            q.save()
            return q
