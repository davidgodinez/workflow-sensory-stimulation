import datajoint as dj
from element_animal import subject
from element_lab import lab
from element_session import session

from element_animal.subject import Subject
from element_lab.lab import Source, Lab, Protocol, User, Project
from element_session.session import Session
from element_sensory_stimulation import stimulation

from .paths import get_sensory_root_data_dir

if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')



# Activate "lab", "subject", "session", "" schema ----------------------------------

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

session.activate(db_prefix + 'session', linking_module=__name__)


# Activate "sensory-stimulation" schema ------------------------------------------------------

stimulation.activate(db_prefix + 'stimulation', linking_module=__name__)