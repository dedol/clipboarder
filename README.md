# Clipboarder
**Главная задача программы** - быстрая отправка фотографий с камеры в диалог ВК с помощью комбинации клавиш. Пользователь подключает камеру к компьютеру, открывает диалог с пользователем ВК в браузере и нажимает сочитание клавиш. Последняя фотография с камеры сразу добавляется в сообщение.

### Комбинации клавиш
1. `«Ctrl + Space»` – вставить последнюю (по дате создания) фотографию из каталога «DCIM\100NCD90\». **Повторное нажатие** сочетания «Ctrl + Space» в течение 60 секунд после первого – вставить предпоследнюю фотографию. **Следующее нажатие комбинации** – вставка третьей с конца фотографии. И так далее.
Если между нажатиями «Ctrl + Space» прошло **более 60 секунд** каталог с фотографиями заново индексируется и вставляется последняя фотография. 
Если после нескольких нажатий «Ctrl + Space» раздается 
**одиночный сигнал** (писк), то список фотографий закончился, то есть были вставлены все фотографии из каталога.
2. `«Ctrl + R»` – ручная индексация каталога, после нажатия раздается двойной сигнал. Таймер в 60 секунд сбрасывается, каталог индексируется и после следующего нажатия комбинации **«Ctrl + Space»** будет вставляться последняя фотография в каталоге.
3. `«Ctrl + Q»` – принудительное завершение программы после тройного сигнала.