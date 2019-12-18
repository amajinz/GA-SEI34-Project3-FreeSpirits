import graphene

import freespirits.back.schema
import graphql_jwt






class Query(freespirits.back.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(freespirits.back.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    


schema = graphene.Schema(query=Query, mutation=Mutation)