from .core_controller import CoreController, CoreControllerOne
from ..models import Guest

class GuestController(CoreController):
    def __init__(self):
        super().__init__(Guest)

class GuestControllerOne(CoreControllerOne):
    def __init__(self):
        super().__init__(Guest)