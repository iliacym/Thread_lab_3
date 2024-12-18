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

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="50%">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/3%20body.gif" alt="3 случайных тела" style="width: 100%; height: auto;"/>
          <figcaption>3 случайных тела</figcaption>
        </div>
      </td>
      <td align="center" valign="top" width="50%">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/earth_sun.gif" alt="Земля и Солнце" style="width: 100%; height: auto;"/>
          <figcaption>Земля и Солнце</figcaption>
        </div>
      </td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

## Задание 2 (Решение задачи Дирихле)

### Описание алгоритма

**Задача Дирихле** — это краевая задача для эллиптических дифференциальных уравнений, где на границе области
задаются постоянные значения функции.

В начале матрица заполняется случайными числами, после чего, через итерационный процесс, вычисляются новые значения на
сетке. Распараллеливание происходит с помощью использования директив препроцессора из OpenMP.

### Описание сходимости

Точность, предложенная в учебнике, мала, даже для сходимости небольшого числа точек, не говоря о
предложенных 5000 точек. Поэтому мы использовали свою.

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="50%">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/Screenshot_17.png" alt="Точность из учебника" style="width: 100%; height: auto;"/>
          <figcaption>Точность из учебника</figcaption>
        </div>
      </td>
      <td align="center" valign="top" width="50%">
        <div style="display: flex; flex-direction: column; align-items: center;">
          <img src="res/Screenshot_18.png" alt="Предложенная нами точность" style="width: 100%; height: auto;"/>
          <figcaption>Предложенная нами точность</figcaption>
        </div>
      </td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

### Оценка работы алгоритма

| ![](res/Screenshot_24.png) | ![](res/Screenshot_25.png) |
|:--------------------------:|:--------------------------:|
| ![](res/Screenshot_26.png) | ![](res/Screenshot_27.png) |

## Анализ полученных результатов

* **Ускорение**:Ускорение программы значительно увеличивалось с ростом числа потоков, что свидетельствует о
  преимуществе параллельных вычислений. Однако после 11-12 потоков, увеличение ускорения прекратилось из-за исчерпания
  аппаратных ресурсов.
* **Эффективность**: Максимальная эффективность при распараллеливании наблюдалась при 1 потоке. Эффективность
  использования ресурсов падала по мере увеличения их числа.

## Заключение

Использование GPU для вычислений позволяет значительно ускорить выполнение программы на больших объемах данных. Однако,
на крайне малых объемах данных, использование GPU может замедлить выполнение программы из-за больших накладных расходов.

Использование параллельных вычислений позволяет существенно ускорить выполнение программы. Оптимальное количество
потоков не превышает количество физических потоков процессора, также дальнейшее увеличение числа потоков замедляет
выполнение программы.