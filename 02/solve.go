package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

var (
	forwardRegex = regexp.MustCompile("^forward (\\d+)$")
	downRegex    = regexp.MustCompile("^down (\\d+)$")
	upRegex      = regexp.MustCompile("^up (\\d+)$")
)

type state struct {
	x, y, aim int
}

type stateUpdater interface {
	updateInPlace(st *state)
}

type forwardInstruction struct {
	displacement int
}

func (fi forwardInstruction) updateInPlace(st *state) {
	st.x += fi.displacement
	st.y += st.aim * fi.displacement
}

type downInstruction struct {
	displacement int
}

func (di downInstruction) updateInPlace(st *state) {
	st.aim += di.displacement
}

type upInstruction struct {
	displacement int
}

func (ud upInstruction) updateInPlace(st *state) {
	st.aim -= ud.displacement
}

func parseInstruction(instruction string) stateUpdater {
	var displacement int

	if forwardRegex.MatchString(instruction) {
		displacement, _ = strconv.Atoi(forwardRegex.FindStringSubmatch(instruction)[1])
		return forwardInstruction{displacement}
	}

	if downRegex.MatchString(instruction) {
		displacement, _ = strconv.Atoi(downRegex.FindStringSubmatch(instruction)[1])
		return downInstruction{displacement}
	}

	if upRegex.MatchString(instruction) {
		displacement, _ = strconv.Atoi(upRegex.FindStringSubmatch(instruction)[1])
		return upInstruction{displacement}
	}

	panic("can't parse instruction: " + instruction)
}

func main() {
	var (
		instruction string
		scanner     = bufio.NewScanner(os.Stdin)
		st          = &state{x: 0, y: 0, aim: 0}
	)

	for scanner.Scan() {
		instruction = scanner.Text()
		parseInstruction(instruction).updateInPlace(st)
	}

	fmt.Printf("Final position: (%d, %d)\n", st.x, st.y)
	fmt.Printf("%d * %d = %d\n", st.x, st.y, st.x*st.y)
}
