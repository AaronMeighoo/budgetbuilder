from __future__ import print_function # In python 2.7
from flask import render_template,session, request,redirect,url_for,flash,current_app
from shop import app,db,photos, search

from .models import Category,Brand,Addproduct,addRAM,addCPU, addGraphicCard, addCase, addHDD,addPSU,pcBuilds, addAirCooling,addWaterCooling,tempBuilds
from .forms import Addproducts, AddRam, AddCpu, addGraphicCARD, addCASE, addBUILD, Tempbuild
import secrets
import os
import random
import re
import sys
import uuid


def brands():
    brands = Brand.query.all()
    return brands

def categories():
    categories = Category.query.all()
    return categories


def cpus():
    cpus = addCPU.query.all()
    return cpus

def builds_drop():
    builds = tempBuilds.query.all()
    return builds

tables = [Addproduct,addRAM,addCPU, addGraphicCard, addCase, addHDD,addPSU,pcBuilds,addAirCooling]
table = random.choice(tables)
@app.route('/')
def home():

    page = request.args.get('page',1, type=int)
    #EDIT!!
    products = table.query.paginate(per_page=8)
    #cpus = table.query.paginate(per_page=2)
    return render_template('products/index.html', products=products,brands=brands(),categories=categories(), builds=builds_drop()) 

@app.route('/brands')
def dispBrand():
    page = request.args.get('page',1, type=int)
    brands = Brand.query.paginate(page=page, per_page=10)
    return render_template('products/dispBrands.html', brands=brands)

@app.route('/components')
def dispComponents():
    cats = Category.query.all()
    #print(cats, file=sys.stderr)
    return render_template('products/components.html', cats=cats)

@app.route('/result')
def result():
    searchword = request.args.get('q')
    #EDIT!!
    products = Addproduct.query.msearch(searchword, fields=['name','max_mem'] , limit=6)
    return render_template('products/result.html',products=products,brands=brands(),categories=categories(), CPU_types = CPU_types())

@app.route('/product/<int:id>')
def single_page_motherboards(id):
    product = Addproduct.query.get_or_404(id)
    return render_template('products/single_page_motherboards.html',product=product,brands=brands(),categories=categories())

@app.route('/cpu/<int:id>')
def single_page_cpus(id):
    product = addCPU.query.get_or_404(id)
    return render_template('products/single_page_cpu.html',product=product,brands=brands(),categories=categories())

@app.route('/ram/<int:id>')
def single_page_rams(id):
    product = addRAM.query.get_or_404(id)
    return render_template('products/single_page_rams.html',product=product,brands=brands(),categories=categories())

@app.route('/GPU/<int:id>')
def single_page_gups(id):
    product = addGraphicCard.query.get_or_404(id)
    return render_template('products/single_page_GPUs.html',product=product,brands=brands(),categories=categories())

@app.route('/PSU/<int:id>')
def single_page_psus(id):
    product = addPSU.query.get_or_404(id)
    return render_template('products/single_page_PSU.html',product=product,brands=brands(),categories=categories())

@app.route('/single_water_cooling/<int:id>')
def single_water_cooling(id):
    product = addWaterCooling.query.get_or_404(id)
    return render_template('products/single_page_PSU.html',product=product,brands=brands(),categories=categories())

@app.route('/single_page_HDD/<int:id>')
def single_page_HDD(id):
    product = addHDD.query.get_or_404(id)
    return render_template('products/single_page_storage.html',product=product,brands=brands(),categories=categories())

@app.route('/single_page_cases/<int:id>')
def single_page_cases(id):
    product = addCase.query.get_or_404(id)
    return render_template('products/single_page_cases.html',product=product,brands=brands(),categories=categories())

@app.route('/single_page/<int:id>')
def single_page(id):
    product = table.query.get_or_404(id)
    return render_template('products/single_page.html',product=product,brands=brands(),categories=categories())

@app.route('/single_page_aircooling/<int:id>')
def single_page_aircooling(id):
    product = addAirCooling.query.get_or_404(id)
    return render_template('products/single_page_aircooling.html',product=product,brands=brands(),categories=categories())

@app.route('/single_page_storage/<int:id>')
def single_page_storage(id):
    product = addAirCooling.query.get_or_404(id)
    return render_template('products/single_page_storage.html',product=product,brands=brands(),categories=categories())

@app.route('/MotherBoards',methods=['GET', 'POST'])
def MotherBoards():
    page = request.args.get('page',1, type=int)
    products = Addproduct.query.paginate(page=page, per_page=5)
    return render_template('products/mother_boards.html',products=products,brands=brands(),categories=categories())

@app.route('/gpus')
def gpus():
    page = request.args.get('page',1, type=int)
    products = addGraphicCard.query.paginate(page=page, per_page=5)
    return render_template('products/gpus.html',products=products,brands=brands(),categories=categories())

@app.route('/PSUs')
def PSUs():
    page = request.args.get('page',1, type=int)
    products = addPSU.query.paginate(page=page, per_page=5)
    return render_template('products/PSUs.html',products=products,brands=brands(),categories=categories())

@app.route('/HDDs')
def HDDs():
    page = request.args.get('page',1, type=int)
    products = addHDD.query.paginate(page=page, per_page=5)
    return render_template('products/harddrives.html',products=products,brands=brands(),categories=categories())

@app.route('/CentralProcessingUnit')
def CentralProcessingUnit():
    page = request.args.get('page',1, type=int)
    cpus = addCPU.query.paginate(page = page, per_page=5)
    return render_template('products/CentralProcessingUnit.html',cpus=cpus,brands=brands(),categories=categories())

@app.route('/cases')
def cases():
    page = request.args.get('page',1, type=int)
    cases = addCase.query.paginate(page = page, per_page=5)
    return render_template('products/Cases.html',cases=cases,brands=brands(),categories=categories())

@app.route('/aircooling')
def aircooling():
    page = request.args.get('page',1, type=int)
    aircooling = addAirCooling.query.paginate(page = page, per_page=5)
    return render_template('products/aircooling.html',aircooling=aircooling,brands=brands(),categories=categories())

@app.route('/watercooling')
def watercooling():
    page = request.args.get('page',1, type=int)
    aircooling = addWaterCooling.query.paginate(page = page, per_page=5)
    return render_template('products/watercooling.html',watercooling=aircooling,brands=brands(),categories=categories())


@app.route('/createBuild')
def createBuild():
    cpus = addCPU.query.paginate(per_page=10)
    return render_template('products/createbuild.html', processors=cpus)


@app.route('/createBuild_1/<int:id>',methods=['GET', 'POST'])
def createBuild_1(id):
    cpu = addCPU.query.get(id)
    socket = cpu.socket_type
    motherboards = Addproduct.query.filter_by(cpu_socket=socket).all()
    id = uuid.uuid1()
    #print(id.hex, file=sys.stderr)
    addBuild = tempBuilds(id=id.hex,single_url="single_page_builds")
    addBuild.processor_id = cpu.id
    db.session.add(addBuild)
    db.session.commit()
    return render_template('products/createbuild_1.html',id=id, mbs=motherboards)

@app.route('/createBuild_2/<int:id>',methods=['GET', 'POST'])
def createBuild_2(id):
    r = []
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    motherboard = Addproduct.query.get(id)
    build.motherboard_id = id
    db.session.add(build)
    db.session.commit()
    memtype = re.split(r'["pin","×",\s]', motherboard.mem_slots)
   # print(build_id, file=sys.stderr)
    rams = addRAM.query.all()
    for ram in rams:
        ramtype = ram.mem_type.split("-")
        if ramtype[0] == memtype[1]:
            r.append(ram)

    return render_template('products/createbuild_2.html', mbs=r, build_id=build_id)

@app.route('/createBuild_3/<int:id>',methods=['GET', 'POST'])
def createBuild_3(id):
    storage = addHDD.query.all()
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    build.memory_id = id
    db.session.add(build)
    db.session.commit()
    return render_template('products/createbuild_3.html',build_id=build_id, mbs=storage)

@app.route('/createBuild_4/<int:id>',methods=['GET', 'POST'])
def createBuild_4(id):
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    build.storage_id = id
    db.session.add(build)
    db.session.commit()
    air = addAirCooling.query.all()
    water = addWaterCooling.query.all()
    return render_template('products/createbuild_4.html',build_id=build_id, airs=air, water=water )

@app.route('/createBuild_5/<int:id>',methods=['GET', 'POST'])
def createBuild_5(id):
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    air = addAirCooling.query.all()
    water = addWaterCooling.query.all()
    for a in air:
        for w in water:
            if id == a.category_id:
                build.aircooler_id=a.id
            elif id == w.category_id:
                build.watercooling_id = w.id

    db.session.add(build)
    db.session.commit()
    psus = addPSU.query.all()
    return render_template('products/createbuild_5.html',build_id=build_id, psus=psus )

@app.route('/createBuild_6/<int:id>',methods=['GET', 'POST'])
def createBuild_6(id):
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    build.psu_id = id
    db.session.add(build)
    db.session.commit()
    gpu = addGraphicCard.query.all()
    return render_template('products/createbuild_6.html',build_id=build_id,gpus=gpu )

@app.route('/createBuild_7/<int:id>',methods=['GET', 'POST'])
def createBuild_7(id):
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    build.graphics_id = id
    db.session.add(build)
    db.session.commit()
    return render_template('products/single_page_builds.html',product=build,brands=brands(),categories=categories() )
'''
@app.route('/commitBuild',methods=['GET', 'POST'])
def commitBuild():
    builds = pcBuilds.query.all()
    build_id = request.args.get('build_id', None)
    build = tempBuilds.query.get(build_id)
    builds = pcBuilds.query.all()
    db.session.add(build)
    db.session.commit()
    return render_template('products/single_page_tempbuilds.html',product=build,brands=brands(),categories=categories() )
'''
@app.route('/builds/<string:id>')
def single_page_builds(id):
    product = tempBuilds.query.get_or_404(id)
    return render_template('products/single_page_builds.html',product=product,brands=brands(),categories=categories())

@app.route('/PCBuilds')
def PCBuilds():
    page = request.args.get('page',1, type=int)
    builds = tempBuilds.query.paginate(page = page, per_page=5)
    return render_template('products/builds.html',products=builds,brands=brands(),categories=categories())

@app.route('/rams')
def rams():
    page = request.args.get('page',1, type=int)
    rams = addRAM.query.paginate(page=page,per_page=5)
    return render_template('products/rams.html',products=rams,brands=brands(),categories=categories())

@app.route('/brand/<int:id>')
def brand(id):
    page = request.args.get('page',1, type=int)
    mb = Addproduct.query.filter_by(brand_id = id).all()
    rams = addRAM.query.filter_by(brand_id = id).all()
    cpus = addCPU.query.filter_by(brand_id=id).all()
    gpus = addGraphicCard.query.filter_by(brand_id=id).all()
    cases = addCase.query.filter_by(brand_id=id).all()
    psus = addPSU.query.filter_by(brand_id=id).all()
    water_cooling = addWaterCooling.query.filter_by(brand_id=id).all()
    HDDs = addHDD.query.filter_by(brand_id=id).all()
    air_coolers = addAirCooling.query.filter_by(brand_id=id).all()
    return render_template('products/brands.html',mb=mb,rams=rams,cpus=cpus,gpus=gpus,cases=cases,psus=psus,water_cooling=water_cooling,hdds=HDDs,air_coolers=air_coolers,brands=brands(),categories=categories())

@app.route('/builds/<int:id>')
def builds(id):
    page = request.args.get('page',1, type=int)
    #get_brand = Brand.query.filter_by(id=id).first_or_404()
    builds = pcBuilds.query.filter_by(category_id=id).paginate(page=page, per_page=8)
    return render_template('products/builds.html',builds=builds,brands=brands(),categories=categories(),get_brand=get_brand)

@app.route('/CPU_type/<int:id>')
def get_CPU_type(id):
    page = request.args.get('page',1, type=int)
    get_CPU_type = CPU_type.query.filter_by(id=id).first_or_404()
    CPU_type = Addproduct.query.filter_by(CPU_type=get_CPU_type).paginate(page=page, per_page=8)
    return render_template('products/index.html',CPU_type=CPU_type,CPU_types=CPU_types(),categories=categories(),get_CPU_type=get_CPU_type)

@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page',1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(page=page, per_page=8)
    return render_template('products/index.html',get_cat_prod=get_cat_prod,brands=brands(),categories=categories(),get_cat=get_cat)


@app.route('/addbrand',methods=['GET','POST'])
def addbrand():
    if request.method =="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand',brands='brands')

@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

#CPU_type start

#CPU_Type end


@app.route('/addcat',methods=['GET','POST'])
def addcat():
    if request.method =="POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'The brand {getcat} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')


@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',updatecat=updatecat)



@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))

#=============builds===================
@app.route('/addPCBuilds',methods=['GET','POST'])
def addPCBuilds():
    form = addBUILD(request.form)
    builds = pcBuilds.query.all()
    aircoolings = addAirCooling.query.all()
    processors = addCPU.query.all()
    memorys = addRAM.query.all()
    storages = addHDD.query.all()
    psus = addPSU.query.all()
    graphicss = addGraphicCard.query.all()
    motherboards = Addproduct.query.all()
    if request.method=="POST":
        name = form.name.data
        processor = request.form.get('processor')
        memory = request.form.get('memory')
        storage = request.form.get('storage')
        psu = request.form.get('psu')
        graphics = request.form.get('graphics')
        motherboard = request.form.get('motherboard')
        category = request.form.get('category')
        aircooling = request.form.get('aircooling')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        single_url = "single_page_builds"
        addbuild = pcBuilds(name=name, processor_id=processor, memory_id=memory, storage_id=storage, psu_id=psu, graphics_id=graphics, motherboard_id=motherboard,category_id=category,image_1=image_1,single_url=single_url, aircooling_id=aircooling)
        db.session.add(addbuild)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('PCBUILDs'))
    return render_template('products/addbuilds.html',processors=processors, memorys=memorys,storages=storages, psus=psus, graphicss=graphicss, motherboards=motherboards, form=form, categories = categories(),getproduct=builds,aircoolings=aircoolings, title='Add a Product')

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    form = Addproducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    #cpu_types = CPU_type.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        model = form.model.data
        chipset = form.chipset.data
        mem_slots = form.mem_slots.data
        channels = form.channels.data
        max_mem = form.max_mem.data
        PCI = form.PCI.data
        storage = form.storage.data
        audio_chipset = form.audio_chipset.data
        audio_channels = form.audio_channels.data
        LAN_chipset = form.LAN_chipset.data
        form_factor = form.form_factor.data
        features = form.features.data
        CPU_type = form.CPU_type.data
        brand = request.form.get('brand')
        single_url = "single_page_motherboards"
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        #EDIT THIS!!!
        addproduct = Addproduct(name=name,model=model,chipset=chipset,mem_slots=mem_slots,channels = channels, max_mem=max_mem,PCI=PCI,storage=storage,audio_chipset=audio_chipset,audio_channels=audio_channels,LAN_chipset=LAN_chipset,form_factor=form_factor,features=features,category_id=category,CPU_type = CPU_type ,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form=form, title='Add a Product', brands=brands,categories=categories )




@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    form = Addproducts(request.form)
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        product.name = form.name.data 
        product.model = form.model.data
        product.CPU_type = form.CPU_type.data
        product.chipset = form.chipset.data 
        product.mem_slots = form.mem_slots.data
        product.max_mem = form.max_mem.data
        product.channels = form.channels.data
        product.PCI = form.PCI.data
        product.storage = form.storage.data
        product.audio_chipset = form.audio_chipset.data
        product.audio_channels = form.audio_channels.data
        product.LAN_chipset = form.LAN_chipset.data
        product.form_factor = form.form_factor.data
        product.features = form.features.data
        #product.release_date = form.release_date.data
        product.category_id = category
        product.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.model.data = product.model
    form.CPU_type.data = product.CPU_type
    form.chipset.data = product.chipset
    form.mem_slots.data = product.mem_slots
    form.max_mem.data = product.max_mem
    form.channels.data = product.channels
    form.PCI.data = product.PCI
    form.storage.data = product.storage
    form.audio_chipset.data = product.audio_chipset
    form.audio_channels.data = product.audio_channels
    form.LAN_chipset.data = product.LAN_chipset
    form.form_factor.data = product.form_factor
    form.features.data = product.features
    #form.release_date.data = product.release_date
    brand = product.brand.name
    category = product.category.name
    return render_template('products/addproduct.html', form=form, title='Update Product',getproduct=product, brands=brands,categories=categories)


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('admin'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))


@app.route('/ADDRAM', methods=['GET','POST'])
def ADDRAM():
    form = AddRam(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    #rdb = addRAM()
    #cpu_types = CPU_type.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        #brand = form.brand.data
        model = form.model.data
        series = form.series.data
        capacity = form.capacity.data
        mem_type = form.mem_type.data
        speed = form.speed.data
        voltage = form.voltage.data
        buff_reg = form.buff_reg.data
        heatspreader = form.heatspreader.data
        features = form.features.data
        #date_released = form.date_released.data
        brand = request.form.get('brand')
        single_url = "single_page_rams"
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        #EDIT THIS!!!
        ADDram = addRAM(name=name,model=model,series=series, capacity = capacity, mem_type = mem_type, speed = speed, voltage = voltage, buff_reg = buff_reg, heatspreader = heatspreader, features=features,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(ADDram)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addram.html', title='Add a Product',form=form, brands=brands,categories=categories )

@app.route('/updateRAM/<int:id>', methods=['GET','POST'])
def updateRAM(id):
    form = AddRam(request.form)
    ram = addRAM.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        ram.name = form.name.data
        #brand = form.brand.data
        ram.model = form.model.data
        ram.series = form.series.data
        ram.capacity = form.capacity.data
        ram.mem_type = form.mem_type.data
        ram.speed = form.speed.data
        ram.voltage = form.voltage.data
        ram.buff_reg = form.buff_reg.data
        ram.heatspreader = form.heatspreader.data
        ram.features = form.features.data
        #ram.date_released = form.date_released.data
        ram.category_id = category
        ram.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + ram.image_1))
                ram.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                ram.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + ram.image_2))
                ram.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                ram.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + ram.image_3))
                ram.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                ram.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('RAMs'))
    form.name.data = ram.name 
    #brand = form.brand.data =
    form.model.data = ram.model 
    form.series.data = ram.series 
    form.capacity.data = ram.capacity
    form.mem_type.data =  ram.mem_type 
    form.speed.data = ram.speed 
    form.voltage.data = ram.voltage 
    form.buff_reg.data = ram.buff_reg 
    form.heatspreader.data = ram.heatspreader 
    form.features.data = ram.features 
    form.date_released.data = ram.date_released 
    brand = ram.brand.name
    category = ram.category.name
    return render_template('products/addram.html', form=form, title='Update RAM', getproduct=ram, brands=brands,categories=categories)

@app.route('/deleteRAM/<int:id>', methods=['POST'])
def deleteRAM(id):
    ram = addRAM.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(ram)
        db.session.commit()
        flash(f'The product {ram.name} was delete from your record','success')
        return redirect(url_for('RAMs'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('RAMs'))

@app.route('/ADDCPU', methods=['GET','POST'])
def ADDCPU():
    form = AddCpu(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    # = addRAM()
    #cpu_types = CPU_type.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        model =  form.model.data
        series =  form.series.data
        cpu_type =  form.cpu_type.data
        socket_type =  form.socket_type.data
        num_core =  form.num_core.data
        num_threads =  form.num_threads.data
        frequency =  form.frequency.data
        l1 =  form.l1.data
        l2 =  form.l2.data
        l3 =  form.l3.data
        Manufacturing_Tech =  form.Manufacturing_Tech.data
        single_url = "single_page_cpus"
        mem_type =  form.mem_type.data
        mem_channel =  form.mem_channel.data
        PCI_Revision =  form.PCI_Revision.data
        power =  form.power.data
        date_released =  form.date_released.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        #EDIT THIS!!!
        ADDcpu = addCPU(name=name,model=model,series=series, cpu_type = cpu_type,socket_type = socket_type, num_core = num_core, num_threads = num_threads, frequency = frequency, l1=l1,l2=l2,l3=l3, Manufacturing_Tech=Manufacturing_Tech,mem_type = mem_type, mem_channel = mem_channel, PCI_Revision = PCI_Revision, power = power, date_released = date_released,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(ADDcpu)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('CPUs'))
    return render_template('products/addcpu.html', title='Add a Product',form=form, brands=brands,categories=categories )

@app.route('/updateCPU/<int:id>', methods=['GET','POST'])
def updateCPU(id):
    form = AddCpu(request.form)
    cpu = addCPU.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        cpu.name = form.name.data
        #brand = form.brand.data
        cpu.model = form.model.data
        cpu.series = form.series.data
        cpu.cpu_type = form.cpu_type.data
        cpu.socket_type = form.socket_type.data
        cpu.num_core = form.num_core.data
        cpu.num_threads = form.num_threads.data
        cpu.frequency = form.frequency.data
        cpu.l1 = form.l1.data
        cpu.l2 = form.l2.data
        cpu.l3 = form.l3.data
        cpu.Manufacturing_Tech = form.Manufacturing_Tech.data
        cpu.mem_type = form.mem_type.data
        cpu.mem_channel = form.mem_channel.data
        cpu.PCI_Revision = form.PCI_Revision.data
        cpu.power = form.power.data
        #cpu.date_released = form.date_released.data
        cpu.category_id = category
        cpu.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_1))
                cpu.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                cpu.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_2))
                cpu.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                cpu.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_3))
                cpu.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                cpu.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('CPUs'))
    form.name.data = cpu.name
    #brand = form.brand.data
    form.model.data = cpu.model
    form.series.data = cpu.series
    form.cpu_type.data = cpu.cpu_type
    form.socket_type.data = cpu.socket_type
    form.num_core.data = cpu.num_core
    form.num_threads.data = cpu.num_threads
    form.frequency.data = cpu.frequency
    form.l1.data = cpu.l1
    form.l2.data = cpu.l2
    form.l3.data = cpu.l3
    form.Manufacturing_Tech.data = cpu.Manufacturing_Tech
    form.mem_type.data = cpu.mem_type
    form.mem_channel.data = cpu.mem_channel
    form.PCI_Revision.data = cpu.PCI_Revision
    form.power.data = cpu.power
    brand = cpu.brand.name
    category = cpu.category.name
    return render_template('products/addcpu.html', form=form, title='Update cpu', getproduct=cpu, brands=brands,categories=categories)

@app.route('/deleteCPU/<int:id>', methods=['POST'])
def deleteCPU(id):
    cpu = addCPU.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + cpu.image_3))
        except Exception as e:
            print(e)
        db.session.delete(cpu)
        db.session.commit()
        flash(f'The product {cpu.name} was delete from your record','success')
        return redirect(url_for('CPUs'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('CPUs'))

#ADDGraphicCard
@app.route('/ADD_GRAPHICCARD', methods=['GET','POST'])
def ADD_GRAPHICCARD():
    form = addGraphicCARD(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    # = addRAM()
    #cpu_types = CPU_type.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        model = form.model.data
        interface = form.interface.data
        Chipset_Manufacturer = form.Chipset_Manufacturer.data
        GPU = form.GPU.data
        Boost_Clock = form.Boost_Clock.data
        Memory_Size = form.Memory_Size.data
        Memory_Interface = form.Memory_Interface.data
        Memory_Type =form.Memory_Type.data
        DirectX = form.DirectX.data
        HDMI =form.HDMI.data
        Multi_Monitor =form.Multi_Monitor.data
        Display_Port = form.Display_Port.data
        max_res = form.max_res.data
        vr_ready =form.vr_ready.data
        cooler = form.cooler.data
        Chipset_Manufacturer =form.Chipset_Manufacturer.data
        power = form.power.data
        req = form.req.data
        power_connector =form.power_connector.data
        features = form.features.data
        dimentions = form.dimentions.data
        date_released =  form.date_released.data
        single_url = "single_page_GPUs"
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        #EDIT THIS!!!
        ADDGraphicCard = addGraphicCard(name=name,model=model,interface=interface, Chipset_Manufacturer = Chipset_Manufacturer,GPU = GPU, Boost_Clock = Boost_Clock, Memory_Size = Memory_Size, Memory_Type=Memory_Type,Memory_Interface=Memory_Interface,DirectX=DirectX,HDMI=HDMI, Multi_Monitor=Multi_Monitor,Display_Port = Display_Port, max_res = max_res, vr_ready = vr_ready, cooler = cooler,power = power, req=req, power_connector=power_connector,features=features ,dimentions = dimentions, date_released = date_released,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(ADDGraphicCard)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('GPUs'))
    return render_template('products/addGraphicCard.html', title='Add a Product',form=form, brands=brands,categories=categories )

@app.route('/updateGPU/<int:id>', methods=['GET','POST'])
def updateGPU(id):
    form = addGraphicCARD(request.form)
    gpu = addGraphicCard.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        gpu.name = form.name.data
        #brand = form.brand.data
        gpu.model = form.model.data
        gpu.interface = form.interface.data
        gpu.Chipset_Manufacturer = form.Chipset_Manufacturer.data
        gpu.GPU = form.GPU.data
        gpu.Boost_Clock = form.Boost_Clock.data
        gpu.Memory_Size = form.Memory_Size.data
        gpu.Memory_Interface = form.Memory_Interface.data
        gpu.Memory_Type = form.Memory_Type.data
        gpu.DirectX = form.DirectX.data
        gpu.HDMI = form.HDMI.data
        gpu.Multi_Monitor = form.Multi_Monitor.data
        gpu.Display_Port = form.Display_Port.data
        gpu.max_res = form.max_res.data
        gpu.vr_ready = form.vr_ready.data
        gpu.cooler = form.cooler.data
        gpu.power = form.power.data
        gpu.req = form.req.data
        gpu.power_connector = form.power_connector.data
        gpu.features = form.features.data
        gpu.dimentions = form.dimentions.data
        #gpu.date_released = form.date_released.data
        gpu.category_id = category
        gpu.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_1))
                gpu.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                gpu.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_2))
                gpu.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                gpu.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_3))
                gpu.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                gpu.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('GPUs'))
    form.name.data=gpu.name
    #brand = form.brand.data
    form.name.data=gpu.model = form.model.data
    form.interface.data=gpu.interface
    form.Chipset_Manufacturer.data=gpu.Chipset_Manufacturer
    form.GPU.data=gpu.GPU
    form.Boost_Clock.data=gpu.Boost_Clock
    form.Memory_Size.data=gpu.Memory_Size
    form.Memory_Interface.data= gpu.Memory_Interface  
    form.Memory_Type.data= gpu.Memory_Type
    form.DirectX.data=gpu.DirectX
    form.HDMI.data=gpu.HDMI
    form.Multi_Monitor.data=gpu.Multi_Monitor
    form.Display_Port.data=gpu.Display_Port
    form.max_res.data=gpu.max_res
    form.vr_ready.data=gpu.vr_ready
    form.cooler.data=gpu.cooler
    form.power.data=gpu.power
    form.req.data=gpu.req
    form.power_connector.data= gpu.power_connector
    form.features.data=gpu.features
    form.dimentions.data=gpu.dimentions
    gpu.brand.name=brand
    gpu.category.name=category
    return render_template('products/addGraphicCard.html', form=form, title='Update gpu', getproduct=gpu, brands=brands,categories=categories)

@app.route('/deletegpu/<int:id>', methods=['POST'])
def deletegpu(id):
    gpu = addGraphicCard.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + gpu.image_3))
        except Exception as e:
            print(e)
        db.session.delete(gpu)
        db.session.commit()
        flash(f'The product {gpu.name} was delete from your record','success')
        return redirect(url_for('GPUs'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('GPUs'))


#ADDCase
@app.route('/ADD_CASE', methods=['GET','POST'])
def ADD_CASE():
    form = addCASE(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    # = addRAM()
    #cpu_types = CPU_type.query.all()
    if request.method=="POST"and 'image_1' in request.files:
        name = form.name.data
        model = form.model.data
        series = form.series.data
        case_type = form.case_type.data
        color = form.color.data
        case_material = form.case_material.data
        power_supply = form.power_supply.data
        Motherboard_Compatibility = form.Motherboard_Compatibility.data
        External_525_Drive_Bays = form.External_525_Drive_Bays.data
        External_35_Drive_Bays = form.External_35_Drive_Bays.data
        External_25_Drive_Bays = form.External_25_Drive_Bays.data
        Expansion_Slots = form.Expansion_Slots.data
        Front_Ports = form.Front_Ports.data
        Fan_Options = form.Fan_Options.data
        Radiator_Options = form.Radiator_Options.data
        Max_GPU_Length= form.Max_GPU_Length.data
        Max_CPU_Cooler_Height  =  form.Max_CPU_Cooler_Height.data
        features  =  form.features.data
        Dimensions_HxWxD = form.Dimensions_HxWxD.data
        Weight = form.Weight.data
        date_released = form.date_released.data
        brand = request.form.get('brand')
        single_url = "single_page_cases"
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        #EDIT THIS!!!
        ADDCase = addCase(name=name,model=model,series=series, case_type = case_type,color = color, case_material = case_material, power_supply = power_supply, Motherboard_Compatibility=Motherboard_Compatibility,External_525_Drive_Bays=External_525_Drive_Bays,External_35_Drive_Bays=External_35_Drive_Bays,External_25_Drive_Bays=External_25_Drive_Bays, Expansion_Slots=Expansion_Slots,Front_Ports = Front_Ports, Fan_Options = Fan_Options, Radiator_Options = Radiator_Options, Max_GPU_Length = Max_GPU_Length,Max_CPU_Cooler_Height = Max_CPU_Cooler_Height, Dimensions_HxWxD=Dimensions_HxWxD, Weight=Weight,features=features, date_released = date_released,category_id=category,brand_id=brand,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(ADDCase)
        flash(f'The product {name} was added in database','success')
        db.session.commit()
        return redirect(url_for('Case'))
    return render_template('products/addCases.html', title='Add a Product',form=form, brands=brands,categories=categories )

@app.route('/updateCase/<int:id>', methods=['GET','POST'])
def updateCase(id):
    form = addCASE(request.form)
    case = addGraphicCard.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    if request.method =="POST":
        case.name = form.name.data
        #brand = form.brand.data
        case.model = form.model.data
        case.series = form.series.data
        case.case_type = form.case_type.data
        case.color = form.color.data
        case.case_material = form.case_material.data
        case.power_supply = form.power_supply.data
        case.Motherboard_Compatibility = form.Motherboard_Compatibility.data
        case.External_525_Drive_Bays = form.External_525_Drive_Bays.data
        case.External_35_Drive_Bays = form.External_35_Drive_Bays.data
        case.External_25_Drive_Bays = form.External_25_Drive_Bays.data
        case.Expansion_Slots = form.Expansion_Slots.data
        case.Front_Ports = form.Front_Ports.data
        case.Fan_Options = form.Fan_Options.data
        case.Radiator_Options = form.Radiator_Options.data
        case.Max_GPU_Length = form.Max_GPU_Length.data
        case.Max_CPU_Cooler_Height = form.Max_CPU_Cooler_Height.data
        case.req = form.req.data
        case.features = form.features.data
        case.Dimensions_HxWxD = form.Dimensions_HxWxD.data
        case.Weight = form.Weight.data
        #case.date_released = form.date_released.data
        case.category_id = category
        case.brand_id = brand
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_1))
                case.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                case.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_2))
                case.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                case.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_3))
                case.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                case.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        flash('The product was updated','success')
        db.session.commit()
        return redirect(url_for('cases'))
    form.name.data=case.name
    #brand = form.brand.data
    form.name.data=case.model = form.model.data
    form.interface.data=case.interface
    form.Chipset_Manufacturer.data=case.Chipset_Manufacturer
    form.case.data=case.case
    form.Boost_Clock.data=case.Boost_Clock
    form.Memory_Size.data=case.Memory_Size
    form.Memory_Interface.data= case.Memory_Interface  
    form.Memory_Type.data= case.Memory_Type
    form.DirectX.data=case.DirectX
    form.HDMI.data=case.HDMI
    form.Multi_Monitor.data=case.Multi_Monitor
    form.Display_Port.data=case.Display_Port
    form.max_res.data=case.max_res
    form.vr_ready.data=case.vr_ready
    form.cooler.data=case.cooler
    form.power.data=case.power
    form.req.data=case.req
    form.power_connector.data= case.power_connector
    form.features.data=case.features
    form.dimentions.data=case.dimentions
    case.brand.name=brand
    case.category.name=category
    return render_template('products/addGraphicCard.html', form=form, title='Update case', getproduct=case, brands=brands,categories=categories)

@app.route('/deleteCase/<int:id>', methods=['POST'])
def deleteCase(id):
    case = addGraphicCard.query.get_or_404(id)
    if request.method =="POST":
        try:
            os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_1))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_2))
            os.unlink(os.path.join(current_app.root_path, "static/images/" + case.image_3))
        except Exception as e:
            print(e)
        db.session.delete(case)
        db.session.commit()
        flash(f'The product {case.name} was delete from your record','success')
        return redirect(url_for('cases'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('cases'))