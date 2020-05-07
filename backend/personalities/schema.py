import graphene 
from graphene_django.types import DjangoObjectType

from .models import Personality

class PersonalityType(DjangoObjectType):
    class Meta:
        model = Personality
        fields = ('id','firstname', 'lastname', 'displayname', 'bio')

class Query(object):
    personality = graphene.Field(PersonalityType, id=graphene.Int())
    all_personalities = graphene.List(PersonalityType)

    def resolve_all_personalities(self, info, **kwargs):
        return Personality.objects.all();

    def resolve_personality(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Personality.objects.get(pk=id)

        return None

class PersonalityCreateMutation(graphene.Mutation):
    personality = graphene.Field(PersonalityType)

    class Arguments:
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        displayname = graphene.String(required=True)
        bio = graphene.String()
        
    def mutate(self, info, firstname, lastname, displayname, bio):
        personality = Personality.objects.create(
            firstname=firstname,
            lastname=lastname,
            displayname=displayname,
            bio=bio
        )
        personality.save()
        return PersonalityCreateMutation(personality=personality)

class PersonalityUpdateMutation(graphene.Mutation):
    personality = graphene.Field(PersonalityType)

    class Arguments:
        id = graphene.Int(required=True)
        # add all fields
    
    def mutate(self, info, id):
        instance = Personality.objects.get(pk=id)
    
        return PersonalityUpdateMutation(personality=instance)

class PersonalityDeleteMutation(graphene.Mutation):
    ok = graphene.Boolean()
    delete_id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        instance = Personality.objects.get(pk=id)
        instance.delete()
        return PersonalityDeleteMutation(delete_id=id, ok=True)

class Mutation(graphene.ObjectType):
    create_personality = PersonalityCreateMutation.Field()
    delete_personality = PersonalityDeleteMutation.Field()