from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold

if __name__ == "__main__":
	here = Path(__file__).resolve().parent
	path_processed = here/"data"/"processed"
	path_labels = path_processed/"labels.npy"
	path_images = path_processed/"images.npy"

	path_split = here/"data"/"datasplits"

	images = np.load(path_images)
	labels = np.load(path_labels)

	# Create index lists for splitting data
	split = dict()
	idx_train, idx_test, _, _ = train_test_split(
        range(len(labels)),
        labels,
        test_size=0.2,
        stratify=labels,
    )

	# Indices in images & labels of training and test data
	split["train"] = idx_train
	split["test"] = idx_test

	# Use indexes with training data to create 5-fold split of training data into 5 new train+val sets (new sets overlap in data)
	skf_train_val = StratifiedKFold(n_splits=5, shuffle=True)
	for i, (idx_train, idx_va) in enumerate(skf_train_val.split(split["train"], labels[split["train"]])):
		split[f"train_{i:02d}"] = idx_train
		split[f"val_{i:02d}"] = idx_va

	# save test data, train data and 5 splits of the train data (train_## + val_##)
	np.savez(path_split/"datasplit.npz", **split)

	"""Print datasplit information"""
	print("Datasplit information:")
	print(f" - Number of samples: {len(labels)}")
	print(f" - Number of train samples: {len(split['train'])}")
	print(f" - Number of test samples: {len(split['test'])}")
	print(f" - Number of train_0* samples: {len(split['train_00'])}")
	print(f" - Number of val_0* samples: {len(split['val_00'])}")

	nbins = 11
	plt.hist(
		[labels[split["train"]], labels[split["test"]]],
		bins=np.arange(nbins) - 0.5,
		rwidth=0.5,
		linewidth=0.5,
		label=["Train", "Val"],
		color=["#2ab0ff", "orange"],
	)
	plt.xticks(range(nbins - 1))
	plt.title(f"Histogram of the N={len(labels)} labels of the MNIST dataset")
	plt.legend()
	plt.tight_layout()
	# plt.show()
	plt.savefig(here/"out"/"images"/"histogram_labels_train_test.png", dpi=300, bbox_inches="tight")
	plt.close()

	"""Plot the histogram of the labels of the training and validation data for the 3-fold cross-validation"""
	nbins = 11
	plt.hist(
		[labels[split["train_00"]], labels[split["val_00"]]],
		bins=np.arange(nbins) - 0.5,
		rwidth=0.5,
		linewidth=0.5,
		label=["Train_00", "Val_00"],
		color=["#2ab0ff", "orange"],
	)
	plt.xticks(range(nbins - 1))
	plt.title(f"Histogram of the N={len(split['train'])} labels of the training split")
	plt.legend()
	plt.tight_layout()
	# plt.show()
	plt.savefig(here/"out"/"images"/"histogram_labels_train_val_00.png", dpi=300, bbox_inches="tight")
	plt.close()