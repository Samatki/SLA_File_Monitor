import os
import time
import subprocess


def run_script(file_path,file):
    if os.path.splitext(os.path.join(file_path,file))[1] == '.scss':
        os.system('SASS ' + os.path.join(file_path,file))
        pass

def file_monitor(FILE_PATH,FILE_ARRAY):
    monitor_array_A = []
    monitor_array_B = []
    for file in FILE_ARRAY:
        monitor_array_A.append(os.stat(os.path.join(FILE_PATH,file)).st_mtime)

    while True:
        monitor_array_B = []
        for file in FILE_ARRAY:
            monitor_array_B.append(os.stat(os.path.join(FILE_PATH,file)).st_mtime)
        if monitor_array_A != monitor_array_B:
            for inx, file in enumerate(monitor_array_B):
                if monitor_array_A[inx] != monitor_array_B[inx]:
                    print FILE_ARRAY[inx] + ' Updated'
                    run_script(FILE_PATH,FILE_ARRAY[inx])
            monitor_array_A = monitor_array_B 
        time.sleep(0.2)


if __name__ == "__main__":
    print 'File Scanner v1'
    print '==============='
    
    file_list = []
    list_status = True

    file_path = raw_input('What is the file path?')
    
    while list_status:
        file_name = raw_input('What is the file name?')
        if file_name == '':
            if file_list == []:
                print 'Nothing entered'
            else:
                print 'Running Script'
                file_monitor(file_path,file_list)
        else:
            if os.path.exists(os.path.join(file_path,file_name)):
                file_list.append(file_name)
                print 'File found'
            else:
                print 'No file Found'


