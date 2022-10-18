from mrjob.job import MRJob
from mrjob.step import MRStep


class MostPopularMovie(MRJob):

    def configure_args(self):
        super(MostPopularMovie, self).configure_args()
        self.add_file_arg(
            '--items', help='Path to u.item')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer_init=self.reducer_init,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_max)
        ]

    def mapper_get_ratings(self, key, value):
        (userID, movieID, rating, timestamp) = value.split('\t')
        yield movieID, 1

    def reducer_init(self):
        self.movieNames = {}

        with open("u.item", encoding="utf8", errors='ignore') as f:
            for line in f:
                fields = line.split('|')
                self.movieNames[fields[0]] = fields[1]

    def reducer_count_ratings(self, movieID, counts):
        yield None, (sum(counts), self.movieNames[movieID])

    def reducer_find_max(self, key, values):
        yield max(values)


if __name__ == '__main__':
    MostPopularMovie.run()
