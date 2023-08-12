# 模型建立基本步骤

建立一个数学规划模型，需要三个步骤：

1. 定义决策变量
2. 生成约束条件（关于变量的关系表达式）
3. 定义目标函数

# 定义决策变量

模型中的决策变量可以通过 `Model`类中的内置方法定义，定义时可以一次生成一个决策变量、决策变量列表或决策变量字典。下表列出了常用的决策变量定义方法：

| Function                    | Creates        |
| --------------------------- | -------------- |
| `binary_var()`            | 单个二进制变量 |
| `binary_var_list()`       | 二进制变量列表 |
| `binary_var_dict()`       | 二进制变量字典 |
| `binary_var_matrix()`     | 二进制变量矩阵 |
| `integer_var()`           | 单个整数变量   |
| `integer_var_list()`      | 整数变量列表   |
| `integer_var_dict()`      | 整数变量字典   |
| `integer_var_matrix()`    | 整数变量矩阵   |
| `continuous_var()`        | 单个连续变量   |
| `continuous_var_list()`   | 连续变量列表   |
| `continuous_var_dict()`   | 连续变量字典   |
| `continuous_var_matrix()` | 连续变量矩阵   |



# 目标函数

可以通过 `modle.minimize()`和 `model.maximize()`定义模型的目标函数，其参数为决策变量的线性表达式。譬如：

```python
model.minimize(model.total_inside_cost + mdl.total_outside_cost)
```


# 生成约束条件

线性规划模型中的约束条件是决策变量的线性表达式。Python中的算数运算符（`+,-,*，/`）和关系运算符（`==,<=,>=`）可以直接使用，譬如：如果 `x,y,z`是决策变量，`3*x + 5*y + 7*z`就是一个合法的线性表达式，`3*x + 5*y + 7*z <= 1`就是一个约束条件。

更多情况下，线性规划模型中约束条件为聚合表达式，譬如\sum_{i \in N} x_{i} \leq1。*DOcplex.MP*可以通过 `Model.sum`方法生成类似约束，`model.sum(x[i] for i in N) <= 1`

下表给出了常用添加约束的方法：

| Function                             | Add              |
| ------------------------------------ | ---------------- |
| `add_constraint(ct, ctname=None)`  | 添加一个线性约束 |
| `add_constraints(cts, names=None)` | 批量添加线性约束 |

模型建立后，可以将模型输出为LP格式，以进行检验，仿真出现错误。导出为LP格式的方法为：`model.export_as_lp()`。


# 模型求解

可以通过模型的*parameters*属性设置模型求解参数，譬如，设置线性整数规划的MIP Gap可以这样操作：`model.parameters.mip.tolerances.mip_gap=0.05`。设置完成后可以直接通过 `solve()`函数求解。

模型的求解结果以类*SolveSolution*形式返回，其中包含了：

* 全部模型信息，譬如求解状态、目标函数值，以及
* 每个变量的值

模型无解时，`solve()`返回 `None`，因此可以直接基于返回结果判断求解结果。对于每个变量对象，可以通过 `solution[vname]`的形式获取变量的值。

[来源](https://brucehan.top/2020/02/02/docplex/)		[github](https://github.com/superhxl/Markdown/tree/master/cplex)
