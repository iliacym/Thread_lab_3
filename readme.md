<h1 align="center">
Thread lab 3
</h1>

<div align="center">
Для замеров использовались:<br>
CPU: Ryzen 5600x<br>
GPU: NVIDIA GTX 1660<br>
Выполнили: Козин Борис (21пи-3), Столетов Максим (21пи-2), Гурьянов Илья (21пми-1)
</div>

## Задание 1 (Задача n тел)

### Описание алгоритма

Алгоритм основан на решении n дифференциальных уравнений, которые позволяют получить траектории всех частиц. Для
решения используется метод Эйлера. В результате получаются итерационные формулы для решения уравнений.

Так как на каждой итерации расчеты не зависят друг от друга, то они были представлены в виде операций с матрицами и
распараллелены с использованием cuda (а именно библиотеки cupy).

### Оценка работы алгоритма

| ![](res/Screenshot_1.png) | ![](res/Screenshot_2.png) |
|:-------------------------:|:-------------------------:|

### Примеры визуализаций

<div style="overflow-x: auto;">
  <table style="width: 100%; table-layout: fixed;">
    <tr>
      <td style="text-align: center; width: 50%; vertical-align: top;">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/3%20body.gif" alt="3 случайных тела" style="width: 100%; height: auto;"/>
          <div>3 случайных тела</div>
        </div>
      </td>
      <td style="text-align: center; width: 50%; vertical-align: top;">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/earth_sun.gif" alt="Земля и Солнце" style="width: 100%; height: auto;"/>
          <div>Земля и Солнце</div>
        </div>
      </td>
    </tr>
  </table>
</div>

## Задание 2 (Решение задачи Дирихле)

### Описание алгоритма

**Задача Дирихле** — это краевая задача для эллиптических дифференциальных уравнений, где на границе области
задаются постоянные значения функции.  
В начале матрица заполняется случайными числами, после чего, через итерационный процесс, вычисляются новые значения на
сетке. Распараллеливание происходит с помощью использования директив препроцессора из OpenMP.

### Описание сходимости

Точность, предложенная в учебнике, мала, даже для сходимости небольшого числа точек, не говоря о
предложенных 5000 точек. Поэтому мы использовали свою.

<div style="overflow-x: auto;">
  <table style="width: 100%; table-layout: fixed;">
    <tr>
      <td style="text-align: center; width: 50%; vertical-align: top;">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/Screenshot_17.png" alt="Точность из учебника" style="width: 100%; height: auto;"/>
          <div>Точность из учебника</div>
        </div>
      </td>
      <td style="text-align: center; width: 50%; vertical-align: top;">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/Screenshot_18.png" alt="Предложенная нами точность" style="width: 100%; height: auto;"/>
          <div>Предложенная нами точность</div>
        </div>
      </td>
    </tr>
  </table>
</div>

### Оценка работы алгоритма

| ![](res/) | ![](res/) |
|:---------:|:---------:|
| ![](res/) | ![](res/) |

## Анализ полученных результатов

* **Ускорение**:
* **Эффективность**:

## Заключение