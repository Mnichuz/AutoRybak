# AutoRybak
By __[Mnichuz](https://github.com/Mnichuz)__

___
### Wymagania:
* Zainstalowany python
* `pip install pyautogui pillow keyboard` (wkleić w cmd)
* Zamienić w kodzie zmienne:
```python
width1 = 1920
height1 = 1080
```
na roździelczość ekranu.

### Uruchamianie:
`pyton main.py` (wkleic w cmd które jest otwarte w lokalizacji folderu)

___

Program szuka w danym obszarze ekranu koloru emotki ryby. Gdy go znajdzie, czeka aż zniknie, a po 2.5 sekundach od zniknięcia klika `e`, a potem `4` aby wyjąc wędke. Te wartości można zmienić w kodzie. Jeżeli nie będziecie w FiveM program dalej będzie szukał na ekranie koloru ryby i jak go znajdzie to i tak naciśnie e chwile po zniknięciu.

Aby zatrzymać program należy w cmd nacisnąć ctrl-c albo nacisnąc `q` na klawiaturze

#

Użyte linki:
* https://github.com/KianBrose/Image-Recognition-Botting-Tutorial
* https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
* https://gist.github.com/arithex/3e953d1eb096afe58ce05ba6846493e4
