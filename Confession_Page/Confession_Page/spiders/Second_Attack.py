from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request,FormRequest
from bs4 import BeautifulSoup
import re
import random
class LoginSpider(BaseSpider):
	name = 'First_Wave'
	# start_urls = ['https://docs.google.com/forms/d/e/1FAIpQLSfKdBPwjGKX-k30w6tD4go8mfXq5MkTEiP2JVgZ39-fP2-a4A/viewform']

	start_urls = ['https://docs.google.com/forms/d/e/1FAIpQLSdsN5kGH0rooRj2iLyhYxj9AM7jUZx-eCpsXTf3UcuHLPtsaQ/viewform']
	count = 36239                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		s_nouns = ["A dude", "My mom","The admin","This hot 4th year CST guy","This really hot 3rd year CST Girl","The beauty in 2nd Year", "The king", "Some 1st year guy", "CST","A cat with rabies","IT", "A sloth","Hottie", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
		p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
		s_verbs = ["eats", "kicks","fucks","kisses","loves","likes","reads","admires","stares","sees","talks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
		p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on","fuck","kisse","love","like","read","admire","stare","see","talk", "retard", "meow on", "flee from", "try to automate", "explode"]
		infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology.","to make a beautiful couple.","to make some love.","to love to see you around."]

		message = random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<100):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<200):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<200):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<400):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<500):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<600):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<700):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<800):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<900):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<500):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		if(random.randint(1,1000)<800):
			message = message+" "+random.choice(s_nouns)+" "+random.choice(s_verbs)+" "+(random.choice(s_nouns).lower() or random.choice(p_nouns).lower())+" "+random.choice(infinitives)
		
		if(random.randint(1,1000)<100):
			message=message+message


		fbzx = hxs.select("//input[@name='fbzx']/@value").extract()[0]	
		draftResponse = hxs.select("//input[@name='draftResponse']/@value").extract()[0]	
		entry = hxs.select("//textarea[@class='quantumWizTextinputPapertextareaInput exportTextarea']/@name").extract()[0]	
		# print msg
		payload = {
							str(entry):message,
							"fvv":"1",
							"draftResponse":str(draftResponse)[:-1],
							"pageHistory":"0",
							"fbzx":str(fbzx)
							}
		print payload
		yield FormRequest.from_response(response,formxpath="//form[@id='mG61Hd']",
		 								formdata=payload,
		 								callback=self.new_issue_next_step
		 								)
	def new_issue_next_step(self,response):
		self.count=self.count+1
		print " "
		if("formResponse" in response.url):
			print "Attack #",self.count,"Successful"
		else:
			print "Attack #",self.count,"Failed"
		# return Request(url='https://docs.google.com/forms/d/e/1FAIpQLSfKdBPwjGKX-k30w6tD4go8mfXq5MkTEiP2JVgZ39-fP2-a4A/viewform',callback=self.parse,dont_filter=True)
		print " "
		return Request(url='https://docs.google.com/forms/d/e/1FAIpQLSdsN5kGH0rooRj2iLyhYxj9AM7jUZx-eCpsXTf3UcuHLPtsaQ/viewform',callback=self.parse,dont_filter=True)
		

	# 	request_headers = {
	# 						"X-OpenAM-Username":str(user_name),
	# 						"X-OpenAM-Password": str(accounts[users[account_index-1]]),
	# 						"Content-Type":"application/json"
	# 						}
	# 	print "Login attempt started"
	# 	return Request(url='https://mayank.yaxalab.net:8443/authgw/json/authenticate?authIndexType=module&authIndexValue=DataStore',method="POST",headers=request_headers,callback=self.check,dont_filter=True)

	# def check(self,response):
	# 	global iPlanetDirectoryPro
	# 	iPlanetDirectoryPro	= response.body.split("\"")[3]
	# 	global k
	# 	k = Request(url="https://mayank.yaxalab.net:443/webmail/login",callback=self.login_attempt,cookies={"amlbcookie":"01","iPlanetDirectoryPro":str(iPlanetDirectoryPro)},dont_filter=True)
	# 	return k
	