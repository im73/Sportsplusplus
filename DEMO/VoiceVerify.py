#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from SDK.CCPRestSDK import REST

#主帐号
accountSid= '8a216da869dca6190169dd10cead00ae';

#主帐号Token
accountToken= 'e9dbe824b1144aa8aa4009b54a752146';

#应用Id
appId='8aaf070869dc0b880169e22fb0510359';

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com';

#请求端口 
serverPort=8883;

#REST版本号
softVersion='2013-12-26';

    # 语音验证码
    # @param verifyCode  必选参数   验证码内容，为数字和英文字母，不区分大小写，长度4-8位
    # @param playTimes  可选参数   播放次数，1－3次
    # @param to 必选参数    接收号码
    # @param displayNum 可选参数    显示的主叫号码
    # @param respUrl 可选参数    语音验证码状态通知回调地址，云通讯平台将向该Url地址发送呼叫结果通知
    # @param lang 可选参数    语言类型
    # @param userData 可选参数    第三方私有数据

def voiceVerify(verifyCode,playTimes,to,displayNum,respUrl,lang,userData):
    #初始化REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.voiceVerify(verifyCode,playTimes,to,displayNum,respUrl,lang,userData)
    print(result)
    for k,v in result.iteritems(): 
        
        if k=='VoiceVerify' :
                for k,s in v.iteritems(): 
                    print ('%s:%s' % (k, s))
        else:
            print ('%s:%s' % (k, v))
   
   
voiceVerify(445566,2,18090531196,"","",'zh-en',"")