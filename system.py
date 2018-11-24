from User import User
from Phone import Phone

import pickle

class systemManager():
    def __init__(self):
        self._phoneList = []

    def systemLoad(self):
        fileObject = open('phoneDatabase', 'rb')
        phoneList = pickle.load(fileObject)

        for i in phoneList:
            self._phoneList.append(i)

        print("SystemLoadedSuccessfully")

        fileObject.close()

    def searchPhone(self, searchPhone):
        searchList = []
        for i in self._phoneList:
            if i.phoneName.find(searchPhone) != -1:
                searchList.append(i)

        return searchList

    def getPhone(self, phoneName):
        for i in self._phoneList:
            print(i.phoneName)
            if i.phoneName == phoneName:
                return i

        return None

    @property
    def phoneList(self):
        return self._phoneList


iPhoneXS =  Phone(
                'https://previews.dropbox.com/p/thumb/AAQ6TQI9ywNO-zBG8Z70YjSX_ijvSgwRyof-j5HBmzVtoBluliIbxZmjJ4g8TgDqKUeary2PoaGnpHxvFBLXZXnVMij4EXg7G0xmICh4at9kLlG-5qor9l7_D5z2nbx7KId6MWMUuF5O8983a6GTvU-i35p0nkrQpjQQgusbKXMXevfvQHYH7XCJwgejZeQpmtyeof8z-lX2MveggMTACu4S1p9o9vcsufH5KpBK28ZoOQ/p.png?size=1600x1200&size_mode=3',
                'iPhone XS',
                'September 2018',
                {'Type': '5.8-inch Super Retina HD display', 'Pixel': '2436 x 1125', 'Other': ['HDR Display', 'True Tone Display']},
                {'Height': '150.9 mm', 'Width': '70.9 mm', 'Depth': '7.7 mm', 'Weight': '177 g'},
                {'Megapixel': 'Dual 12-megapixel wide-angle', 'Other': ['Dual optical image stabilisation', 'Portrait mode with advanced bokeh and Depth Control']},
                {'BatteryLife': '12.5 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery', 'Other': ['Wireless Charging', 'Fast Charging']},
                {'OS': 'IOS', 'Chipset': 'A12 Bionic chip with next-generation Neural Engine', 'RAM': 'Unknown'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

iPhoneX =  Phone(
                'https://previews.dropbox.com/p/thumb/AATrHRqqMC223wcmxxQxit5q50uWj1zDY1Hw7Eaul1aKtuaXfPjiZdvldrBs3mZIqOdTAo-nnJdT5W0nm7BfKs1OxZ_aabM6GfWK30ZOR7WQSPdpXnG5-zEGS3uTn31eyuM8oQCJaY8HArfiHnMVt5o2D6trICSRrji7eR5FVh0xLUwi5D-dFks8xeByGZ3yv3VFEMM-LZc-Ij9L8lYUnlNLJxntX8cr89Z4cDHodFdD5Q/p.png?size=1600x1200&size_mode=3',
                'iPhone X',
                'September 2017',
                {'Type': '5.8-inch', 'Pixel': '2436 x 1125', 'Other': ['HDR Display', 'True Tone Display']},
                {'Height': '143.6 mm', 'Width': '70.9 mm', 'Depth': '7.7 mm', 'Weight': '177 g'},
                {'Megapixel': 'Dual 12-megapixel', 'Other': ['Dual optical image stabilisation', 'Portrait mode with advanced bokeh and Depth Control']},
                {'BatteryLife': '12 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery', 'Other': ['Wireless Charging']},
                {'OS': 'IOS', 'Chipset': 'Apple A11 Bionic', 'RAM': '3 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )
SamsungGalaxyS9 =  Phone(
                'https://previews.dropbox.com/p/thumb/AASm3ASI3XmXs92QKv8WXreZ-r6qZVs0IdN8DrMRAwzphc0fZy56QRVDzS0yIbNsoHqpMfW-JDQsvcpiWmCcC1voKX3CZjKgqyeGGxjgbzNx5YU-atQptF0_83HOPsxvlDApeGye6Qu_WUatXxf6g_Kl3xZ8-L-YJx4LjN9aFNQsTQRcNpoaeulxh8JOyRZxEP6vmMe2VWsopeLTeeIBb95KHDj9-kZBm6FOglIuTGmE_g/p.png?size=1600x1200&size_mode=3',
                'Samsung Galaxy S9',
                'March 2018',
                {'Type': '5.8" full rectangle, 5.6" rounded corners', 'Pixel': '2960 x 1440', 'Other': ['dual edge Super AMOLED']},
                {'Height': '147.7 mm', 'Width': '68.7 mm', 'Depth': '8.5 mm', 'Weight': '163 g'},
                {'Megapixel': 'Dual 12-megapixel', 'Other': ['Auto Focus', 'F1.5/F2.4 (Dual Aperture)']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3000 mAh)', 'Other': ['Wireless Charging', 'Fast Charging']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 845 chip', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

HuaweiMate20Pro =  Phone(
                'https://previews.dropbox.com/p/thumb/AAQWbIp0XfWp_I6_WjcFmlV-JUEpn2CZGo8cxksfO4_mBJrOuKov9Lnp8LQhczSp-z04yrwf1KWQat03BJshfBwBuX9oPTMOgDs-FrVtr3RqOnOBTdt9ZWzhWsP0kVq24_n91N0eCjNkPW9fLDF_ANw2meY7V0ec775XqRDZrk_Gy5dE27Mw3fXmTLoh5lBxNnIFgdxXm7ELhDKWjOtOrx1DuWR-fXRnGYCXwyO7cBOgXQ/p.png?size=1600x1200&size_mode=3',
                'Huawei Mate 20 Pro',
                'October 2018',
                {'Type': '6.39-inch', 'Pixel': '3120 x 1440', 'Other': ['16.7 million colours', 'OLED']},
                {'Height': '157.8 mm', 'Width': '72.3 mm', 'Depth': '6.8 mm', 'Weight': '189 g'},
                {'Megapixel': '40 MP (Wide Angle Lens) + 20 MP (Ultra Wide Angle Lens) + 8 MP (Telephoto)', 'Other': ['Auto Focus', 'Huawei AI Image Stabilization']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3000 mAh)', 'Other': ['Wireless Charging', 'Fast Charging']},
                {'OS': 'Android 9', 'Chipset': 'HUAWEI Kirin 980', 'RAM': '6 GB RAM + 128 GB ROM'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

GooglePixel3XL =  Phone(
                'https://previews.dropbox.com/p/thumb/AARTY6kS6wlNgOCSQkymjqVN8oZdT6_u5MYYdffEcR9DWrS-K1Mn-ufrQvBYvcUiix7JxiN9JBqBYfEHtqG0a1MQjv-5uqJpmKEKNpyGd6kZH4qbRZ1jjU2Db60WglJY3dN-y09vxugEqsoC8qGQqxbNhMbd7M7vNfODu-DOLKdAdpP-m5qm8tso4ZY7JORLarW7bZhAn3Wi97Hfu6FVsjutQ6v0RahbewLvGkKO3Vy2-Q/p.png?size=1600x1200&size_mode=3',
                'Google Pixel 3 XL',
                'October 2018',
                {'Type': '6.3-inch', 'Pixel': '2960 x 1440', 'Other': ['QHD+ OLED', 'Gorilla Glass 5']},
                {'Height': '158.0 mm', 'Width': '76.7 mm', 'Depth': ' 7.9 mm', 'Weight': '184 g'},
                {'Megapixel': '12.2 MP dual-pixel', 'Other': ['Spectral + flicker sensor']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3430 mAh)', 'Other': ['18 W/2 A USB type-C charger']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 845 chip', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

iPhone8 =  Phone(
                'https://previews.dropbox.com/p/thumb/AARYsr_KDDPV4cr0MB5jMhM_D0VECj8SK1JTb28mnjfKAEpaGzpLCncWckxMLQiZ3O_2SGUuHWwKfReNSpEyBKPBUR-Oh3aXvp5HpVE7cUTPuWoeibCRVMvkosIujmilf2ct7BpcvdPMxSNDvruIF-jgmwQYlAC-MzpoL6bKBhiXs-1UHPFLyxyb_Xb7QDjAfndY0NBazl75ciajnFQXbl32Ndy_RpjRolDgIK3HAYvVwA/p.png?size=1600x1200&size_mode=3',
                'iPhone 8',
                'September 2018',
                {'Type': '4.7-inch', 'Pixel': '1334 x 750', 'Other': ['Retina HD display']},
                {'Height': '138.4 mm', 'Width': '57.3 mm', 'Depth': '7.3 mm', 'Weight': '148 g'},
                {'Megapixel': '12.0 MP', 'Other': ['Optical image stabilisation', 'Optical Zoom at 5x']},
                {'BatteryLife': '12 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (1,821 mAh)', 'Other': ['Wireless Charging', 'Charging via USB']},
                {'OS': 'Android 9', 'Chipset': 'A11 Bionic chip', 'RAM': '6 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

GooglePixel3 = Phone(
                'https://previews.dropbox.com/p/thumb/AASFMFTqh3LtKDwDsJnoPdFdyg_2oJvyNh96xBx6QS0IlXBttHtBgHjhu28tSG1YBGGos9xNN6aTxfQf-JeJ14TU90_ydTKRcUODJeaemahyrbxdXqMKsFk8UyF6JCJcmyIEv-qXby0JWxASM4c6O4JUY2uyNgXqnfxo_tOjn6aGaNrP-KlnD-RUdbNenSiCGejAHgMV2VTA7Et0E1UyeXsWBmLTtdujU57FvYSB3QLN1w/p.png?size=1600x1200&size_mode=3',
                'Google Pixel 3',
                'October 2018',
                {'Type': '5.5-inch', 'Pixel': '2160 x 1080', 'Other': ['QHD+ OLED', 'Gorilla Glass 5']},
                {'Height': '145.6 mm', 'Width': '68.2 mm', 'Depth': ' 7.9 mm', 'Weight': '148 g'},
                {'Megapixel': '12.2 MP dual-pixel', 'Other': ['Spectral + flicker sensor']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (2915 mAh)', 'Other': ['18 W/2 A USB type-C charger']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 845 chip', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

OnePlus5 = Phone(
                'https://previews.dropbox.com/p/thumb/AASIDTbX9jrk5m6GP4niCYUwKUJx7Gbj714GKIOugZ1OqBN2k5CfygW8t7hwdWdiw5c03h6ka9ssLaFsOKeCptt1dDEDM_q2r7sjDcxlef995T_9vDctqDUeO0MXDIhVmyuNZls85EcJd93c_oDB3-X4PrsjkNzgT7Y6Mx5ghzDxqJC4rZkHLMrPlbfoMnm0wbA-fiwmOEH8J1Pe2pirkln7rxMcPrlgPTEKZq9-3SNOcQ/p.png?size=1600x1200&size_mode=3',
                'OnePlus 5',
                'June 2017',
                {'Type': '5.5-inch', 'Pixel': '1920 x 1080', 'Other': ['Optic AMOLED', 'Gorilla Glass 5']},
                {'Height': '154.2 mm', 'Width': '74.1 mm', 'Depth': '7.25 mm', 'Weight': '153 g'},
                {'Megapixel': '16 MP Wide Angel, 20MP Telephoto', 'Other': ['Sony Sony IMX 398']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3300 mAh)', 'Other': ['Dash Charge']},
                {'OS': 'Android 7', 'Chipset': 'Snapdragon 835 chip', 'RAM': '6 - 8 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

OnePlus6T = Phone(
                'https://previews.dropbox.com/p/thumb/AASuJ77ICq_heVzc-tJReMGaqMO9Z351BAXupfznsW0VSoYZMQG3L0dD-rPEe9v61e0Q6zEEnOiMhPZRrAvS738aGi9YyVT7-iyKAYlpItknsHXqI7lVoW4icdpMybntoPOB1KbGXP4mdtLjHWos_7ErVr4kc6qZpDhZNgp6xQrVIoDiv9VqSh74DuoUZtY0IpE2UITVmklcGRTXGk1TOTOryxrS2m3E9Xooa9I5yFlDwg/p.png?size=1600x1200&size_mode=3',
                'OnePlus 6T',
                'October 2018',
                {'Type': '6.41-inch', 'Pixel': '2280 x 1080', 'Other': ['QHD+ OLED', 'Gorilla Glass 5']},
                {'Height': '157.5 mm', 'Width': '74.8 mm', 'Depth': '8.2 mm', 'Weight': '185 g'},
                {'Megapixel': '16 MP Wide Angel, 20MP Telephoto', 'Other': ['Exmor RS sensor']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3700 mAh)', 'Other': ['SuperCharge']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 845 chip', 'RAM': '6 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

XiaomiMiMix = Phone(
                'https://previews.dropbox.com/p/thumb/AAS2QtOZunM6k-CniYSaG0PIk6DJ1Q1-YjmPFXYRK29m1k1umWQmy0s-Qq0ZpoBpR6JycnwSnq4TMcx0U9MwZ_T5eP84r_9aVZe2Rsb5T4ZRRGevpZ4cPc-tvvAeBZYcO3Uqp_Eos9erBUNCGHVcgGP8y1O8tr1JVNkJLOIWXilg2zalGIUNBaSePtRTIdg_cSYWxZYm7mpJxUQC2TrvaoKDa8Y5WlTZF6gTiIHMbfDKlQ/p.png?size=1600x1200&size_mode=3',
                'Xiaomi Mi Mix',
                'October 2018',
                {'Type': '6.4-inch', 'Pixel': '2040 x 1080', 'Other': ['Sunlight display', 'Full HD 2040 x 1080p']},
                {'Height': '158.8 mm', 'Width': '81.9 mm', 'Depth': '7.9 mm', 'Weight': '209 g'},
                {'Megapixel': '16 MP', 'Other': ['Two-tone flash', 'Burst mode']},
                {'BatteryLife': '12 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (4400 mAh)', 'Other': ['Quick Charge 3.0']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 821', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

Honor10 = Phone(
                'https://previews.dropbox.com/p/thumb/AATuPYk_FuxGpGIpwz7W-qkTFuAlvYzXGqyT1gbNcByAF5gZ-VXnYZpnEjSMQmFrpj9plANnvbSBY6r-zLgi_H68NvMnN7Xs9F9r70YreDCimzg8yZXeSHZuScLkrZHEZVHWPwoYCRl3Eov41BCrXg9jHTrsYdyZIeVmlS39UIRrb1ZCECSVYi-kue7xfr1nrLuvaYZq7LsUjCuzQAJag6YloLP2LPADk21J9BelGscdPA/p.png?size=1600x1200&size_mode=3',
                'Honor 10',
                'November 2018',
                {'Type': '5.84-inch', 'Pixel': '2280 x 1080', 'Other': []},
                {'Height': '149.6 mm', 'Width': '71.2 mm', 'Depth': '7.7 mm', 'Weight': '153 g'},
                {'Megapixel': '24 MP + 16 MP Dual Camera', 'Other': ['LED Flash']},
                {'BatteryLife': '12 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3400 mAh)', 'Other': ['Wireless Charging', 'SuperCharge']},
                {'OS': 'Android 9', 'Chipset': 'HUAWEI Kirin 980', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

SamsungGalaxyNote9 =  Phone(
                'https://previews.dropbox.com/p/thumb/AATQdvY8Feth-ZPWLy1VsHBfDpeH8XmfnqjJJxGR3WvZz02mQRx0wmjnhCFS1NZ3FsjSJ-89NlinF4VDlMnWO51QCKKd4KljixEdlJM-G4_hh8waasOWATfC0FVDoY-gmIy25K3JhXAsr1wGXe4qs43Rf2cXedCr4Ew2HRNSCwybuFU16Q1v_S2oYqHAXIrn3Hx6y05ysokIPIrTgXDh2TcZYixPcAd0nX6Am1hgMgeafw/p.png?size=1600x1200&size_mode=3',
                'Samsung Galaxy Note 9',
                'August 2018',
                {'Type': '6.4-inch full rectangle, 6.3-inch rounded corners', 'Pixel': '2960 x 1440', 'Other': ['dual edge Super AMOLED', 'Quad HD+', 'S Pen Support']},
                {'Height': '161.9 mm', 'Width': '76.4 mm', 'Depth': '8.8 mm', 'Weight': '201 g'},
                {'Megapixel': '12.0 MP', 'Other': ['Auto Focus', 'Optical Zoom at 2x' , 'Digital Zoom up to 10x']},
                {'BatteryLife': '14 hours', 'BatteryType': 'Built-in rechargeable Li-Polymer battery (4000 mAh)', 'Other': ['Wireless Charging', 'Dash charge']},
                {'OS': 'Android 9', 'Chipset': 'Snapdragon 845 chip', 'RAM': '6 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )

LGG7ThinQ =  Phone(
                'https://previews.dropbox.com/p/thumb/AASEZZiJNUdM9mRF3yE74GYR-nqeHN-JymKRnrEM6ZJwwsAWq9YA5oi9YHkl7qY1REQpl6pILnKx5Ls8oUOzAJNQ8EBAWGZI5b3pH7J0hzVXXT8p5qCeWEQZztGFMcfryLo4U9yaOjlovBX9sqFC09IRpqR20-RK9l53_-zvs3M9UA4iNY3h9wPwSmUdMh7_m1fwUdAgtphV2iCWUS91Nw3KmVey176zVPbIKnhKskoOjA/p.png?size=1600x1200&size_mode=3',
                'LG G7 ThinQ',
                'May 2018',
                {'Type': '6.1-inch', 'Pixel': '3120 x 1440', 'Other': ['LCD with Notch']},
                {'Height': '153.2 mm', 'Width': '71.9 mm', 'Depth': '7.9 mm', 'Weight': '162 g'},
                {'Megapixel': '16 MP Wide Angle', 'Other': ['Rear Flash']},
                {'BatteryLife': '12 hours', 'BatteryType': 'Built-in rechargeable lithium‑ion battery (3000 mAh)', 'Other': ['Wireless Charging', 'Fast Charging']},
                {'OS': 'Android 8', 'Chipset': 'Snapdragon 845 chip', 'RAM': '4 GB'},
                {'MostSoldRanking': '', 'CustomerRanking': ''}
            )
#
# iPhoneXR
# HuaweiMate10Pro
# SonyXperiaXZ3



buf = [iPhoneX, iPhoneXS]

fileObject = open('PhoneDatabase', 'wb')
pickle.dump(buf, fileObject)
fileObject.close()

fileObject = open('PhoneDatabase', 'rb')
buf = pickle.load(fileObject) # List of Phones
fileObject.close()

buf.append(SamsungGalaxyS9)
buf.append(HuaweiMate20Pro)
buf.append(GooglePixel3XL)
buf.append(iPhone8)
buf.append(GooglePixel3)
buf.append(OnePlus5)
buf.append(OnePlus6T)
buf.append(XiaomiMiMix)
buf.append(Honor10)
buf.append(SamsungGalaxyNote9)
buf.append(LGG7ThinQ)

fileObject = open('PhoneDatabase', 'wb')
pickle.dump(buf, fileObject)
fileObject.close()

fileObject = open('PhoneDatabase', 'rb')
buf = pickle.load(fileObject) # List of Phones
fileObject.close()

# for i in buf:
#     print(i.phoneName)
#     print(i.software)

print(iPhoneXS.picture)
