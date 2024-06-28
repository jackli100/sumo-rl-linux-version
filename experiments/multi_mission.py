import subprocess
from multiprocessing import Pool

def run_program(command):
    # 运行命令
    subprocess.run(command, check=True)

if __name__ == "__main__":
    # 定义要运行的命令和参数
    commands = [
        # 17-stage (net-2)
        ["python", "experiments/train_class2.py",
         '--num_of_episodes', '9',
         '--net_path', "sumo_rl/nets/2way-single-intersection/single-intersection-4.net.xml",
         '--total_timesteps', '900000',
         '--fix_ts',
         '--proportion_of_saturations', '0.75,0.75,0.75,0.75',  
         '--note', 'intersection-4, 0.75 saturation, fix ts'],
        ["python", "experiments/train_class2.py",
         '--num_of_episodes', '9',
         '--net_path', "sumo_rl/nets/2way-single-intersection/single-intersection-3.net.xml",
         '--total_timesteps', '900000',
         '--fix_ts',
         '--proportion_of_saturations', '0.75,0.75,0.75,0.75',  
         '--note', 'intersection-3, 0.75 saturation, fix ts'] 
    ]
    # 使用多进程池并行运行命令
    with Pool(processes=len(commands)) as pool:
        pool.map(run_program, commands)
