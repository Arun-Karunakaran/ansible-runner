#! /usr/bin/ptyhon3

import os, sys, getopt
import ansible_runner
from runnerapi import *

def usage():
    """

    usage: runner.py [-h ] 
    
    eg: runner.py --install_latestpatch -p OR -v 11.2.0 -o a64.win -f sanet

    mandatory args:
        [--install_latestpatch | --install_previouspatch | --upgrade_tolatestpatch | 
        --install_allpreviouspatches | --install_allpatches | 
        --upgradeall_to_latestpatch | --upgrade_allcombination ]
        {-p -v -o -f | --project --version --os --feature }

        Arguments:                  Description:                                        Purpose: 
        ----------                  ------------                                        ---------
        install_latestpatch         installs only the latest patch in staging           deploy/test
        install_previouspatch       installs only the previous patch in staging         deploy/test
        upgrade_tolatestpatch       upgrades a patch to latest patch                    deploy/test
        install_allpreviouspatches  installs all previous patches                       test
        install_allpatches          installs all patches                                test
        upgrade_alltolatestpatch    upgrades all patches to latest patch                test
        upgrade_allcombination      upgrades all patches with all combinations possible test
        project                     specifies product name OR, LNR or EA
        version                     specify product version 11.2.0 | 11.3.0 | 11.4.0
        os                          specify platform specific patch
        feature                     specify product feature to be installed/upgraded 
                                    example: sanet, sanetruntime
        help                        Show this help

    optional arguments:
        -h, --help            show this help message and exit

    returns:
        success message

    """

def main():

    opts , args = getopt.getopt(sys.argv[2:], "p:v:o:f:l:", \
    ["project=", "version=", "os=", "feature=", "limithosts="])
    for opt , arg in opts:
        if opt in ("-p", "--project"):
            p = arg
        elif opt in ("-v", "--version"):
            v = arg
        elif opt in ("-o", "--os"):
            o = arg        
        elif opt in ("-f", "--feature"):
            f = arg
        elif opt in ("-l", "--limithosts"):
            l = arg
        elif opt not in ("-p", "-v", "-o", "-f", "-l"):
            print(usage.__doc__)
            sys.exit() 
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print(usage.__doc__)
        sys.exit() 
    elif sys.argv[1] == "--install_latestpatch":
        runinstall_latestpatch(p ,v ,o, f, l)
    elif sys.argv[1] == "--install_previouspatch":
        runinstall_previouspatch(p ,v ,o, f, l)
    elif sys.argv[1] == "--upgrade_tolatestpatch":
        runupgrade_tolatestpatch(p ,v ,o, f, l)
    elif sys.argv[1] == "--install_allpreviouspatches":
        runinstall_all_previouspatch(p ,v ,o, f, l)
    elif sys.argv[1] == "--install_allpatches":
        runinstall_all_patches(p ,v ,o, f, l)
    elif sys.argv[1] == "--upgrade_alltolatestpatch":
        runupgrade_all_tolatestpatch(p ,v ,o, f, l)
    elif sys.argv[1] == "--upgrade_allcombination":
        runupgrade_all_combi(p ,v ,o, f, l, 'upgrade')

def run_current():
    
    extravars = '{' + \
    "'{}'".format('as_user') + ':' + \
    "'{}'".format(config.get('adhocvars','as_user').strip()) + ',' + \
    "'{}'".format('filepath') + ':' + \
    "'{}'".format(config.get('adhocvars','filepath').strip()) + ',' + \
    "'{}'".format('filename') + ':' + \
    "'{}'".format(config.get('adhocvars','filename').strip()) + ',' + \
    "'{}'".format('feature') + ':' + \
    "'{}'".format(config.get('adhocvars','feature').strip()) + '}'
    out, err, rc = ansible_runner.run_command(
        executable_cmd='ansible-playbook', 
        cmdline_args=['{}'.format(pbookfilepath), '-i', 
        'inventory', '-v', '-l', '{}'.format(config.get('adhocvars','hostnames').strip()), 
        '-e', "{}".format(extravars), 
        '--tags', '{}'.format(config.get('adhocvars','tags').strip()), 
        '--skip-tags', '{}'.format(config.get('adhocvars','skiptags').strip()) 
        ],
        input_fd=sys.stdin,
        output_fd=sys.stdout,
        error_fd=sys.stderr,
        private_data_dir='{}'.format(ANSIBLE_PROJ_ROOT_DIR)
    )
    print("rc: {}".format(rc))
    print("out: {}".format(out))
    print("err: {}".format(err))

def runinstall_latestpatch(p ,v ,o, f, l):

    func = get_latestpatch(p, v, o)
    set_curr_filepath(p, v, o, func)
    set_curr_filename(p, v, o, func)
    setvars_install(p, v, f)
    set_hostname(l)
    run_current()

def runinstall_previouspatch(p ,v ,o, f,l):

    func = get_previouspatch(p, v, o)
    set_curr_filepath(p, v, o, func)
    set_curr_filename(p, v, o, func)
    setvars_install(p, v, f)
    set_hostname(l)
    run_current()

def runupgrade_tolatestpatch(p ,v ,o, f,l):
    
    func = get_latestpatch(p, v, o)
    set_curr_filepath(p, v, o, func)
    set_curr_filename(p, v, o, func)
    setvars_upgrade(p, v, f)
    set_hostname(l)
    run_current()

def runinstall_all_previouspatch(p ,v ,o, f,l):
    
    geninstall = getcurr_install_patchlist(p, v, o)
    for i in range(0 , len(getpatchids_combi_tolatest(p ,v , o))):      
        currpatchinstall = next(geninstall)
        set_curr_filepath(p, v, o, currpatchinstall)
        set_curr_filename(p, v, o, currpatchinstall)
        setvars_install(p, v, f)
        set_hostname(l)
        run_current()

def runinstall_all_patches(p ,v ,o, f, l):

    runinstall_all_previouspatch(p, v, o, f, l)
    runinstall_latestpatch(p, v, o, f, l)

def runupgrade_all_tolatestpatch(p ,v ,o, f, l):

    geninstall = getcurr_install_patchlist(p, v, o)
    genupgrade = getcurr_upgrade_patchlist(p, v, o)
    for i in range(0 , len(getpatchids_combi_tolatest(p ,v , o))):      
        currpatchinstall = next(geninstall)
        set_curr_filepath(p, v, o, currpatchinstall)
        set_curr_filename(p, v, o, currpatchinstall)
        setvars_install(p, v, f)
        set_hostname(l)
        run_current()
        currpatchupgrade = next(genupgrade)
        set_curr_filepath(p, v, o, currpatchupgrade)
        set_curr_filename(p, v, o, currpatchupgrade)
        setvars_upgrade(p, v, f)
        set_hostname(l)
        run_current()

def runupgrade_all_combi(p ,v ,o, f, l, condition):
    
    geninstall = getcurr_install_patchlist_all(p, v, o, condition)
    genupgrade = getcurr_upgrade_patchlist_all(p, v, o, condition)
    for i in range(0 , len(getpatchids_all_combi(p ,v , o, condition))):     
        currpatchinstall = next(geninstall)
        set_curr_filepath(p, v, o, currpatchinstall)
        set_curr_filename(p, v, o, currpatchinstall)
        setvars_install(p, v, f)
        set_hostname(l)
        run_current()
        currpatchupgrade = next(genupgrade)
        set_curr_filepath(p, v, o, currpatchupgrade)
        set_curr_filename(p, v, o, currpatchupgrade)
        setvars_upgrade(p, v, f)
        set_hostname(l)
        run_current()

def _buildadhocvars():
    
    file1 = open('adhocvars.ini', "w")
    file1.write("[adhocvars]\n")
    file1.close()
    file1 = open('adhocvars.ini', "a+")
    file1.write("hostnames = None\n")
    file1.write("as_user = ingres\n")
    file1.write("filepath = None\n")
    file1.write("filename = None\n")
    file1.write("tags = None\n")
    file1.write("skiptags = None\n")
    file1.write("feature = None\n")
    file1.close()

if __name__ == '__main__':
    main()
    # runinstall_latestpatch('OR', '11.2.0', 'a64.win','sanet','usau-or-dlw10')
    # get_latestpatch()
    # run_install_latestpatch('OR', '11.2.0', 'a64.win','sanet')
    # run_install_latestpatch('OR', '11.2.0', 'a64.win', 'sanet')
    # get_filenm_currpatch('OR', '11.2.0', 'a64.win', 'p15625')