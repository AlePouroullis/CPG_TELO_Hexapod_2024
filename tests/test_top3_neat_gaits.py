"""View top 3 gaits generated by NEAT for the CPG controller
"""
import sys
import os

sys.path.append(os.path.abspath("."))

from hexapod.controllers.cpg_controller import CPGParameterHandlerMAPElites
import controller_tools
import adapt.MBOA as map_handler
import numpy as np

# All Failure scenarios for reference
# S0 = [[]]
# S1 = [[1],[2],[3],[4],[5],[6]]
# S2 = [[1,4],[2,5],[3,6]]
# S3 = [[1,3],[2,4],[3,5],[4,6],[5,1],[6,2]]
# S4 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]

FAILED_LEGS = []
COLLISION_FATAL = True

if __name__ == "__main__":
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "all-best-genomes.txt")
	
	individuals = controller_tools.read_in_individuals([path])
	for top in range(1,4):
		print(controller_tools.evaluate_gait_cpg(individuals[-top], visualiser=True, collision_fatal=COLLISION_FATAL, delay=0.003, failed_legs=FAILED_LEGS)[0])