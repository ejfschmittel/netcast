import graphene 
from graphene_django.types import DjangoObjectType

from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name', 'slug')

class Query(object):
    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all();

    def resolve_category(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id is not None:
            return Category.objects.get(pk=id)

        if id is not None:
            return Category.objects.get(name=name)

        return None

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        category.save()
        return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()