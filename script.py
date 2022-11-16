# python api written for CYSE 465 - lgsvl - lidar point cloud

# group members include: Viren Kumar, David Thai, Kinza Rizvi, Hajrah Chourdhry, Luke A____

# code grabbed from github/lgsvl/quickstart

from environs import Env
import lgsvl
from .wise import DefaultAssets, SimulatorSettings

print("Python API Quickstart #7: Saving a point cloud from the Lidar sensor")
env = Env()

sim = lgsvl.Simulator(env.str("LGSVL__SIMULATOR_HOST", lgsvl.wise.SimulatorSettings.simulator_host), env.int("LGSVL__SIMULATOR_PORT", lgsvl.wise.SimulatorSettings.simulator_port))
if sim.current_scene == lgsvl.wise.DefaultAssets.map_borregasave:
    sim.reset()
else:
    sim.load(lgsvl.wise.DefaultAssets.map_borregasave)

spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]
ego = sim.add_agent(env.str("LGSVL__VEHICLE_0", lgsvl.wise.DefaultAssets.ego_lincoln2017mkz_apollo5), lgsvl.AgentType.EGO, state)

sensors = ego.get_sensors()
for s in sensors:
    if s.name == "Lidar":
        s.save("lidar.pcd")
        break
