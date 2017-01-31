
__author__ = 'khouly'

import os
import operator
from os import walk
import shutil

startpath="C:\\work\\enron"
startpath=os.path.join('C:','work','enron')
privatepath="c:\\work\\enron\\1\\private"
privatepath=os.path.join('C:','work','enron','1','private')
workpath="c:\\work\\enron\\1\\work"
privatepath=os.path.join('C:','work','enron','1','work')



iwork=0
iprivate=0
names=dict()
private_words=list()
private_words.append('personal')

work_words=list()
work_words.append('bankruptcy')
work_words.append('gas')
work_words.append('mexico')
work_words.append('canada')
work_words.append('budget')
for root, dirs, files in os.walk("C:\\work\\enron", topdown=False):
    #for name in files:
        #print(os.path.join(root, name))
    for name in dirs:

        for word in private_words:
            if(word in name):
                print(word)
                for root2,dir2,files2 in os.walk(os.path.join(root,name)):
                    for file in files2:
                        #file=file+'.'
                        print(os.path.join(root2,file))
                        iprivate=iprivate+1
                        src1=os.path.join(root2,file)
                        dst1=os.path.join(privatepath,str(iprivate))
                        print(src1)
                        print(dst1)
                        shutil.copy2(src1, dst1)


        for word in work_words:
            if(word in name):
                print(word)
                for root2,dir2,files2 in os.walk(os.path.join(root,name)):
                    for file in files2:
                        #file += '.'
                        print(os.path.join(root2,file))
                        iwork=iwork+1
                        src1=os.path.join(root2,file)
                        dst1=os.path.join(workpath,str(iwork))
                        print(src1)
                        print(dst1)
                        shutil.copy2(src1, dst1)


#sorted_names = (sorted(names.items(), key=operator.itemgetter(1)))
#print(sorted_names)

print(iwork)
print(iprivate)


            #for root,dirs,files in os.walk(personal_dir):
                #for name in files:
                    #print(os.path.join(personal_dir,name))


         #if('florida') in name or ('bankruptcy'):
            #personal_dir=os.path.join(root, name)


            #for root,dirs,files in os.walk(personal_dir):
                #for name in files:
                    #print(os.path.join(personal_dir,name))