#!/bin/bash
echo "Wir sind die Borg. Deaktivieren Sie Ihre Schutzschilde und ergeben Sie sich. Wir werden Ihre biologischen und technologischen Charakteristika den unseren hinzufügen. Ihre Kultur wird sich anpassen und uns dienen. Widerstand ist zwecklos!"
# "{none, keyfile, repokey}"
verschluesselung="repokey"
# "none,lz4,zlib,lzma"
kompression="lzma,5"
#repopfad="/media/HDD-Backup/borgbackup"
repopfad="/media/extern/safe"

#read pass < db.key

#MySQL Dump
echo "[MySQL] dumpen"
#mysqldump --single-transaction -h localhost -u root nextcloud > /var/www/sql/nextcloud-sqlbkp_`date +"%Y%m%d"`.bak
mysqldump --single-transaction -h localhost -u root nextcloud > /var/www/sql/nextcloud-sqlbkp.bak
echo "[MySQL] zippen"
zip -o /var/www/sql/nextcloud-sqlbkp.bak.zip /var/www/sql/nextcloud-sqlbkp.bak > /var/log/telegrambot/extern.log
rm -rf /var/www/sql/nextcloud-sqlbkp.bak
echo "[MySQL] fertig"

echo "[Borg] Starten"
# Init borg-repo if absent
if [ ! -d $repopfad ]; then
  borg init --encryption=$verschluesselung $repopfad
  echo "->Borg-Repository erzeugt unter $repopfad"
  echp "Warte 5s"
  sleep 5s
fi

# backup data
echo "->Start der Sicherung $(date)." > /var/log/telegrambot/extern.log
echo "->Start der Sicherung $(date)."
borg create --compression $kompression --exclude-caches --one-file-system -v --stats --progress $repopfad::'HDD4TB-{now:%Y-%m-%d-%H%M%S}' /home/ /media/HDD /var/www /etc/apache2/ /etc/letsencrypt /var/lib/docker/volumes/ --exclude *.tmp
echo "-> Ende der Sicherung $(date). Dauer: $SECONDS Sekunden"
echo "-> Ende der Sicherung $(date). Dauer: $SECONDS Sekunden"  > /var/log/telegrambot/extern.log

# prune archives
read telegramid < /media/HDD/Backup-New/empf.id
python3 /media/HDD/Backup-New/telegramsendapi.py -id $telegramid -txt "Das Backup benötig die Passphrase."

#borg prune -v --list $repopfad --prefix 'HDD4TB-' --keep-within=7d --keep-daily=7 --keep-weekly=4 --keep-monthly=24
borg prune -v --list $repopfad --prefix 'HDD4TB-' --keep-within=14d --keep-daily=21 --keep-weekly=14 --keep-monthly=44
echo "-> Wir sind die Borg! Wiederstand war zwecklos."
echo "[Borg] fertig"
echo "[Borg] fertig" > /var/log/telegrambot/extern.log

echo "[Borg] Compact"
borg compact $repopfad
echo "[Borg] Compact finished"


# MySQL Backup löschen
echo "[MySQL] entferne MySQL Backup"
rm -rf /var/www/sql/nextcloud-sqlbkp.bak.zip

# Telegram Nachricht senden
read telegramid < /media/HDD/Backup-New/empf.id
python3 /media/HDD/Backup-New/telegramsendapi.py -id $telegramid -txt "Das externe Backup ist fertig."
echo "[Telegram] Nachricht gesendet!"
