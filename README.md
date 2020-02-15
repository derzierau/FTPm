# Freelance Time- and Projectmanagement CLI - FTPm

## Developer Set Up
```
git clone 
virtualenv .env
pip install -r requirements.txt
```

```
ftpm init
ftpm init --config CONFIG_PATH
ftpm update --config CONFIG_PATH
ftpm start -m MESSAGE --serviceId dev --account --project
ftpm task -m MESSAGE -> Audit Trail
ftpm stop --all --account --project -> Geldwert / Stunden
ftpm ui
ftpm stats --all --week --month --quarterly --start --end

```

Stoppen und Starten werden immer die Current Working Dirs oder GLobals ->

ftpm start within /projects geht nicht ->
ftpm start within /projects/peix -> timer für peix
ftpm start within /projects/peix/iisy -> (sub) timer für project iisy
ftpm start within /projects/peix/n/api -> (sub) timer für n und api

ftpm stop  within /projects -> delete all timer if one is open
ftpm stop within /projects/peix -> stopt alle timer /projects/peix-->
ftpm stop within /projects/peix/n -> stoppt den timer pro customer

```

## Fragen
- Pauschale Abrechnung?
- Runden auf viertel Stunde - was sind die Einstellungen?
- standby vom System = Stop Timer
- Repo Time Integration - CSV oder so?
- Message pro Timer -> Task weise?
- Stats
- Timer starte projekt gleich öffnen? mit code oder ähnlichen? 
- Pausenvorschlag

/account/project/.../api