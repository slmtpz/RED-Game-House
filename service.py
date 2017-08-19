import smtplib
import db_query
import setts

from email.mime.text import MIMEText

results = db_query.get_daily_docs()

aggregated = []
currAgg = []
date = ''
for result in results:
    if date != result[0]:
        if currAgg: aggregated.append(currAgg)
        currAgg = []
        date = result[0]
        currAgg.append(result[0])
        currAgg.append(result[1])
    currAgg.append(result[2:])

send = ''
for agg in aggregated:
    send += '________________________________\n'
    send += 'Başlama Zamanı: ' + agg[0][:-7] + '\n'
    send += 'Bitiş Zamanı: ' + agg[1][:-7] + '\n\n'
    total = 0
    for each in agg[2:]:
        # send += 'Tip: ' + each[0] + '  --  '
        send += 'Ürün: ' + each[1] + '  --  '
        zmr = 'Süre: ' if each[0] == 'game' else 'Sayı: '
        qty = str(int(each[2])) if zmr == 'Sayı: ' else str(each[2])
        send += zmr + str(each[2]) + '\n'
        send += 'Ücret: ' + str(each[3]) + '\n\n'
        total += each[3]
    send += 'Toplam: ' + str(total) + '\n\n'


msg = MIMEText(send)

msg['Subject'] = 'RED Playstation Cafe Ozeti'
msg['From'] = setts.FROM
msg['To'] = setts.TO

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(setts.MAIL, setts.PASS)
s.send_message(msg)
s.quit()