from knn import *

LOOPS_COUNT = 10
CLUSTERS_COUNT = 16

im = Image.open('lenna.png')

without_alpha = lambda x: x[:-1]
arr = list(map(without_alpha, im.getdata()))

centers, colors = knn(arr, LOOPS_COUNT, CLUSTERS_COUNT)

res_coords = fill_with_centers(arr, centers, colors)

print(res_coords.shape)
print(np.array(colors).shape)


res_img = Image.fromarray(res_coords)
res_img.show()
res_img.save('result_png.png')
