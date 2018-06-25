import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas import read_json

# Reading Json

JSON_PATH = ('file:///home/intelivix_s2/Documentos/Projetos/Linkehub/'
             'processed-data/modules/files/stackoverflow_jobs.json')

read_params = {
    'path_or_buf': JSON_PATH,
    'orient': 'index'
}
readed_json = read_json(**read_params)

import ipdb; ipdb.set_trace()
