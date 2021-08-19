def arithmetic_arranger(problems,ans=False):
    
    if len(problems)>5:
      return "Error: Too many problems."
    first=[]
    last=[]
    operators=[]
    max_num=[]
    for i in problems:
      if not('+' in i or '-' in i):
        return "Error: Operator must be '+' or '-'."
      temp_list=i.split(' ')
      if not temp_list[0].isdigit():
        return "Error: Numbers must only contain digits."
      if not temp_list[2].isdigit():
        return "Error: Numbers must only contain digits."
      if len(temp_list[0])>4:
        return "Error: Numbers cannot be more than four digits."
      if len(temp_list[2])>4:
        return "Error: Numbers cannot be more than four digits."
      first+=[temp_list[0]]
      last+=[temp_list[2]]
      operators+=[temp_list[1]]
      max_num+=[max(len(temp_list[0]),len(temp_list[2]))]
    return_str=''
    for i in range(len(max_num)):
      return_str+="  "+" "*(max_num[i]-len(first[i]))+first[i]
      return_str+=' '*4
    return_str=return_str[:len(return_str)-4]
    return_str+='\n'
    for i in range(len(max_num)):
      return_str+=f"{operators[i]} "+" "*(max_num[i]-len(last[i]))+last[i]
      return_str+=' '*4
    return_str=return_str[:len(return_str)-4]
    return_str+='\n'
    for i in range(len(max_num)):
      return_str+="-"*(2+max_num[i])
      return_str+=' '*4
    return_str=return_str[:len(return_str)-4]
    if ans:
      return_str+='\n'
      for i in range(len(problems)):
        if operators[i]=='+':
         answer=str(int(first[i])+int(last[i]))
        else:
          answer=str(int(first[i])-int(last[i]))
        length=len(answer)
        max_num[i]+=2
        return_str+=' '*(max_num[i]-length)+answer
        return_str+=' '*4
      return_str=return_str[:len(return_str)-4]
    return return_str
    #return arranged_problems
