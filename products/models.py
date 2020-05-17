from shop import db
from datetime import datetime, date


class pcBuilds(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=True)

    processor_id = db.Column(db.Integer, db.ForeignKey('addCPU.id'),nullable=True)
    processor = db.relationship('addCPU',backref=db.backref('builds_processor', lazy=True))

    memory_id = db.Column(db.Integer, db.ForeignKey('addRAM.id'),nullable=True)
    memory = db.relationship('addRAM',backref=db.backref('builds_memory', lazy=True))

    storage_id = db.Column(db.Integer, db.ForeignKey('addHDD.id'),nullable=True)
    storage = db.relationship('addHDD',backref=db.backref('builds_storage', lazy=True))

    psu_id = db.Column(db.Integer, db.ForeignKey('addPSU.id'),nullable=True)
    psu = db.relationship('addPSU',backref=db.backref('builds_psu', lazy=True))

    graphics_id = db.Column(db.Integer, db.ForeignKey('add_graphic_card.id'),nullable=True)
    graphics = db.relationship('addGraphicCard',backref=db.backref('builds_graphics', lazy=True))

    motherboard = db.relationship('Addproduct',backref=db.backref('builds_motherboards', lazy=True))
    motherboard_id = db.Column(db.Integer, db.ForeignKey('addproduct.id'),nullable=True)

    aircooler_id = db.Column(db.Integer, db.ForeignKey('add_air_cooling.id'))
    aircooler = db.relationship('addAirCooling',backref=db.backref('builds_aircooling', lazy=True))

    watercooling_id = db.Column(db.Integer, db.ForeignKey('add_water_cooling.id'))
    watercooling = db.relationship('addWaterCooling',backref=db.backref('builds_watercooling', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=True)
    category = db.relationship('Category',backref=db.backref('builds_categories', lazy=True))

    single_url = db.Column(db.String(30))

    image_1 = db.Column(db.String(150), nullable=True, default='image1.jpg')

    def __repr__(self):
        return '<pcBuilds %r>' % self.name
    
class tempBuilds(db.Model):
    id=db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=True)

    processor_id = db.Column(db.Integer, db.ForeignKey('addCPU.id'),nullable=True)
    processor = db.relationship('addCPU',backref=db.backref('tempbuilds_processor', lazy=True))

    memory_id = db.Column(db.Integer, db.ForeignKey('addRAM.id'),nullable=True)
    memory = db.relationship('addRAM',backref=db.backref('tempbuilds_memory', lazy=True))

    storage_id = db.Column(db.Integer, db.ForeignKey('addHDD.id'),nullable=True)
    storage = db.relationship('addHDD',backref=db.backref('tempbuilds_storage', lazy=True))

    psu_id = db.Column(db.Integer, db.ForeignKey('addPSU.id'),nullable=True)
    psu = db.relationship('addPSU',backref=db.backref('tempbuilds_psu', lazy=True))

    graphics_id = db.Column(db.Integer, db.ForeignKey('add_graphic_card.id'),nullable=True)
    graphics = db.relationship('addGraphicCard',backref=db.backref('tempbuilds_graphics', lazy=True))

    motherboard = db.relationship('Addproduct',backref=db.backref('tempbuilds_motherboards', lazy=True))
    motherboard_id = db.Column(db.Integer, db.ForeignKey('addproduct.id'),nullable=True)

    aircooler_id = db.Column(db.Integer, db.ForeignKey('add_air_cooling.id'))
    aircooler = db.relationship('addAirCooling',backref=db.backref('tempbuilds_aircooling', lazy=True))

    watercooling_id = db.Column(db.Integer, db.ForeignKey('add_water_cooling.id'))
    watercooling = db.relationship('addWaterCooling',backref=db.backref('tempbuilds_watercooling', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=True)
    category = db.relationship('Category',backref=db.backref('tempbuilds_categories', lazy=True))

    single_url = db.Column(db.String(30))

    image_1 = db.Column(db.String(150), nullable=True, default='image1.jpg')

    def __repr__(self):
        return '<pcBuilds %r>' % self.name


class Addproduct(db.Model):
    __seachbale__ = ['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    CPU_type = db.Column(db.String(80), nullable=False)
    cpu_socket= db.Column(db.String(30))
    chipset = db.Column(db.String(80), nullable=False)
    mem_slots = db.Column(db.String(80), nullable=False)
    max_mem = db.Column(db.String(80), nullable=False)
    channels = db.Column(db.String(80), nullable=False)
    PCI = db.Column(db.String(500), nullable=False)
    storage = db.Column(db.String(80), nullable=False)
    audio_chipset = db.Column(db.String(80), nullable=False)
    audio_channels = db.Column(db.String(80), nullable=False)
    LAN_chipset = db.Column(db.String(80), nullable=False)
    form_factor = db.Column(db.String(80), nullable=False)
    features = db.Column(db.String(1000), nullable=False)
    single_url = db.Column(db.String(30))
    release_date = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    #price = db.Column(db.Numeric(10,2), nullable=False)
    #discount = db.Column(db.Integer, default=0)
    #stock = db.Column(db.Integer, nullable=False)
    #colors = db.Column(db.Text, nullable=False)
    #discription = db.Column(db.Text, nullable=False)
    #desc = db.Column(db.Text, nullable=False)
    #pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    #CPU_type_id = db.Column(db.Integer, db.ForeignKey('CPU_type.id'), nullable=False)
    #CPU_type = db.relationship('CPU_type', backref=db.backref('CPU_type'), lazy=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))



    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Post %r>' % self.name

class addRAM(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    capacity = db.Column(db.String(30), nullable = False)
    mem_type = db.Column(db.String(30), nullable = False)
    speed = db.Column(db.String(30), nullable = False)
    voltage = db.Column(db.String(30), nullable = False)
    buff_reg = db.Column(db.String(30), nullable = False)
    heatspreader = db.Column(db.String(5), nullable = False)
    features = db.Column(db.String(1000), nullable = False)
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('RAM_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('RAM_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


    def __repr__(self):
        return '<addRAM %r>' % self.name

class addCPU(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    cpu_type = db.Column(db.String(30), nullable = False)
    socket_type = db.Column(db.String(30), nullable = False)
    num_core = db.Column(db.String(30), nullable = False)
    num_threads = db.Column(db.String(30), nullable = False)
    frequency = db.Column(db.String(30), nullable = False)
    l1 = db.Column(db.String(10))
    l2 = db.Column(db.String(10))
    l3 = db.Column(db.String(10))
    Manufacturing_Tech = db.Column(db.String(5), nullable=False)
    mem_type = db.Column(db.String(10), nullable = False)
    mem_channel = db.Column(db.Integer, nullable = False)
    PCI_Revision = db.Column(db.String(10), nullable = False)
    power = db.Column(db.String(10), nullable = False)
    features = db.Column(db.String(1000))
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('CPU_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('CPU_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

class addGraphicCard(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    interface = db.Column(db.String(30), nullable = False)
    Chipset_Manufacturer = db.Column(db.String(30), nullable = False)
    GPU = db.Column(db.String(30), nullable = False)
    Boost_Clock = db.Column(db.String(30), nullable = False)
    Memory_Size = db.Column(db.String(30), nullable = False)
    Memory_Interface = db.Column(db.String(30), nullable = False)
    Memory_Type = db.Column(db.String(10))
    DirectX = db.Column(db.String(10))
    HDMI = db.Column(db.String(10))
    Multi_Monitor = db.Column(db.String(10))
    Display_Port = db.Column(db.String(30))
    max_res = db.Column(db.String(30))
    vr_ready = db.Column(db.String(10))
    cooler =  db.Column(db.String(10))
    power = db.Column(db.String(10), nullable = False)
    req = db.Column(db.String(50), nullable = False)
    power_connector = db.Column(db.String(10))
    single_url = db.Column(db.String(30))
    features = db.Column(db.String(1000), nullable = False)
    dimentions = db.Column(db.String(10), nullable = False)
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('GraphicCard_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('GraphicCard_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


    def __repr__(self):
        return '<addGraphicCard %r>' % self.name

class addCase(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    case_type = db.Column(db.String(30), nullable = False)
    color = db.Column(db.String(30), nullable = False)
    case_material = db.Column(db.String(30), nullable = False)
    power_supply = db.Column(db.String(30), nullable = False)
    Motherboard_Compatibility = db.Column(db.String(30), nullable = False)
    External_525_Drive_Bays = db.Column(db.String(10), nullable = False)
    External_35_Drive_Bays = db.Column(db.String(10))
    External_25_Drive_Bays = db.Column(db.String(10))
    Expansion_Slots = db.Column(db.String(10))
    Front_Ports = db.Column(db.String(10))
    Fan_Options = db.Column(db.String(50))
    Radiator_Options = db.Column(db.String(30))
    Max_GPU_Length= db.Column(db.String(10))
    Max_CPU_Cooler_Height  =  db.Column(db.String(10))
    features  =  db.Column(db.String(1000))
    Dimensions_HxWxD = db.Column(db.String(10), nullable = False)
    Weight = db.Column(db.String(10), nullable = False)
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('Case_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('Case_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

class addPSU(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    PSU_type = db.Column(db.String(30), nullable = False)
    max_power = db.Column(db.String(30), nullable = False)
    fans = db.Column(db.String(30), nullable = False)
    Main_Connector = db.Column(db.String(30), nullable = False)
    rail_12v = db.Column(db.String(30), nullable = False)
    PCI_Express_Connector = db.Column(db.String(10), nullable = False)
    SATA_Power_Connector = db.Column(db.String(10))
    SLI = db.Column(db.String(10))
    Modular = db.Column(db.String(10))
    CrossFire = db.Column(db.String(10))
    Efficiency = db.Column(db.String(50))
    Energy_Efficient = db.Column(db.String(30))
    Input_Voltage= db.Column(db.String(10))
    Input_Frequency_Range  =  db.Column(db.String(10))
    Input_Current = db.Column(db.String(10), nullable = False)
    Output = db.Column(db.String(30), nullable = False)
    MTBF = db.Column(db.String(30), nullable = False)
    Dimensions = db.Column(db.String(30), nullable = False)
    Max_PSU_Length = db.Column(db.String(30), nullable = False)
    features  =  db.Column(db.String(1000))
    connectors  =  db.Column(db.String(100))
    Weight = db.Column(db.String(10), nullable = False)
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('PSU_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('PSU_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<addPSU %r>' % self.name

class addAirCooling(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    cooler_type = db.Column(db.String(30), nullable = False)
    Fan_Size = db.Column(db.String(30), nullable = False)
    Socket_Compatibility = db.Column(db.String(100), nullable = False)
    RPM = db.Column(db.String(30), nullable = False)
    Noise_Level = db.Column(db.String(30), nullable = False)
    Power_Connector = db.Column(db.String(10), nullable = False)
    Color = db.Column(db.String(10))
    LED = db.Column(db.String(10))
    Heatsink_Material = db.Column(db.String(10))
    Fan_Dimensions = db.Column(db.String(10))
    Heatsink_Dimensions = db.Column(db.String(50))
    Weight = db.Column(db.String(30))
    features  =  db.Column(db.String(1000))
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('AirCooler_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('AirCooler_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


    def __repr__(self):
        return '<addAirCooler %r>' % self.name

class addWaterCooling(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    cooler_type = db.Column(db.String(30), nullable = False)
    Block_Compatibility = db.Column(db.String(30), nullable = False)
    Block_Dim = db.Column(db.String(30), nullable = False)
    Pump_Dim = db.Column(db.String(30), nullable = False)
    Pump_Noise = db.Column(db.String(30), nullable = False)
    Radiator_Dim = db.Column(db.String(10), nullable = False)
    Radiator_Material = db.Column(db.String(10))
    Fan_Size = db.Column(db.String(10))
    Fan_Dim = db.Column(db.String(10))
    Fan_RPM = db.Column(db.String(10))
    Fan_Air_Flow = db.Column(db.String(50))
    Fan_Noise = db.Column(db.String(30))
    Fan_Connector = db.Column(db.String(10))
    Fan_Color  =  db.Column(db.String(10))
    Input_Current = db.Column(db.String(10), nullable = False)
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('WaterCooling_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('Water_Cooling_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<addWaterCooling %r>' % self.name

class addHDD(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(30), nullable = False)
    series = db.Column(db.String(30), nullable = False)
    Interface = db.Column(db.String(30), nullable = False)
    Capacity = db.Column(db.String(30), nullable = False)
    RPM = db.Column(db.String(30), nullable = False)
    Cache = db.Column(db.String(30), nullable = False)
    features = db.Column(db.String(30), nullable = False)
    Usage = db.Column(db.String(10), nullable = False)
    Form_Factor = db.Column(db.String(10))
    Height = db.Column(db.String(10))
    Width = db.Column(db.String(10))
    Length = db.Column(db.String(10))
    date_released = db.Column(db.String(20), nullable=False,default=datetime.utcnow)
    single_url = db.Column(db.String(30))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('HDD_categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('HDD_brands', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<addHDD %r>' % self.name

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    image_1 = db.Column(db.String(150),default='image1.jpg')

    def __repr__(self):
        return '<Brand %r>' % self.name
    
class CPU_type(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<CPU_type %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    url = db.Column(db.String(20), unique=True)
    image_1 = db.Column(db.String(150),default='image1.jpg')
    def __repr__(self):
        return '<Catgory %r>' % self.name


db.create_all()