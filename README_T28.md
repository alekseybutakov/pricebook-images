# T28 — картинки (кассеты Mitsubishi SLZ-AF / Pioneer Quantum Ultra)

1. Алекс: `cd images/T28 && bash download_T28.sh` — качает исходники по manifest_T28.tsv.
   У исполнителя и контролёра нет сети к hvacdirect.com и pioneerminisplit.com, поэтому качает Алекс.
2. Затем: `cd images && python3 T28/build_T28.py` — делает квадраты 1200 на белом в `images/upload/photos_05/`
   и копирует фото кассеты Pioneer под именем CT0918DPNL.jpg (своего фото у панели нет).
3. Папку `upload/photos_05` залить в корень репозитория github.com/alekseybutakov/pricebook-images.
4. Файл импорта Image1 собирает контролёр (см. 90_reports/T28_photos.xlsx — колонка ImageFile).

Реестр: `90_reports/T28_photos.xlsx`.
