import src.config as cfg
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline


tree_pipe = Pipeline([
    ('model', DecisionTreeClassifier(random_state=cfg.RANDOM_STATE))
])