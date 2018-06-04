class ColissionManager:
    def __init__(self, game):
        self.game = game
        self.char_width = self.game.getCharacterWidth()
        self.char_height = self.game.getCharacterHeight()

    def checkRightColission(self, ball):
        right_limit = ball.getPos()[0] + ball.getWidth()
        upper_limit = ball.getPos()[1]
        lower_limit = ball.getPos()[1] + ball.getHeight()
        self.checkRightHitChar(ball, right_limit, upper_limit, lower_limit)
        self.checkRightHitBorder(ball, right_limit)
        self.checkRightHitEnemy(ball, right_limit, upper_limit, lower_limit)

    def checkRightHitBorder(self, ball, right_limit):
        if right_limit > 950:
            ball.changeFading()
    
    def checkRightHitChar(self, ball, right_limit, upper_limit, lower_limit):
        char_pos = self.game.getCharacterPosition()
        char_left_limit = char_pos[0]
        char_upper_limit = char_pos[1]
        char_lower_limit = char_pos[1] + self.game.getCharacterHeight()

        if(right_limit > char_left_limit and right_limit - self.game.getCharacterWidth() < char_left_limit):
            if(upper_limit < char_lower_limit and lower_limit > char_upper_limit):
                self.charColission(ball)
    
    def checkRightHitEnemy(self, ball, right_limit, upper_limit, lower_limit):
        for enemy in self.game.getEnemies():
            enemy_pos = enemy.getPos()
            enemy_left_limit = enemy_pos[0]
            enemy_upper_limit = enemy_pos[1]
            enemy_lower_limit = enemy_pos[1] + enemy.getHeight()
            
            if(right_limit > enemy_left_limit and right_limit - enemy.getWidth() < enemy_left_limit):
                if(upper_limit < enemy_lower_limit and lower_limit > enemy_upper_limit):
                    self.enemyColission(ball, enemy)

    def checkLeftColission(self, ball):
        left_limit = ball.getPos()[0]
        upper_limit = ball.getPos()[1]
        lower_limit = ball.getPos()[1] + ball.getHeight()
        self.checkLeftHitChar(ball, left_limit, upper_limit, lower_limit)
        self.checkLeftHitBorder(ball, left_limit)
        self.checkLeftHitEnemy(ball, left_limit, upper_limit, lower_limit)

    def checkLeftHitBorder(self, ball, left_limit):
        if left_limit < 50:
            ball.changeFading()
    
    def checkLeftHitChar(self, ball, left_limit, upper_limit, lower_limit):
        char_pos = self.game.getCharacterPosition()
        char_right_limit = char_pos[0] + self.game.getCharacterWidth()
        char_upper_limit = char_pos[1]
        char_lower_limit = char_pos[1] + self.game.getCharacterHeight()

        if(left_limit < char_right_limit and left_limit + self.game.getCharacterWidth() > char_right_limit):
            if(upper_limit < char_lower_limit and lower_limit > char_upper_limit):
                self.charColission(ball)

    def checkLeftHitEnemy(self, ball, left_limit, upper_limit, lower_limit):
        for enemy in self.game.getEnemies():
            enemy_pos = enemy.getPos()
            enemy_right_limit = enemy_pos[0] + enemy.getWidth()
            enemy_upper_limit = enemy_pos[1]
            enemy_lower_limit = enemy_pos[1] + enemy.getHeight()

            if(left_limit < enemy_right_limit and left_limit + enemy.getWidth()> enemy_right_limit):
                if(upper_limit < enemy_lower_limit and lower_limit > enemy_upper_limit):
                    self.enemyColission(ball, enemy)

    def charColission(self, ball):
        self.game.hurtCharacter(ball.getDamage())
        ball.changeFading()

    def enemyColission(self, ball, enemy):
        #self.game.maze.enemies.remove(enemy)
        self.game.killEnemy(enemy)
        ball.changeFading()
        if len(self.game.maze.enemies) == 0:
            self.game.win()
        