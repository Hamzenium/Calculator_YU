import PySimpleGUI as sg
str= ' 1+(4*5+1 )*2'  
answer=[]






#print(answer.remove(0))

def subOrSum(answer):
    
    for j in answer:
        counter=1
        if j=='+' or j=='-':
            a=int (answer[counter-1])
            b=int (answer[counter+1])
            if j=='+':
                result=a+b
            else:
                result=a-b
            
    
    counter=counter+1

    result2=f'{result}'
    return result2

def multiOrDiv(answer):
    
    for j in answer:
        counter=1
        if j=='*' or j=='/':
            a=int (answer[counter-1])
            b=int (answer[counter+1])
            if j=='*':
                result=a*b
            else:
                result=a/b
            
    
    counter=counter+1

    result2=f'{result}'
    return result2



def pre(answer):
    counter=1
    for i in answer:
        
        if i=='(':
            counter2=1
            for j in answer:
                if j == ')':
                    break
                else:
                    counter2=counter2+1

            answer2=answer[counter:counter2-1]
            result=pre(answer2)
            answer[counter-1]=result[0]
            del answer[counter:counter2]
    
    
        counter=counter+1


    
    counter=1
    for i in answer:
        
        if i=='*' or i=="/":
            answer2=answer[counter-2:counter+1]
            result=multiOrDiv(answer2)
            answer[counter-2]=result
            del answer[counter-1:counter+1]
    
        counter=counter+1


    counter=1
    for i in answer:
            
        if i=='+' or i=="-":
            answer2=answer[counter-2:counter+1]
            result=subOrSum(answer2)
            answer[counter-2]=result
            del answer[counter-1:counter+1]

        counter=counter+1
                
  

    if(len(answer)!=1):
        pre(answer)
        
    return answer

#GUI Part
layout = [
    [sg.Text("Please enter the text for the calculator: "),sg.Input(key="-IN-"),],
    [sg.Text("The answer calculated below is: ", size=(0, 1))],
    [sg.Output(size=(80, 4),  key='OUTPUT')],
    [sg.Exit(), sg.Button("Calculate")],sg.Button("Reset"),sg.Text("\t\t\t\t© Team Anonymous")],

window=sg.Window("\t\tAdvanced Calculator", layout, [50,50])
while True:
    event, values = window.read()
    print(event,values)
    if event in (sg.WINDOW_CLOSED,"Exit"):
       break
   
    if event =="Calculate":
        str= values[r"-IN-"]
        for i in str:
            counter=1
            if i.isnumeric() or i=='+' or i=='-' or i=='*' or i=='/' or i==')' or i=='(':
                 answer.append(i)
            counter=counter+1 
        final  =  pre(answer)
        print(final[0])
        window['OUTPUT'].update(value=final[0])
    if event == "Reset":
        str = ""
        answer= []

        
window.close()


