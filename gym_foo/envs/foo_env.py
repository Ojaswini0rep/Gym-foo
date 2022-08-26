import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from gym.envs.mujoco import MuJocoPyEnv
from gym.spaces import Box
import xml.etree.ElementTree as ET1


class inv_pendulum(MuJocoPyEnv.MujocoEnv,  utils.EzPickle):
    """
       ### Description
       This is the description
    """
    def __init__(self,**kwargs):

        FILE_PATH = os.getcwd() +'/drive/MyDrive/Colab Notebooks/inv_pendulum.py'
        observation_space = Box(low=-np.inf, high=np.inf, shape=(4,), dtype=np.float64)
        utils.EzPickle.__init__(self,**kwargs)
        MuJocoPyEnv.__init__(self, FILE_PATH, 5, observation_space=observation_space, **kwargs)


        # Angle at which to fail the episode
        self.theta_threshold_radians = 12 * 2 * math.pi / 360
        # cart position when the episode fails
        self.x_threshold = 2.4
        # steps after termination
        self.steps_beyond_terminated = None

        #Variable to store state 
        self.state = None

    def step(self, action):
        assert self.state is not None, "Call reset before using step method."
        # Carry out one step 
        self.do_simulation(action, self.frame_skip)
        xpos = self.sim.data.qpos[0]

    
        x = self.sim.data.qpos[0]
        x_dot = self.sim.data.qvel[0]
        theta = self.sim.data.qpos[1]
        theta_dot= self.sim.data.qpos[1]
        
        # Set State 
        self.state= [ x, x_dot, theta, theta_dot]
       

        # observation
        ob = self._get_obs() 

        # Check if done
        terminated = bool( x < -self.x_threshold or x > self.x_threshold or theta < -self.theta_threshold_radians or theta > self.theta_threshold_radians)

        # Calculate Reward
        if not terminated:
            reward = 1/abs(theta)
        elif self.steps_beyond_terminated is None:
            # Pole just fell! in this step 
            self.steps_beyond_terminated = 0
            reward = 0
        else:
            if self.steps_beyond_terminated == 0:
                logger.warn(
                    "You are calling 'step()' even though this "
                    "environment has already returned terminated = True. You "
                    "should always call 'reset()' once you receive 'terminated = "
                    "True' -- any further steps are undefined behavior."
                )
            self.steps_beyond_terminated += 1
            reward = 0.0
                
        
        return (ob,reward, terminated,False,{}, )
   

    def _get_obs(self):
      # later try returning self.state
        return np.concatenate(
            [
                self.sim.data.qpos.flat,
                self.sim.data.qvel.flat,
            ]
        )
  

    def viewer_setup(self):
        assert self.viewer is not None
        self.viewer.cam.distance = self.model.stat.extent * 0.5

    def reset_model(self):
        # Reset model to original state. 
        qpos = np.array([0 , 0])
        qvel = np.array([0 , 0])
        self.set_state(qpos, qvel)
        return self._get_obs()
        
    
