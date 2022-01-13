class Bird :
    '''Базовый класс, определяющий свойства птиц'''
    count = 0
    def _init_(self , chat) :
        self.sound = chat
        Bird.count += 1
        def talk( self ) :
            return self.sound