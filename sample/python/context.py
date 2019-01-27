import os,sys,yaml
from classes.ParseJson import ParseJson
from classes.LogMessage import LogMessage
projectpath=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
logpath=projectpath + '/logs/LOG'
sys.path.insert(0, projectpath)
config=yaml.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))+'/config.yml'))
