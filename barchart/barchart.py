import numpy,json
from matplotlib import pyplot

def readInfoByJson()->tuple:
    #通过JSON从文件内读入数据
    with open('./schoolID2qq.txt','r') as reader:
        schoolID2qq=json.load(reader)
    with open('./schoolID2freq.txt','r') as reader:
        schoolID2freq=json.load(reader)
    with open('./schoolID2days.txt','r') as reader:
        schoolID2days=json.load(reader)
    with open('./schoolID2rate.txt','r') as reader:
        schoolID2rate=json.load(reader)
    return schoolID2qq,schoolID2freq,schoolID2days,schoolID2rate

info=readInfoByJson()

schoolID2qq,schoolID2freq,schoolID2days,schoolID2rate=info[0:4]
schoolIDs=[]
qqs=[]
freqs:list=[]
schoolIDs_freq:list=[]

def paint(num):
    for schoolID,qq in schoolID2qq.items():
        schoolIDs.append(schoolID)
        qqs.append(schoolID)
    for schoolID in schoolIDs:
        freq=schoolID2freq[schoolID]
        if freq>num:
            freqs.append(schoolID)
            schoolIDs_freq.append(schoolID)

    fig,ax=pyplot.subplots()

    x=numpy.array(schoolIDs_freq)
    y=numpy.array(freqs)
    ax.bar(x,y)
    ax.xlabel('Students who spoke over %d times'%num)
    ax.ylabel('The accurate number of messages')
    ax.title('Frequency')

    return fig