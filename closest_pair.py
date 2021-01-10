# CS4102 Spring 2020 - Homework 3
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: jr2dj
# Collaborators: None
# Sources: Introduction to Algorithms, Cormen
#################################
class ClosestPair:
    import math 
    import operator
    def __init__(self):
        return
    
    
    def brute_force(self, list_of_points):
        minimum_distance = 10000000000000000000000
        for i in range(0, len(list_of_points) - 1 ): 
            for j in range(i + 1, len(list_of_points) ):
                p1 = list_of_points[i]
                p2 = list_of_points[j]
                
                x1 = p1[0]
                y1 = p1[1]
                x2 = p2[0]
                y2 = p2[1]
                
                distance = self.calculateDistance(x1, y1, x2, y2)
                
                if distance < minimum_distance: 
                    minimum_distance = distance
                    
        return minimum_distance
    
    
    def calculateDistance(self, x1, y1, x2, y2):
        return self.math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    
    
    def closest(self, point_list):
        # brute force the smallest distance
        if len(point_list) <= 3: 
            return self.brute_force(point_list)
        
        # split on median of x-coordinates
        split_index = len(point_list) // 2 
        left_split = point_list[0:split_index]
        right_split = point_list[split_index:len(point_list)]
        
        # call closest recursively on left and right splits
        left_min_distance = self.closest(left_split)
        right_min_distance = self.closest(right_split)
        
        # get delta 
        if left_min_distance < right_min_distance: 
            delta = left_min_distance 
        else: 
            delta = right_min_distance 
        
        # getting minimmum distance (left-right)
        delta = str(delta)
        delta = float(delta)
       
        return delta
        
    
    

    def closestMiddle(self, delta, point_list):
         # getting minimum distance (middle)
        left_endpoint = point_list[len(point_list) // 2 ][0] - delta 
        right_endpoint = point_list[len(point_list) // 2 ][0] + delta 
        
        middle_points = []
        for point in point_list: 
            if point[0] >= left_endpoint and point[0] <= right_endpoint:
                middle_points.append(point)
                
        middle_points.sort(key = self.operator.itemgetter(1))
        
        minimum = delta
        size = len (middle_points)
        for i in range(size - 1 ): 
            for j in range(i + 1, min(i + 15, size)):
                p1 = middle_points[i]
                p2 = middle_points[j]
                
                x1 = p1[0]
                y1 = p1[1]
                x2 = p2[0]
                y2 = p2[1]

                distance = self.calculateDistance(x1, y1, x2, y2)
                
                if distance < minimum: 
                    minimum = distance 
                    
        return minimum
        


    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distance
    # and return that value from this method
    #
    # @return the distance between the closest pair 
    def compute(self, point_list):
        list_of_tuples= []
        for point in point_list: 
            x_and_y = point.split()
            x = float(x_and_y[0])
            y = float(x_and_y[1])
            
            points_tuple = (x, y)
            list_of_tuples.append(points_tuple)


        list_of_tuples.sort(key = self.operator.itemgetter(0))
        
        
        
        
        left_right_min = self.closest(list_of_tuples)
        middle_min = self.closestMiddle(left_right_min, list_of_tuples)
        
        if left_right_min < middle_min: 
            return left_right_min 
        else: 
            return middle_min
        
