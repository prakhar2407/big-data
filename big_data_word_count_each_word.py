from mrjob.job import MRJob

class MrWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

    def maxWord(self, key, value):
        yield key, max(value)

if __name__ == '__main__':
    MrWordFrequencyCount.run()