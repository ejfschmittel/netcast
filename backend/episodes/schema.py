import graphene 
from graphene_django.types import DjangoObjectType

from podcasts.schema import PodcastType

from .models import Episode

class EpisodeType(DjangoObjectType):



    class Meta:
        model = Episode
        fields = ('id','title', 'description', 'upload_date', 'personalities', 'episode_num', 'youtube_id', 'podcast')

class Query(object):
    episode = graphene.Field(EpisodeType, id=graphene.Int())
    all_episodes = graphene.List(EpisodeType)
    podcast_episodes = graphene.List(EpisodeType, podcast_id=graphene.Int())
    podcast_episode = graphene.Field(EpisodeType, podcast_id=graphene.Int(), episode_num=graphene.Int())

    def resolve_all_episodes(self, info, **kwargs):
        return Episode.objects.all();

    def resolve_podcast_episode(self, info, podcast_id, episode_num):
        if podcast_id and episode_num: 
            return Episode.objects.filter(podcast=podcast_id, episode_num=episode_num).first();   
        return None

    def resolve_podcast_episodes(self, info, **kwargs):
        id = kwargs.get("podcast_id");
        return Episode.objects.filter(podcast=id);

    def resolve_episode(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Episode.objects.get(pk=id)

        return None

class EpisodeCreateMutation(graphene.Mutation):
    episode = graphene.Field(EpisodeType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        upload_date = graphene.types.datetime.Date()
  

    def mutate(self, info, title, description, upload_date):
        episode = Episode.objects.create(
            title=title,
            description=description,
            upload_date=upload_date
        )
        episode.save()
        return EpisodeCreateMutation(episode=episode)

class EpisodeUpdateMutation(graphene.Mutation):
    episode = graphene.Field(EpisodeType)

    class Arguments:
        id = graphene.Int(required=True)
        # add all fields
    
    def mutate(self, info, id):
        instance = Episode.objects.get(pk=id)
    
        return EpisodeUpdateMutation(episode=instance)

class EpisodeDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()
    delete_id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        instance = Episode.objects.get(pk=id)
        instance.delete()
        return EpisodeDeleteMutation(delete_id=id, ok=True)

class Mutation(graphene.ObjectType):
    create_episode = EpisodeCreateMutation.Field()
    delete_episode = EpisodeDeleteMutation.Field()