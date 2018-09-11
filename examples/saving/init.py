"""
init.py 

Example of saving different network components to file

Contributors: salvadordura@gmail.com
"""

from netpyne import sim

from netParams import netParams
from cfg import cfg

sim.createSimulateAnalyze(netParams, cfg)

# Saving different network components to file
sim.cfg.saveJson = True

# save network params (rules) 
sim.saveData(include=['netParams'], filename='out_netParams')

# save network instance
sim.saveData(include=['net'], filename='out_netInstance')

# save sim config
sim.saveData(include=['simConfig'], filename='simConfig')

# save sim output data
sim.saveData(include=['simData'], filename='simData')

# save network instance with compact conn format (list instead of dict)
sim.cfg.compactConnFormat = True
sim.gatherData()
sim.saveData(include=['net'], filename='out_netInstance_compact')
