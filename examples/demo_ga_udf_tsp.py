# demo: GA for TSP with UDF(user defined functions)
import numpy as np
# step1: randomly generate the data
from sko.demo_func import function_for_TSP

num_points, points_coordinate, distance_matrix, cal_total_distance = function_for_TSP(num_points=15)

# step2: DO GA with UDF
from sko.GA import GA_TSP
from sko.GA import selection_tournament, mutation_TSP_1

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=num_points, size_pop=500, max_iter=800, Pm=0.2)
ga_tsp.register('selection', selection_tournament, tourn_size=3). \
    register('mutation', mutation_TSP_1)

best_points, best_distance = ga_tsp.fit()
print('best routine:', best_points, 'best_distance:', best_distance)
# %%
# step3: plot
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
best_points_ = np.concatenate([best_points, [best_points[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax.plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
plt.show()
