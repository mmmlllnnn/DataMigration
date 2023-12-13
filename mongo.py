#连接 MongoDB以字典形式返回数据表的字段和嵌套关系
global mongo
mongo = {}

class Dict:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    def cle(self):
        mongo.clear()
        return mongo
    def main(self, dictionary=None, father=None):
        if dictionary is None:
            dictionary=self.dictionary 
            father=[]
            if dictionary is None:
                return mongo
        for key, value in dictionary.items():
            if isinstance(value, list):
                if (len(value) > 0):
                    if (type(value[0]) == dict):
                        father.append(key)
                        self.main(value[0], father)
                        father.remove(key)
                if (len(value) > 0):
                    if (type(value[0]) != dict):
                        a = '.'.join(father)
                        if a == '':
                            b = key
                        else:
                            b = "{father}.{key}".format(father='.'.join(father), key=key)
                        if mongo.get(key) == None:
                            mongo[key] = "${b}".format(b=b)
                        else:
                            mongo['{mark}_{key}'.format(key=key, mark=a)] = "${b}".format(b=b)
            elif isinstance(value, dict):
                father.append(key)
                self.main(value, father)
                father.remove(key)
            else:
                a = '.'.join(father)
                if a == '':
                    b = key
                else:
                    b = "{father}.{key}".format(father='.'.join(father), key=key)
                if mongo.get(key) == None:
                    mongo[key] = "${b}".format(b=b)
                else:
                    mongo['{mark}_{key}'.format(key=key, mark=a)] = "${b}".format(b=b)
        return mongo
