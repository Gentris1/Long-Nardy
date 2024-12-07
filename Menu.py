import pygame
import sys

BEIGE = (245, 222, 179)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Long Nardy')

class Menu:
    @staticmethod
    def draw_menu(game, board):
        screen.fill(BEIGE)

        font = pygame.font.SysFont(None, 72)

        name_text = font.render('Long Nardy', True, BLACK)
        start_text = font.render('Start Game', True, BLACK)
        load_text = font.render('Load Game', True, BLACK)

        name_rect = name_text.get_rect()
        start_rect = start_text.get_rect()
        load_rect = load_text.get_rect()

        name_rect.center = (WIDTH // 2, HEIGHT // 2 - 150)

        start_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)
        load_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)

        screen.blit(name_text, name_rect)

        pygame.draw.rect(screen, GREY, start_rect.inflate(20, 20))
        pygame.draw.rect(screen, GREY, load_rect.inflate(20, 20))

        screen.blit(start_text, start_rect)
        screen.blit(load_text, load_rect)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if start_rect.inflate(20, 20).collidepoint(mouse_pos):
                        running = False

                    elif load_rect.inflate(20, 20).collidepoint(mouse_pos):
                        running = False
                        loaded_board, loaded_player1, loaded_player2 = game.load_game()
                        if loaded_board:
                            board.board = loaded_board.board
                            board.flag_keep = loaded_board.flag_keep
                            board.checker_keep = loaded_board.checker_keep
                            board.home = loaded_board.home
                            board.white_total_checkers = loaded_board.white_total_checkers
                            board.black_total_checkers = loaded_board.black_total_checkers
                            board.is_ready_black = loaded_board.is_ready_black
                            board.is_ready_white = loaded_board.is_ready_white

                            game.player1.remaining_moves = loaded_player1.remaining_moves.copy()
                            game.player1.move_flag = loaded_player1.move_flag
                            game.player1.dice_numbers = loaded_player1.dice_numbers.copy()

                            game.player2.remaining_moves = loaded_player2.remaining_moves.copy()
                            game.player2.move_flag = loaded_player2.move_flag
                            game.player2.dice_numbers = loaded_player2.dice_numbers.copy()

            pygame.time.Clock().tick(30)