import json

class VedovelleLoader:

    def loadVedovelleFromJson(filepath: str) -> list:
        f = open(r"resources\Vedovelle_final.json", "r")
        loadedJson = json.load(f)

        return loadedJson 

