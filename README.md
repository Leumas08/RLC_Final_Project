# RLC_Final_Project

This repository is for the final project of Reinforcement Learning and Controls. <br/>
It utilizes the OffWorld Environment and the stablebaselines3 repository to evaluate 3 different algorithms.

Link to OffWorld Repository: https://github.com/offworld-projects/offworld-gym <br/>
Link to stablebaselines3 Repository: https://github.com/DLR-RM/stable-baselines3

To train and evaluate the DQN algorithm: python test_DQN.py <br/>
To train and evaluate the PPO algorithm: python test_PPO.py <br/>
To train and evaluate the A2C algorithm: python test_A2C.py <br/>
Note: The above scripts assume you have successfully installed offworld-gym using the instructions provided in their repository and installed the stabe-baselines3 library as well.

The results can be created by executing "tensorboard --logdir <dir/folder/>" and opening the link displayed if the command was successful.
