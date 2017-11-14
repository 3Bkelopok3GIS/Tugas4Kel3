import folium

def inisiasi(long,lat):
	m = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')
	return m
	
def hitam(long,lat):
	c = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Toner')	
	return c

def masukkin(apa,ini):
	d = folium.Map(
	location=[apa,ini],
	zoom_start=12,
    tiles='Stamen Terrain')	
	return d
	
def simpan(anu,gede):
	anu.save(gede)

d = masukkin(-6.9052436,107.314146)
c = hitam(-6.9052436,107.314146)
m = inisiasi(-6.9052436,107.314146)
tooltip = 'Click me!'


m = folium.Marker(
    location=[-6.9045005,107.314102,11],
    zoom_start=12,
    )
folium.Marker(
    Location=[-6.755192, 107.305862],
    popup='Margaluyu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.707458, 107.352554],
    popup='Cipeundeuy',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.697911, 107.378647],
    popup='Puteran',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.693819, 107.412979],
    popup='Tenjolaut',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.745305, 107.511169],
    popup='Ganjarsari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.776671, 107.561294],
    popup='Tugumukti',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.753488, 107.575027],
    popup='Karyawangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.767807, 107.617599],
    popup='Jayagiri',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.777353, 107.652618],
    popup='Cikidang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.794399, 107.677337],
    popup='Wangunharja',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.824398, 107.662918],
    popup='Cibodas',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.850646, 107.629963],
    popup='Mekarwangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.843488, 107.586331],
    popup='Cigugur Girang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.874166, 107.570538],
    popup='Sariwangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.851669, 107.556805],
    popup='Padaasih',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.828489, 107.545132],
    popup='Pakuhaji',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.847578, 107.527966],
    popup='Ngamprah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.880301, 107.512173],
    popup='Laksanamekar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.903478, 107.510113],
    popup='Batujajar Tim',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.933471, 107.519039],
    popup='Selacau',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.954600, 107.516293],
    popup='Situwangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.954600, 107.516293],
    popup='Sukarama',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-6.933811, 107.244068],
    popup='Sukaresmi',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-7.064665, 107.271534],
    popup='Sirnajaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-6.922905, 107.279774],
    popup='Kemang',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-6.886095, 107.326466],
    popup='Cihea',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-6.959712, 107.200123],
    popup='Karangnunggal',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-7.056487, 107.201496],
    popup='Cilangari',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
    Location=[-6.815194, 107.721974],
    popup='Suntenjaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
 	Location=[-6.771557, 107.627216],
    popup='Ciater',
    icon=folium.Icon(icon='info-sign')
).add_to(m),
folium.Marker(
	Location=[-6.734735, 107.499500],
    popup='Pasirangin',
    icon=folium.Icon(icon='info-sign')
).add_to(m),

folium.Marker(
    Location=[-6.835647, 107.428444],
    popup='Tebing Citatah 48',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.836757, 107.431204],
    popup='Masjid Al Hikmah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.834746, 107.425074],
    popup='Rumah Makan Pulen 2 Cibogo Citata',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832999, 107.426071],
    popup='Warung Mas Wasito',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832147, 107.428281],
    popup='Alfamart Citatah Pumarin N760',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.833973, 107.427777],
    popup='Toko Hd',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831843, 107.434681],
    popup='TB Gani Jaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832860, 107.435690],
    popup='WARUNG BASO',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831414, 107.437177],
    popup='CV. HEGAR JAYA',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.829328, 107.437609],
    popup='Bukit Ashar. PT',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    Location=[-6.999924, 107.186390],
    popup='Sukamanah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.758602, 107.330586],
    popup='Waduk Citara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.848601, 107.326466],
    popup='Haurwangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.909954, 107.304493],
    popup='Cibitung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.941309, 107.448689],
    popup='Cililin',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.999924, 107.483021],
    popup='Mukapayung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.047629, 107.443195],
    popup='Buninagara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.092603, 107.408863],
    popup='Lebakmuncang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.851328, 107.612110],
    popup='Cidadap',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.954941, 107.518726],
    popup='Cihampelas',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.867493, 107.570308],
    popup='SMK Insan Mandiri',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.859557, 107.565599],
    popup='Sekolah Kampoeng Quran',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.857863, 107.579020],
    popup='Taman Pendidikan Firdaus Percikan Iman',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.852963, 107.573055],
    popup='SMP & SMK IT Nurul Imam',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.847680, 107.580780],
    popup='MI Nurul Huda',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.846956, 107.591981],
    popup='Mutiara Nusantara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.847850, 107.580093],
    popup='SMP Negeri 2 Parongpong',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.841075, 107.573914],
    popup='Sekolah Tinggi Alkitab Tiranus',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.842652, 107.561511],
    popup='SDN BUDI ASIH',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.837794, 107.584471],
    popup='Yayasan Eco Pesantren Daarut Tauhiid',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.813293, 107.600821],
    popup='SMP Kahuripan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.975389, 107.252995],
    popup='Bojongsalam',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.005376, 107.252995],
    popup='Cibedug',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.036044, 107.260548],
    popup='Bunijaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.057169, 107.276340],
    popup='Sirnajaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.057169, 107.310673],
    popup='Gununghalu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.105549, 107.376591],
    popup='Mekarwangi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.042177, 107.393070],
    popup='Wangunsari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.040814, 107.457615],
    popup='Buninagara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.015599, 107.466541],
    popup='Naggereng',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.017644, 107.471348],
    popup='Karyamuki',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.802938, 107.583420],
    popup='Villa Istana Bunga',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.801745, 107.583281],
    popup='Detasemen Kavaleri berkuda',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.799295, 107.577509],
    popup='Curug Rainbow',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.798496, 107.572617],
    popup='Warung Makan Sans',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.798379, 107.569355],
    popup='Saung Kusumah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.861235, 107.514733],
    popup='Toko Voucher',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.861054, 107.519894],
    popup='Borma Permata',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.854407, 107.516203],
    popup='Cilame Futsal',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.851478, 107.526074],
    popup='Masjid Al - Muhajirin',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.854162, 107.532586],
    popup='SDN 1 Ciledug',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.794988, 107.648979],
    popup='Kopi Luwak Cikole',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.871950, 107.513713],
    popup='Masjid Al-Barokah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.853544, 107.514743],
    popup='Masjid Jabal Nur',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.855589, 107.527446],
    popup='Masjid Jabal Rohmah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.872622, 107.565897],
    popup='Masjid Al-Muhajirin',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.873985, 107.575510],
    popup='Masjid Lukmanul Hakim',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.867850, 107.568987],
    popup='Masjid Jami Al Hikmah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.864441, 107.579630],
    popup='Masjid Al IKHLAS',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.853874, 107.568301],
    popup='Masjid At Tawajun',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.859328, 107.573107],
    popup='Masjid Nurul Iman',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.851829, 107.585810],
    popup='Al Hidayah Setiabudi Regensi',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.901774, 107.378651],
    popup='Saguling',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.888140, 107.400623],
    popup='Cipangeran',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.892912, 107.424656],
    popup='Girimukti',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.882687, 107.442509],
    popup='Cikande',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.865644, 107.456242],
    popup='Bojonghaleuang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.937219, 107.385517],
    popup='Karanganyar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.961075, 107.404743],
    popup='Cipongkor',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.826784, 107.370411],
    popup='Cipatat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.023777, 107.250935],
    popup='Cilangari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.044903, 107.296253],
    popup='Sinarjaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    Location=[-6.833487, 107.437957],
    popup='Tebing Cilio Camp',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832918, 107.438150],
    popup='SDN Gunung Masigit',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832513, 107.437941],
    popup='Sony Minang RM MASAKAN PADA',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831698, 107.436771],
    popup='Citra Onix',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.828117, 107.435101],
    popup='Garasi Indominerals',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.827227, 107.435541],
    popup='Tebing Masigit',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.825827, 107.435192],
    popup='Homestay Wahana Indianacamp',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.825464, 107.435948],
    popup='Indianacamp',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.825550, 107.437043],
    popup='Sekretariat Pokdarwis Stone Garde',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.824773, 107.438146],
    popup='Stone Garden Citatah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.932203, 107.502070],
    popup='Waduk Saguling',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.930839, 107.372294],
    popup='Cipongkor',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.794739, 107.555801],
    popup='Cisarua',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.877914, 107.492629],
    popup='Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.768829, 107.603866],
    popup='Sukajaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.763374, 107.396499],
    popup='Kanangasari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.962438, 107.238571],
    popup='Bojong',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.006057, 107.404739],
    popup='Ranca Senggang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.025140, 107.355300],
    popup='Celak',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.829402, 107.595533],
    popup='Kampung Gahjah Wonderland',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.829800, 107.594990],
    popup='Tahu Gejrot Mang Sulim',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.828639, 107.595360],
    popup='Villa Diamond',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831484, 107.595074],
    popup='Sugar & Ice Cream',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831749, 107.595025],
    popup='Maja House',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831413, 107.596761],
    popup='Cihideung Park',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832649, 107.596631],
    popup='Black Bird Hotel',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.835027, 107.595300],
    popup='Surabi Bu Chien',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.836814, 107.595151],
    popup='Hotel Amoory & Cafe',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.827851, 107.594373],
    popup='Villa Gajah',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    Location=[-6.823480, 107.436671],
    popup='Tukang Es Kelapa Goa Pawon',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.823355, 107.436180],
    popup='Bale Riung Pariwisata Gua Pawon',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.823229, 107.436689],
    popup='Gua Pawon',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.819467, 107.433189],
    popup='Izral Cell',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.818795, 107.431953],
    popup='Masjid Mekar Mulya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.815513, 107.433949],
    popup='Toko Almira Cipatat',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.825624, 107.430529],
    popup='CV.FITRIINDO LITE',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831817, 107.450973],
    popup='Kios Peuyeum Bapak A Rohana',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831199, 107.449942],
    popup='Cape Coffee FJM',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.831808, 107.448856],
    popup='PT. Batumas Mekar Agung (BAMA)',
    icon=folium.Icon(icon='info-sign')
).add_to(m)   
folium.Marker(
    Location=[-6.794740, 107.399248],
    popup='Sumurbandung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.969936, 107.320971],
    popup='Cintaasih',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.794740, 107.431521],
    popup='Cirawamekar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.822012, 107.456926],
    popup='Ciburuy',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.962439, 107.470659],
    popup='Karangtanjung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.008102, 107.441820],
    popup='Nanggerang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.936538, 107.317537],
    popup='Cibenda',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.966528, 107.353930],
    popup='Neglasari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.990383, 107.387575],
    popup='Puncaksari',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-7.000606, 107.373842],
    popup='Cicangkang Girang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.865708, 107.473922],
    popup='RS Cahya Kawaluyaan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.864952, 107.475403],
    popup='STIKes Santo Borromeus',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.864227, 107.477399],
    popup='Al Irsyad Satya Islamic School',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.864696, 107.477613],
    popup='Masjid Al Irsyad',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.865293, 107.469985],
    popup='TKK-SDK BPK Penabur Bandung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.868350, 107.467936],
    popup='Cahaya Bangsa Classical School',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.871013, 107.470478],
    popup='Bumi Pancasona Sports Club',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.872589, 107.470221],
    popup='Damian School',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.863940, 107.479973],
    popup='MASON PINE HOTEL',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.857027, 107.490466],
    popup='Bale Pare',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832084, 107.448438],
    popup='Sekretariat FOX Riders Indonesia',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832170, 107.441289],
    popup='Jaya Teknik Mandiri',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832973, 107.438944],
    popup='Balai Desa Gunungmasigit',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.841146, 107.485329],
    popup='Masjid Besar Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.840891, 107.485769],
    popup='Ps. Tagog Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.839464, 107.487083],
    popup='Padalarang Motor',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.838750, 107.487533],
    popup='PLN Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.837600, 107.488145],
    popup='RM.CIGANEA',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.838026, 107.487845],
    popup='Polsek Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.765420, 107.480959],
    popup='Cipada',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.941991, 107.399248],
    popup='Citalem',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.963802, 107.451433],
    popup='Batulayang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.969254, 107.391009],
    popup='Pasirpogor',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.916089, 107.424654],
    popup='Tanjungjaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.895639, 107.321657],
    popup='Baranangsiang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.990383, 107.307924],
    popup='Cicadas',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.824739, 107.490571],
    popup='Bojongkoneng',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.813830, 107.512543],
    popup='Cimanggu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.839738, 107.575028],
    popup='Cihanjung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.791331, 107.510487],
    popup='Sedangmekar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.802240, 107.485767],
    popup='Togagapu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.809058, 107.454182],
    popup='Cempakamekar',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.852691, 107.438389],
    popup='Gunungmasigit',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.855418, 107.376591],
    popup='Ciptaharja',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.805308, 107.520958],
    popup='Pasirlungu',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.832409, 107.491432],
    popup='Sukatani',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.841783, 107.498813],
    popup='Kartajaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.853884, 107.502590],
    popup='Margajaya',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.869564, 107.507053],
    popup='Gadobangkong',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

folium.Marker(
    Location=[-6.856127, 107.498685],
    popup='Kost Pak Haji Syarif',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.855857, 107.497824],
    popup='Jl. Raya Caringin No.355',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.856085, 107.497782],
    popup='PT Indofood CBP Sukses Makmur',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.855595, 107.498054],
    popup='SPBU 34-40513 Caringin, Padalara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.852815, 107.498173],
    popup='Al Azhar Syifa Budi Parahyangan',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.850669, 107.495741],
    popup='Holland Bakery',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.852190, 107.493887],
    popup='Puspa Iptek Sundial',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.849543, 107.492696],
    popup='SMP Negeri 1 Padalarang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    Location=[-6.847710, 107.492031],
    popup='Apotek Jaya Medika',
    icon=folium.Icon(icon='info-sign')
).add_to(m)

    
m
#m nya jangan di hapus yaa
