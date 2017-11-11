from ruleset import Ruleset
from dataset import Dataset

class AQ(object):
    def __init__(self, dataset = Dataset()):
        self._dataset = dataset
        self._ruleset = Ruleset()
        self.decision
