# Огляд алгоритмів для видачі решти

## Жадібний алгоритм

Жадібний алгоритм (`find_coins_greedy`) працює за принципом вибору найбільшої доступної монети, доки вся сума не буде розподілена. Він швидкий і працює за час **O(n)**, де _n_ — кількість номіналів монет. Однак цей підхід не завжди дає оптимальний результат, якщо набір монет нестандартний.

### Плюси:

- Висока швидкість виконання.
- Простота реалізації.

### Мінуси:

- Не завжди знаходить оптимальне рішення (мінімальну кількість монет).
- Не підходить для всіх можливих наборів монет.

## Алгоритм динамічного програмування

Алгоритм динамічного програмування (`find_min_coins`) використовує метод знаходження оптимального рішення через проміжні значення.

### Плюси:

- Завжди знаходить оптимальне рішення.
- Підходить для будь-яких наборів монет.

### Мінуси:

- Потребує більше пам'яті.
- Повільніший за жадібний алгоритм для великих значень.

## Порівняння ефективності

Протестовано обидва алгоритми на сумі 113:

- **Жадібний алгоритм**: працює швидше, але не гарантує мінімальну кількість монет.
- **Динамічне програмування**: трохи повільніше, проте завжди знаходить мінімальне число монет.

## Висновки

Якщо набір монет стандартний (як у більшості валютних систем), жадібний алгоритм — чудовий варіант. Якщо ж набір монет особливий, краще використовувати метод динамічного програмування, щоб завжди отримати оптимальне рішення.
