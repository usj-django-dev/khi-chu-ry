package config

// Rules to know who win the game
var Rules = map[string]string{
	"rock":     "scissors",
	"paper":    "rock",
	"scissors": "paper",
}

// GameOptions representes the available options to play
var GameOptions = []string{"rock", "paper", "scissors"}
