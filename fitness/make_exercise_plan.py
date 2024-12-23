### Weekly Undulating Periodization

from typing import NamedTuple
import sys


class CycleParameters(NamedTuple):
    reps: int
    one_rep_maximum_percent: float

def main():
    
    data_file_name = 'exercise_to_orm.txt'
    cycle = {
        1 : CycleParameters(10, 0.7),
        2 : CycleParameters(8, 0.75),
        3 : CycleParameters(5, 0.88),
        4 : CycleParameters(3, 0.93),
        5 : CycleParameters(6, 0.65), # Transition
    }
    
    current_week = get_input_week()

    if current_week not in cycle.keys():
        raise ValueError("There isn't such a week in the training cycle")

    ex_to_orm = read_one_rep_max_for_exercise(data_file_name)
    get_formated_training_plan(cycle, current_week, ex_to_orm)


def get_input_week():
    if len(sys.argv) - 1 < 1:
            raise TypeError("You should enter current week as an integer")
    if not sys.argv[1].isdigit():
        raise ValueError("Incorrect Input. You must write an integer")
    return int(sys.argv[1])


def get_formated_training_plan(cycle, current_week, ex_to_orm):
    cycle_parameters = cycle[current_week]
    print(f' 3 Times X {cycle_parameters.one_rep_maximum_percent:1.2f} 1-RM X {cycle_parameters.reps:2} Reps')
    for exercise, orm in ex_to_orm.items():
        print(f'{exercise:15} | {orm * cycle_parameters.one_rep_maximum_percent: 3.2f}')


def read_one_rep_max_for_exercise(file_name):
    with open(file_name, "r") as f:
        ex_to_orm = dict(
                (
                    (exercise.strip(), float(orm))  for exercise, orm  in  (line.strip().split(":") for line in f.read().split('\n'))
                )
            )
    return ex_to_orm


if __name__ == "__main__":
    main()