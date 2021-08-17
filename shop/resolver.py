from ariadne import QueryType, make_executable_schema, MutationType
from .models import *
query = QueryType()

type_defs= """

type Query{
    all_schools: [School]
}

type School {
    id: ID
    school_name: String!
    school_population: Int!

}
type Mutation{
    add_school(input: SchoolInput): SchoolResults

}
input SchoolInput {
    school_name: String
    school_population: Int
}
  type SchoolResults {
        created: Boolean!
        school: School
        err: String
}

"""