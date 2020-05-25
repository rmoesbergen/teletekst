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

Dit zal een cronjob installeren die elke nacht om 00:01 het script start en de CSV file in /home/pi/teletekst-<maand>.csv schijft.
