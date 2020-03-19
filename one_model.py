import re
import subprocess
import time
from os import popen
import random

#Clear all history
command_stop = "docker kill $(sudo docker ps -q)"
subprocess.Popen(command_stop,shell=True)
time.sleep(5)
command_clear = "docker rm $(sudo docker ps -a -q)"
subprocess.Popen(command_clear,shell=True)
time.sleep(5)

def run_container(container_name,container_model):
    command_run = 'nohup docker run --name {} {} > {}.log &'.format(container_name,container_model,container_name)
    subprocess.Popen(command_run,shell=True)
    print("Succesfully run container ",container_name,"collecting data now!")

container_list = ["test1","test2","test3","test4","test5","test6","test7","test8","test9","test10"]
#container_model_list = ["fuzzychen/1000batch","fuzzychen/vgg16","fuzzychen/inceptionv3","fuzzychen/res50","fuzzychen/xcep"]
container_model = "fuzzychen/inceptionv3"


#ran_list = random.sample(range(len(container_model_list)), len(container_model_list))
#ran_time = random.sample(range(0, 300), len(container_list))
#print("ran_list: ", ran_list)

for i in range(len(container_list)):
    run_container(container_list[i], container_model)
    print(container_list[i], container_model)
   # time.sleep(ran_time[i])
    time.sleep(50)
#    print("initializing~~~~~~~~~~~~Takes 180 seconds")

time.sleep(60)

#ran_list[i % len(container_model_list)