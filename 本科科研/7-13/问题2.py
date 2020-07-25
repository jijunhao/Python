"""
依次取下面字典中的”小白”“好好学习”“天天向上”并打印。
"""

class_info = {"python":[
    {"name":"小明","hobby":["写python", "好好学习"]},
    {"name":"小白","hobby":["跑步", "吃饭"]},
    {"name":"小红","hobby":["98k", "天天向上"]}
]}
print(class_info["python"][1]["name"],
      class_info["python"][0]["hobby"][1],
      class_info["python"][2]["hobby"][1])
