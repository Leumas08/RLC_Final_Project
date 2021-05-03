import gym
import offworld_gym
from offworld_gym.envs.common.channels import Channels
from offworld_gym.envs.common.actions import FourDiscreteMotionActions
from offworld_gym.envs.real.real_env import AlgorithmMode, LearningType
from stable_baselines3 import PPO as alg
import cloudpickle
import torch

# Load in the OffWorld Environment (Discrete with Monolith Simulation)
env = gym.make("OffWorldDockerMonolithDiscreteSim-v0", channel_type=Channels.RGB_ONLY)

# Apply a model to the environment and learn it for x time steps
model = alg("MlpPolicy", env, verbose=1, tensorboard_log = 'PPO1k/').learn(total_timesteps=1000)

# reset the environment
obs = env.reset()

# Test the Environment
for i in range(100):
    actions, _states = model.predict(obs,deterministic=True)
    obs, reward, done, info = env.step(actions)
    env.render()
    #print(i)
    if done:
        obs = env.reset()
        torch.save(model.policy.state_dict(), 'PPO_1k.pt')

env.close()
