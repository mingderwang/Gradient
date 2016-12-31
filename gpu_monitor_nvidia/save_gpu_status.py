import pymongo
import time
from nvidia import *

if __name__ == '__main__':
    metric_init({})
    connection = pymongo.MongoClient("localhost", 27017)
    db = connection["gradient"]
    print ("Start collecting gpu status data.\nData will be saved to MongoDB localhost:27017")

    while(1):
        save_gpu_status_data()
        time.sleep(5)




def save_gpu_status_data():
    '''
    #Collect folling data
    timestamp
    gpu_util
    gpu_mem_speed
    gpu_graphics_speed
    '''
    gpu_num = get_gpu_num()
    for i in range(gpu_num):
        collection_name = "gpu%s_status" % i
        collection = db[collection_name]

        gpu_util_name = "gpu%s_util" % i
        gpu_mem_util_name = "gpu%s_mem_util" % i
        gpu_fan_name = "gpu%s_fan" % i
        gpu_power_usage_name = "gpu%s_power_usage_report" % i

        gpu_status_row = {"timestamp" : str(time.time()),
                "gpu_util" :  str(gpu_device_handle(gpu_util_name))
                "gpu_mem_util_name" : str(gpu_device_handle(gpu_mem_util_name))
                "gpu_fan" : str(gpu_devie_handle(gpu_fan_name))
                "gpu_power_usage" : str(gpu_device_handle(gpu_power_usage_name))
                }

        collection.insert(gpu_status_row)





