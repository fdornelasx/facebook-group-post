#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI

#Author: T Shrinivasan <tshrinivasan@gmail.com>
#Edited by: Fillipe Dornelas
# get api from here  https://developers.facebook.com/tools/explorer

api = ""

graph = GraphAPI(api)

message = '''
Bluehack, o maior hackathon da America Latina.
05 e 06 de novembro na IBM Tutóia.
São 4 desafios: Cognitive, Agicultura Urbana, Marketplaces e inclusão de mulheres na tecnologia.
Inscreva-se em: www.bluehack.org.
Descrição do evento
https://www.youtube.com/watch?v=m3uoq3sv_Ec&app=desktop

Espero vocês lá!
'''

# Find the ids of your desired groups from http://lookup-id.com/
# and add this in this array groups

groups = ['1142411415843149'] #you could add more group ids, just put commas like: groups =['1','2','3','n'] when n=1000000

timer = 60 #seconds to wait

for group_id in groups:
	print "Post " + 'http://www.facebook.com/groups/' + str(group_id)

	try: #edited by fillipe dornelas
		graph.post(path =str(group_id) + '/feed', message=message)
		print "waiting "+str(timer)+" seconds to post again"
		time.sleep(timer) #will wait 60 seconds to post again. It prevents facebook to block you.
	except:
		print "fail."
print "Done!"