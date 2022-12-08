from enum import Enum


class OutcomePoints(Enum):
    WIN = 6
    LOSS = 0
    DRAW = 3


class ScenarioPoints(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Scenario(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


values = {
    "A": Scenario.ROCK,
    "B": Scenario.PAPER,
    "C": Scenario.SCISSORS,
    "X": Scenario.ROCK,
    "Y": Scenario.PAPER,
    "Z": Scenario.SCISSORS,
}

decrypt_values = {
    "X": OutcomePoints.LOSS,
    "Y": OutcomePoints.DRAW,
    "Z": OutcomePoints.WIN,
}


def score(elf: str, op: str) -> int:
    score = ScenarioPoints[values[op].value].value
    if values[elf] == values[op]:
        score += OutcomePoints.DRAW.value
        return score
    if values[op] == Scenario.ROCK and values[elf] == Scenario.SCISSORS:
        score += OutcomePoints.WIN.value
        return score
    if values[op] == Scenario.PAPER and values[elf] == Scenario.ROCK:
        score += OutcomePoints.WIN.value
        return score
    if values[op] == Scenario.SCISSORS and values[elf] == Scenario.PAPER:
        score += OutcomePoints.WIN.value
        return score
    score += OutcomePoints.LOSS.value
    return score


def decrypt(elf: str, op: str) -> int:
    score = 0
    if decrypt_values[op] == OutcomePoints.DRAW:
        score += ScenarioPoints[values[elf].value].value
        score += OutcomePoints.DRAW.value
        return score
    if decrypt_values[op] == OutcomePoints.WIN:
        if values[elf] == Scenario.ROCK:
            score += ScenarioPoints.PAPER.value
        if values[elf] == Scenario.PAPER:
            score += ScenarioPoints.SCISSORS.value
        if values[elf] == Scenario.SCISSORS:
            score += ScenarioPoints.ROCK.value
        score += OutcomePoints.WIN.value
        return score
    if decrypt_values[op] == OutcomePoints.LOSS:
        if values[elf] == Scenario.ROCK:
            score += ScenarioPoints.SCISSORS.value
        if values[elf] == Scenario.PAPER:
            score += ScenarioPoints.ROCK.value
        if values[elf] == Scenario.SCISSORS:
            score += ScenarioPoints.PAPER.value
        score += OutcomePoints.LOSS.value
        return score


with open("day-2-input.txt", "r") as f:
    op_score = 0
    decrypt_op_score = 0
    for x in f.read().split("\n"):
        op_score += score(x.split()[0], x.split()[1])
        decrypt_op_score += decrypt(x.split()[0], x.split()[1])
    print(f"OP score 1st strat: {op_score}")
    print(f"DEC OP score 2st strat: {decrypt_op_score}")
