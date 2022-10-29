
class Processor:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modelprocessor = "Processor -> Intel core I5"

class Videocard:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modelvideocard = "Videocard -> GTX Geforce"

class Compdisk_C:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.C_compinfo = "Computer disk C:"
        self.C_compmemory = 800
        self.C_magnitude = "MB"

class Compdisk_D:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.D_compinfo = "Hard disk D:"
        self.D_compmemory = 1
        self.D_magnitude = "Terabit"

class DiskSSD:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ssdinfo = "SSD disk -> SONY SLW-M Series"
        self.ssdmemory = 240
        self.magnitude_ssd = "MB"

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "Resoltion -> 4k"

class Comp_model:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = "Computer -> Asus FXSO4 Series"

class Computer(Display, Processor, Videocard, Compdisk_C, Compdisk_D, DiskSSD, Comp_model):
    def print_info(self):
        print(self.model)
        print(self.modelprocessor)
        print(self.modelvideocard)
        print(self.C_compinfo,self.C_compmemory,self.C_magnitude)
        print(self.D_compinfo,self.D_compmemory,self.D_magnitude)
        print(self.ssdinfo,self.ssdmemory,self.magnitude_ssd)
        print(self.resolution)

Asus = Computer()
Asus.print_info()