for segment in snake.snake_list:
        if snake.snake_list[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.gameOver()