import torch.optim


class Solver(torch.optim):
	def __init__(lr):
		self.optimizer = super().AdamW(
			model.parameters(),
			lr=configuration["lr"],
			)