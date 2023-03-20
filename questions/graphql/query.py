from typing import List
from reversion.models import Version
from strawberry_django_plus import gql, relay
from strawberry.types import Info
from questions.graphql.types import QuestionType, ReversionVersionType
from djangorev.utils import decode_id_from_gql_id


@gql.type
class Query:
    questions: relay.Connection[QuestionType] = relay.connection()
    versions: List[ReversionVersionType] = gql.django.field()

    @gql.django.field
    def question_versions(
        self,
        info: Info,
        question_id: gql.ID,
    ) -> List[ReversionVersionType]:
        return Version.objects.filter(object_id=decode_id_from_gql_id(question_id))
