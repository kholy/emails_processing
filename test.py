import mailbox
import sys
outputdir='C:/work/Mail/Takeout/Mail/out/'

def uwritefile(*objects, sep=' ', end='\n', file):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg,cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    #Walk through the parts of the email to find the text body.    
    if msg.is_multipart():    
        for part in msg.walk():

            # If part is multipart, walk through the subparts.            
            if part.is_multipart(): 

                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        # Get the subpart payload (i.e the message body)
                        body = subpart.get_payload(decode=True) 
                        #charset = subpart.get_charset()

            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                #charset = part.get_charset()

    # If this isn't a multi-part message then get the payload (i.e the message body)
    elif msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True) 

   # No checking done to match the charset with the correct part. 
    for charset in getcharsets(msg):
        print(charset)
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            handleerror("UnicodeDecodeError: encountered.",msg,charset)
        except AttributeError:
             handleerror("AttributeError: encountered" ,msg,charset)
    return body    


def getcharsetfromemail(msg):
    return (getcharsets(msg))



mboxfile = 'C:/work/Mail/Takeout/Mail/software.mbox'
# print(mboxfile)
# charsets=set()
# for thisemail in mailbox.mbox(mboxfile):
#     #print(++i)
#     for charset in getcharsetfromemail(thisemail):
#         charsets.add(charset)

#for charset in charsets:
#    print(charset)
def mygetbody(mail):
    body=""
#mail = email.message_from_string(email_body)
    for part in mail.walk():
        c_type = part.get_content_type()
        c_disp = part.get('Content-Disposition')

        if c_type == 'text/plain' and c_disp == None:
            body = body + '\n' + part.get_payload()
        else:
            continue
        return(body)

#for thisemail in mailbox.mbox(mboxfile):
    #body=getbodyfromemail(thisemail)
    #if(body!=None):
        #print(body.decode('utf-8','ignore'))
    #print(body.decode('utf-8'))
#shareimprove this answer
#answered Aug 25 '11 at 9:27
inbox=mailbox.mbox(mboxfile)
ks=mailbox.mbox(mboxfile).keys()
maxindex=(max(ks))
for i in range(maxindex):
    try:

        #print(i)
        #print(mygetbody(inbox[i]))
        file = open(outputdir+''+str(i), "w")

        id=inbox[i]['Message-ID']
        if(not(id is None)):
            file.write('Message-ID :'+id+'\n')

        d=inbox[i]['Date']
        if(not(d is None)):
            file.write('Date :'+d+'\n')

        if('To' in inbox[i].keys()):
            to=inbox[i]['To']
            if(not(to is None)):
                file.write('To :'+to+'\n')


        if('Subject' in inbox[i].keys()):
            subject=inbox[i]['Subject']
            if(not(subject is None)):
                file.write('Subject :'+subject+'\n')

        body=mygetbody(inbox[i])
        if(not(body is None)):
            #file.write(body.encode(encoding='utf-8',errors='ignore'))
            file.write(body)
            #uwritefile(body,file=file)

        file.close()



    except :
        print('error at '+str(i))
        #file.close()

    #print((inbox[1].keys()))
    #print(inbox[i]['to'])




