from .q_learner import QLearner
from .coma_learner import COMALearner
from .s_learner import SLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["s_learner"] = SLearner
