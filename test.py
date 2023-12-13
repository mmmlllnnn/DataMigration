#工具===


from os import sep


a={"code": "custBasicInfo", "judges": "6b8e6408d3c24111ad28b733210111e1,7a268decbb0b46e6b473b24015a92955,cc90a4649e774f818f58345f377d7db3,15c68e3efceb4c06a0f3ad75a5af07ff,575934dbca904a2aad947801c03f6433", "moneySum": "lte", "principal": 50000, "recheckMG": "a9ad957b10494aba9b008be5e43a0d47", "worthRate": 0, "processNum": "20", "isInproject": "1", "meetingName": "会议02", "meetingTime": "2023-07-10", "primaryMGXS": "a9ad957b10494aba9b008be5e43a0d47", "projectType": "03", "CommonLessee": "[\"7731909081012895923\"]", "worthRateAll": 0, "meetingzhuRen": "6b8e6408d3c24111ad28b733210111e1", "commonLesseeId": "7731909081012895923", "isCommonLessee": "1", "meetingAddress": "济南", "worthRateBasic": 0, "riskManagerIdXS": "5556efa32909455cbb63fe47272f8c29", "shareholderRate": 0, "ChoosefengShenId": "7731909081012896425", "rentMangerSubmit": "INFORFLOW_ALL", "riskMangerSubmit": "INFORFLOW_ALL", "worthRateRelation": 0, "faShenMangerSubmit": "INFORFLOW_ALL", "newPorjectCommitId": "7731909081012896178_2", "businessTypeProject": "", "fileRelatedFieldName": {"projectNo": "HTJZ202307005"}}

#自动添加列表拆分语句
# for key,value in a.items():
#     print(key,':{{$arrayElemAt:[{fla},0]}}'.format(fla=("'"+value+"'")),",")


#自动格式化对象
for key,value in a.items():
    print(key,":",value,sep='')