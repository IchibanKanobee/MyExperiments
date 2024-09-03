#https://codehandbook.org/how-to-read-email-from-gmail-using-python/

import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def find_sub_list(sub_list,this_list):
    return (this_list.index(sub_list[0]),len(sub_list))


def parse_body(body):
    parts = body.split('\n')
    pattern = "Unsubscribe from this Google Alert:" +'\r'
    pos = parts.index(pattern)
    content = parts[2 : pos - 2]
    block_length = 7
    block_count = len(content) / block_length
    dict = {}
    for i in range(block_count):
        dict['Title'] = content[block_length * i]
        dict['URL'] = content[block_length * i + 5]

    return dict


def read_email_from_gmail(smtp_server, account, password, label):
    try:
        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(account,password)
#        mail.select('inbox')
        mail.select(label)

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
#                    print 'From : ' + email_from + '\n'
#                    print 'Subject : ' + email_subject + '\n'

                    body =""
                    if msg.is_multipart():
                        for part in msg.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            # skip any text/plain (txt) attachments
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
                    else:
                        body = msg.get_payload(decode=True)

                    content = parse_body(body)

                    print content

    except Exception, e:
        print str(e)



labels = ['Crime', 'Design', 'Fashion', 'Lifestyle', 'News', 'Transportation', 'Travel']

for label in labels:
    read_email_from_gmail("smtp.gmail.com", account, password, label)
