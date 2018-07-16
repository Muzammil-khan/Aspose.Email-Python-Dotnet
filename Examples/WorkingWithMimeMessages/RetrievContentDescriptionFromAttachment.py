from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = ""
    #ExStart: RetrievContentDescriptionFromAttachment
    # Create an instance of MailMessage class
    message = MailMessage.load("EmailWithAttandEmbedded.eml")

    # Save attachments from message
    for index, att in enumerate(message.attachments):
        print(att.headers.get("Content-Description"))
    #ExEnd: RetrievContentDescriptionFromAttachment

if __name__ == '__main__':
    run()
