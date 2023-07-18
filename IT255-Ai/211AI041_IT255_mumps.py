# Import necessary libraries
# import os
# os.environ["THEANO_FLAGS"] = "compiler=mingw32"

import pymc3 as pm
import numpy as np

# Create a PyMC3 model
with pm.Model() as model:
    # Define categorical variables with their probabilities
    I = pm.Categorical('I', [0.8, 0.2])  # P(I)
    R = pm.Categorical('R', [0.4, 0.6])  # P(R)
    M = pm.Categorical('M', [
        [0, 1],  # P(M | I = +i, R = +r)
        [1, 0],  # P(M | I = +i, R = -r)
        [0, 1],  # P(M | I = -i, R = +r)
        [0.7, 0.3]  # P(M | I = -i, R = -r)
    ], shape=4)

    # Define the deterministic variable p_IRM
    p_IRM = pm.Deterministic('p_IRM', pm.math.switch(
        pm.math.eq(I, 0),
        pm.math.switch(
            pm.math.eq(R, 0),
            pm.math.switch(
                pm.math.eq(M, 0),
                0,
                pm.math.switch(
                    pm.math.eq(M, 1),
                    0,
                    0
                )
            ),
            pm.math.switch(
                pm.math.eq(M, 0),
                0,
                pm.math.switch(
                    pm.math.eq(M, 1),
                    1,
                    0
                )
            )
        ),
        pm.math.switch(
            pm.math.eq(R, 0),
            pm.math.switch(
                pm.math.eq(M, 0),
                0,
                pm.math.switch(
                    pm.math.eq(M, 1),
                    1,
                    0
                )
            ),
            pm.math.switch(
                pm.math.eq(M, 0),
                0.7,
                pm.math.switch(
                    pm.math.eq(M, 1),
                    0.3,
                    0
                )
            )
        )
    ))

    # Define observed values
    observed_values = {'R': 1}

    # Sample from the model
    trace = pm.sample(10000, tune=2000, cores=1)

    # Calculate the summary statistics for p_IRM
    p_irm = pm.summary(trace, var_names=['p_IRM'])
    print("Table with I R M values and P(I,R,M):")
    print(p_irm, type(p_irm))

    # Calculate the marginal probability P(+m) that you have the mumps
    p_m = np.mean(trace['M'])
    print("Marginal probability P(+m) that you have the mumps:", p_m)

    # Calculate the probability P(+r | +m) that your roommate has the mumps given that you have the mumps
    p_r_given_m = np.mean(trace['R'][trace['M'][:, 0] == 1])
    print("Probability P(+r | +m) that your roommate has the mumps given that you have the mumps:", p_r_given_m)
