import os,sys,yaml
__projectpath=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
__logpath=__projectpath + '/logs/LOG'
sys.path.insert(0, __projectpath)
__config=yaml.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))+'/config.yml'))
