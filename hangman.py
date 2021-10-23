#########################
#  Hangman Project for  #
# Python is Easy course #
# on Pirple.com         #
#                       #
# Created by:           #
# Bojan Adzic           #
# aka Coder::Owl        #
#                       #
# Soecial thanks to:    #
# www.hangmanwords.com  #
#                       #
#########################

import os
os.system('color')
import sys
from random import randint
# from termcolor import colored, cprint
  
# list of 213 words
word_list = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

# Global variables
running = True
done = False
word = word_list[randint(0, 212)]
guesses = []
tries_left = 7
guess_count = 0
player = 1
word_pl_1 = ""
word_pl_2 = ""
player1_guesses = []
player2_guesses = []
player1_tries_left = 7
player2_tries_left = 7
player1_guess_count = 0
player2_guess_count = 0

# Global functios
def clear_screen():
	print(chr(27) + "[2J")

def playing(word, count, guesses):
	clear_screen()
	draw_hangman(count)
	for letter in word:
		if letter.lower() in guesses:
			print(letter, end=" ")
		else:
			print("_", end=" ")
	print("")

def draw_hangman(count):
	if count == 0:
		print("-----")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("=======\n")
	elif count == 1:
		print("-----")
		print("|   |")
		print("|")
		print("|")
		print("|")
		print("|")
		print("=======\n")
	elif count == 2:
		print("-----")
		print("|   |")
		print("|   O")
		print("|")
		print("|")
		print("|")
		print("=======\n")
	elif count == 3:
		print("-----")
		print("|   |")
		print("|   O")
		print("|   |")
		print("|")
		print("|")
		print("=======\n")
	elif count == 4:
		print("-----")
		print("|   |")
		print("|   O")
		print("|  /|")
		print("|")
		print("|")
		print("=======\n")
	elif count == 5:
		print("-----")
		print("|   |")
		print("|   O")
		print("|  /|\\")
		print("|")
		print("|")
		print("=======\n")
	elif count == 6:
		print("-----")
		print("|   |")
		print("|   O")
		print("|  /|\\")
		print("|  /")
		print("|")
		print("=======\n")
	elif count == 7:
		print("-----")
		print("|   |")
		print("|   O")
		print("|  /|\\")
		print("|  / \\")
		print("|")
		print("=======\n")

while running:
	clear_screen()
	choose_game = input("Choose game type ('1' - 1 Player, '2' - 2 Players, 'q' - Quit game): ")
	if choose_game == '1':
		word = word_list[randint(0, 212)]
		while not done:
			clear_screen()
			playing(word, guess_count, guesses)
			guess = input(f"\nTries left {tries_left}. Guess the letter: ")
			guesses.append(guess.lower())
			if guess.lower() not in word.lower():
				guess_count += 1
				tries_left -= 1
				if tries_left == 0:
					playing(word, guess_count, guesses)
					tries_left = 7
					guess_count = 0
					running = False
					break

			done = True
			for letter in word:
				if letter.lower() not in guesses:
					done = False

		if done:
			print(f"\nCongratulations! You found the word! It was {word}.")
			running = False
		else:
			print(f"\nGame Over! The word was {word}.")
	elif choose_game == '2':
		clear_screen()
		word_pl_1 = input("Player 1, enter the word for Player 2 to guess: ")
		clear_screen()
		word_pl_2 = input("Player 2, enter the word for Player 1 to guess: ")
		
		while not done:
			if player == 1:
				clear_screen()
				playing(word_pl_2, player1_guess_count, player1_guesses)
				print(f"\nPlayer {player} turn\n")
				guess = input(f"Tries left {player1_tries_left}. Guess the letter: ")
				player1_guesses.append(guess.lower())
				if guess.lower() not in word_pl_2.lower():
					player1_guess_count += 1
					player1_tries_left -= 1
					if player1_tries_left == 0:
						playing(word_pl_2, player1_guess_count, player1_guesses)
						player1_tries_left = 7
						player1_guess_count = 0
						print(f"\nNo more tries left. Game Over. The word was: {word_pl_2}")
						running = False
						break

				pl1_wins = True
				for ch in word_pl_2:
					if ch.lower() not in player1_guesses:
						pl1_wins = False
				if not pl1_wins:
					clear_screen()
					playing(word_pl_2, player1_guess_count, player1_guesses)
					print(f"\nPlayer {player} turn")
					player = 2
					input("\nPress Enter to switch players")
				else:
					clear_screen()
					playing(word_pl_2, player1_guess_count, player1_guesses)

				done = True
				for letter in word_pl_2:
					if letter.lower() not in player1_guesses:
						done = False
				if done:
					print(f"\nPlayer 1 wins! The word was: {word_pl_2}")
					running = False
					break

			elif player == 2:
				clear_screen()
				playing(word_pl_1, player2_guess_count, player2_guesses)
				print(f"\nPlayer {player} turn\n")
				guess = input(f"Tries left {player2_tries_left}. Guess the letter: ")
				player2_guesses.append(guess.lower())
				if guess.lower() not in word_pl_1.lower():
					player2_guess_count += 1
					player2_tries_left -= 1
					if player2_tries_left == 0:
						playing(word_pl_1, player2_guess_count, player2_guesses)
						player2_tries_left = 7
						player2_guess_count = 0
						print(f"\nNo more tries left. Game Over. The word was: {word_pl_1}")
						running = False
						break

				pl2_wins = True
				for ch in word_pl_1:
					if ch.lower() not in player2_guesses:
						pl2_wins = False
				if not pl2_wins:
					clear_screen()
					playing(word_pl_1, player2_guess_count, player2_guesses)
					print(f"\nPlayer {player} turn")
					player = 1
					input("\nPress Enter to switch players")
				else:
					clear_screen()
					playing(word_pl_1, player2_guess_count, player2_guesses)

				done = True
				for letter in word_pl_1:
					if letter.lower() not in player2_guesses:
						done = False

				if done:
					print(f"\nPlayer 2 wins! The word was: {word_pl_1}")
					running = False
					break
	else:
		break