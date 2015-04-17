imaprestful
===========

List mailboxs

    curl -u user:pass http://hostapi/mailbox

List mails

    curl -u user:pass http://hostapi/mailbox/MailboxName
    
List and mark as seen

    curl -u user:pass http://hostapi/mailbox/MailboxName?markSeen=True

List and mark as seen

    curl -u user:pass http://hostapi/mailbox/MailboxName?markUnseen=True

View mail

    curl -u user:pass http://hostapi/mailbox/MailboxName/uid
    
Delete mail

    curl -u user:pass http://hostapi/mailbox/MailboxName/uid -X DELETE
