from core.range_base import RangeBase

def execute_reader(range_base: RangeBase):
    while True:
        try:
            user_input = input()
            output = range_base.execute(user_input)
            print(output)
        except:
            break