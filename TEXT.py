import json

with open("c:/Python/MY_TEST.json") as m:
	try:
		res = json.load(m)
	except ValueError as ex:
		print(ex)
		res = {}

print(res)

