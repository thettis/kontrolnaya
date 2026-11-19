import random
import math

def print_matrix(matrix, title="Матрица"):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{x:>4}" for x in row))

def generate_matrix(rows, cols):
    print("\nВыберите способ заполнения матрицы:")
    print("1 последовательными числами (по строкам)")
    print("2 случайными числами от 1 до 50")
    
    while True:
        choice = input("Ваш выбор: ").strip()
        if choice == '1':
            matrix = []
            counter = 1
            for _ in range(rows):
                row = []
                for _ in range(cols):
                    row.append(counter)
                    counter += 1
                matrix.append(row)
            break
        elif choice == '2':
            matrix = [[random.randint(1, 50) for _ in range(cols)] for _ in range(rows)]
            break
        else:
            print("Некорректный ввод. Введите 1 или 2.")
            
    return matrix

def analyze_matrix(matrix, rows, cols):
    print_matrix(matrix, "Исходная матрица")

    # сумма эл-тов
    row_sums = [sum(row) for row in matrix]
    row_prods = [math.prod(row) for row in matrix]
    
    for i in range(rows):
        print(f"Строка {i+1}: Сумма = {row_sums[i]}, Произведение = {row_prods[i]}")
        
    # транспонтруем для удобного поиска по столбцам
    transposed_for_calc = list(zip(*matrix))
    col_sums = [sum(col) for col in transposed_for_calc]
    col_prods = [math.prod(col) for col in transposed_for_calc]
    
    for j in range(cols):
        print(f"Столбец {j+1}: Сумма = {col_sums[j]}, Произведение = {col_prods[j]}")

    # строка и столбец с максимальной суммой
    max_row_ind = row_sums.index(max(row_sums))
    max_col_ind = col_sums.index(max(col_sums))
    print(f"\nМаксимальная сумма в строке: {max_row_ind + 1} (Сумма = {row_sums[max_row_ind]})")
    print(f"Максимальная сумма в столбце: {max_col_ind + 1} (Сумма = {col_sums[max_col_ind]})")

    # замена первой и последней строки столбца
    
    matrix[0], matrix[-1] = matrix[-1], matrix[0]
    for i in range(rows):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
        
    print_matrix(matrix, "Матрица после замены крайних строк и столбцов")

    # 5. транспонирование и проверка на симметричность
    transposed = [list(col) for col in zip(*matrix)]
    if rows == cols:
        is_symmetric = (matrix == transposed)
        if is_symmetric: 
            print(f"\nМатрица квадратная, совпадает с транспонированной.")
        else:
            print(f"\nМатрица квадратная, но не совпалает с транспонированной.")
    else:
        print("\nМатрица не квадратная, проверка на равенство транспонированной не выполняется.")

    # седловые точки
    print("Седловые точки")
    saddle_points = []
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            
            is_row_min = all(val <= matrix[i][k] for k in range(cols))
            is_col_max = all(val >= matrix[k][j] for k in range(rows))
            
            is_row_max = all(val >= matrix[i][k] for k in range(cols))
            is_col_min = all(val <= matrix[k][j] for k in range(rows))
            if (is_row_min and is_col_max) or (is_row_max and is_col_min):
                saddle_points.append((i + 1, j + 1, val))
                
    if saddle_points:
        for sp in saddle_points:
            print(f"Строка {sp[0]}, Столбец {sp[1]}, Значение: {sp[2]}")
    else:
        print("Седловых точек не найдено.")

    # 7. Уникальные элементы
    all_elements = [num for row in matrix for num in row]
    unique_sorted = sorted(list(set(all_elements)))
    print(f"\nУникальные элементы в порядке возрастания:\n{unique_sorted}")

    # 8. След матрицы (дополнительно)
    if rows == cols:
        trace = sum(matrix[i][i] for i in range(rows))
        print(f"\nСлед матрицы (сумма главной диагонали) = {trace}")
    else:
        print("\nСлед матрицы не вычисляется (матрица не квадратная).")


def main():
    
    while True:
        try:
            r = int(input("Введите количество строк (2 <= R <= 12): "))
            c = int(input("Введите количество столбцов (2 <= C <= 12): "))
            
            if 2 <= r <= 12 and 2 <= c <= 12:
                break
            else:
                print("Ошибка: размеры должны быть от 2 до 12. Попробуйте снова.")
        except ValueError:
            print("Ошибка: вводите целые числа.")

    matrix = generate_matrix(r, c)
    analyze_matrix(matrix, r, c)

main()