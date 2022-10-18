from mrjob.job import MRJob

class MrWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if (word.startswith('P') or word.startswith('p')):
                yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MrWordFrequencyCount.run()