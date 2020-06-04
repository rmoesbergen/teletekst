## Teletekst vluchttijden scraper
Teletekst scraper voor vluchtinformatie van/naar Maastricht Airport

### Installatie instructies

- Log in via SSH op de Raspberry pi
```bash
ssh pi@<ip adres pi>
```
- Start het volgende commando:
```bash
curl https://raw.githubusercontent.com/rmoesbergen/teletekst/master/install.sh | bash
```

Dit zal een cronjob installeren die elke nacht om 00:15 het script start en de CSV file in /home/pi/teletekst-<maand>.csv schijft.


### Handmatig opstarten

Het script kan ook handmatig worden gestart:

```bash
./teletekst.py <betandsnaam.csv>
```

De eerste en enige parameter is de naam van het bestand waarin de gegevens geschreven moeten worden.
In de bestandsnaam kunnen datum/tijd formatterings tekens worden opgenomen:

https://strftime.org/
