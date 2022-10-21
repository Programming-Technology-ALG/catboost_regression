import src.config as cfg
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


def make_2D_plot(data):
    """Make 2D plot of the data"""
    tsne = TSNE(n_components=2, random_state=cfg.RANDOM_STATE, perplexity=15, n_iter=1000, verbose=0)
    tsne_representation = tsne.fit_transform(data)

    plt.figure(figsize=(10,8))
    sns.scatterplot(data=pd.DataFrame(tsne_representation))


def make_3D_plot(data):
    tsne = TSNE(n_components=3, random_state=cfg.RANDOM_STATE, perplexity=30, n_iter=1000)
    tsne_representation = tsne.fit_transform(data)

    sns.set_style("whitegrid", {'axes.grid' : True})

    fig = plt.figure(figsize=(10,8))

    ax = Axes3D(fig)
    x = tsne_representation[:, 0]
    y = tsne_representation[:, 1]
    z = tsne_representation[:, 2]

    g = ax.scatter(x, y, z, c=x, marker='o', depthshade=False, cmap='Paired')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')