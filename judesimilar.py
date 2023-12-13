from fuzzywuzzy import fuzz
#工具返回相似度最高的 word


def similar(string: str, dic: list,confidence:int):
    if string==None:
        return
    if dic==None:
        return
    ratio = 0
    word = ''
    for i in dic:
        similarity_ratio = fuzz.ratio(string, i)
        if similarity_ratio > ratio:
            ratio = similarity_ratio
            word = i
        # print(similarity_ratio)
    if ratio < confidence:
        return ''
    return word
