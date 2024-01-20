# Порівняльний Аналіз Алгоритмів Пошуку Підрядка

Цей документ представляє результати порівняльного аналізу трьох алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта (KMP) та Рабіна-Карпа. Тестування проводилося на двох текстових файлах з використанням двох типів підрядків - існуючого та уявного.

## Методологія

Використовуючи модуль `timeit`, було виміряно час виконання кожного алгоритму для пошуку підрядків у двох різних текстах.

## Результати Тестування

### Текст 1: Уявний Підрядок

- **Боєр-Мур:** 0.00037 секунд
- **KMP:** 0.00111 секунд
- **Рабін-Карп:** 0.00268 секунд

### Текст 2: Існуючий Підрядок

- **Боєр-Мур:** 0.00049 секунд
- **KMP:** 0.00138 секунд
- **Рабін-Карп:** 0.00330 секунд

### Текст 2: Уявний Підрядок

- **Боєр-Мур:** 0.00052 секунд
- **KMP:** 0.00158 секунд
- **Рабін-Карп:** 0.00372 секунд

## Висновки

За результатами тестування, алгоритм **Боєра-Мура** продемонстрував найкращі часові показники при пошуку як існуючих, так і уявних підрядків у обох текстах. Алгоритм KMP показав трохи гірші результати, але все ж значно швидше, ніж Рабін-Карп, особливо при пошуку уявних підрядків.

Хоча алгоритм Рабіна-Карпа виявився найповільнішим у цих тестах, його можна рекомендувати для застосування в специфічних випадках, наприклад, при пошуку множини патернів одночасно або у випадках, коли важлива їх швидкість зміни.

Ці результати свідчать про важливість вибору відповідного алгоритму для конкретного типу тексту та підрядка, враховуючи їх властивості та контекст використання.