class Phone():
    def __init__(self, picture, phoneName, launchDate, display, sizeWeight, camera, powerBattery, software, ranks):
        self._picture = picture # link or directory of the picture
        self._phoneName = phoneName
        self._launchDate = launchDate
        self._display = display # {Type, Pixel, Other}
        self._sizeWeight = sizeWeight # {Height, Width, Depth, Weight}
        self._camera = camera # {Megapixel, Other}
        self._powerBattery = powerBattery # {BatteryLife, BatteryType, Other}
        self._software = software # {OS, Chipset}
        self._ranks = ranks # {MostSoldRanking, CustomerRanking}

    @property
    def picture(self):
        return self._picture

    @property
    def phoneName(self):
        return self._phoneName

    @property
    def launchDate(self):
        return self._launchDate

    @property
    def display(self):
        return self._display

    @property
    def sizeWeight(self):
        return self._sizeWeight

    @property
    def camera(self):
        return self._camera

    @property
    def powerBattery(self):
        return self._powerBattery

    @property
    def software(self):
        return self._software

    @property
    def ranks(self):
        return self._ranks

    @property
    def spec(self):
        return self._software

# Example
# iPhoneXS =  Phone(
#                 'iPhone XS',
#                 'September 2018',
#                 {Type: 'Super Retina HD display', Pixel: '2436 x 1125', Other: ['HDR Display', 'True Tone Display']},
#                 {Height: '150.9 mm', Width: '70.9 mm', Depth: '7.7 mm', Weight: '177 g'},
#                 {Megapixel: 'Dual 12-megapixel wide-angle', Other: ['Dual optical image stabilisation', 'Portrait mode with advanced bokeh and Depth Control']},
#                 {BatteryLife: '12 hours' ,BatteryType: 'Built-in rechargeable lithium‑ion battery', Other: ['Wireless Charging', 'Fast Charging']},
#             )
