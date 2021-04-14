class Budget:
	def __init__(self, category, availableBalance = 0):
		self.category  = category
		self.availableBalance = availableBalance

	def depositFunds(self, amount):
		''' Adds the amount provided to the residual balance of the budget'''
		self.availableBalance += amount
		return self.availableBalance

	def withdrawFunds(self, amount):
		''' Withdraws the amount specified from the residual balance of the budget'''
		if (amount <= self.availableBalance):
			self.availableBalance -= amount
			return self.availableBalance
		else:
			print(f"You just tried to withdraw more than the available funds in the {self.category} budget")

	def balance(self):
		''' Prints the available balance of the budget category upon which it is called upon'''
		print(f"The available balance in the {self.category} budget is {self.availableBalance} naira")

	def transferFunds(self, categoryToTransferTo, amount):
		self.availableBalance -= amount
		categoryToTransferTo.availableBalance += amount
		print(f"{amount} naira has been transferred from {self.category} budget to {categoryToTransferTo.category} budget")
		

	


