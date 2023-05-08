""""Object processor"""
import glob
import shutil
import os


source_path = '../source/*'
destination_path = '../destination/'
while True:
    postfix = [1, 2, 3]
    source_object = glob.glob(source_path)
    if len(source_object)>0:
        #print(source_object)
        object_path = source_object[0]
        #print(object_path)
        #print(shutil.copy(object_path, '.'))
        shutil.copy(object_path, '.')
        object_name = object_path.split('\\')[-1].split('.')
        copy_soruce_file_path = object_path.split('\\')[-1]
        prefix = object_name[0]
        postfix2 = object_name[1]
        #print(object_name)
        #print(type(object_name))
        for item in range(len(postfix)):
            filename = prefix + '_' + str(item) + '.' + postfix2
            #print(filename)
            shutil.copy(object_path,f'{destination_path}/{filename}')
        os.remove(object_path)
        os.remove(copy_soruce_file_path)
