import os
import sys

import gymnasium as gym
from stable_baselines3.dqn.dqn import DQN



if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
import traci

from sumo_rl import SumoEnvironment


if __name__ == "__main__":
    # 修改这个变量
    output_folder = "outputs/dqn-0623-t1"

    # 维持默认即可
    csv_name = "dqn"
    tripinfo_name = "tripinfos.xml"
    out_csv_name = os.path.join(output_folder, csv_name)
    tripinfo_output_name = os.path.join(output_folder, tripinfo_name)
    tripinfo_cmd = f"--tripinfo {tripinfo_output_name}"

    env = SumoEnvironment(
        net_file="sumo_rl/nets/2way-single-intersection/single-intersection-2.net.xml",
        route_file=r"D:\trg1vr\sumo-rl-main\sumo-rl-main\output.rou.xml",
        out_csv_name=out_csv_name,
        single_agent=True,
        use_gui=False,
        num_seconds=100000,
    )
    # 创建结果文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 加载模型
    model = DQN.load(r"D:\trg1vr\sumo-rl-main\sumo-rl-main\outputs\dqn-20240623-1151-1\model.zip")
    model.set_env(env)
    model.learn(total_timesteps=200000)
