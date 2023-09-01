import time
from turtle import Screen
from player import Player
from score import ScoreBoard
from cars import Car, speed_up, CARS_NUM, reset_speed

screen = Screen()

repeat = True
while repeat:
    repeat = False
    reset_speed()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    screen.update()

    player = Player()
    score_board = ScoreBoard()
    cars_list = []
    for _ in range(CARS_NUM):
        car = Car()
        cars_list.append(car)

    screen.onkeypress(player.go_forward, "Up")
    screen.onkeypress(player.go_backward, "Down")

    screen.update()

    game_is_on = True
    while game_is_on:
        time.sleep(0.01)
        screen.update()
        for car in cars_list:
            if (0 < player.ycor() - car.ycor() < 20 or 0 < car.ycor() - player.ycor() < 30) and -5 < car.xcor() - 20 < 5:
                score_board.game_over()
                game_is_on = False
        if player.reach_the_end():
            time.sleep(1)
            score_board.level_up()
            speed_up()
            player.reset_player()
        for car in cars_list:
            car.move()
            car.reset_car()

    end_game_input = screen.textinput("Exit or Repeat", "R for repeat\nE for  exit")
    if end_game_input:
        if end_game_input.strip().lower() == "r":
            repeat = True
            screen.reset()
            score_board.reset()
            cars_list = []
        elif end_game_input.strip().lower() == "e":
            time.sleep(1)
            raise SystemExit
        else:
            raise SystemExit
    else:
        raise SystemExit

screen.exitonclick()
