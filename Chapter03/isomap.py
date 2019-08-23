import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.datasets import fetch_olivetti_faces
from sklearn.manifold import Isomap

# Set random seed for reproducibility
np.random.seed(1000)


if __name__ == '__main__':
    # Create the dataset
    faces = fetch_olivetti_faces()

    # Train Isomap
    isomap = Isomap(n_neighbors=5, n_components=2)
    X_isomap = isomap.fit_transform(faces['data'])

    # Plot the result
    sns.set()
    fig, ax = plt.subplots(figsize=(18, 10))

    for i in range(100):
        ax.scatter(X_isomap[i, 0], X_isomap[i, 1], marker='o', s=200)
        ax.annotate('%d' % faces['target'][i], xy=(X_isomap[i, 0] + 0.35, X_isomap[i, 1] + 0.35))

    ax.set_xlabel(r'$x_0$', fontsize=18)
    ax.set_ylabel(r'$x_1$', fontsize=18)
    ax.grid(True)

    plt.show()