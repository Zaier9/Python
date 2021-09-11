# -*- coding: utf-8 -*-


class Lamp:
    _LAMPS = ['''
             .
        .    |    ,
         \   '   /
        `  ,-. '
      --- (   ) ---
           \ /
          _|=|_
         |_____|
      ''',
      '''
           ,-.
          (   )
           \ /
          _|=|_
         |_____|
      ''']

    #metodo de instancia __init__: es el constructor de la clase
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on
    
    #metodos publicos
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()
    
    #metodo privado
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])