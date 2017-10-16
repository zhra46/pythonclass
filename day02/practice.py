score1=int(input('please enter xiaoming\'s score last year'))
score2=int(input('please enter xiaoming\'s score this year'))
result = (score2-score1)/score1*100
print ('小明去年的成绩是%d，小明今年的成绩是%d，成绩提高了%%%.1f'%(score1,score2,result))