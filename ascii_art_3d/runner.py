from rendering.renderer import Renderer
from input.user_input import UserInput

class Runner:
    def __init__(self):
        self.renderer = Renderer()
        self.user_input = UserInput()

    def run(self):
        shape_type, params = self.user_input.get_shape_params()
        self.renderer.render(shape_type, params)
