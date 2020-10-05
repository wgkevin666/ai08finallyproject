#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition
import jieba
from gtts import gTTS
from pygame import mixer
import tempfile
import time
import wave


# In[2]:


def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)
def Voice_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("請開始說話:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")
    except r.UnknownValueError:
        Text = "無法翻譯"
    except speech_recognition.RequestError as e:
        Text = "無法翻譯{0}".format(e)
    return Text
def Audio_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.WavFile("rec0925-154053.wav") as source:
        audio = r.record(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")
    except LookupError:
        Text = "無法翻譯"
    return Text


# In[ ]:


Text = Voice_To_Text()
textList = jieba.lcut(Text, cut_all=True, HMM=True)
print(textList)
if "頭" in textList:
    speak('告訴我詳細一點, 例如有什麼症狀', 'zh-tw')
    print('告訴我詳細一點, 例如有什麼症狀')
    time.sleep(5)
    Text = Voice_To_Text()
    textList = jieba.lcut(Text, cut_all=True, HMM=True)
    print(textList)
    if "脖子" in textList:
        speak('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑', 'zh-tw')
        print('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑')
        time.sleep(15)
    elif "肌肉" in textList:
        speak('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑', 'zh-tw')
        print('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑')
        time.sleep(15)
    elif "僵硬" in textList:
        speak('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑', 'zh-tw')
        print('可能症狀為【肌肉緊縮性疼痛】建議服用止痛劑、肌肉鬆弛劑、抗憂鬱劑')
        time.sleep(15)
    elif "喝酒" in textList:
        speak('可能症狀為【偏頭痛】建議直接到附近的診所就醫', 'zh-tw')
        print('可能症狀為【偏頭痛】建議直接到附近的診所就醫')
        time.sleep(15)
    elif "藥" in textList:
        speak('可能症狀為【藥物濫用】建議暫時停止用藥', 'zh-tw')
        print('可能症狀為【藥物濫用】建議暫時停止用藥')
        time.sleep(15)
    elif "鼻水" in textList:
        speak('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物', 'zh-tw')
        print('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物')
        time.sleep(15)
    elif "眼睛" in textList:
        speak('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物', 'zh-tw')
        print('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物')
        time.sleep(15)
    elif "紅" in textList:
        speak('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物', 'zh-tw')
        print('可能症狀為【叢發性頭痛】建議預備類固醇藥物、避免含硝酸鹽的食物')
        time.sleep(15)
    elif "憂鬱症" in textList:
        speak('可能症狀為【憂鬱症頭痛】建議使用抗憂鬱劑', 'zh-tw')
        print('可能症狀為【憂鬱症頭痛】建議使用抗憂鬱劑')
        time.sleep(15)
    elif "眼" in textList:
        speak('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療', 'zh-tw')
        print('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療')
        time.sleep(15)
    elif "流" in textList:
        speak('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療', 'zh-tw')
        print('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療')
        time.sleep(15)
    elif "淚" in textList:
        speak('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療', 'zh-tw')
        print('可能症狀為【急性青光眼】建議雷射 虹膜造孔治療')
        time.sleep(15)
    elif "用" in textList:
        speak('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。', 'zh-tw')
        print('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。')
        time.sleep(15)
    elif "手" in textList:
        speak('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。', 'zh-tw')
        print('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。')
        time.sleep(15)
    elif "機" in textList:
        speak('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。', 'zh-tw')
        print('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。')
        time.sleep(15)
    elif "電" in textList:
        speak('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。', 'zh-tw')
        print('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。')
        time.sleep(15)
    elif "腦" in textList:
        speak('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。', 'zh-tw')
        print('可能症狀為【一般頭痛】建議讓眼睛休息 使用鬆弛眼睛的藥水。')
        time.sleep(15)
    elif "鼻水" in textList:
        speak('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。', 'zh-tw')
        print('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。')
        time.sleep(15)
    elif "鼻" in textList:
        speak('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。', 'zh-tw')
        print('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。')
        time.sleep(15)
    elif "竇炎" in textList:
        speak('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。', 'zh-tw')
        print('可能症狀為【竇性頭痛】建議治療以抗生素、鼻用類固醇及去除腫脹劑來處理。')
        time.sleep(15)
    elif "感冒" in textList:
        speak('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷', 'zh-tw')
        print('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷')
        time.sleep(15)
    elif "瘧疾" in textList:
        speak('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷', 'zh-tw')
        print('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷')
        time.sleep(15)
    elif "腦炎" in textList:
        speak('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷', 'zh-tw')
        print('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷')
        time.sleep(15)
    elif "腦膜炎" in textList:
        speak('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷', 'zh-tw')
        print('可能症狀為【急性頭痛】建議使用止痛藥 睡眠休息 熱敷')
        time.sleep(15)
    elif "摔倒" in textList:
        speak('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓', 'zh-tw')
        print('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓')
        time.sleep(15)
    elif "跌倒" in textList:
        speak('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓', 'zh-tw')
        print('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓')
        time.sleep(15)
    elif "打" in textList:
        speak('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓', 'zh-tw')
        print('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓')
        time.sleep(15)
    elif "出血" in textList:
        speak('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓', 'zh-tw')
        print('可能症狀為【頭部外傷】建議植入顱內壓監測器、開顱清除血塊、顱骨切除減壓')
        time.sleep(15)
    elif "深" in textList:
        speak('可能症狀為【腦瘤】建議外科手術或放射性治療', 'zh-tw')
        print('可能症狀為【腦瘤】建議外科手術或放射性治療')
        time.sleep(15)
    elif "處" in textList:
        speak('可能症狀為【腦瘤】建議外科手術或放射性治療', 'zh-tw')
        print('可能症狀為【腦瘤】建議外科手術或放射性治療')
        time.sleep(15)
    elif "舒服" in textList:
        speak('可能症狀為【腦瘤】建議外科手術或放射性治療', 'zh-tw')
        print('可能症狀為【腦瘤】建議外科手術或放射性治療')
        time.sleep(15)
    elif "重重" in textList:
        speak('可能症狀為【腦瘤】建議外科手術或放射性治療', 'zh-tw')
        print('可能症狀為【腦瘤】建議外科手術或放射性治療')
        time.sleep(15)
    elif "劇" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "頸" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "僵硬" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "噁" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "吐" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "額" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "眼睛" in textList:
        speak('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除', 'zh-tw')
        print('可能症狀為【腦動脈瘤破裂】建議腦動脈瘤夾除')
        time.sleep(15)
    elif "腸" in textList:
        speak('可能症狀為【消化系統導致的頭痛】建議注意消化系統問題，改善飲食生活習慣', 'zh-tw')
        print('可能症狀為【消化系統導致的頭痛】建議注意消化系統問題，改善飲食生活習慣')
        time.sleep(15)
    elif "胃" in textList:
        speak('可能症狀為【消化系統導致的頭痛】建議注意消化系統問題，改善飲食生活習慣', 'zh-tw')
        print('可能症狀為【消化系統導致的頭痛】建議注意消化系統問題，改善飲食生活習慣')
        time.sleep(15)
    else:
        speak('建議直接到附近的診所就醫', 'zh-tw')
        print('建議直接到附近的診所就醫')
        time.sleep(15)
elif "肚子" or "胃" in textList:
    speak('告訴我詳細一點, 例如有什麼症狀及位置', 'zh-tw')
    print('告訴我詳細一點, 例如有什麼症狀及位置')
    time.sleep(5)
    Text = Voice_To_Text()
    textList = jieba.lcut(Text, cut_all=True, HMM=True)
    print(textList)
    if "膽" in textList:
        speak('可能症狀為【急性膽囊炎】建議禁食 皮穿肝膽引流術及膽囊引流術', 'zh-tw')
        print('可能症狀為【急性膽囊炎】建議禁食 皮穿肝膽引流術及膽囊引流術')
        time.sleep(15)
    elif "結" in textList:
        speak('可能症狀為【急性膽囊炎】建議禁食 皮穿肝膽引流術及膽囊引流術', 'zh-tw')
        print('可能症狀為【急性膽囊炎】建議禁食 皮穿肝膽引流術及膽囊引流術')
        time.sleep(15)
    elif "吃" in textList:
        speak('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑', 'zh-tw')
        print('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑')
        time.sleep(15)
    elif "肋骨" in textList:
        speak('可能症狀為【狹心症 心肌梗塞】建議掛急診 不停大口呼吸 咳嗽', 'zh-tw')
        print('可能症狀為【狹心症 心肌梗塞】建議掛急診 不停大口呼吸 咳嗽 ')
        time.sleep(15)
    elif "上腹" in textList:
        speak('可能症狀為【狹心症 心肌梗塞】建議掛急診 不停大口呼吸 咳嗽', 'zh-tw')
        print('可能症狀為【狹心症 心肌梗塞】建議掛急診 不停大口呼吸 咳嗽 ')
        time.sleep(15)       
    elif "中" in textList:
        speak('可能症狀為【胃潰瘍 十二指腸潰瘍 腹膜炎】建議胃鏡檢查 配合制酸劑 黏膜保護劑 抗生素', 'zh-tw')
        print('可能症狀為【胃潰瘍 十二指腸潰瘍 腹膜炎】建議胃鏡檢查 配合制酸劑 黏膜保護劑 抗生素')
        time.sleep(15)
    elif "拉肚子" in textList:
        speak('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑', 'zh-tw')
        print('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑')
        time.sleep(15)
    elif "便秘" in textList:
        speak('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑', 'zh-tw')
        print('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑')
        time.sleep(15)
    elif "飯" in textList:
        speak('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑', 'zh-tw')
        print('可能症狀為【腸躁症】建議藥物治療止瀉劑 軟便劑 肌肉鬆弛劑')
        time.sleep(15)
    elif "右下" in textList:
        speak('可能症狀為【闌尾炎】建議手術切除闌尾', 'zh-tw')
        print('可能症狀為【闌尾炎】建議手術切除闌尾')
        time.sleep(15)
    elif "下方" or "下面" in textList:
        speak('可能症狀為【腎結石 膀胱結石】建議多喝水 體外震波碎石術', 'zh-tw')
        print('可能症狀為【腎結石 膀胱結石】建議多喝水 體外震波碎石術')
        time.sleep(15)
    elif "刺痛" in textList:
        speak('可能症狀為【腎結石 膀胱結石】建議多喝水 體外震波碎石術', 'zh-tw')
        print('可能症狀為【腎結石 膀胱結石】建議多喝水 體外震波碎石術')
        time.sleep(15)
    elif "左上" in textList:
        speak('可能症狀為【胰臟炎】建議打止痛劑 彎曲身體減輕疼痛', 'zh-tw')
        print('可能症狀為【胰臟炎】建議打止痛劑 彎曲身體減輕疼痛')
        time.sleep(15)
    elif "上方" or "上面" in textList:
        speak('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ', 'zh-tw')
        print('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ')
        time.sleep(15)
    elif "發" in textList:
        speak('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ', 'zh-tw')
        print('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ')
        time.sleep(15)
    elif "燒" in textList:
        speak('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ', 'zh-tw')
        print('可能症狀為【盲腸炎】建議照超音波 斷層掃描 ')
        time.sleep(15)
    elif "臍" in textList:
        speak('可能症狀為【腸炎】建議暫時停止進食 就醫 配合止痛劑 抗生素', 'zh-tw')
        print('可能症狀為【腸炎】建議暫時停止進食 就醫 配合止痛劑 抗生素')
        time.sleep(15)
    elif "拉肚子" in textList:
        speak('可能症狀為【腸炎】建議暫時停止進食 就醫 配合止痛劑 抗生素', 'zh-tw')
        print('可能症狀為【腸炎】建議暫時停止進食 就醫 配合止痛劑 抗生素')
        time.sleep(15)
    elif "全部" in textList:
        speak('可能症狀為【重金屬中毒】建議採用螯合療法 將有害重金屬排出體外', 'zh-tw')
        print('可能症狀為【重金屬中毒】建議採用螯合療法 將有害重金屬排出體外')
        time.sleep(15)
    elif "整" in textList:
        speak('可能症狀為【重金屬中毒】建議採用螯合療法 將有害重金屬排出體外', 'zh-tw')
        print('可能症狀為【重金屬中毒】建議採用螯合療法 將有害重金屬排出體外')
        time.sleep(15)
    else:
        speak('建議直接到附近的診所就醫', 'zh-tw')
        print('建議直接到附近的診所就醫')
        time.sleep(15)
else:
    speak('我沒有聽清楚可以再說一次嗎', 'zh-tw')
    print('我沒有聽清楚可以再說一次嗎')
    time.sleep(15)

