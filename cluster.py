class ClusterCreator:
    def __init__(self, data, k):
        """"data -- A list of numbers"""
        self.data = data
        self.scores = self.score_data(data, k)
        return
    
    @staticmethod
    def score_point(point_i, data, k):
        # point_i is the index of the point to compare in data
        # data is a list of all points
        # k is the number of nearest neighbors to compare point to

        point = data[point_i]
        squared_distances = []
        for neighbor_i, neighbor in enumerate(data):
            # Prevent comparing point to itself
            if point_i == neighbor_i:
                continue

            # Get squared distance between points
            d = (neighbor - point) ** 2
            # Add this distance to scores
            squared_distances.append(d)

        # Multiply scores of closest k neighbors
        k_total = sum(sorted(squared_distances)[:k])

        # Take kth root of k_total to get score
        score = k_total / k
        return score

    def score_data(self, data, k):
        scores = []
        for point_i, _ in enumerate(data):
            score = self.score_point(point_i, data, k)
            scores.append(score)
        return scores
    
    def remove_outliers(self, max_s):
        # max_s is the maximum allowed score for a point
        # to be returned. Exclusive.

        no_outliers = []
        for i, point in enumerate(self.data):
            if self.scores[i] < max_s:
                no_outliers.append(point)
        return no_outliers
