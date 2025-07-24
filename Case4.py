def max_dragon_power(N):
    dp = [0] * (N + 1)
    dp[0] = 1  # Базовый случай: 0 голов — сила 1 (по соглашению)

    for i in range(1, N + 1):
        for k in range(1, 8):  # У одного дракона может быть от 1 до 7 голов
            if i >= k:
                dp[i] = max(dp[i], dp[i - k] * k)

    return dp[N]

# Ввод
try:
    N = int(input("Введите общее количество голов драконьей стаи (1–99): "))
    if 0 < N < 100:
        max_power = max_dragon_power(N)
        print(f"Максимально возможная сила стаи: {max_power}")
    else:
        print("Ошибка: число должно быть от 1 до 99.")
except ValueError:
    print("Ошибка: введите целое число.")
