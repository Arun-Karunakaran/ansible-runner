#! /usr/bin/ptyhon3

import os,re,sys
from itertools import combinations
import ansible_runner
from configparser import ConfigParser

config = ConfigParser()
config.read('adhocvars.ini')
config1 = ConfigParser()
config1.read('ansible.cfg')
ANSIBLE_PROJ_PLATFORM_WINDOWS = os.environ.get('ANSIBLE_PROJ_PLATFORM_WINDOWS')
ANSIBLE_PROJ_ROOT_DIR = os.environ.get('ANSIBLE_PROJ_ROOT_DIR')
pbookname = 'main.yml'
pbookfilepath = os.path.join(ANSIBLE_PROJ_PLATFORM_WINDOWS,pbookname)


def get_filepath(p, v, o):
    
    if p == 'OR' or p == 'LNR':
        project = 'OpenROAD'
        flpth = '\\usau-engfs01\\staging\\' + project + '\\' + 'OR' + '_' + v + '\\' + o
        return flpth
    else:
        pass

def get_mntpath(p, v, o):
    
    if p == 'OR' or p == 'LNR':
        project = 'OpenROAD'
        mntpath = '/mnt/' + project + '/' + 'OR' + '_' + v + '/' + o + '/'
        return mntpath
    else:
        pass

def get_patchdirnames(p, v, o):

    for root, dirnames, files in os.walk(get_mntpath(p, v, o)):
        r = re.compile("(^p[0-9][0-9][0-9][0-9][0-9]$)")
        newdirnames = list(filter(r.match, dirnames))
        return newdirnames

def get_patchsorteddirnames(p, v, o, val):
    '''
    Default argument value, val is : False
    '''
    pids = []
    for e in get_patchdirnames(p, v, o):
        patchid = e.split('p')[1]
        pids.append(patchid)
    return (['p' + p for p in sorted(pids, reverse=val)])

def get_latestpatch(p, v, o):
    
    previous_patches = get_patchsorteddirnames(p, v, o, False)
    return previous_patches.pop()

def get_previouspatches(p, v, o):

    previous_patches = get_patchsorteddirnames(p, v, o, False)
    previous_patches.pop()
    return previous_patches

def get_previouspatch(p, v, o):
    
    previous_patches = get_previouspatches(p, v, o)
    return previous_patches.pop()

def getpatchids_combi_tolatest(p, v, o):
    
    previouspatches = get_patchsorteddirnames(p, v, o, False)
    latestpatch = previouspatches.pop()
    patchesdict = {pp : latestpatch for pp in previouspatches}
    patchitems = list(patchesdict.items())
    return patchitems

def getcurr_install_patchlist(p, v, o):

    for i in range(0 , len(getpatchids_combi_tolatest(p ,v , o))):
        yield getpatchids_combi_tolatest(p ,v , o)[i][0];

def getcurr_upgrade_patchlist(p, v, o):
    
    for i in range(0 , len(getpatchids_combi_tolatest(p ,v , o))):
        yield getpatchids_combi_tolatest(p ,v , o)[i][1];

def getpatchids_all_combi(p, v, o, condition):

    if condition == 'upgrade':
        allpatches = get_patchsorteddirnames(p, v, o,False)
        allcombi = []
        for subset in list(combinations(allpatches, 2)):
            allcombi.append(subset)
        return allcombi
    elif condition == 'downgrade':
        allpatches = get_patchsorteddirnames(p, v, o,True)
        allcombi = []
        for subset in list(combinations(allpatches, 2)):
            allcombi.append(subset)
        return allcombi

def getcurr_install_patchlist_all(p, v, o, condition):
    
    for i in range(0 , len(getpatchids_all_combi(p ,v , o, condition))):
        yield getpatchids_all_combi(p ,v , o, condition)[i][0];

def getcurr_upgrade_patchlist_all(p, v, o, condition):
    
    for i in range(0 , len(getpatchids_all_combi(p ,v , o, condition))):
        yield getpatchids_all_combi(p ,v , o, condition)[i][1];

def get_filepath_currpatch(p, v, o, func):

    flpth_currpatch = get_filepath(p ,v, o) + '\\' + '{}'.format(func)
    return flpth_currpatch

def get_mntpath_currpatch(p, v, o, func):
  
    mntcurrpath = get_mntpath(p, v, o) + '{}'.format(func)
    return mntcurrpath

def get_filenm_currpatch(p, v, o, func):

    for root, dirnames, files in os.walk(get_mntpath_currpatch(p, v, o, func)):
        if p == 'OR':
            r = re.compile("(^open.+(?:com|p[0-9][0-9][0-9][0-9][0-9])-a.zip$)") 
            currfilenm = list(filter(r.match, files))
            return currfilenm[0]
            break
        elif p == 'LNR':
            r = re.compile("(^loadn.+(?:com|p[0-9][0-9][0-9][0-9][0-9])-a.zip$)") 
            currfilenm = list(filter(r.match, files))
            return currfilenm[0]
            break
        else:
            pass

def set_hostname(limithosts):

    config.set('adhocvars', 'hostnames', '{}'.format(limithosts))
    with open('adhocvars.ini', 'w') as configfile:
        config.write(configfile)

def set_curr_filepath(p, v, o, func):
    
    currpath = get_filepath_currpatch(p, v, o, func)
    config.set('adhocvars', 'filepath', '{}'.format(currpath))
    with open('adhocvars.ini', 'w') as configfile:
        config.write(configfile)        

def set_curr_filename(p, v, o, func):

    currflnm = get_filenm_currpatch(p, v, o, func)
    config.set('adhocvars', 'filename', '{}'.format(currflnm))
    with open('adhocvars.ini', 'w') as configfile:
        config.write(configfile)        

def setvars_install(product, version, feature):
    
    if product == 'OR' and version == '11.2.0' and feature == 'sanet':
        config.set('adhocvars', 'tags', 'or, or112, install')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, lnr')
        config.set('adhocvars','feature','sanet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)       
    elif product == 'OR' and version == '11.2.0' and feature == 'sanetruntime':
        config.set('adhocvars', 'tags', 'or, or112, install')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, lnr')
        config.set('adhocvars','feature','sanetruntime')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile) 
    elif product == 'LNR' and version == '11.2.0' and feature == 'sanet':
        config.set('adhocvars', 'tags', 'lnr, lnr112, install')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, or')
        config.set('adhocvars','feature','sanet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)       
    elif product == 'LNR' and version == '11.2.0' and feature == 'nonet':
        config.set('adhocvars', 'tags', 'lnr, lnr112, install')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, or')
        config.set('adhocvars','feature','nonet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile) 
    else:
        raise ValueError ("Pass correct values as input")
    
def setvars_upgrade(product, version, feature):

    if product == 'OR' and version == '11.2.0' and feature == 'sanet':
        config.set('adhocvars', 'tags', 'or, or112, upgrade')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, lnr, cleaninstall')
        config.set('adhocvars','feature','sanet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)
    elif product == 'OR' and version == '11.2.0' and feature == 'sanetruntime':
        config.set('adhocvars', 'tags', 'or, or112, upgrade')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, lnr, cleaninstall')
        config.set('adhocvars','feature','sanetruntime')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)
    elif product == 'LNR' and version == '11.2.0' and feature == 'sanet':
        config.set('adhocvars', 'tags', 'lnr, lnr112, upgrade')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, or, cleaninstall')
        config.set('adhocvars','feature','sanet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)
    elif product == 'LNR' and version == '11.2.0' and feature == 'nonet':
        config.set('adhocvars', 'tags', 'lnr, lnr112, upgrade')
        config.set('adhocvars', 'skiptags', 'debug, installoptions, or, cleaninstall')
        config.set('adhocvars','feature','nonet')
        with open('adhocvars.ini', 'w') as configfile:
            config.write(configfile)
    else:
        raise ValueError ("Pass correct values as input")


# def setconfigskiptags(arg):

#     config1.set('tags', 'skip', '{}'.format(arg))
#     with open('ansible.cfg', 'w') as ansiblecfg:
#         config1.write(ansiblecfg)
    

# def setconfigtags(arg):
    
#     config1.set('tags', 'run', '{}'.format(arg))
#     with open('ansible.cfg', 'w') as ansiblecfg:
#         config1.write(ansiblecfg)


# if __name__ == '__main__':
#     set_hostname('usau-or-dlw10')
#    get_patchdirnames('OR', '11.2.0', 'a64.win')
#     geninstall = getcurr_install_patchlist_all('OR', '11.2.0', 'a64.win', 'upgrade')
#     genupgrade = getcurr_upgrade_patchlist_all('OR', '11.2.0', 'a64.win', 'upgrade')
#     for i in range(0, len(getpatchids_all_combi('OR', '11.2.0', 'a64.win', 'upgrade'))):
#         print(next(geninstall) + ':' + next(genupgrade))
    