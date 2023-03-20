from questions.graphql.query import Query as QuestionsQuery
from questions.graphql.mutation import Mutation as QuestionsMutation
from strawberry.tools import merge_types
import strawberry

Queries = merge_types(
    "Queries",
    (QuestionsQuery,),
)

Mutations = merge_types(
    "Mutations",
    (QuestionsMutation,),
)


schema = strawberry.Schema(query=Queries, mutation=Mutations)
