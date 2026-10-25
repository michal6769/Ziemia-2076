from flask import Flask, render_template

app = Flask(__name__)

STATISTICS = [
    {
        "number": 1,
        "title": "Globalna temperatura",
        "baseline": "+1,1°C",
        "baseline_note": "średnia dla lat 2011–2020 względem okresu 1850–1900",
        "future": "+2,0 do +3,5°C",
        "description": "Świat może być znacznie cieplejszy, co zwiększy ryzyko fal upałów, susz i ekstremalnych opadów.",
        "image": "1.jpg",
        "source": "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/"
    },
    {
        "number": 2,
        "title": "Poziom mórz",
        "baseline": "Okres bazowy",
        "baseline_note": "1995–2014 — punkt odniesienia dla pomiarów",
        "future": "+35 do +75 cm",
        "description": "Podnoszący się poziom oceanów może zagrażać wybrzeżom, wyspom i miastom położonym nisko nad morzem.",
        "image": "2.jpg",
        "source": "https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/"
    },
    {
        "number": 3,
        "title": "Liczba ludności świata",
        "baseline": "8,2 mld",
        "baseline_note": "szacunek dla 2024 roku",
        "future": "około 10,2 mld",
        "description": "Więcej ludzi będzie oznaczać większe zapotrzebowanie na żywność, wodę, energię i mieszkania.",
        "image": "3.jpg",
        "source": "https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/wpp2024_summary_of_results_final_web.pdf"
    },
    {
        "number": 4,
        "title": "Stężenie CO₂ w atmosferze",
        "baseline": "około 423 ppm",
        "baseline_note": "wartość z 2024 roku",
        "future": "500–650 ppm",
        "description": "Dwutlenek węgla zatrzymuje ciepło w atmosferze. Przyszłe stężenie zależy przede wszystkim od skali emisji.",
        "image": "4.jpg",
        "source": "https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide"
    },
    {
        "number": 5,
        "title": "Powierzchnia lasów na świecie",
        "baseline": "4,06 mld ha",
        "baseline_note": "szacunek dla 2020 roku",
        "future": "3,5–4,0 mld ha",
        "description": "Wylesianie, pożary i zmiany klimatu mogą zmniejszać powierzchnię lasów oraz osłabiać ich zdolność do pochłaniania CO₂.",
        "image": "5.jpg",
        "source": "https://www.fao.org/interactive/forest-resources-assessment/2020/en/"
    },
    {
        "number": 6,
        "title": "Odnawialne źródła energii",
        "baseline": "około 30%",
        "baseline_note": "udział OZE w produkcji energii elektrycznej w 2023 roku",
        "future": "60–90%",
        "description": "Energia słoneczna, wiatrowa i inne źródła odnawialne mogą dostarczać większość światowej energii elektrycznej.",
        "image": "6.jpg",
        "source": "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/"
    },
    {
        "number": 7,
        "title": "Plastik w oceanach",
        "baseline": "około 32 mln ton",
        "baseline_note": "szacunek modelowy dla 2020 roku",
        "future": "100–250 mln ton",
        "description": "Bez ograniczenia zanieczyszczeń plastik będzie gromadził się w środowisku morskim i szkodził zwierzętom oraz ekosystemom.",
        "image": "7.jpg",
        "source": "https://www.oecd.org/en/publications/global-plastics-outlook_aa1edf33-en/full-report/component-11.html"
    },
    {
        "number": 8,
        "title": "Ludzie narażeni na zmiany klimatu",
        "baseline": "około 3,6 mld",
        "baseline_note": "ludzie żyjący w obszarach szczególnie podatnych na zmiany klimatu",
        "future": "4–6 mld",
        "description": "Najbardziej narażone społeczności mogą częściej doświadczać niedoborów wody, upałów, powodzi i problemów z żywnością.",
        "image": "8.jpg",
        "source": "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/"
    },
    {
        "number": 9,
        "title": "Lód morski w Arktyce",
        "baseline": "4–5 mln km²",
        "baseline_note": "typowy zakres letniego minimum, zależny od roku",
        "future": "0–3 mln km²",
        "description": "Letnia pokrywa lodowa może mocno się zmniejszyć. W niektórych scenariuszach Arktyka może niemal utracić letni lód morski.",
        "image": "9.jpg",
        "source": "https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/"
    },
    {
        "number": 10,
        "title": "Zgony związane ze zmianami klimatu",
        "baseline": "prognoza: ok. 250 tys. rocznie",
        "baseline_note": "szacunek WHO na lata 2030–2050",
        "future": "250 tys.–1 mln rocznie",
        "description": "Upały, choroby, niedożywienie i inne skutki klimatyczne mogą zwiększać zagrożenia dla zdrowia. Zakres na 2076 rok jest orientacyjnym szacunkiem, a nie oficjalną prognozą WHO.",
        "image": "10.jpg",
        "source": "https://www.who.int/news-room/fact-sheets/detail/climate-change-and-health"
    },
]

SOURCES = [
    ("IPCC — raport podsumowujący", "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/"),
    ("IPCC — raport o podstawach fizycznych klimatu", "https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/"),
    ("ONZ — World Population Prospects 2024", "https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/wpp2024_summary_of_results_final_web.pdf"),
    ("NOAA / Climate.gov — dwutlenek węgla w atmosferze", "https://www.climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-dioxide"),
    ("FAO — Global Forest Resources Assessment 2020", "https://www.fao.org/interactive/forest-resources-assessment/2020/en/"),
    ("OECD — Global Plastics Outlook", "https://www.oecd.org/en/publications/global-plastics-outlook_aa1edf33-en/full-report/component-11.html"),
    ("WHO — zmiany klimatu i zdrowie", "https://www.who.int/news-room/fact-sheets/detail/climate-change-and-health"),
]

@app.route("/")
def index():
    return render_template("index.html", statistics=STATISTICS, sources=SOURCES)

if __name__ == "__main__":
    app.run(debug=True)
