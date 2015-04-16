from ann.net import RecurrentNeuralNet
from simulator.environment import Environment
import numpy as np
class Simulator():

    def __init__(self, pull=False, wrap=True):
        if wrap:
            self.layers = [5,2,2]
        else:
            self.layers = [7,2,2]
        self.agent = RecurrentNeuralNet(self.layers, wrap=wrap)
        self.environment = Environment(30,15, pull=pull, wrap=wrap)

    def run(self, p, rec=False):
         parameters = self.agent.restructure_parameters(p)
         self.agent.set_weights(parameters)
         return self.environment.score_agent(self.agent, timesteps=600, rec= rec)

    def get_recording(self):
        return self.environment.get_recording()