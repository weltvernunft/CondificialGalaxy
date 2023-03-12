import numpy as np

def random_predict(number:int=1) -> int:
    """Guess randomly the number
    Args:
        number (int, optional): Guessed number. Default = 1.
    Return: num of tries.
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return (count)

print(f'Number of tries: {random_predict()}')

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Your algorithm guesses the number in mean for: {score} tries')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)