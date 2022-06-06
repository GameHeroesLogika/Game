import json
import os
config = dict()
def create_Json(name_Json, name_Dict):
    abspath_main_dir = os.path.join(os.path.abspath(__file__ + "/.."),"saves")
    print("Путь сохранении:", abspath_main_dir)
    os.chdir(abspath_main_dir)
    with open(name_Json,"w") as file:
        json.dump(name_Dict, file, ensure_ascii=False, indent=4)
def createDict(name_Json, name_Dict):
    abspath_json_file = os.path.join(os.path.abspath(__file__ + "/.."),"saves/" + name_Json)
    print(abspath_json_file)
    with open(abspath_json_file, "r") as file:
        name_Dict = json.load(file)
    return name_Dict
config = createDict("config.json",config)