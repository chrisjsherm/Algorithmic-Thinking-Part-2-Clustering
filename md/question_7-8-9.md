Hierarchical clustering distortion: 1.752 X 10^11
K-means clustering distortion: 2.713 X 10^11

Hierarchical clustering creates three clusters with lower distortion that fit more
closely to the geographical lines of the states of California, Oregon, and
Washington. The iterative nature of the hierarchical clustering algorithm
has the downside of taking more time, but it produces less distortion because
it doesn't take take the population heuristic we chose with the k-means
clustering algorithm to seed the initial clusters.

The k-means algorithm also creates three clusters on the west coast, however,
its clusters have greater distortion due to the fact that we seeded the
algorithm with initial clusters based on population centers. The southern
part of California is more densely populated than the northern part of the 
state as well as Oregon and Washington, so the k-means algorithm creates two
clusters around the population centers of San Diego and Los Angeles while
lumping the rest of California, Oregon, and Washington into a single cluster.

The hierarchical clustering algorithm requires less human supervision to produce
clusters with relatively low distortion.