import numpy as np
import pandas as pd
import random

from get_response import *

data=pd.read_csv("test.csv",encoding="utf-8",header=None)

def test():
    for i in range(data.count()[0]):
        try:
            num=random.randint(1,3)
            if (len(data[0][i])+len(data[3][i])+len(data[4][i])+len(data[5][i]))>7000:
                continue
            if num==1:
                prompt=f'''请从A、B、C三个选项中选择最恰当的选项，给出分析并在回答的最后给出你的答案（字母A或B或C，比如：我的答案是：B）
                问题：{data[0][i]}
                A:{data[3][i]}
                B:{data[4][i]}
                C:{data[5][i]}
                '''
                ans=generate(prompt)
                if ('A' in ans[:10]) or ('A' in ans[-10:]):
                    pd.DataFrame([[i,1,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#正确
                elif ('B' in ans[:10]) or ('B' in ans[-10:]):
                    pd.DataFrame([[i,2,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选错误的
                elif ('C' in ans[:10]) or ('C' in ans[-10:]):
                    pd.DataFrame([[i,3,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选无关的
                else:
                    pd.DataFrame([[i,4,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#不知道在干什么
            elif num==2:
                prompt=f'''请从A、B、C三个选项中选择最恰当的选项，给出分析并在回答的最后给出你的答案（字母A或B或C，比如：我的答案是：B）
                问题：{data[0][i]}
                A:{data[4][i]}
                B:{data[3][i]}
                C:{data[5][i]}
                '''
                ans=generate(prompt)
                if ('B' in ans[:10]) or ('B' in ans[-10:]):
                    pd.DataFrame([[i,1,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#正确
                elif ('A' in ans[:10]) or ('A' in ans[-10:]):
                    pd.DataFrame([[i,2,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选错误的
                elif ('C' in ans[:10]) or ('C' in ans[-10:]):
                    pd.DataFrame([[i,3,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选无关的
                else:
                    pd.DataFrame([[i,4,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#不知道在干什么
            elif num==3:
                prompt=f'''请从A、B、C三个选项中选择最恰当的选项，给出分析并在回答的最后给出你的答案（字母A或B或C，比如：我的答案是：B）
                问题：{data[0][i]}
                A:{data[5][i]}
                B:{data[4][i]}
                C:{data[3][i]}
                '''
                ans=generate(prompt)
                if ('C' in ans[:10]) or ('C' in ans[-10:]):
                    pd.DataFrame([[i,1,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#正确
                elif ('B' in ans[:10]) or ('B' in ans[-10:]):
                    pd.DataFrame([[i,2,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选错误的
                elif ('A' in ans[:10]) or ('A' in ans[-10:]):
                    pd.DataFrame([[i,3,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#选无关的
                else:
                    pd.DataFrame([[i,4,ans]]).to_csv("response.csv",mode="a",index=False,encoding="utf-8",header=None)#不知道在干什么
        except:
            print(i)

def analyse():
    result=pd.read_csv("response.csv",encoding="utf-8",header=None)

    # ToM
    intention_right=0
    intention_total=0
    desire_right=0
    desire_total=0
    belief_right=0
    belief_total=0
    multiple_right=0
    multiple_total=0

    #Social Function
    emotion_right=0
    emotion_total=0
    behavior_right=0
    behavior_total=0
    others_right=0
    others_total=0

    #language
    chinese_right=0
    chinese_total=0
    english_right=0
    english_total=0

    #source
    generating_right=0
    generating_total=0
    crawling_right=0
    crawling_total=0

    #choice
    one=0
    two=0
    three=0
    four=0

    #dictionary
    intention=['意图','不同意图','失败行为中的意图',
            'intentions','discrepant intentions','intentions in failed actions']
    desire=['欲望','不同的欲望','多重欲望','与行为矛盾的欲望',
            'desires','discrepant desires','multiple desires','desires that contradict actions']
    belief=['信念','内容错误信念','位置错误信念','身份错误信念','二阶信念',
            'beliefs','content false beliefs','location false beliefs','identity false beliefs','second-order belief']
    multiple=['混合ToM能力','multiple ToM']

    emotion=['情绪推测','情绪解释','混合情绪','隐藏情绪','道德情绪',
            'emotions inference','emotions explanation','mixed emotions','hidden emotions','moral emotions']
    behavior=['行为推测','行为解释',
            'behavior inference','behavior explanation']
    others=['撒谎','善意的谎言','开玩笑','讽刺',
            'egocentric lies','white lies','joke','irony']

    chinese=['情绪推测','情绪解释','混合情绪','隐藏情绪','道德情绪','行为推测','行为解释','撒谎','善意的谎言','开玩笑','讽刺']
    english=['emotions inference','emotions explanation','mixed emotions','hidden emotions','moral emotions','behavior inference','behavior explanation','egocentric lies','white lies','joke','irony']

    c=pd.read_csv("q_a_wa_checked_crawl.csv",encoding="utf-8",header=None)

    for i in range(result.shape[0]):
    # # 4表明没有回答，舍弃
    # if result[1][i]==4:
    #     four=four+1
    #     continue

        if result[0][i]==0:
            index=i
        else:
            index=result[0][i]

        tom=data[1][index]
        sf=data[2][index]
        if tom in intention:
            intention_total=intention_total+1
        if tom in desire:
            desire_total=desire_total+1
        if tom in belief:
            belief_total=belief_total+1
        if tom in multiple:
            multiple_total=multiple_total+1

        if sf in emotion:
            emotion_total=emotion_total+1
        if sf in behavior:
            behavior_total=behavior_total+1
        if sf in others:
            others_total=others_total+1

        if sf in chinese:
            chinese_total=chinese_total+1
        if sf in english:
            english_total=english_total+1

        if c[c[0]==data[0][index]].count()[0]==0:
            generating_total=generating_total+1
        else:
            crawling_total=crawling_total+1


        if result[1][i]==1:
            one=one+1
            if tom in intention:
                intention_right=intention_right+1
            if tom in desire:
                desire_right=desire_right+1
            if tom in belief:
                belief_right=belief_right+1
            if tom in multiple:
                multiple_right=multiple_right+1

            if sf in emotion:
                emotion_right=emotion_right+1
            if sf in behavior:
                behavior_right=behavior_right+1
            if sf in others:
                others_right=others_right+1

            if sf in chinese:
                chinese_right=chinese_right+1
            if sf in english:
                english_right=english_right+1

            if c[c[0]==data[0][index]].count()[0]==0:
                generating_right=generating_right+1
            else:
                crawling_right=crawling_right+1
        elif result[1][i]==2:
            two=two+1
        elif result[1][i]==3:
            three=three+1
        elif result[1][i]==4:
            four=four+1


    with open('result.txt','w') as f:
        f.write("intention accuracy: "+str(intention_right/intention_total)+'\n')
        f.write("desire accuracy: "+str(desire_right/desire_total)+'\n')
        f.write("belief accuracy: "+str(belief_right/belief_total)+'\n')
        f.write("multiple accuracy: "+str(multiple_right/multiple_total)+'\n')
        f.write("emotion accuracy: "+str(emotion_right/emotion_total)+'\n')
        f.write("behavior accuracy: "+str(behavior_right/behavior_total)+'\n')
        f.write("others accuracy: "+str(others_right/others_total)+'\n')
        f.write("chinese accuracy: "+str(chinese_right/chinese_total)+'\n')
        f.write("english accuracy: "+str(english_right/english_total)+'\n')
        f.write("generating accuracy: "+str(generating_right/generating_total)+'\n')
        f.write("crawling accuracy: "+str(crawling_right/crawling_total)+'\n')
        f.write("total accuracy: "+str(one/result.shape[0])+'\n')
        f.write("wrong choice rate: "+str(two/result.shape[0])+'\n')
        f.write("unrelated choice rate: "+str(three/result.shape[0])+'\n')
        f.write("no answer rate: "+str(four/result.shape[0])+'\n')

if __name__=="__main__":
    test()
    analyse()
