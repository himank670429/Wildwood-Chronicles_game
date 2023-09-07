from abc import ABC, abstractmethod
class Scene(ABC):
    '''
    every scene has some actor that are going to be drawn, updated on the screen.
    these Scene are creates seperatley in Scene folder.
    '''

    @abstractmethod
    def draw(self):
        '''
        draw the scene
        '''
        pass

    @abstractmethod
    def events(self):
        '''
        handle events for that scene
        '''
        pass

    @abstractmethod
    def update(self):
        '''
        update all the actors in that scene
        '''
        pass

class SceneManager():
    '''
    a wrapper that swaps in/out scene based on certain action.
    '''
    def __init__(self, game, current_scene):
        self.current_scene = current_scene
        self.game = game
    
    def set_scene(self, scene : Scene):
        self.current_scene = scene
    
    def draw_scene(self):
        self.current_scene.draw()
    
    def handle_scene_events(self):
        self.current_scene.events()
    
    def update_scene(self):
        self.current_scene.update()