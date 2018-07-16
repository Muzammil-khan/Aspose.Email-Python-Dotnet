import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

#ExStart: ForwardEmail
eml = MailMessage.load("Message.eml")
eml.from_address = "kashif.iqbal.aspose@gmail.com"

#Send using Smtp Client
client = SmtpClient("smtp.gmail.com", 995, "username", "password")
client.security_options = SecurityOptions.AUTO
client.forward("Recipient1@domain.com", "Recipient2@domain.com", eml)
#ExEnd: ForwardEmail
