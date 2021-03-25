import yaml

print(yaml.load(open("test.yml"), Loader=yaml.FullLoader))

print(yaml.dump({'a': ['name', 'age']}))

with open("test1.yml", "w") as f:
    yaml.dump(data={'a': ['name', 'age']}, stream=f)

