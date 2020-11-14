package player

import (
	"testing"

	c "github.com/sergivillar/rock-paper-scissors/config"
)

func TestCpuPlay(t *testing.T) {
	result := RockPaperScissor()

	if !contains(c.GameOptions, result) {
		t.Fatal("Incorrect game option")
	}
}

func TestCreatePlayer(t *testing.T) {
	expected := Player{"Player"}

	p, err := Create("Player")
	if err != nil {
		t.Fatal(err)
	}
	if expected != p {
		t.Error("Player is not created correctly")
	}
}

func TestCreatePlayerNoName(t *testing.T) {
	expected := "You must provide a player name"

	_, err := Create("")
	if err == nil {
		t.Fatalf("Expected '%v', but instead got no error", expected)
	}
}

func contains(s []string, e string) bool {
	for _, item := range s {
		if item == e {
			return true
		}
	}
	return false
}
