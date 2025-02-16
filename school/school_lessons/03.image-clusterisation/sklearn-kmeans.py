import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

from knn import fill_with_centers

CLUSTERS_COUNT = 16


im = Image.open('lenna.png')

without_alpha = lambda x: x[:-1]
arr = list(map(without_alpha, im.getdata()))

kmeans = KMeans(n_clusters=CLUSTERS_COUNT, random_state=0).fit(arr)
print(kmeans)

colors = kmeans.predict(arr) # kmeans.labels_
centers = kmeans.cluster_centers_


res_coords = fill_with_centers(arr, centers, colors)

print(res_coords.shape)


res_img = Image.fromarray(res_coords)
res_img.show()

res_img.save('result_sklearn.png')
