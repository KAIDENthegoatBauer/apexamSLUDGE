from cmu_graphics import *

app.background = 'lavender'
##timer stuff 
app.stepsPerSecond = 1

##photos no credit to me
app.gramaURL= 'https://media.istockphoto.com/id/1133906430/photo/happy-old-woman-smiling-happy-in-old-age.jpg?s=2048x2048&w=is&k=20&c=dunxAWqliibHbNZyYCKw_evJVCDS85AiXFL_pJDiNVU='
app.cookieURL= 'https://images.ricardocuisine.com/services/recipes/496x670_443664758542a9fa22f234.jpg'
app.keebURL= 'https://images.huffingtonpost.com/2017-01-03-1483473909-7717010-keeblerbanner.jpg'

##this one just says cookies
Label('cookies',63, 100, font='orbitron',size=25)

## this one should be the number of cookies
cLabel = Label(0,140,101,font='orbitron',size=25)

##this is the image of the cookie
Cookie = Image(app.cookieURL,0,130,width=180,height=175)

##first upgrade below all things for grama
grama = Image(app.gramaURL,220,65, width=125 , height=95)

Label('grama cost =', 270,55,font='orbitron',size = 15 )
granprice = Label(15,330,55,font='orbitron' ,size = 15)


keebprice = Label(300,333,225,font='orbitron', size = 15 )
Label('keeb tree price =', 265, 225 , font='orbitron', size = 15)

gramaon = False
keebon = False

##second upgrade the kebler factory
keeble = Image( app.keebURL,220, 235,width=125, height=95)

##this is how the timer works and starting with only gramas
def onStep():
 
 if (keebon == True):
  cLabel.value += keebprice.value// 8 + 1
  
 if (gramaon == True):
    cLabel.value += granprice.value//5 + 1

## mandatory list
cpsList = []



amOfUp = Label(len(cpsList),140,45, font ='orbitron',size = 15)
  
##this is the mouse function


def onMousePress(mouseX,mouseY):
    
    if((grama.hits(mouseX,mouseY)) and (cLabel.value >= granprice.value)):
     global gramaon 
     gramaon = True
     cLabel.value -= granprice.value
     granprice.value += 2
     cpsList.insert(1,1)
     
     for sum in cpsList:
       
       print("consider this line 1 upgrade!")
     
    if((keeble.hits(mouseX,mouseY)) and (cLabel.value >= keebprice.value)):
     global keebon 
     keebon = True
     cLabel.value -= keebprice.value
     keebprice.value += 45  
     


    if(Cookie.hits(mouseX,mouseY) ):
       
        
        ##this below should increase c label when mouse press but im not sure yet
        ##update yes it does
      cLabel.value += 1
      

Label('upgrades bought=',70,45,font='orbitron',size=15)

##these are going to be for making the numbers nice and round i think
rounded(cLabel.value)

rounded(granprice.value)
rounded(keebprice.value)




cmu_graphics.run()