import numpy as np
from random import randint
import random as rd
from Classes import *
def initialize():
    items_num = np.arange(1, 101)
    items = []
    for num in items_num:
        item_price = np.random.randint(2, 21)
        item_weight = np.random.randint(1, 11)
        item = Item(num, item_weight, item_price)
        items.append(item)
    backpack = Backpack(250,items)
    return backpack, items_num, items


def calculate_cost(backpack, population, capacity):
    cost = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        sum1 = np.sum(population[i] * backpack.get_price_list())
        sum2 = np.sum(population[i] * backpack.get_weight_list())
        if sum2 <= capacity:
            cost[i] = sum1
        else :
            cost[i] = 0
    return cost.astype(int)

def selection(cost, num_parents, population):
    cost = list(cost)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(cost == np.max(cost))
        parents[i,:] = population[max_fitness_idx[0][0], :]
        cost[max_fitness_idx[0][0]] = -999999
    return parents

def crossing_over(parents, offsprings_amount):
    offsprings = np.empty((offsprings_amount, parents.shape[1]))
    point = 50
    crossover_rate = 0.7
    i=0
    while (parents.shape[0] < offsprings_amount):
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]
        offsprings[i,0:point] = parents[parent1_index,0:point]
        offsprings[i,point:] = parents[parent2_index,point:]
        i=+1
    return offsprings

def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.05
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i,:] = offsprings[i,:]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0,offsprings.shape[1]-1)
        if mutants[i,int_random_value] == 0 :
            mutants[i,int_random_value] = 1
        else :
            mutants[i,int_random_value] = 0
    return mutants

def local_optimization(backpack, population, pop_size, iterations):
    threshold = backpack.get_capacity()
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents
    for i in range(iterations):
        fitness = calculate_cost(backpack, population, threshold)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossing_over(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        np.seterr(divide='ignore', invalid='ignore')
        population[parents.shape[0]:, :] = mutants
    fitness_last_gen = calculate_cost(backpack, population, threshold)
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0],:])
    return parameters
def print_result(selected_items, items):
    j = 0
    total_weight = 0
    total_price = 0
    for i in range(0,selected_items.shape[1]):
      if selected_items[0][i] != 0:
          j+=1
          items[i].show_info()
          print( "Total weight:", total_weight, "+",items[i].get_weight(),"=", total_weight+items[i].get_weight() )
          total_weight += items[i].get_weight()
          total_price += items[i].get_price()
          print("--------------------------------------------------")
    print("\n\nAMOUNT OF ITEMS IN BACKPACK: ", j)
    print("TOTAL WEIGHT: ", total_weight)
    print("TOTAL PRICE: ", total_price)
