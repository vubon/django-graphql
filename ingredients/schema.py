import graphene
from graphene_django.types import DjangoObjectType
from .models import Category, Ingredient, Test


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class TestType(DjangoObjectType):
    class Meta:
        model = Test


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    all_tests = graphene.List(TestType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_all_tes(self):
        return Test.objects.all()
