class Query:
    def __init__(self, select, from_, where, join, orderBy, groupBy):
        self.select = select
        self.from_ = from_
        self.where = where
        self.join = join
        self.orderBy = orderBy
        self.groupBy = groupBy


class QueryBuilder:
    @staticmethod
    def builder():
        return QueryBuilder.Builder()

    class Builder:
        def __init__(self):
            self.query_builder = QueryBuilder()

        def select(self, select):
            self.query_builder.select = select
            return self

        def from_(self, from_):
            self.query_builder.from_ = from_
            return self

        def where(self, where):
            self.query_builder.where = where
            return self

        def join(self, join):
            self.query_builder.join = join
            return self

        def orderBy(self, orderBy):
            self.query_builder.orderBy = orderBy
            return self

        def groupBy(self, groupBy):
            self.query_builder.groupBy = groupBy
            return self

        def build(self):
            query_builder = QueryBuilder()
            query_builder.select = self.query_builder.select
            query_builder.from_ = self.query_builder.from_
            query_builder.where = self.query_builder.where
            query_builder.join = self.query_builder.join
            query_builder.orderBy = self.query_builder.orderBy
            query_builder.groupBy = self.query_builder.groupBy
            return query_builder

