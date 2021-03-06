from . import tools, setup
from .states import gaming
from . import constants as c

def main():
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {c.GAMING: gaming.gaming()}

    run_it.setup_states(state_dict, c.GAMING)
    run_it.main()