# بسم الله الرحمن الرحيم
# Noor Islam | منصة نور الإسلام

A modular Arabic-first Django starter platform for Islamic daily services.

## Included
- Responsive Arabic/English-ready dashboard and navigation
- Prayer times lookup through AlAdhan API (internet required)
- Quran reader with all 114 Surahs and complete Ayah text fetched from AlQuran Cloud API (internet required)
- Search Surahs and browse the Quran by Surah
- Morning/evening Azkar and a working repetition counter
- Digital Tasbeeh counter
- Zakat calculator
- 99 Names of Allah
- Duas, Hadith and Hijri calendar starter sections
- Django authentication (register, login, logout)
- Django admin

## Run on Windows (PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Notes
- SQLite is configured by default, so PostgreSQL/Docker are not required to run this starter.
- Quran text is retrieved from the public AlQuran Cloud API. An internet connection is required to load full Surah text.
- Prayer times are retrieved from the public AlAdhan API. Choose a city on the Prayer Times page.
- The Azkar, Duas, Names and Hadith pages include starter content. Verify religious texts and references with trusted sources before production use.
- Zakat calculations are educational estimates, not a personal fatwa. Nisab and asset eligibility can vary by scholarly opinion and date.
- Before deployment, set a secure secret key, DEBUG=False, configure ALLOWED_HOSTS, HTTPS, database backups and production static files.

## Architecture
- `config/`: project settings and root URLs
- `apps/`: independent Django applications
- `templates/`: shared UI templates
- `static/`: CSS and JavaScript
