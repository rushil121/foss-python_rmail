# R mail v0.5

import datetime

# misc vars/functions
currTime = datetime.datetime.now()
currTimeF = currTime.strftime("%H:%M %d-%m-%Y")
def emptyLine():
    print(" ")
def emptyLine2():
    print(" ")
    print(" ")

# EMAIL class
class email:
    def __init__(self, subject, body, creationTime, senderEmail, senderFname, recipient, cc=0):
        self.subject = subject
        self.body = body
        self.creationTime = creationTime
        self.senderEmail = senderEmail  # email id
        self.senderFname = senderFname  # first name
        self.recipient = recipient      # email id
        self.cc = cc

    def saveDraft(self):
        return self.body

    def blength(self):
        return len(self.body)

    def ePreview(self):
        emptyLine()
        print('Here is a preview')
        emptyLine2()
        print("To: {}".format(self.recipient))
        if self.cc != 0:
            print("cc: {}".format(self.cc))
        print("Subject: {}".format(self.subject))
        emptyLine()
        print(self.body)
        emptyLine()
        print("From: {} ({}) ".format(self.senderFname, self.senderEmail))

    def eSend(self):
        emptyLine()
        print("Email has been sent(at {}).".format(str(currTimeF)))
        emptyLine()
        print('Here is a copy of it:')
        emptyLine2()
        print("To: {}".format(self.recipient))
        if self.cc != 0:
            print("cc: {}".format(self.cc))
        print("Subject: {}".format(self.subject))
        emptyLine()
        print(self.body)
        emptyLine2()
        print("From: {} ({}) ".format(self.senderFname, self.senderEmail))
        emptyLine()
        print(currTimeF)

    def askDraft(self):
        ans_draft2 = input('Do you want to save this as a draft? [y/n]')
        ans_draft2 = ans_draft2.lower()
        if ans_draft2 == 'y':
            mail1.saveDraft()
            emptyLine()
            print("Your mail has been saved as a draft succefully.\nYou can send it later anytime. ")
        else:
            emptyLine()
            print("No prob, see you later.")


# UI / Program start
print("Welcome to R-mail")
emptyLine2()
ans_yn = input("Do you want to write an email? [y/n]\n")
ans_yn = ans_yn.lower()
if ans_yn == 'y':
    emptyLine()
    print('Answer the following:')
    emptyLine2()
    thesenderFname = input("Whats your name?\n")
    emptyLine2()
    thesenderEmail = input("Enter your email id:\n")
    emptyLine()
    thesubject = input("Subject of your email: ")
    emptyLine()
    eContent = input("Content of the email:\n")
    contentForsending = "{}\n{}".format(thesubject, eContent)           # THE MSG
    emptyLine()

    thecreationTime = currTimeF
    therecipient = input("Send this to whom? [recipient email]: ")
    emptyLine()
    ans_cc = input("Any cc? [y/n]\n")
    ans_cc = ans_cc.lower()
    # cc
    if ans_cc == 'y':
        thecc = input("Enter all the emails in the cc. [email_id1, email_id2, ....]\n")
        mail1 = email(thesubject, eContent, thecreationTime, thesenderEmail, thesenderFname, therecipient, thecc)
        emptyLine2()
        ans_prev = input("Would you like to preview it before sending? [y/n]")
        ans_prev = ans_prev.lower()
        if ans_prev == 'y':
            mail1.ePreview()
        emptyLine2()
        ans_fsend = input("Send the mail:'{}' to {} ? [y/n]\n ".format(mail1.subject, mail1.recipient))
        ans_fsend = ans_fsend.lower()
        if ans_fsend == 'y':
            mail1.eSend()
            emptyLine2()
            print('Thanks for using R-mail, hope to see you again!')
        else:
            mail1.askDraft()
    # no cc
    else:
        mail1 = email(thesubject, eContent, thecreationTime, thesenderEmail, thesenderFname, therecipient)
        emptyLine2()
        ans_prev = input("Would you like to preview it before sending? [y/n]")
        ans_prev = ans_prev.lower()
        if ans_prev == 'y':
            mail1.ePreview()
        emptyLine2()
        ans_fsend = input("Send the mail:'{}' to {} ? [y/n]\n ".format(mail1.subject, mail1.recipient))
        ans_fsend = ans_fsend.lower()
        if ans_fsend == 'y':
            mail1.eSend()
            emptyLine2()
            print('Thanks for using R-mail, hope to see you again!')
        else:
            mail1.askDraft()
