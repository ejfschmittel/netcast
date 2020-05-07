import graphene 
from graphene_django.types import DjangoObjectType
import random

from .models import Podcast

class PodcastType(DjangoObjectType):
    class Meta:
        model = Podcast
        fields = ('id','name', 'slug', 'description', 'categories')

class Query(object):
    podcast = graphene.Field(PodcastType, id=graphene.Int())
    random_podcast = graphene.Field(PodcastType)
    all_podcasts = graphene.List(PodcastType)

    def resolve_all_podcasts(self, info, **kwargs):
        return Podcast.objects.all();

    def resolve_random_podcast(self, info, **kwargs):
        podcasts = Podcast.objects.all();
        return random.choice(podcasts)

    def resolve_podcast(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Podcast.objects.get(pk=id)

        return None

class PodcastCreateMutation(graphene.Mutation):
    podcast = graphene.Field(PodcastType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        personalities =  graphene.List(graphene.Int)
  

    def mutate(self, info, name, description, personalities):
        podcast = Podcast.objects.create(name=name, description=description)
        for id in personalities:
            podcast.hosts.add(id)
        podcast.save()
        return PodcastCreateMutation(podcast=podcast)

class PodcastUpdateMutation(graphene.Mutation):
    podcast = graphene.Field(PodcastType)

    class Arguments:
        id = graphene.Int(required=True)
        # add all fields
    
    def mutate(self, info, id):
        instance = Podcast.objects.get(pk=id)
    
        return PodcastDeleteMutation(podcast=instance)

class PodcastDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()
    delete_id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        instance = Podcast.objects.get(pk=id)
        instance.delete()
        return PodcastDeleteMutation(delete_id=id, ok=True)

class Mutation(graphene.ObjectType):
    create_podcast = PodcastCreateMutation.Field()
    delete_podcast = PodcastDeleteMutation.Field()