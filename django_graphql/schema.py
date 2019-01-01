import graphene

from ingredients.schema import Query


class QueryType(Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=QueryType)