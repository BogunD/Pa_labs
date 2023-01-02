from Functions import *
backpack, items_num, items = initialize()
print("Backpack: ")
backpack.show_info()
solutions_per_pop = len(items_num)
population_size = (solutions_per_pop, items_num.shape[0])
population = (np.random.randint(2, size = population_size)).astype(int)
iterations = input("Enter iterations amount [20-1000]:")
while not iterations.isdigit() or int(iterations) < 20 or int(iterations)>1000:
    iterations = input("Enter iterations amount [20-1000]!!!:")
iterations = int(iterations)
print("Running...")
parameters = local_optimization(backpack, population, population_size, iterations)
selected_items = items_num * parameters
print('\nSelected items that will maximize the knapsack without breaking it:')
print_result(selected_items,items)

