def Prayer():
	
	question = input('Would you like me to say a prayer for you?: ')
	
if question.strip().lower() == 'y':
	name = input('What is your name?: ')
	print('Lord God, please watch over %s and protect %s. Bless %s with favor, prosperity, and the unconditional love of Jesus Christ. In Jesus\n Amen' % (name,name))
else:
	print("Praise Jesus!") 
return


Prayer()
