from statfit import data_generator 
import numpy as np
import math

def round_to_2_sig_figs(number):
    if number == 0:
        return 0
    
    # Calculate the exponent for the number
    exponent = int(number and math.floor(math.log10(abs(number))))
    
    # Calculate the multiplier for rounding
    multiplier = 10 ** (2 - exponent)
    
    # Round the number to 2 significant figures
    rounded_number = round(number * multiplier) / multiplier
    
    return rounded_number

testing_sigma = 0.2

data_1_noRandom_even = data_generator.gaussian_fit(sigma=testing_sigma, numOfParameters=4, mean_width=0.1, rand=False)

data_2_Random_even = data_generator.gaussian_fit(sigma=testing_sigma, numOfParameters=4, mean_width=0.1, rand=True)

data_3_noRandom_odd = data_generator.gaussian_fit(sigma=testing_sigma, numOfParameters=5, mean_width=0.1, rand=False)

data_4_Random_odd = data_generator.gaussian_fit(sigma=testing_sigma, numOfParameters=5, mean_width=0.1, rand=True)

# assert(np.std(data_1_noRandom_even) == testing_sigma)
print(np.std(data_1_noRandom_even))
print(testing_sigma)
# assert(np.std(data_2_Random_even) == testing_sigma)
# assert(np.std(data_3_noRandom_odd) == testing_sigma)
# assert(np.std(data_4_Random_odd) == testing_sigma)






