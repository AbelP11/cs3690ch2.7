import random

population_size = 50
chromosome_length = 8
mutation_rate = 0.04
generations = 10


def fitness_function(chromosome):
    return sum(chromosome)


population = [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

for generation in range(generations):
    fitness_scores = [fitness_function(chromosome) for chromosome in population]

    best_solution = population[fitness_scores.index(max(fitness_scores))]

    print(f"Generation {generation + 1}: Best Fitness = {max(fitness_scores)}, Best Solution = {best_solution}")

    new_population = []

    for _ in range(population_size):
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]

        crossover_point = random.randint(1, chromosome_length - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]

        for i in range(chromosome_length):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        new_population.append(child)

    population = new_population
