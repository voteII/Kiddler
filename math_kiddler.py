def calculation():
    s=0
    ques=["what is 3+4..?", "what is 5*3+8*9/3..?", "what is 8+9*0+9/3-6..?","what is (3+3)*3/3+6-9...?"]
    ans=[7,5*3+8*9/3,8+9*0+9/3-6,(3+3)*3/3+6-9]  
    user_ans=[0,0,0,0]
    for i in range(len(ques)):
        a=ques[i]
        user_ans[i]=int(raw_input(a + "  "  ))
        if user_ans[i]==ans[i]:
            print "correct answer\n"
            score()
            s=score()
        else:
            print "wrong answer\n"
    print "game over,your score %r" % s

def score():
    c=0
    c+=10
    return c
        
def variable():
    s=0
    ques=["if x=x+3, what is x..?", "if x=3 and y=6, what is x+y..? ", "if x=4 and x+y=6, what is y..?","if x+y=3 and x-y=9, what is x...?"]
    ans=[0,9,2,6]  
    user_ans=[0,0,0,0]
    for i in range(len(ques1)):
        a=ques[i]
        user_ans[i]=int(raw_input(a + "  "  ))
        if user_ans[i]==ans[i]:
            print "correct answer\n"
            score()
            s=score()
        else:
            print "wrong answer\n"
    print "game over,your score %r" % s
        

    
