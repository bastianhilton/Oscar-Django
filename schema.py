import graphene
from graphene_generator.holder import QueriesHolder, MutationsHolder


class Query(QueriesHolder, graphene.ObjectType):
    pass


class Mutation(MutationsHolder, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=MutationsHolder)