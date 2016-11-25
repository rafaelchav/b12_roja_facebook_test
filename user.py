import requests
import json

class User:
	nombre = ""

	def __init__(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBANkXbwmig9IXP4a5oWVCR3GeJVvjwC4Pd5FXVaT1lTZAz40gcxBK1dDvimxCBC5VTvxxD9BqZAUSyRR2SittUE5xnMXNjVbaMHvNV9BfGYDj7J1oYeI9ztf2vmxxsBcYzEZCEPsuwMCZApze9skuYvAqscV1mgZDZD"

	def obtenInfo(self):
		parametros = {"access_token": self.token}
		resultado = requests.get(sel.url, params= parametros).json()
		print(resultado)
		return resultado
