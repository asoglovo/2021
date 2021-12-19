from chiton import find_safest_path
from extended_riskmap import ExtendedRiskMap

times_extended = 5

if __name__ == '__main__':
    risk_map = ExtendedRiskMap.from_input(times_extended)
    path, score = find_safest_path(risk_map)

    # print_path(risk_map, path)
    print(f'Risk score: {score}')
