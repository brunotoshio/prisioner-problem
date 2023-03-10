import concurrent.futures

import scenario


NUMBER_OF_ATTEMPTS = 1000


def main():
    # Random selection
    print('Random selection:\n')
    scenarios = [scenario.RandomSelectionScenario(100, 50) for _ in range(NUMBER_OF_ATTEMPTS)]
    with concurrent.futures.ThreadPoolExecutor(40) as executor:
        futures = [executor.submit(scenario.run) for scenario in scenarios]
        success = [future.result() for future in concurrent.futures.as_completed(futures)].count(True)
    print(f'\t{success} success attempts in {NUMBER_OF_ATTEMPTS} attempts\n')

    # Graph selection
    print('Graph selection:\n')
    scenarios = [scenario.GraphSelectionScenario(100, 50) for _ in range(NUMBER_OF_ATTEMPTS)]
    with concurrent.futures.ThreadPoolExecutor(40) as executor:
        futures = [executor.submit(scenario.run) for scenario in scenarios]
        success = [future.result() for future in concurrent.futures.as_completed(futures)].count(True)
    print(f'\t{success} success attempts in {NUMBER_OF_ATTEMPTS} attempts\n')


if __name__ == '__main__':
    main()
