import imp
from os import stat
from mrjob.job import MRJob, MRStep

class MRMaxWord(MRJob):
    def steps(self):
        return [MRStep(mapper=self.func1), MRStep(reducer=self.func2)]

    def func1(self, _, line):
        for word in line.split():
            yield word, 1

    def func2(self, key, values):
        yield None, (sum(values), key)

    def maxWord(self, key, values):
        yield max(values)

if __name__ == '__main__':
    MRMaxWord.run()