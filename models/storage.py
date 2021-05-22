capacity = 160 * 2  # 2 storage systems 160 kWh each
depth_of_discharge = 0.7
critical_discharge = 0.2
eta = 0.96


class StorageModel(object):
    def __init__(
        self,
        capacity=capacity,
        depth_of_discharge=depth_of_discharge,
        critical_discharge=critical_discharge,
        eta=eta,
    ):

        self.capacity = capacity
        self.depth_of_discharge = depth_of_discharge
        self.critical_discharge = critical_discharge
        self.eta = eta
        self._init_storage()

    def _init_storage(self):
        self.max_capacity = self.capacity * self.eta
        self.min_capacity = self.capacity * self.critical_discharge
        self.storage = self.depth_of_discharge * self.capacity * self.eta

    def process_load(self, load):
        self.storage += load

        if self.max_capacity < self.storage:
            self.storage = self.max_capacity
        elif self.min_capacity > self.storage:
            self.storage = self.min_capacity

        return self.storage
