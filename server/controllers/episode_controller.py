from .core_controller import CoreController, CoreControllerOne
from ..models import Episode

class EpisodeController(CoreController):
    def __init__(self):
        super().__init__(Episode)

class EpisodeControllerOne(CoreControllerOne):
    def __init__(self):
        super().__init__(Episode)