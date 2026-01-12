from sdk.moveapps_spec import hook_impl
from sdk.moveapps_io import MoveAppsIo
from movingpandas import TrajectoryCollection
import logging
import matplotlib.pyplot as plt

from app.panel import build_panel_app, serve_panel_app

class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:

        logging.info(f'Welcome to the {config}')

        """Your app code goes here"""
        
        pn_app = build_panel_app(data)

        serve_panel_app(pn_app)
        
        logging.info("Panel app running on port 5006")

        # return the resulting data for next Apps in the Workflow
        return data
