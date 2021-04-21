"""
Seth Brenneman
--------------
Analysis of Algorithms
----------------------
March 23, 2021
--------------
Dynamic Programming - minimum cost of travel
--------------------------------------------
This problem comes from chapter 6, exercise 4 in Algorithm Design by Jon Kleinberg and Eva Tardos. 'Suppose you’re running a lightweight 
consulting business, just you, two associates, and some rented equipment. Your clients are distributed between the East Coast and the West Coast, 
and this leads to the following question. Each month, you can either run your business from an office in New York (NY) or from an office in San 
Francisco (SF). In month i, you’ll incur an operating cost of Ni if you run the business out of NY; you’ll incur an operating cost of Si if you run 
the business out of SF. If you begin in NY and travel to SF, there will be an additional movement cost.'
"""

# Memoized Solution
def memoized_NYSF():
    cacheNY = {0:0}
    def optNY(j):

        if j in cacheNY:
            return cacheNY[j]
        else:
            cacheNY[j] = NY[j - 1] + min(optSF(j - 1) + movement_cost, optNY(j - 1))
            return cacheNY[j]

    cacheSF = {0:0}
    def optSF(j):
        
        if j in cacheSF:
            return cacheSF[j]
        else:
            cacheSF[j] = SF[j - 1] + min(optNY(j - 1) + movement_cost, optSF(j - 1))
            return cacheSF[j]

    min_cost_of_travel = min(optNY(len(NY)), optSF(len(SF)))

    print(f'The minimum cost of travel is: {min_cost_of_travel}')

# Tabulated Solution
def tabulated_NYSF():
    MNY = [0] * (len(NY) + 1)
    MSF = [0] * (len(SF) + 1)

    for j in range(1, len(MNY)):
        MNY[j] = NY[j - 1] + min(MSF[j - 1] + movement_cost, MNY[j - 1])
        MSF[j] = SF[j - 1] + min(MNY[j - 1] + movement_cost, MSF[j - 1])

    min_cost_of_travel = min(MNY[-1], MSF[-1])

    print(f'The minimum cost of travel is: {min_cost_of_travel}')

# Brute Force Solution
def brute_force_NYSF():
    
    def optNY(j):
        if j == 0:
            return j
        else:
            return NY[j - 1] + min(optSF(j - 1) + movement_cost, optNY(j - 1))

    def optSF(j):
        if j == 0:
            return j
        else:
            return SF[j - 1] + min(optNY(j - 1) + movement_cost, optSF(j - 1))

    min_cost_of_travel = min(optNY(len(NY)), optSF(len(SF)))

    print(f'The minimum cost of travel is: {min_cost_of_travel}')


if __name__ == '__main__':
    NY = [55, 30, 105, 40, 10, 70]
    SF = [200, 10, 65, 110, 25, 40]
    movement_cost = 35

    memoized_NYSF()
    tabulated_NYSF()
    brute_force_NYSF()

