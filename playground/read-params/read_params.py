import yaml

f = open("../params/train.yml", "r")
params = yaml.load(f, Loader=yaml.SafeLoader)
f.close()

print(params)
print(type(params))
print(params['DATASET'])
print(type(params['DATASET']))