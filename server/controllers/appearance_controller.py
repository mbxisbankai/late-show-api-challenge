from .core_controller import CoreController, CoreControllerOne
from ..models import Appearance

class AppearanceController(CoreController):
    def __init__(self):
        super().__init__(Appearance)

class AppearanceControllerOne(CoreControllerOne):
    def __init__(self):
        super().__init__(Appearance)