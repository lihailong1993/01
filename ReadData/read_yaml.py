import yaml

with open("../Data/day.yaml", 'r',encoding="utf-8") as f:
    data = yaml.load(f)
    print(data)  # 打印data返回值