#!/usr/bin/env python3
import subprocess

with open('api-resources.txt', 'w') as f:
    subprocess.run(['kubectl','api-resources'], stdout=f)

file1 = open('api-resources.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    final = line.strip().split()[1].split(',')[0]
    if ('v1' not in final) and ('v1beta1' not in final) and ('v1alpha1' not in final):
        output = subprocess.getoutput('kubectl explain '+final)
        if output == 'the server doesn\'t have a resource type "'+final+'"':
            print('INVALID STRING');
        else:
            items = output.split()
            if items[len(items)-2].strip() == 'DESCRIPTION:' and items[len(items)-1].strip() == '<empty>':
                print("-------------------->",final, "-----------> X")
            else:
                print(final, "------> T")
