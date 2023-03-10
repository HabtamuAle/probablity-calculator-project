import copy
from collections import Counter
import random


class Hat:

  def __init__(self, **balls):
    balls = dict(balls)
    self.contents = []
    for ball in balls:
      for i in range(balls[ball]):
        self.contents.append(ball)

  def draw(self, number):
    if len(self.contents) < number:
      return self.contents

    drawn_balls = []
    contents = self.contents

    for i in range(number):
      ball = random.choice(contents)
      drawn_balls.append(ball)
      contents.remove(ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  experiments = []
  for i in range(num_experiments):
    hat_exp = copy.deepcopy(hat)
    result = hat_exp.draw(num_balls_drawn)
    result = dict(Counter(ball for ball in result))
    experiments.append(result)

  failed = []
  for ball in list(expected_balls.keys()):
    for r in experiments:
      if not (ball in list(r.keys())):
        failed.append(r)

  experiments = [r for r in experiments if r not in failed]

  failed = []
  for ball in list(expected_balls.keys()):
    for r in experiments:
      if int(expected_balls[ball]) > int(r[ball]):
        failed.append(r)

  experiments = [r for r in experiments if r not in failed]

  return len(experiments) / num_experiments
