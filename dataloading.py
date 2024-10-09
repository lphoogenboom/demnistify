from pathlib import Path
import numpy as np
import torch as tt
import sys

class Dataset(tt.utils.data.Dataset):

	def __init__(self,images,labels):
		self.images = images  # (Batch, Height, Width)
		self.images = self.images[:, None]  # (Batch, 1, Height, Width)
		self.images = tt.from_numpy(self.images)  # Convert to tensor

		self.labels = tt.from_numpy(labels)  # (Batch)
		self.labels = tt.nn.functional.one_hot(self.labels.long(), num_classes=10)  # (Batch, 10)

	def __len__(self):
		return len(self.images)

	def __getitem__(self, index): # get image-label pair
		return dict(image=self.images[index], label=self.labels[index])

if __name__ == "__main__":

	here = Path(__file__).resolve().parent
	path_splits = here/"data"/"datasplits"
	path_processed = here/"data"/"processed"

	# split contains test data + train data + train data-->(5 * (train_##,val_##) overlapping)
	split = np.load(path_splits/"datasplit.npz")

	# load processed images and labels
	images = np.load(path_processed/"images.npy")
	labels = np.load(path_processed/"labels.npy")
    
	# use indices from split to create data for splits
	split_images_data = images[split["train_00"]]
	split_labels_data = labels[split["train_00"]]

	#  create Dataset for specific split
	dataset_train = Dataset(split_images_data,split_labels_data)

	# pass to dataset loader
	loader_train = tt.utils.data.DataLoader(dataset_train, batch_size=5, shuffle=True)

	for data in loader_train:
		image = data["image"]
		label = data["label"]
		print(f"Image shape: {image.shape}, Label shape: {label.shape}")
		print(f"Image min: {image.min()}, Image max: {image.max()}")
		sys.exit()  # Exit after first iteration