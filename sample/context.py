import os,sys,yaml
relpath=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, relpath)
config=yaml.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+'/config.yml'))
