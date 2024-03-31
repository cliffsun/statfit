import random
import numpy as np

def generate_random_numbers(n, top):
    random_numbers = [random.uniform(0, top) for _ in range(n)]
    return random_numbers

def gaussian_odd_input(sigma, numOfParameters, mean_width, rand=False):
    delta = numOfParameters * sigma**2 / 2 
    arrDiv2 = np.zeros(numOfParameters//2 + 1)
    final_arr = np.zeros(numOfParameters)
    top_bound = random.randint(0, 50)
    if (rand):
        rannum = generate_random_numbers(numOfParameters - 1, top=top_bound)
        delta = delta / np.sum(rannum)
    else:
        sum = (numOfParameters - 1) * (numOfParameters)/2
        delta = delta / sum
    for i in range(1, numOfParameters//2 + 2):
        arrDiv2[i - 1] = np.sqrt((i-1) * delta)
    final_arr = np.concatenate((np.flip(-1 * arrDiv2[1:]), arrDiv2))
    final_arr += mean_width
    return final_arr



def gaussian_even_input(sigma, numOfParameters, mean_width, rand=False):
    delta = numOfParameters * sigma**2 / 2 
    arrDiv2 = np.zeros(numOfParameters//2 + 1)
    final_arr = np.zeros(numOfParameters)
    top_bound = random.randint(0, 50)
    if (rand):
        rannum = generate_random_numbers(numOfParameters - 1, top=top_bound)
        rannum.append(1)
        delta = delta/np.sum(rannum)
    else:
        sum = (numOfParameters/2 * (numOfParameters/2 + 1))/2
        delta = delta / sum
    for i in range(1, numOfParameters//2 + 1):
        arrDiv2[i - 1] = np.sqrt(i * delta)
    final_arr = np.concatenate((np.flip(-1 * arrDiv2), arrDiv2))
    final_arr += mean_width
    return final_arr

def gaussian_fit(sigma, numOfParameters, mean_width, rand=False):
    fitted_data = []
    if (numOfParameters % 2 == 0):
        fitted_data = gaussian_even_input(sigma=sigma, numOfParameters=numOfParameters, mean_width=mean_width, rand=rand)
    else:
        fitted_data = gaussian_odd_input(sigma=sigma, numOfParameters=numOfParameters, mean_width=mean_width, rand=rand)
    return fitted_data