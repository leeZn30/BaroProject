import os
import psutil

class gpu:

    def gpu_fixed():
        # gpu_fixed 딕셔너리들을 담을 리스트
        gpus_fixed = []
        # gpu 각각의 고정된 값을 담아줌, 메모리 총량, 이름, 인덱스, Ip
        gpu_fixed = {}
        # 총 GPU 메모리 총량을 더해줌
        total_gpu = {}

        # info = "GPU\n"

        #gpu 개수(index 뽑기 용)
        number_of_gpu = int(os.popen("nvidia-smi -q -d memory | grep 'Attached GPUs'").read().split(':')[1])
        #각 gpu 메모리 총량
        gpu_memories = os.popen("nvidia-smi -q -d memory | grep 'Total'").read().strip().split('\n')
        #gpu 모델명
        gpu_models = os.popen("nvidia-smi -L").read().split('\n')

        total_gpu_memory_capacity_MB = 0

        for i in range(number_of_gpu):
            gpu_model = gpu_models[i]

            gpu_info = []

            name: str = ' '.join(gpu_model.split()[2:-2])
            memory: int = int(gpu_memories[i*2].split(':')[-1].split()[0])

            total_gpu_memory_capacity_MB += memory

            gpu_fixed["gpu_index"] = i
            gpu_fixed["gpu_name"] = name
            gpu_fixed["each_total_gpu_memory_capacity_MB"] = memory 
            
            gpus_fixed.append(gpu_fixed)
            gpu_fixed = {}

            # gpu_info.extend([name, memory, using_memory, using_percent])



            # gpus_info.append(gpu_info)
        total_gpu["total_gpu_memory_capacity_MB"] = total_gpu_memory_capacity_MB
        gpus_fixed.append(total_gpu)

        return gpus_fixed

    def gpu_change():
        #변하는 gpu 딕셔너리를 담을 리스트
        gpus_change = []
        #각 gpu 딕셔너리, 인덱스, ip, 각 gpu사용량(MB), 각 gpu사용률(%), ip는 나중에 따로
        gpu_change = {}

        gpu_using_memories = os.popen("nvidia-smi -q -d memory | grep 'Used'").read().strip().split('\n')

        #gpu 개수(index 뽑기 용)
        number_of_gpu = int(os.popen("nvidia-smi -q -d memory | grep 'Attached GPUs'").read().split(':')[1])
        
        #각 gpu 메모리 총량
        gpu_memories = os.popen("nvidia-smi -q -d memory | grep 'Total'").read().strip().split('\n')

        for i in range(number_of_gpu):
            
            using_memory: int = int(gpu_using_memories[i*2].split(':')[-1].split()[0])
            using_percent: float = round(int(gpu_using_memories[i*2].split(':')[-1].split()[0])/int(gpu_memories[i*2].split(':')[-1].split()[0])*100, 3)

            gpu_change["gpu_index"] = i
            gpu_change["gpu_memory_using_MB"] = using_memory
            gpu_change["gpu_memory_using_percent"] = using_percent

            gpus_change.append(gpu_change)
            gpu_change = {}
        return gpus_change


print(gpu.gpu_fixed())
print(gpu.gpu_change())