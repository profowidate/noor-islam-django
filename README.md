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

## Screenshots

<img width="1798" height="840" alt="6" src="https://github.com/user-attachments/assets/417f521e-da50-4ff8-a109-afb0fc29229e" />

<img width="1772" height="902" alt="88" src="https://github.com/user-attachments/assets/499a7c81-979f-41f2-b370-f85858a32ab1" />

<img width="1781" height="897" alt="111" src="https://github.com/user-attachments/assets/9a9f0353-7875-4af9-872b-65a538c5022f" />

<img width="1770" height="870" alt="dfdf" src="https://github.com/user-attachments/assets/c00087a2-5181-490f-a5ff-6e0ed14b54f3" />

<img width="1730" height="873" alt="7" src="https://github.com/user-attachments/assets/0b4bad2e-6d79-4d22-8363-b59c9b942cf7" />

<img width="1723" height="877" alt="11" src="https://github.com/user-attachments/assets/ecdcb766-0def-4023-bdf9-bc7baf6d2084" />








## Architecture
- `config/`: project settings and root URLs
- `apps/`: independent Django applications
- `templates/`: shared UI templates
- `static/`: CSS and JavaScript
