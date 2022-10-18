import imp
from os import stat
from mrjob.job import MRJob, MRStep


class MRFemaleKidsWithLetters(MRJob):
    def steps(self):
        return [MRStep(mapper=self.filter_by_gender),MRStep(mapper = self.count_by_letter, reducer = self.sum_birth)]

    def filter_by_gender(self, key, record):
        splits = record.split(',')
        if splits[1] == 'F':
            yield "F",(splits[0]+","+splits[2])

    def count_by_letter(self, key, record):
        splits = record.split(',')
        yield splits[0][0], int(splits[1])

    def sum_birth(self, letter, births):
        yield letter, sum(births)

if __name__ == '__main__':
    MRFemaleKidsWithLetters.run()