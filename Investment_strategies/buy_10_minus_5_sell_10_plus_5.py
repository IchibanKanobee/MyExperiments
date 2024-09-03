class Asset:
	m_cash = 100.
	m_inv = 0.
	m_comission = 0.2
	
	def total_assets(self):
		return (self.m_cash + self.m_inv)
		
	
	def buy (self, drop_percentage, cash_percentage):
		cash_to_spend = cash_percentage / 100
		self.m_cash = self.m_cash - cash_to_spend - self.m_comission
		self.m_inv = self.m_inv + cash_to_spend


	def sell (self, up_percentage, cash_percentage):
		self.m_inv = self.m_inv * (1 + up_percentage / 100)
		to_sell = self.m_inv * cash_percentage / 100
		self.m_inv = self.m_inv - to_sell
		self.m_cash = self.m_cash + to_sell - self.m_comission
		

asset = Asset()
print (asset.total_assets())
asset.buy(5, 10)
print (asset.total_assets())
asset.sell(50, 5)
print (asset.total_assets())

