import time
import constants

class main():
    def __init__(self):
        self.ratelimit_delay = constants.ratelimit_delay
        self.burst_index = constants.ratelimit_burst_size
        self.burst_delay = constants.ratelimit_burst_delay
        self.limited_in_burst = False

    def increase_ratelimit(self):
        time.sleep(self.ratelimit_delay) #Wait for the rate limit to be over.
        self.ratelimit_delay += constants.ratelimit_increment #Add to the delay to try to not get ratelimited again.
        self.burst_delay += constants.ratelimit_burst_increment
        self.limited_in_burst = True
        print(constants.colors.yellow + f"Rate delay increased. Now {round(self.ratelimit_delay, 2)} seconds." + constants.colors.default)
        print(constants.colors.yellow + f"Burst delay increased. Burst delay now {round(self.burst_delay, 2)} seconds." + constants.colors.default)
    def ratelimit(self):
        time.sleep(self.ratelimit_delay) #Wait for the rate limit to be over.
        self.burst_index -= 1
        if self.burst_index == 0:
            print(constants.colors.purple + f"Burst limit reached. Sleeping {round(self.burst_delay, 2)} seconds." + constants.colors.default)
            time.sleep(self.burst_delay) 
            self.burst_index = constants.ratelimit_burst_size #Reset the burst index.
            if not self.limited_in_burst:
                self.ratelimit_delay -= constants.ratelimit_decrement #Try to decrease the rate limit.
                self.burst_delay -= constants.ratelimit_burst_decrement #Try to decrease the burst delay.
                if (self.ratelimit_delay < constants.ratelimit_minimum): #Make sure the value doesn't go below the minimum.
                    self.ratelimit_delay = constants.ratelimit_minimum
                if (self.burst_delay < constants.ratelimit_burst_minimum): #Make sure the value doesn't go below the minimum.
                    self.burst_delay = constants.ratelimit_burst_minimum
                print(constants.colors.green + f"Tryed to decrease rate limit. Now {round(self.ratelimit_delay, 2)} seconds." + constants.colors.default)
                print(constants.colors.green + f"Tryed to decrease burst delay. Now {round(self.burst_delay, 2)} seconds." + constants.colors.default)
            self.limited_in_burst = False #Reset the ratelimit check variable.
