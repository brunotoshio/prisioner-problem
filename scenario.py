from typing import Callable
import random

class Scenario:
    def __init__(self, number_of_prisioners: int, number_of_chances: int):
        if number_of_prisioners < 1:
            raise ValueError('Number of prisioners must be greater than 0')
        if number_of_chances > number_of_prisioners:
            raise ValueError('Number of chances must be lesser than number of prisioners')

        self.boxes = list(range(number_of_prisioners))
        self.number_of_chances = number_of_chances

    def _shuffle(self):
        random.shuffle(self.boxes)

    def _get_box(self, number: int) -> int:
        return self.boxes[number]


class RandomSelectionScenario(Scenario):
    def __init__(self, number_of_prisioners: int, number_of_chances: int):
        super().__init__(number_of_prisioners, number_of_chances)

    def run(self) -> bool:
        ''' Run simulation and return True if all prisioners is saved, False otherwise
        '''
        self._shuffle()
        for prisioner in range(len(self.boxes)):
            if not any([self._get_box(chance) == prisioner for chance in range(self.number_of_chances)]):
                return False
        return True


class GraphSelectionScenario(Scenario):
    def __init__(self, number_of_prisioners: int, number_of_chances: int):
        super().__init__(number_of_prisioners, number_of_chances)

    def run(self) -> bool:
        ''' Run simulation and return True if all prisioners is saved, False otherwise
        '''
        self._shuffle()
        for prisioner in range(len(self.boxes)):
            next_attempt = prisioner
            found = False
            for _ in range(self.number_of_chances):
                next_attempt = self._get_box(next_attempt)
                if next_attempt == prisioner:
                    found = True
                    break
            if not found:
                return False
        return True
