import scrapy
import json
from pprint import pprint


class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['covid-19.sledilnik.org']
    start_urls = ['https://api.sledilnik.org/api/stats']

    def parse(self, response):
        params = {}
        resp = json.loads(response.body)
        for i in resp:
            if((i['year'] == 2020)):
                params['year'] = i['year']
                params['dayFromStart'] = i['dayFromStart']
                params['year'] = i['year']
                params['day'] = i['day']
                params['month'] = i['month']
                params['LJ regija'] = i['statePerRegion']['lj']
                params['po regija'] = i['statePerRegion']['po']
                params['kr regija'] = i['statePerRegion']['kr']
                params['ce regija'] = i['statePerRegion']['ce']
                params['foreign regija'] = i['statePerRegion']['foreign']
                params['nm regija'] = i['statePerRegion']['nm']
                params['kk regija'] = i['statePerRegion']['kk']
                params['mb regija'] = i['statePerRegion']['mb']
                params['ms regija'] = i['statePerRegion']['ms']
                params['za regija'] = i['statePerRegion']['za']
                params['ng regija'] = i['statePerRegion']['ng']
                params['kp regija'] = i['statePerRegion']['kp']
                for l, k in i['tests']['positive'].items():
                    if(l == 'toDate'):
                        params['tested_poz_to_date'] = k
                    else:
                        params['tested_poz_today'] = k
                for b, c in i['tests']['performed'].items():
                    if(b == 'toDate'):
                        params['tested_to_date'] = c
                    else:
                        params['tested_today'] = c
                for j in i['statePerAgeToDate']:
                    if(j.get('ageFrom') == 15):
                        params['age 15-24'] = j.get('allToDate')
                        params['age 15-24 FEMALE'] = j.get('femaleToDate')
                        params['age 15-24 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 25):
                        params['age 25-34'] = j.get('allToDate')
                        params['age 25-34 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 25-34 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 35):
                        params['age 35-44'] = j.get('allToDate')
                        params['age 35-44 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 35-44 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 45):
                        params['age 45-54'] = j.get('allToDate')
                        params['age 45-54 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 45-54 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 55):
                        params['age 55-64'] = j.get('allToDate')
                        params['age 55-64 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 55-64 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 65):
                        params['age 65-74'] = j.get('allToDate')
                        params['age 65-74 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 65-74 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 75):
                        params['age 75-84'] = j.get('allToDate')
                        params['age 75-84 FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 75-84 MEN'] = j.get('maleToDate')
                    if(j.get('ageFrom') == 85):
                        params['age 85+'] = j.get('allToDate')
                        params['age 85+ FEMALE'] = j.get(
                            'femaleToDate')
                        params['age 85+ MEN'] = j.get('maleToDate')

            yield params
