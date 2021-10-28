#!/bin/bash
echo "Wir sind die Borg. Deaktivieren Sie Ihre Schutzschilde und ergeben Sie sich. Wir werden Ihre biologischen und technologischen Charakteristika den unseren hinzufügen. Ihre Kultur wird sich anpassen und uns dienen. Widerstand ist zwecklos!"
# "{none, keyfile, repokey}"
verschluesselung="none"
# "none,lz4,zlib,lzma"
kompression="none"
#repopfad="/media/HDD-Backup/borgbackup"
repopfad="/media/urs/Safe1/safe"

read pass < db.key

#MySQL Dump
echo "[MySQL] dumpen"
mysqldump --single-transaction -h localhost -u nextcloud -p$pass nextcloud > /var/www/sql/nextcloud-sqlbkp_`date +"%Y%m%d"`.bak
echo "[MySQL] fertig"

sleep 3
echo "[Borg] Starten"
# Init borg-repo if absent
if [ ! -d $repopfad ]; then
  borg init --encryption=$verschluesselung $repopfad 
  echo "->Borg-Repository erzeugt unter $repopfad"
fi

# backup data
echo "->Start der Sicherung $(date)."
borg create --compression $kompression --exclude-caches --one-file-system -v --stats --progress $repopfad::'HDD4TB-{now:%Y-%m-%d-%H%M%S}' /media/HDD /var/www --exclude *.tmp 
echo "-> Ende der Sicherung $(date). Dauer: $SECONDS Sekunden"

# prune archives
borg prune -v --list $repopfad --prefix 'HDD4TB-' --keep-within=5d --keep-daily=7 --keep-weekly=4 --keep-monthly=12
echo "-> Wir sind die Borg! Wiederstand war zwecklos."
echo "[Borg] fertig"

# MySQL Backup löschen
echo "[MySQL] entferne MySQL Backup"
rm -rf /var/www/sql/nextcloud-sqlbkp_`date +"%Y%m%d"`.bak


# E-Mail senden
python3 request.py "Externes Backup ist fertig."
