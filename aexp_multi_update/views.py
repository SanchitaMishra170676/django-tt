from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

lis = [
    {'waveinfo': 'wave1','server_name':'hvidlipaw01','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave1','server_name':'hwidlipaw02','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave1','server_name':'hvidlipaw03','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave2','server_name':'hoidlipaw04','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave2','server_name':'hoidlipaw05','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave2','server_name':'hoidlipaw06','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave3','server_name':'hvidlipaw07','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave3','server_name':'hsidlipaw08','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave3','server_name':'hsidlipaw09','app_acronym':'abc','dashboard_mnt':'mar'},
    {'waveinfo': 'wave3','server_name':'hvidlipaw10','app_acronym':'abc','dashboard_mnt':'mar'},
    ]

lis_update=[]
msg=[]

def index(request):
    lis_update.clear()
    msg.clear()
    if request.method =='POST':
        type= request.POST['itype']
        if type == '1':
            new_wave = request.POST['new_wave']
            for i in lis:
                sname=i.get('server_name')
                try:
                    checkbox = request.POST[sname]
                    print(checkbox)
                    if checkbox == "on":
                        i.update({'waveinfo':new_wave})
                        update_rec= {'waveinfo': i.get('waveinfo'),'server_name':i.get('server_name'),'app_acronym':i.get('app_acronym'),'dashboard_mnt':i.get('dashboard_mnt')}
                        lis_update.append(update_rec)
                except:
                    pass
        elif type=='2':
            details = request.POST['details']
            details= details.replace(',',' ')
            str= details.split()
            if len(str) % 2 != 0:
                messages.error(request,"Kindly enter all the wave values for servers")
                print("msg")
                context = {'lis':lis, 'ulis':lis_update}
                return render(request,'index.html',context)
            i=0
            while i<len(str):
                server_name= str[i]
                if i+1 < len(str):
                    wave_name= str[i+1]
                    i+=2
                found= False
                for li in lis:
                    s_name= li.get('server_name')
                    if s_name== server_name:
                        found=True
                        li.update({'waveinfo':wave_name})
                        update_rec= {'waveinfo': li.get('waveinfo'),'server_name':li.get('server_name'),'app_acronym':li.get('app_acronym'),'dashboard_mnt':li.get('dashboard_mnt')}
                        lis_update.append(update_rec)
                        break
                if found==False:
                    msg.append(server_name)
            if len(msg)>0:
                s="Following input servers had no match: "
                for el in msg:
                    s += el +" "                
                messages.error(request,s)
            
    context = {'lis':lis, 'ulis':lis_update}
    return render(request,'index.html',context)