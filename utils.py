import numpy as np
import pandas as pd

MAX_LENGTH = 150 #n = 150
DICTIONARY_ARRAY = ['a','b','c','d','e','f','g','h','i','j','k','l',
                    'm','n','o','p','q','r','s','t','u','v','w',
                    'x','y','z','0','1','2','3','4','5','6','7',
                    '8','9',' ',',','.','!','?',':','\"','\'',
                    '/','|','_','@','#','$','&','-','(',')','+','*'] #DICTIONARY
DICTIONARY_SIZE = len(DICTIONARY_ARRAY) # |V| = DICTIONARY_SIZE


def convert_text_to_numpy(text):
    """
    Convert feature (text) to matrix
    :param text:
    :return: numpy array (matrix) with shape (|V| * n)
    """
    if len(text) > MAX_LENGTH:
        text = text[0:MAX_LENGTH]
    text_matrix = np.zeros((DICTIONARY_SIZE, MAX_LENGTH))
    for i in range(len(text)):
        index = DICTIONARY_ARRAY.index(text[i])
        text_matrix[index][i] = 1
    return text_matrix

def create_feature_matrix(matrix1, matrix2):
    """
    Concentrate matrix to create input data of an item
    :param matrix1:
    :param matrix2:
    :return: features matrix of an item
    """
    return np.concatenate(matrix1, matrix2)

def stack_matrix(array_of_matrix):
    """
    Create input of network
    :param array_of_matrix:
    :return: 3d-input of network
    """
    return np.stack(array_of_matrix, axis=0)

def creat_movie_dictionary():
    df = pd.read_csv('../data/movies.csv', names=['movieId', 'title', 'genres'])
    values = df.values
    values = values[1:-1]
    print(len(values[0]))
    # for item in values:
creat_movie_dictionary()
