import re
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}
def arithmetic_arranger(problems,boolean=False):
    result="";
    problemlen = len(problems);
    operandlines = ["firstop","secondop","dashes"];
    if(boolean):
       operandlines.append("answer");
    completeproblem =list();
    for maths in problems:
      sign =  re.findall("[+-]",maths);
      if(sign):
        index = maths.index(sign[0]);
      if (len(sign)==0):
        return("Error: Operator must be '+' or '-'."); 

      elif (re.search("\D",maths[0:index-1]) or re.search("\D",maths[index+2:])):
          return("Error: Numbers must only contain digits."); 
      
      elif (len(maths[0:index-1])>4 or len(maths[index+2:])>4):
          return("Error: Numbers cannot be more than four digits."); 
    if problemlen>5:
      return("Error: Too many problems.");
    else:
          for maths in problems:
              eachproblem = dict();
              sign =  re.findall("[+-]",maths);
              if(sign):
                index = maths.index(sign[0]);
              lensecop=len(maths[index+2:]);
              maximum = max(len(maths[0:index-1]),lensecop);     
              space=" ";
              if (lensecop<maximum):
                 space=" "+(" "*(maximum-lensecop));
              secop= maths[index]+space+maths[index+2:];
              dashes=   "-"*len(secop);
              eachproblem["firstop"]= maths[0:index-1].rjust(len(secop));
              eachproblem["secondop"]= secop;
              eachproblem["dashes"]= dashes.rjust(len(secop));
              if(boolean):
                  eachproblem["answer"]=str(ops[sign[0]](int(maths[0:index-1]),int(maths[index+2:]))).rjust(len(secop))
              completeproblem.append(eachproblem);
          print(completeproblem);    
          for ind in operandlines:
              i=0;
              while i<problemlen:
                if(i==problemlen-1):
                  result+= completeproblem[i][ind];
                else:
                  result+= completeproblem[i][ind] +"    ";
                i+=1;
              if(operandlines.index(ind)<len(operandlines)-1): 
                result+="\n";    
           
        
    return result