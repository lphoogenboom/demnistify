# this module takes data from ./data/raw/ and transforms it as defined below into /data/processed/
from pathlib import Path
import pandas as pd
import numpy as np

if __name__ == "__main__":
	# Input paths
	here = Path(__file__).resolve().parent
	path_raw = here/"data"/"raw"
	# MMNIST comes pre-split
	path_train = path_raw/"mnist_train.csv"
	path_test = path_raw/"mnist_test.csv"
	
	# Output path
	path_processed = here/"data"/"processed"
	
	# load raw data
	data_test = pd.read_csv(path_test)
	data_train = pd.read_csv(path_train)
	data_full = pd.concat([data_train, data_test], ignore_index=True) # We don't want to keep old indexing
	
	
	labels = data_full['label'].values.astype(np.uint8)
	images = data_full.drop(columns=['label']).values
	images = images.reshape(images.shape[0],28,28).astype(np.uint8) # create tensor for ease of use

	np.save(path_processed/"images.npy", images)
	np.save(path_processed/"labels.npy", labels)