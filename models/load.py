import numpy as np

# distribution coefficenints dervied from the research effort:
# https://www.researchgate.net/publication/235675567_A_frequentist_and_Bayesian_regression_analysis_to_daily_peak_electricity_load_forecasting_in_South_Africa
# coefficients reflect the portion of maximum load which is not the same as a critical load

hour_loads = {
    0: 0.722,
    1: 0.694,
    2: 0.667,
    3: 0.667,
    4: 0.639,
    5: 0.694,
    6: 0.778,
    7: 0.9,
    8: 0.917,
    9: 0.917,
    10: 0.9,
    11: 0.889,
    12: 0.889,
    13: 0.875,
    14: 0.861,
    15: 0.834,
    16: 0.847,
    17: 0.861,
    18: 0.917,
    19: 0.972,
    20: 1,
    21: 0.972,
    22: 0.93,
    23: 0.834,
}

max_p = 620
mean_p = 194.375
std_p = 120
min_p = 150
cf = 0.5123


class Consumer:
    def __init__(
        self,
        min_load=min_p,
        max_load=max_p,
        avg_load=mean_p,
        std=std_p,
        cf=cf,
        use_hour_priors=True,
        hours_dict=hour_loads,
    ):

        self.min_load = min_load
        self.max_load = max_load
        self.avg_load = avg_load
        self.std = std
        self.cf = cf

        if (use_hour_priors) and (hours_dict is not None):
            self.hour_priors = hours_dict

    def load_grid(self, hour=None):

        if hour is None:
            return self.avg_load

        if hour >= 24:
            hour = hour % 24

        load_coef = self.hour_priors[hour]

        load_scenario = np.random.choice(['min', 'max', 'regular'],
            size=1, p=[(1-self.cf)/4, self.cf, 3*(1-self.cf)/4])[0]

        if load_scenario == 'min':
            load = np.random.normal(self.min_load, self.std, 1)[0]
        elif load_scenario == 'max':
            load = np.random.normal(self.max_load, self.std, 1)[0]
        else:
            load = np.random.normal(load_coef*self.max_load, self.std, 1)[0]

        load = 0 if load < 0 else load

        return load
