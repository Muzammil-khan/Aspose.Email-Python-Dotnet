import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    try:
    #ExStart: ListingMessagesWithPagingSupport
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:
                client.select_folder("Inbox")
                pages = []
                itemsPerPage = 1
                pageInfo = client.list_messages_by_page(itemsPerPage)
                print(pageInfo.total_count)
                pages.append(pageInfo)

                while not pageInfo.last_page:
                    pageInfo = client.list_messages_by_page(pageInfo.next_page)
                    pages.append(pageInfo)

                retrievedItems = 0
                for folderCol in pages:
                    retrievedItems+= len(folderCol.items)

                print(str(retrievedItems))
    #ExEnd: ListingMessagesWithPagingSupport
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
