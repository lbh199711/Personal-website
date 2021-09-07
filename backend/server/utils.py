from django.conf import settings

import numpy as np
import os
import json

# helper functions
# General util functions
def bundle_request_data(data, signature="serving_default"):
    request_data = json.dumps({
        "signature_name": signature,
        "instances": data.tolist()
    })
    return request_data
    
# SentimentAnalysisView util functions
def load_word_index(json_path):
    a_file = open(os.path.join(settings.BASE_DIR, json_path), "r")
    word_index = json.load(a_file)
    return word_index

def remove_punct(sentences):
  sentences = sentences.replace(',', ' ')
  sentences = sentences.replace('.', ' ')
  sentences = sentences.replace('!', ' ')
  sentences = sentences.replace('?', ' ')
  sentences = sentences.replace('(', ' ')
  sentences = sentences.replace(')', ' ')
  sentences = sentences.replace('\'', ' ')
  sentences = sentences.replace('-', ' ')
  sentences = sentences.replace('*', ' ')
  return sentences

def process_data_SA(data, word_index):
    input_string = data.get('input_string')
    input_string = remove_punct(input_string)

    word_list = input_string.split()
    # word list to indexes
    num_list = []
    for word in word_list:
        index = word_index.get(word)
        if index is not None: #skip unknown words
            num_list.append(index)

    num_list_length = len(num_list)
    seq_lenght = 500
    # cut the list to seq_length
    if num_list_length > seq_lenght:
        num_list = np.asarray(num_list[0:seq_lenght])
    # pad the list to seq_length
    elif num_list_length < seq_lenght:
        padding = np.zeros(seq_lenght - num_list_length, dtype=int)
        num_list = np.append(padding, num_list)
        
    num_list = num_list.astype('int64')
    # reshape to -1,500
    return np.reshape(num_list,(-1,500))