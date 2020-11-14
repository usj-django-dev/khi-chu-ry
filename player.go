package player

import (
	"errors"
	"math/rand"
	"time"

	"github.com/sergivillar/rock-paper-scissors/config"
)

// Player struct to create new players
type Player struct {
	Name string
}

// Create a new player with params
func Create(name string) (Player, error) {
	if name == "" {
		return Player{}, errors.New("You must provide a player name")
	}

	return Player{
		Name: name,
	}, nil
}

// RockPaperScissor function to get a random game option
func RockPaperScissor() string {
	s := rand.NewSource(time.Now().UnixNano())
	r := rand.New(s)

	i := r.Intn(len(config.GameOptions))
	return config.GameOptions[i]
}
