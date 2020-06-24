print('201911267 컴퓨터공학부 이성찬')
input=0
print('1 -> 4.0000')

for i in range(101,902):
  for j in range(1,i+1):
      
    if j%2 ==0:
        temp=-1/(2*j-1)
        input+=temp
        
    elif j%2==1:
        temp=1/(2*j-1)
        input+=temp
      
  cir=4*input
  print(i,'    ',format(cir,'.4f'))

  
  input=0
