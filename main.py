# -*- coding: utf-8 -*-
# python 3.6

import psutil


class Demo:
    def users(self):
        userss = psutil.users()
        name = [x[0] for x in userss]
        host = [x[2] for x in userss]

        boot = psutil.boot_time()

        dict_user = {"Username": name,
                     "Host": host,
                     "Boot time": boot}
        print("USER \n", dict_user)

    def cpu(self):
        logical_cores = psutil.cpu_count()
        cores = psutil.cpu_count(logical=False)

        dict_cpu = {"Cores": cores,
                    "Logical cores": logical_cores}
        print("CPU: \n", dict_cpu)

    def mem(self):
        vir_mem = psutil.virtual_memory()

        dict_mem = {"Total memory": vir_mem[0],
                    "Used memory": vir_mem[3],
                    "Free memory": vir_mem[4]}
        print("VIRTUAL MEMORY (Byte)\n", dict_mem)

    def swap(self):
        swap = psutil.swap_memory()
        dict_swap = {"Total memory": swap[0],
                     "Used memory": swap[1],
                     "Free memory": swap[2]}

        print("SWAP MEMORY (Byte) \n", dict_swap)


if __name__ == "__main__":
    obj = Demo()
    obj.users()
    obj.cpu()
    obj.mem()
    obj.swap()
