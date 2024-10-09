import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleConv(nn.Module):
	def __init__(self):
		super(SimpleConv, self).__init__()

		# Convolutional block: Conv2D -> ReLU -> MaxPool
		self.conv_block = nn.Sequential(
			nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),  # Conv layer
			nn.ReLU(),  # Activation function
			nn.MaxPool2d(kernel_size=2, stride=2)  # Downsampling (Max pooling)
			)

		# Fully connected layer to map down the features
		self.fc = nn.Linear(32 * 14 * 14, 10)  # Assuming input images are 28x28 (like MNIST)

	def forward(self, x):
		# Forward pass through convolutional block
		x = self.conv_block(x)

		# Flatten the output from the conv block
		x = x.view(x.size(0), -1)

		# Forward pass through fully connected layer
		x = self.fc(x)

		return x

	def describe(self):
		model = SimpleConv()
		print(model)


# Instantiate the model

if __name__ == "__main__":
	model = SimpleConv()
	# Print the model architecture
	model.describe()
