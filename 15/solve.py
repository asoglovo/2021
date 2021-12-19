from chiton import find_safest_path
from riskmap import RiskMap

if __name__ == '__main__':
    risk_map = RiskMap.from_input()
    path, score = find_safest_path(risk_map)

    risk_map.print_path(path)
    print(f'Risk score: {score}')
