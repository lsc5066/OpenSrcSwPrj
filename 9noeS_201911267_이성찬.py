from datetime import datetime
import urllib.request
import json
import sys
import io
import os
now=datetime.now()
os.system('cls')
def clear():
    os.system('cls')

while True:
    print('-'*60)
    print('어서오세요 당신의 여행을 도와줄 9noeS라고 합니다! 반갑습니다')
    print('[1] 현재 시간')
    print('[2] 네이버 검색')
    print('[3] 기상 정보')
    print('[4] 번역')
    print('[5] 콘솔창 정리')
    print('[0] 프로그램 종료')
    print('-'*60)      
    insert=int(input('이용하실 서비스를 입력해주세요 :\n'))

    if insert==1:
        print('-'*60)
        print('지금은',now.year,'년',now.month,'월',now.day,'일',now.hour,'시',now.minute,'분',now.second,'초 입니다.')
        print('-'*60)
        print('시작 화면으로 돌아갑니다...')

    elif insert==2:
        a=int(input('(1) 블로그 검색 (2) 이미지 검색\n'))
        if a==1:
            client_id = "ZcH7nM3x72UUDgmgbHyo" # 애플리케이션 등록시 발급 받은 값 입력
            client_secret = "UOWzjMfUrT" # 애플리케이션 등록시 발급 받은 값 입력
            print('-'*28)
            encText = urllib.parse.quote(input("검색할 내용을 입력해주세요 :\n"))
            print('-'*28)
            url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText + "display=10&sort=sim"
            
            #Open API 검색 요청 개체 설정
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)

            #검색 요청 및 처리
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                json_rt = response.read().decode('utf-8')
                py_rt = json.loads(json_rt)
                print(json_rt)
                #response_body = response.read()
                #print(response_body.decode('utf-8'))
            else:
                 print("Error Code:" + rescode)

            print('시작 화면으로 돌아갑니다...')


        elif a==2:
            
            client_id = "ZcH7nM3x72UUDgmgbHyo"
            client_secret = "UOWzjMfUrT"
            print('-'*30)
            encText = urllib.parse.quote(input("검색할 이미지를 입력해주세요 :\n"))
            print('-'*30)
            url = "https://openapi.naver.com/v1/search/image.json?query=" + encText + "display=10&sort=sim"
            option = "&display=3&sort=count"
             
            #Open API 검색 요청 개체 설정
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
             
            #검색 요청 및 처리
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            
            if(rescode == 200):
                #response_body = response.read()
                json_rt = response.read().decode('utf-8')
                py_rt = json.loads(json_rt)
                print(json_rt)
                #print(response_body.decode('utf-8'))
            else:
                print("Error code:"+rescode)

            print('시작 화면으로 돌아갑니다...')
            
        else:
            print('잘못된 입력입니다. 시작 화면으로 돌아갑니다...')

    elif insert==3:
        
        b=int(input('(1) 미세먼지 정보 (2) 날씨 정보\n'))
        
        if b==1:
            client_id = "ZcH7nM3x72UUDgmgbHyo" # 애플리케이션 등록시 발급 받은 값 입력
            client_secret = "UOWzjMfUrT" # 애플리케이션 등록시 발급 받은 값 입력
            print('-'*35)
            print('키워드를 날짜와 함께 입력해주세요 : ')
            encText = urllib.parse.quote(input('예) 11월 16일 미세먼지 \n'))
            print('-'*35)
            url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "display=10&sort=date"
            
            #Open API 검색 요청 개체 설정
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)

            #검색 요청 및 처리
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                json_rt = response.read().decode('utf-8')
                py_rt = json.loads(json_rt)
                print(json_rt)
                 #response_body = response.read()
                 #print(response_body.decode('utf-8'))
            else:
                 print("Error Code:" + rescode)

            print('시작 화면으로 돌아갑니다...')
                 
        elif b==2:
            def Forecast():
                print('예) Seoul[서울], Busan[부산], Daegu[대구], Incheon[인천]...')
                city_name=input('날씨를 알고 싶으신 도시의 이름을 영문으로 입력해주세요 : \n')
                url_data=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&lang=ko'+'&APPID=0301b4f5682555c6be20a8a2867b2934')
                weather_data=url_data.read()
                j=json.loads(weather_data)
                weather=j['weather'][0]['main']
                temp=int(j['main']['temp'] - 273.15)
                print('-'*60)
                print(city_name+'의 현재 날씨는 '+weather+'이며, 현재 온도는',temp,'℃ 입니다.')
                print('-'*60)

            Forecast()

            print('시작 화면으로 돌아갑니다...')
            
            '''
            client_id = "ZcH7nM3x72UUDgmgbHyo" # 애플리케이션 등록시 발급 받은 값 입력
            client_secret = "UOWzjMfUrT" # 애플리케이션 등록시 발급 받은 값 입력
            encText = urllib.parse.quote(input('키워드를 날짜와 함께 입력해주세요 : '+'ex) 11월 16일 날씨 :\n'))
            url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "display=10&sort=date"
            
            #Open API 검색 요청 개체 설정
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)

            #검색 요청 및 처리
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                json_rt = response.read().decode('utf-8')
                py_rt = json.loads(json_rt)
                print(json_rt)
                #response_body = response.read()
                #print(response_body.decode('utf-8'))
            else:
                 print("Error Code:" + rescode)

            print('시작 화면으로 돌아갑니다...')
            '''


        else:
            print('잘못된 입력입니다. 시작 화면으로 돌아갑니다...')
            

            
    elif insert==4:
        
        client_id = "ZcH7nM3x72UUDgmgbHyo" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "UOWzjMfUrT" # 개발자센터에서 발급받은 Client Secret 값
        
        print('-'*42)
        print('[ko]한국어, [en]영어, [ja]일본어')
        print('[vi]베트남어, [id]인도네시아어')
        print('[th]베트남어, [de]독일어, [ru]러시아어')
        print('[es]스페인어, [it]이탈리아어, [fr]프랑스어')
        print('-'*42)   
        source_language=input('입력할 언어를 선택해주세요 :\n')
        
        print('-'*42)
        print('[ko]한국어, [en]영어, [ja]일본어')
        print('[vi]베트남어, [id]인도네시아어')
        print('[th]베트남어, [de]독일어, [ru]러시아어')
        print('[es]스페인어, [it]이탈리아어, [fr]프랑스어')
        print('-'*42)
        target_language=input('출력할 언어를 선택해주세요 :\n')
        
        
        encText = urllib.parse.quote(input('번역을 원하는 문장을 입력하세요 : \n'))
        data="source="+source_language+"&target="+target_language+"&text=" +encText
        url = "https://openapi.naver.com/v1/papago/n2mt."
        
        #Open API 검색 요청 개체 설정
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        
        #검색 요청 및 처리
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            json_rt = response.read().decode('utf-8')
            py_rt = json.loads(json_rt)
            print(json_rt)
            #response_body = response.read()
            #print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)

    elif insert==5:
        clear()

        
    elif insert==0:
        print('-'*26)
        print('프로그램을 종료합니다.')
        print('이용해주셔서 감사합니다 :)')
        print('-'*26)
        break
              

   


    
            








        
                 
    
    




    

    
