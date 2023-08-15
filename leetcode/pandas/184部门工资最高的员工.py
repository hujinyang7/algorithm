'''
表： Employee
+--------------+---------+
| 列名          | 类型    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
在 SQL 中，id是此表的主键。
departmentId 是 Department 表中 id 的外键（在 Pandas 中称为 join key）。
此表的每一行都表示员工的 id、姓名和工资。它还包含他们所在部门的 id。
表： Department
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
在 SQL 中，id 是此表的主键列。
此表的每一行都表示一个部门的 id 及其名称。
查找出每个部门中薪资最高的员工。
按 任意顺序 返回结果表。
查询结果格式如下例所示。

示例 1:
输入：
Employee 表:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department 表:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
输出：
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
解释：Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在销售部的工资最高。
'''



import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # merge_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner', suffixes=['_left', '_right'])
    # group_df = merge_df.groupby('departmentId').max()
    # salaries = group_df['salary'].to_list()
    # name_right = group_df['name_right'].to_list()
    # df = pd.DataFrame(columns=['name_right', 'name_left', 'salary'])
    # for i in range(len(salaries)):
    #     _df = merge_df.loc[(merge_df['salary']==salaries[i]) & (merge_df['name_right']==name_right[i]), ['name_left', 'salary', 'name_right']]
    #     df = pd.concat([df, _df], ignore_index=True, join="inner")
    # df.rename(columns={'name_right': 'Department', 'name_left': 'Employee', 'salary': 'Salary'}, inplace=True)
    # return df

    # 合并两张表
    merge_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner', suffixes=['_left', '_right'])
    # 通过部门名称分组并按，并按最大工资过滤
    highest_salary_per_department = merge_df.groupby('name_right').apply(
        lambda df: df[df['salary'] == df['salary'].max()]).reset_index(drop=True)
    df = highest_salary_per_department[['name_right', 'name_left', 'salary']]
    df.rename(columns={'name_right': 'Department', 'name_left': 'Employee', 'salary': 'Salary'}, inplace=True)
    return df
