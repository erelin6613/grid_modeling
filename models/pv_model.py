class PVModel(object):
    """
    PVModel is an object modeling a photovoltaic system.

    @param: num_modules - number of photovoltaic moduels
                            in the system (not to be confused
                            with panels)
    @param: module_area - surface active area of one module
                            (area exposed to solar raiation)
    @param: eta_r - nominal module efficiency coeffiecient
    @param: eta_tr - efficiency coeffiecient attributed to
                        tracking system (deafult is no tracking
                        system efficiency, more info can be found at
                        https://www.mdpi.com/1996-1073/13/16/4224)
    @param: noct - Nominal Operating Cell Temperature (NOCT),
                    provided by manufacturer
    @param: beta - Temperature coefficient efficiency,
                    provided by manufacturer
    """

    def __init__(self, num_modules,
                module_area,
                eta_r=0.19,
                eta_tr=0.25,
                noct=45,
                beta=0.005):

        self.num_modules = num_modules
        self.module_area = module_area
        self.eta_r = eta_r
        self.eta_tr = eta_tr
        self.noct = noct
        self.beta = beta

    def calc_state(self, radiation, temperature_amb, temperature_prev=20):

        eta = self.eta_r*self.eta_tr*(
            1- (self.beta*(temperature_amb-temperature_prev)))
        state = eta*self.num_modules*radiation
        return state
