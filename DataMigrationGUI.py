from fuzzywuzzy import fuzz
import PySimpleGUI as sg
import datamain as main 



# layout1
mongo_text = sg.Text('MongoDB',font=('Arial Bold', 30),justification='left',text_color='white',background_color='LightSlateGray')
jiantou_text = sg.Text('===>',font=('Arial Bold', 30),justification='center',background_color='grey')
mysql_text = sg.Text('Mysql',font=('Arial Bold', 30),justification='left',text_color='white',background_color='LightSlateGray')
# layout2
mongo_input=sg.Input(default_text='contract_loan_info',font=('Arial Bold', 15),  justification='left')
convert_button=sg.Button("点击生成转换语句",key='convert',font=('Arial Bold', 15))
mysql_input=sg.Input(default_text='contract_loan_info',font=('Arial Bold', 15), justification='left')
# layout3
jiantou_trust = sg.Text('置信度:',font=('Arial Bold', 18),justification='left',text_color='black',background_color='white')
mongo_confidence=sg.Input(default_text=70,font=('Arial Bold', 18),justification='left')
common_button=sg.Button("常用mongo语句",key='common',font=('Arial Bold', 13),button_color='grey')
# layout4
result_Multiline=sg.Multiline(font=('微软雅黑', 12),autoscroll=True)
layout = [
    [mongo_text,jiantou_text,mysql_text],
    [mongo_input,convert_button,mysql_input],
    [jiantou_trust,mongo_confidence,common_button],
    [result_Multiline]
]
# sg.theme_previewer()#主题大全SystemDefaultForReal
sg.theme('LightGrey1')#改变主题LightGrey2 LightGrey6 DarkBlue8 DarkBlue3 LightGreen4
window = sg.Window('DataMigration 1.2.2', layout)


#转换按钮点击事件
def convert_btn_click(value):
    mongo_name = mongo_input.get()
    mysql_name = mysql_input.get()
    confidence=int(mongo_confidence.get())
    result=main.getResult(mongo_name,mysql_name,confidence)
    result_Multiline.update(' ')
    result_Multiline.print("db.{db}.aggregate(".format(db=mongo_name),text_color='black')
    result_Multiline.print('\n',"    ",result,",",'\n',text_color='blue')
    result_Multiline.print(")")

#显示常用语句
def common_btn_click(value):
    with open("yuju.txt","r",encoding='utf-8') as f:
        data=f.read()
    result_Multiline.update(data,text_color='green')


#event与函数体对应
event_callbacks = {
    'convert': convert_btn_click,
    'common':common_btn_click
}
# event事件监听
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED: break
    if event in event_callbacks:
        event_callbacks[event](value)
window.close()

