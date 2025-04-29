from langchain.tools import Tool
import csv
import json
import ast

def generate_csv_and_decide_winner(weights_input) -> str:
    if isinstance(weights_input, str):
        try:
            weights = json.loads(weights_input)  # JSON-style string (double quotes)
        except json.JSONDecodeError:
            weights = ast.literal_eval(weights_input)  # Python dict-style string (single quotes)
    else:
        weights = weights_input
    humans = list(weights.keys())
    
    # Sort Pokémon by weight descending
    for human in humans:
        weights[human].sort(key=lambda x: -x[1])

    min_length = min(len(weights[humans[0]]), len(weights[humans[1]]))
    team1 = weights[humans[0]][:min_length]
    team2 = weights[humans[1]][:min_length]

    winner_counts = {humans[0]: 0, humans[1]: 0}
    
    with open("pokemon_duel.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([humans[0], humans[1], "Winner"])
        
        for (poke1, w1), (poke2, w2) in zip(team1, team2):
            if w1 > w2:
                writer.writerow([f"{poke1}({w1})", f"{poke2}({w2})", humans[0]])
                winner_counts[humans[0]] += 1
            elif w2 > w1:
                writer.writerow([f"{poke1}({w1})", f"{poke2}({w2})", humans[1]])
                winner_counts[humans[1]] += 1
            else:
                writer.writerow([f"{poke1}({w1})", f"{poke2}({w2})", "Tie"])

    if winner_counts[humans[0]] > winner_counts[humans[1]]:
        return (f"The winner of the duel between {humans[0]} and {humans[1]} is {humans[0]}! "
                f"Congratulations {humans[0]}!! {humans[0]} won against {humans[1]} with a score of "
                f"{winner_counts[humans[0]]} to {winner_counts[humans[1]]}!")
    elif winner_counts[humans[1]] > winner_counts[humans[0]]:
        return (f"The winner of the duel between {humans[0]} and {humans[1]} is {humans[1]}! "
                f"Congratulations {humans[1]}!! {humans[1]} won against {humans[0]} with a score of "
                f"{winner_counts[humans[1]]} to {winner_counts[humans[0]]}!")
    else:
        return "The competition is a tie!"

generate_csv_and_decide_winner_tool = Tool(
    name="generate_csv_and_decide_winner",
    description="Generate CSV file and decide final winner",
    func=generate_csv_and_decide_winner,
)