import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




urls = ['https://obi.ru/products/perchatki-rabochie-svs-sinie-10-sht-2922169',
'https://obi.ru/products/nakolennik-2-sht-4010534',
'https://obi.ru/products/perchatki-sadovye-berta-xl-4120796',
'https://obi.ru/products/perchatki-sadovye-berta-l-4120812',
'https://obi.ru/products/perchatki-sadovye-berta-universalnye-chernye-4521589',
'https://obi.ru/products/perchatki-rabochie-svs-oranzhevye-xxl-3581527',
'https://obi.ru/products/antiseptik-dlja-ruk-bestol-10-l-4588919',
'https://obi.ru/products/perchatki-sadovye-berta-freddy-m-3990819',
'https://obi.ru/products/galoshi-uteplennye-zhenskie-oyo-jeva-r-36-41-4092755',
'https://obi.ru/products/berushi-mnogorazovye-s-soedinitelnym-shnurom-4641957',
'https://obi.ru/products/filtrujuschaja-polumaska-gigienicheskaja-kn95-4573572',
'https://obi.ru/products/pojas-montazhnyj-up-1-g-uderzhivajuschij-4916854',
'https://obi.ru/products/galoshi-uteplennye-zhenskie-gow-r-36-41-4862553',
'https://obi.ru/products/kombinezon-zaschitnyj-micromax-xxl-belyj-4817995',
'https://obi.ru/products/dozhdevik-plasch-100-sm-krasnyj-1561158',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-gow-r-40-45-4862579',
'https://obi.ru/products/zaschitnye-brjuki-baltika-1-48-50-164-sm-hlopok-temno-sinij-4507851',
'https://obi.ru/products/perchatki-maslobenzostojkie-svs-oilresist-xxl-v-assortimente-4641890',
'https://obi.ru/products/zhilet-s-karmanami-44-64-4209862',
'https://obi.ru/products/sabo-zhenskie-gavary-zatik-jeva-r-36-41-3841376',
'https://obi.ru/products/perchatki-rabochie-tegera-10-3711579',
'https://obi.ru/products/polumaska-filtrujuschaja-skladnaja-istok-pro-ffp2-s-klpanom-belaja-4900700',
'https://obi.ru/products/zaschitnye-brjuki-baltika-1-hlopok-48-50-188-sm-temno-sinij-4512018',
'https://obi.ru/products/perchatki-rabochie-xl-4139804',
'https://obi.ru/products/botinki-uteplennye-zhenskie-oyo-r-36-41-4862611',
'https://obi.ru/products/zaschitnaja-kurtka-baltika-1-hlopok-52-54-176-sm-temno-sinij-4511952',
'https://obi.ru/products/perchatki-sadovye-garden-show-cvety-m-8-1599729',
'https://obi.ru/products/sabo-muzhskie-gavary-zatik-1zs-jeva-r-40-45-3953114',
'https://obi.ru/products/perchatki-sadovye-tegera-90014-7-7-4783379',
'https://obi.ru/products/perchatki-sadovye-berta-499-universalnye-4120788',
'https://obi.ru/products/maska-svarochnaja-hameleon-svona-iskra-m-f-1-90h35-mm-4916797',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-oyo-r-40-45-v-assortimente-3841384',
'https://obi.ru/products/kostjum-muzhskoj-troja-korichnevyj-sop-52-54-3-4-razmer-5002102',
'https://obi.ru/products/perchatki-rabochie-svs-rubifrost-3718749',
'https://obi.ru/products/perchatki-sadovye-lux-tools-397087-3029253',
'https://obi.ru/products/nakolenniki-garden-show-19x15x1-3-sm-3763836',
'https://obi.ru/products/kostjum-muzhskoj-troja-temno-sinij-44-46-3-4-razmer-5002108',
'https://obi.ru/products/perchatki-rabochie-oilresist-nl13nt-9-4057345',
'https://obi.ru/products/perchatki-sadovye-berta-s-3667995',
'https://obi.ru/products/perchatki-rabochie-svs-chernye-2922094',
'https://obi.ru/products/perchatki-sadovye-lux-tools-397088-sadovye-s-3029220',
'https://obi.ru/products/perchatki-sadovye-berta-roza-m-4120804',
'https://obi.ru/products/galoshi-zhenskie-oyo-2d-jeva-r-36-41-4092730',
'https://obi.ru/products/ochki-zaschitnye-ochki-o-05-prozrachnye-na-rezinke-4641999',
'https://obi.ru/products/perchatki-rabochie-svs-belye-2922102',
'https://obi.ru/products/perchatki-rabochie-svs-belye-2922102',
'https://obi.ru/products/sabo-zhenskie-gavary-zatik-2zs-jeva-r-36-41-3953106',
'https://obi.ru/products/filtrujuschaja-polumaska-zaschitnaja-serdce-hlopok-4602124',
'https://obi.ru/products/filtrujuschaja-polumaska-zaschitnaja-usy-4602090',
'https://obi.ru/products/polumaska-filtrujuschaja-istok-u-2k-ffp1-s-klapanom-zelenaja-4900676',
'https://obi.ru/products/galoshi-zhenskie-oyo-jeva-r-36-41-2859379',
'https://obi.ru/products/perchatki-rabochie-2hands-5k30-boa-11-4642104',
'https://obi.ru/products/svarochnaja-maska-elitech-ms-900prof-hameleon-4912150',
'https://obi.ru/products/kostjum-muzhskoj-gor-gorec-letnij-hb-56-58-5-6-razmer-5002065',
'https://obi.ru/products/zaschitnaja-kaska-rosomz-somz-55-favorit-termo-krasnaja-4641916',
'https://obi.ru/products/perchatki-rabochie-svs-v-assortimente-2922128',
'https://obi.ru/products/perchatki-zaschitnye-2hands-gazorezchik-xl-4642187',
'https://obi.ru/products/kostjum-vlagozaschitnyj-hunter-zelenyj-kamufljazh-52-54-5-6-razmer-5002038',
'https://obi.ru/products/kostjum-vlagozaschitnyj-hunter-zelenyj-kamufljazh-44-46-3-4-razmer-5002033',
'https://obi.ru/products/rukavicy-rabochie-g18-2337905',
'https://obi.ru/products/perchatki-sadovye-tegera-zaschitnye-razmer-8-5001850',
'https://obi.ru/products/kasketka-zaschitnaja-kas502-oranzhevaja-4916904',
'https://obi.ru/products/perchatki-rabochie-tegera-9-r-4783486',
'https://obi.ru/products/botinki-muzhskie-trejl-pljus-naturalnaja-kozha-r-38-4389953',
'https://obi.ru/products/botinki-uteplennye-muzhskie-oyo-r-40-45-4862660',
'https://obi.ru/products/perchatki-sadovye-tegera-zaschitnye-razmer-9-5001851',
'https://obi.ru/products/perchatki-sadovye-tegera-zaschitnye-razmer-7-5001849',
'https://obi.ru/products/gigienicheskoe-sredstvo-dlja-ruk-forester-s-antisepticheskim-jeffektom-250-ml-4587820',
'https://obi.ru/products/zaschitnyj-kombinezon-ansell-alphatec-polijetilen-s-5xl-belyj-4641965',
'https://obi.ru/products/sabo-muzhskie-gavary-zatik-jeva-r-40-45-3841400',
'https://obi.ru/products/kostjum-muzhskoj-lider-vas-hb-56-58-5-6-razmer-5002085',
'https://obi.ru/products/kostjum-muzhskoj-lider-vas-hb-56-58-3-4-razmer-5002084',
'https://obi.ru/products/kostjum-muzhskoj-lider-vas-hb-48-50-3-4-razmer-5002080',
'https://obi.ru/products/kepka-hb-tekstil-temno-sinjaja-reguliruemaja-5002032',
'https://obi.ru/products/perchatki-zaschitnye-2hands-0516-10-4642120',
'https://obi.ru/products/naushniki-zaschitnye-istok-s-krepleniem-4916888',
'https://obi.ru/products/maska-svarochnaja-svona-iskra-m-f-5-110h90-mm-4916805',
'https://obi.ru/products/naushniki-zaschitnye-istok-4916870',
'https://obi.ru/products/dozhdevik-plasch-2hands-polijetilen-xl-v-assortimente-4642237',
'https://obi.ru/products/perchatki-stroitelnye-2hands-armaturschik-kombinirovannye-xl-4642195',
'https://obi.ru/products/perchatki-sadovye-berta-m-3668001',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-oyo-jeva-r-41-45-4092748',
'https://obi.ru/products/perchatki-sadovye-lux-tools-s-7-1703214',
'https://obi.ru/products/kragi-ogneupornye-g540-10-2338275',
'https://obi.ru/products/kragi-sadovye-berta-universalnye-3764321',
'https://obi.ru/products/zaschitnyj-schitok-sibrteh-svona-230-1-1s-nbt-01-jekonom-prozrachnyj-4642310',
'https://obi.ru/products/kragi-svarochnye-2hands-grenadjor-universalnye-4717211',
'https://obi.ru/products/perchatki-sadovye-lux-tools-s-3029303',
'https://obi.ru/products/krem-maz-universalnaja-vashe-hozjajstvo-pohodnaja-zazhivljajuschaja-40-g-4301925',
'https://obi.ru/products/krem-dlja-ruk-vashe-hozjajstvo-sadovo-ogorodnyj-zaschitnyj-75-ml-4301941',
'https://obi.ru/products/dozhdevik-plasch-koopman-international-polijetilen-detskij-v-assortimente-4479952',
'https://obi.ru/products/antiseptik-gel-dlja-ruk-bestol-200-ml-4588885',
'https://obi.ru/products/strahovochnyj-pojas-tech-krep-usp-2azh-4629663',
'https://obi.ru/products/maska-svarschika-daewoo-dwh-400-4837985',
'https://obi.ru/products/galoshi-uteplennye-zhenskie-retro-r-36-41-4862546',
'https://obi.ru/products/perchatki-sadovye-garden-friend-7-5-4108965',
'https://obi.ru/products/perchatki-rabochie-tegera-90069-8-r-4783478',
'https://obi.ru/products/sabo-muzhskie-ayo-jeva-r-40-45-v-assortimente-4752937',
'https://obi.ru/products/dozhdevik-poncho-koopman-international-polipropilen-one-size-v-assortimente-4479960',
'https://obi.ru/products/perchatki-rabochie-tegera-618-9-r-4783510',
'https://obi.ru/products/kaska-zaschitnaja-istok-s-reechnym-mehanizmom-oranzhevaja-4900668',
'https://obi.ru/products/botinki-muzhskie-toff-superstajl-naturalnaja-kozha-r-41-4663225',
'https://obi.ru/products/polukombinezon-muzhskoj-standart-temno-sinij-52-54-5-6-razmer-5002143',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-ayo-r-40-45-v-assortimente-3841392',
'https://obi.ru/products/dozhdevik-plasch-dlja-vzroslyh-52-54-r-4783403',
'https://obi.ru/products/perchatki-rabochie-tegera-90068-8-r-4783452',
'https://obi.ru/products/kaska-zaschitnaja-istok-s-reechnym-mehanizmom-belaja-4900650',
'https://obi.ru/products/perchatki-svs-osen-relefnyj-lateks-10-xl-5057110',
'https://obi.ru/products/sredstvo-dlja-ochistki-ruk-jekstrim-chistik-200ml-tuba-4895421',
'https://obi.ru/products/perchatki-sadovye-tegera-11-4783395',
'https://obi.ru/products/perchatki-sadovye-tegera-7-9-4753604',
'https://obi.ru/products/sabo-zhenskie-ayo-jeva-r-36-41-v-assortimente-4752945',
'https://obi.ru/products/zaschitnye-ochki-ljucerna-r-otkrytye-zheltye-4641981',
'https://obi.ru/products/polukombinezon-muzhskoj-standart-temno-sinij-44-46-3-4-razmer-5002138',
'https://obi.ru/products/perchatki-sadovye-garden-show-jagody-8-4595070',
'https://obi.ru/products/perchatki-sadovye-garden-show-pushistiki-8-4595054',
'https://obi.ru/products/kragi-svarochnye-elitech-606-016300-4618856',
'https://obi.ru/products/dozhdevik-plasch-polijefir-l-180-sm-v-assortimente-4783411',
'https://obi.ru/products/perchatki-sadovye-tegera-nejlon-belye-razmer-8-5001854',
'https://obi.ru/products/perchatki-zaschitnye-2hands-0526-10-4642146',
'https://obi.ru/products/perchatki-rabochie-tegera-90067-8-r-4783437',
'https://obi.ru/products/perchatki-sadovye-garden-show-jagody-9-4595088',
'https://obi.ru/products/ugolnik-elitech-45-90-135-gradusov-4493888',
'https://obi.ru/products/galoshi-uteplennye-zhenskie-oyo-r-36-41-4201547',
'https://obi.ru/products/galoshi-muzhskie-oyo-nga1-jeva-r-40-45-3841418',
'https://obi.ru/products/perchatki-sadovye-9-10-4106175',
'https://obi.ru/products/botinki-muzhskie-toff-superstajl-naturalnaja-kozha-r-42-4663233',
'https://obi.ru/products/botinki-muzhskie-toff-naturalnaja-kozha-r-42-4663159',
'https://obi.ru/products/galoshi-uteplennye-zhenskie-oyo-r-36-41-v-assortimente-3841434',
'https://obi.ru/products/perchatki-rabochie-lux-tools-xl-10-3628211',
'https://obi.ru/products/perchatki-sadovye-garden-show-pushistiki-9-4595062',
'https://obi.ru/products/fartuk-berta-v-assortimente-4521571',
'https://obi.ru/products/zaschitnye-ochki-rosomz-jetalon-zn4-zakrytye-4641908',
'https://obi.ru/products/rukavicy-rabochie-g13-2337962',
'https://obi.ru/products/nakolenniki-zaschitnye-s-mjagkimi-plastikovymi-chashkami-svona-izolon-1-para-4916771',
'https://obi.ru/products/kostjum-vlagozaschitnyj-liven-sinij-48-razmer-5002046',
'https://obi.ru/products/botinki-uteplennye-zhenskie-retro-r-36-41-4862587',
'https://obi.ru/products/perchatki-dijelektricheskie-g49-2338176',
'https://obi.ru/products/perchatki-zaschitnye-2hands-0543-eco-10-4642112',
'https://obi.ru/products/perchatki-sadovye-palisad-l-8-3729506',
'https://obi.ru/products/krem-pasta-dlja-ruk-vashe-hozjajstvo-alba-chistonik-ochischajuschaja-150-ml-4301958',
'https://obi.ru/products/polusapogi-uteplennye-ayo-np23-zhenskie-r-36-41-4456927',
'https://obi.ru/products/perchatki-sadovye-tegera-nejlon-chernye-razmer-9-5001860',
'https://obi.ru/products/perchatki-rabochie-berta-universalnye-3667987',
'https://obi.ru/products/botinki-muzhskie-toff-naturalnaja-kozha-r-40-4663134',
'https://obi.ru/products/dozhdevik-plasch-berta-polijefir-48-50-r-4521720',
'https://obi.ru/products/podkolennik-sadovyj-lux-tools-classic-40h18h2-sm-1142280',
'https://obi.ru/products/antiseptik-sprej-dlja-ruk-i-poverhnostej-sanita-protect-500-ml-4636536',
'https://obi.ru/products/kombinezon-zaschitnyj-odnorazovyj-kasper-xxl-belyj-4817987',
'https://obi.ru/products/perchatki-sadovye-garden-show-master-l-9-1599711',
'https://obi.ru/products/perchatki-rabochie-svs-15-sht-2922136',
'https://obi.ru/products/kragi-svarochnye-2hands-metallurg-universalnye-4717203',
'https://obi.ru/products/perchatki-rabochie-berta-s-3764305',
'https://obi.ru/products/zaschitnye-ochki-zn-svona-230-1-zakrytye-4642005',
'https://obi.ru/products/perchatki-sadovye-berta-209-universalnye-3711553',
'https://obi.ru/products/dozhdevik-plasch-polijefir-xxxl-188-sm-v-assortimente-4783429',
'https://obi.ru/products/zaschitnye-ochki-lux-tools-comfort-zakrytye-106040-1131804',
'https://obi.ru/products/perchatki-rabochie-tegera-90068-7-r-4783445',
'https://obi.ru/products/maska-svarochnaja-resanta-ms-4-4895207',
'https://obi.ru/products/perchatki-sadovye-lux-tools-classic-l-9-1164128',
'https://obi.ru/products/dozhdevik-poncho-koopman-international-polijetilen-leopard-v-assortimente-4479986',
'https://obi.ru/products/perchatki-sadovye-berta-3764313',
'https://obi.ru/products/perchatki-sadovye-tegera-hlopkovye-razmer-8-5001862',
'https://obi.ru/products/zaschitnyj-kostjum-muzhskoj-xxxl-188-sm-sinij-4828240',
'https://obi.ru/products/zaschitnyj-kostjum-muzhskoj-m-176-sm-sinij-4828208',
'https://obi.ru/products/perchatki-sadovye-lux-tools-39900-m-8-3074275',
'https://obi.ru/products/perchatki-rabochie-tegera-6-3711561',
'https://obi.ru/products/dozhdevik-plasch-polijefir-l-176-sm-zelenyj-4828315',
'https://obi.ru/products/galoshi-zhenskie-ayo-jeva-r-36-41-v-assortimente-3841442',
'https://obi.ru/products/ugolnik-elitech-30-45-60-75-90-135-gradusov-4493896',
'https://obi.ru/products/kragi-svarochnye-elitech-606-015700-4618849',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-4h4-r-40-46-4752978',
'https://obi.ru/products/dozhdevik-plasch-forest-polijefir-xl-188-sm-sinij-4828174',
'https://obi.ru/products/kombinezon-zaschitnyj-25-g-kv-m-spanbond-belyj-4587564',
'https://obi.ru/products/perchatki-rabochie-g304-10-2338283',
'https://obi.ru/products/perchatki-sadovye-ladiesgift-polijester-9-4052437',
'https://obi.ru/products/zaschitnyj-kostjum-bulat-muzhskoj-kurtka-brjuki-52-54-176-sm-haki-4389896',
'https://obi.ru/products/dozhdevik-plasch-koopman-international-detskij-v-assortimente-4306502',
'https://obi.ru/products/podstavka-pod-koleni-4330296',
'https://obi.ru/products/respirator-polumaska-istok-300-rpg-67-ffp3-4642047',
'https://obi.ru/products/dozhdevik-plasch-polijefir-xl-188-sm-zelenyj-4828323',
'https://obi.ru/products/dozhdevik-detskij-polivinil-da7000260-4479945',
'https://obi.ru/products/antiseptik-universalnyj-big-d-150-ml-4852323',
'https://obi.ru/products/berushi-lux-tools-comfort-mnogorazovye-s-lentoj-2-pary-1131671',
'https://obi.ru/products/dozhdevik-plasch-polijefir-l-176-sm-sinij-4828166',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-retro-r-40-45-4862561',
'https://obi.ru/products/zaschitnye-ochki-lux-tools-classic-398553-3628252',
'https://obi.ru/products/galoshi-uteplennye-muzhskie-gmu1-r-40-45-4456877',
'https://obi.ru/products/perchatki-sadovye-garden-friends-detskie-s-4109047',
'https://obi.ru/products/perchatki-sadovye-ladiesgift-m-9-4052445',
'https://obi.ru/products/perchatki-sadovye-garden-friends-razmer-s-7-5-4092813',
'https://obi.ru/products/remen-dlja-instrumentov-lux-tools-comfort-nejlonovyj-1-3-m-1936855',
'https://obi.ru/products/perchatki-sadovye-lux-tools-397093-m-8-3074291',
'https://obi.ru/products/perchatki-sadovye-lux-tools-professional-m-8-3074283',
'https://obi.ru/products/botinki-uteplennye-ayo-npb22-zhenskie-r-36-41-4456901',
'https://obi.ru/products/dozhdevik-plasch-koopman-international-polivinil-detskij-v-assortimente-4479911',
'https://obi.ru/products/krem-dlja-ruk-safety-lab-eso-line-zaschitnyj-100-ml-4564647',
'https://obi.ru/products/galoshi-zhenskie-4h4-r-36-41-4752960',
'https://obi.ru/products/perchatki-sadovye-garden-friend-razmer-7-5-detskie-4108973',
'https://obi.ru/products/perchatki-rabochie-pro-hand-torro-2337954',
'https://obi.ru/products/perchatki-dlja-sadovyh-rabot-razmer-5-detskie-1842798',
'https://obi.ru/products/ugolnyj-gril-cleveland-47-5h47-5h92-sm-4028833',
'https://obi.ru/products/ugolnyj-gril-oil-drum-93h64-5h90-sm-4206827',
'https://obi.ru/products/ugolnyj-gril-jamestown-grill-ben-xl-142h64h92-sm-4622940',
'https://obi.ru/products/jelektricheskij-gril-nastolnyj-22x40x10-sm-2851566',
'https://obi.ru/products/gril-jelektricheskij-cmi-2200-vt-4565065'
 ]

urls_1 = ['https://obi.ru/products/zaschitnye-brjuki-baltika-1-hlopok-48-50-188-sm-temno-sinij-4512018',
'https://obi.ru/products/dozhdevik-plasch-2hands-polijetilen-xl-v-assortimente-4642237',
'https://obi.ru/products/kombinezon-zaschitnyj-odnorazovyj-kasper-xxl-belyj-4817987',
'https://obi.ru/products/ugolnyj-gril-cleveland-47-5h47-5h92-sm-4028833'
]

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    with uc.Chrome(version_main=112, chrome_options=options) as browser:
        with open('resOBI_2.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for url in urls_1:
                result = []
                browser.get(url)
                try:
                    wait = WebDriverWait(browser, 15)
                    name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_3LdDm")))
                    result.append(name.text)
                    article = browser.find_element(By.CLASS_NAME, '_2XlQF')
                    result.append(article.text)
                    time.sleep(1)
                    discriptions = [result.append(i.text) for i in browser.find_elements(By.CLASS_NAME, '_2pA08')]
                    time.sleep(1)
                    price = browser.find_element(By.CLASS_NAME, '_3IeOW').text.replace('&nbsp;', '')
                    result.append(price)
                    time.sleep(1)
                    subscriptions_1 = [result.append(i.text) for i in browser.find_elements(By.CLASS_NAME, '_3LqYU')]
                    time.sleep(1)
                    subscriptions_2 = [result.append(i.text) for i in browser.find_elements(By.TAG_NAME, 'dt')]
                    time.sleep(1)
                    subscriptions_3 = [result.append(i.text) for i in browser.find_elements(By.CLASS_NAME, '_1sZLj')]
                    time.sleep(1)
                    in_stock = browser.find_element(By.CLASS_NAME, '_2KVcZ.AX0Hx').text
                    result.append(in_stock)
                except:
                    print(f'нет товара по ссылке: {url}')
                writer.writerow(result)
