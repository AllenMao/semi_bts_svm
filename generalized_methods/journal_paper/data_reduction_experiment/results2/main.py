import numpy as np
import os
import sys
import fcntl
import copy
import pdb
sys.path.append('/home/local/USHERBROOKE/havm2701/git.repos/semi_bts_svm/semi_bts_svm/generalized_methods/')
sys.path.append('/home/local/USHERBROOKE/havm2701/git.repos/semi_bts_svm/semi_bts_svm/generalized_methods/journal_paper/data_reduction_experiment/')
from string import Template
import mlpython.datasets.store as dataset_store
from mlpython.learners.third_party.libsvm.classification import SVMClassifier
import compute_statistics
import time
import data_utils
from libsvm_training_reduction import svm_model as svm_model
from libsvm_training_reduction import create_datasets as create_datasets
#import ipdb

# make a dictionary of the selected brains with their best c and gamma parameters. 
#brain_list = {'HG_0002': [1,50], 'HG_0001': [1,0.01], 'HG_0003': [1,1], 'HG_0010': [1,50], 'HG_0008': [1,5], 'HG_0012': [50,50], 'HG_0011': [1,5], 'HG_0022': [1,5], 'HG_0025': [1,50], 'HG_0027': [1,10], 'LG_0008': [1,200], 'LG_0001': [1,50], 'LG_0006': [1,1], 'LG_0015': [100,200], 'HG_0014': [1,5]}
brain_list = {'HG_0012': [50,50], 'HG_0011': [1,5], 'HG_0022': [1,5], 'HG_0025': [1,50], 'HG_0027': [1,10]}
sys.argv.pop(0); # Remove first argument

# Get arguments
dataset_directory = sys.argv[0]
#dataset_name = sys.argv[1]
output_folder = sys.argv[1]

results_path = output_folder + '/libsvm_results/'
if not os.path.exists(results_path):
    os.makedirs(results_path)

#Factors = [1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8]
#Factors = [9,10,11,12,13,14,15,16,17,18,19,20]
Factors = [2000,1500,1000,900,800,700,600,500,400,300,200,100,75,50,40,30,20,10]
# measure the sensitivity of gamma for the selected brains and save the text file

brain_names = brain_list.keys()
results_file_c = 'libsvm_measures_factor.txt'
results_file_metadata = 'libsvm_measures_factor_metadata.txt'

for brain in brain_names[0:2]:
    dataset_dir = os.path.join(os.environ.get('MLPYTHON_DATASET_REPO') + '/' + dataset_directory, brain)
    all_data = data_utils.load_data(dataset_dir)
    test = all_data['test']
    fulltrain_backup = all_data['finaltrain']    
    resultc1, resultc2 = '' ,''           
    brain_str = brain + ' \n'
    
    for factor in Factors:
        resultc3 = ''
        dice_t = np.zeros((10))
        processed_timet = np.zeros((10))
        for nb in range(10):
            resultc3 = ''
            all_data = data_utils.data_reduction(fulltrain_backup , factor)
            all_data['test'] = test
            print len(fulltrain_backup[0])
            print len(all_data['finaltrain'][0])
            train = [int(t[1]) for t in all_data['train'][0]] 
            valid = [int(v[1]) for v in all_data['valid'][0]]
            finaltrain = [int(f[1]) for f in all_data['finaltrain'][0]]
            train = np.asarray(train)
            valid = np.asarray(valid)
            finaltrain = np.asarray(finaltrain)
            datasets = create_datasets(all_data)
            dice_t[nb] , processed_timet[nb] = svm_model(datasets)


            resultc3 += 'factor = ' + str(factor) + '\n'
            resultc3 += 'finaltrain = ' + str(len(all_data['finaltrain'][0])) + '\n'
            resultc3 += 'train = ' + str(len(all_data['train'][0])) + '\t' + 'class_0 = ' + str(sum(train==0)) + '\t' +  'class_2 = ' + str(sum(train==2)) + '\t' +'class_3 = ' + str(sum(train==3)) + '\t' +'class_4 = ' + str(sum(train==4)) + '\n' 
            resultc3 += 'valid = ' + str(len(all_data['valid'][0])) + '\t' + 'class_0 = ' + str(sum(valid==0)) + '\t' +'class_2 = ' + str(sum(valid==2)) + '\t' +'class_3 = ' + str(sum(valid==3)) + '\t' +'class_4 = ' + str(sum(valid==4)) + '\n' 
            resultc3 += 'healthy = ' +  str(sum(train==0) + sum(valid==0)) + '\t' + 'non_healthy = ' + str(sum(finaltrain==2) + sum(finaltrain==3) + sum(finaltrain==4)) + '\n'
            resultc3 += 'dice = ' "%.7f" % dice_t[nb] + '\t' + 'processed_time = ' + "%.4f" % processed_timet[nb] + '\n'
            resultc3 += '\n'
            if not os.path.exists(results_path + results_file_metadata):
              with open(results_path + results_file_metadata,'w') as d:
                d.write(brain_str)
                d.write(resultc3)
            else:
              with open(results_path + results_file_metadata,'a') as d:
                d.write(brain_str )
                d.write(resultc3)            
            dice_c = dice_t.mean()
            processed_timec = processed_timet.mean()
        resultc1 += "%.7f" % dice_c + '\t'
        resultc2 += "%.4f" % processed_timec + '\t'

    resultc1 += '\n'
    resultc2 += '\n'
     
    if not os.path.exists(results_path + results_file_c):
          with open(results_path + results_file_c,'w') as c:
            c.write(brain_str)
            c.write(resultc1)
            c.write(resultc2)
    else:
          with open(results_path + results_file_c,'a') as c:
              c.write(brain_str)
              c.write(resultc1)
              c.write(resultc2)

    if not os.path.exists(results_path + results_file_metadata):
          with open(results_path + results_file_metadata,'w') as d:
            d.write(brain_str)
            d.write(resultc3)
    else:
          with open(results_path + results_file_metadata,'a') as d:
              d.write(brain_str)
              d.write(resultc3)
