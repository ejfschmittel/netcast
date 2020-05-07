import graphene

from categories.schema import Query as CategoryQuery, Mutation as CategoryMutation
from podcasts.schema import Query as PodcastQuery, Mutation as PodcastMutation
from episodes.schema import Query as EpisodeQuery, Mutation as EpisodeMutation
from personalities.schema import Query as PersonalityQuery, Mutation as PersonalityMutation

class Query(
    CategoryQuery, 
    EpisodeQuery,
    PersonalityQuery,
    PodcastQuery,
    graphene.ObjectType):
    pass

class Mutation(
    CategoryMutation, 
    EpisodeMutation,
    PersonalityMutation,
    PodcastMutation,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)